import numpy as np
from scipy.stats import poisson
from scipy.linalg import block_diag

def mutation_free_population(strains, G):
    p = np.array([ [0] * G for _ in range(strains) ], dtype=np.float64)
    p[0,0] = 1
    assert np.allclose(p.sum(), 1)
    return p

def smooth_fitness(s, H, strains, G):
    w = np.array([ [ (1 - s ) ** (k + i) for k in range(G)] for i in range(strains) ])
    return w

def rugged_fitness(s, H, strains, G):
    w = smooth_fitness(s, H, strains, G)
    w[-1,:] *= (1 + s * H)/((1 - s) ** 2) # fix fitness of the double mutant strain
    return w

def mean_fitness(p, w):
    return (p*w).sum()

def mutation_rates_matrix(U, pi, tau, w):
    mutation_rates = np.ones(w.shape) * U
    mutation_rates[w < pi] *= tau
    return mutation_rates

def big_mutation_matrix(mutation_rates, repeats, small_mutation_matrix_function):
    assert mutation_rates.shape[0] == 3 or mutation_rates.shape[1] == 3
    M = np.zeros((0,0))
    for i in range(repeats):
        m = small_mutation_matrix_function(mutation_rates[i,:])
        M = block_diag(M, m)
    assert np.allclose(M.sum(axis=0),1)
    return M

def small_background_mutation_matrix(mutation_rates):
    assert mutation_rates.shape[0] == len(mutation_rates)	
    mutation_rvs = poisson(mutation_rates)
    m = np.diag(mutation_rvs.pmf(0))
    for k in range(1,mutation_rates.shape[0]):
        m += np.diag(mutation_rvs.pmf(k)[:-k],-k)
    # absorb further mutations in the last class
    for j in range(mutation_rates.shape[0]):
        m[-1,j] = 1 - mutation_rvs.cdf(mutation_rates.shape[0] - 2 - j)[j]
    return m

def small_strain_mutation_matrix(mutation_rates):
    assert mutation_rates.shape[0] == len(mutation_rates)
    mu = mutation_rates
    u = np.array([ [ (1 - mu[0]) ** 2, 0, 0 ], [2 * mu[0] * (1 - mu[0]) , 1 - mu[1], 0], [ mu[0] ** 2, mu[1], 1 ] ])
    return u

def run(pop_size, s, H, U, beta, G, pi, tau, tick_interval=1000000):
    # init population
    w = smooth_fitness(s, H, 3, G)
    mutation_rates = mutation_rates_matrix(U, pi, tau, w)
    Mm = big_mutation_matrix(mutation_rates, 3, small_background_mutation_matrix)
    mutation_rates2 = mutation_rates.copy()
    Mu = big_mutation_matrix((mutation_rates2 * beta).transpose(), G, small_strain_mutation_matrix)

    p = mutation_free_population(3, G)
    ps = [p]
    shape = p.shape
    W = mean_fitness(p,w)
    Ws = [W]
    
    tick = 0
    print("Starting simulation")

    ## MSB

    while tick < 5000:
        # selection
        p = w * p

        # strain mutations
        p = Mu.dot( p.flatten(order="F") )
        p = p.reshape(shape, order="F")

        # background mutations 
        p = Mm.dot( p.flatten(order="C") )
        p = p.reshape(shape, order="C")

        p /= p.sum()

        # drift
        if pop_size > 0:
            p = np.random.multinomial(pop_size, p.flatten()) / np.float64(pop_size)
            p = p.reshape(shape)

        # mean fitness
        W = mean_fitness(p,w)

        # monitoring and logging

        if tick_interval != 0 and tick % tick_interval == 0:
            print("Tick %d" % tick)
        tick += 1
        ps.append(p)
        Ws.append(W)

    print("MSB reached at tick %d with mean fitness %.4g" % (tick, W))
    
    w = rugged_fitness(s, H, 3, G)
    mutation_rates = mutation_rates_matrix(U, pi, tau, w)
    Mm = big_mutation_matrix(mutation_rates, 3, small_background_mutation_matrix)
    mutation_rates2 = mutation_rates.copy()
    Mu = big_mutation_matrix((mutation_rates2 * beta).transpose(), G, small_strain_mutation_matrix)

    ## Double mutant appearance

    while p[2,:].sum() == 0:
        # selection
        p = w * p

        # strain mutations
        p = Mu.dot( p.flatten(order="F") )
        p = p.reshape(shape, order="F")

        # background mutations 
        p = Mm.dot( p.flatten(order="C") )
        p = p.reshape(shape, order="C")

        p /= p.sum()

        # drift
        if pop_size > 0:
            p = np.random.multinomial(pop_size, p.flatten()) / np.float64(pop_size)
            p = p.reshape(shape)

        # mean fitness
        W = mean_fitness(p,w)

        # monitoring and logging

        if tick_interval != 0 and tick % tick_interval == 0:
            print("Tick %d" % tick)
        tick += 1
        ps.append(p)
        Ws.append(W)

    print("Double mutant appeared at tick %d with mean fitness %.4g" % (tick, W))
    AB0,AB1,AB2,AB3 = p[2,0],p[2,1],p[2,2],p[2,3]
    print("AB/0 %.4g, AB/1 %.4g, AB/2 %.4g, AB/3 %.4g" % (AB0, AB1, AB2, AB3))


    ## Double mutant fixation

    while p[2,:].sum() > 0 and p[2,:].sum() < 1:
        # selection
        p = w * p

        # NO strain mutations
        # p = Mu.dot( p.flatten(order="F") )
        # p = p.reshape(shape, order="F")

        # background mutations 
        p = Mm.dot( p.flatten(order="C") )
        p = p.reshape(shape, order="C")

        p /= p.sum()

        # drift
        if pop_size > 0:
            p = np.random.multinomial(pop_size, p.flatten()) / np.float64(pop_size)
            p = p.reshape(shape)

        # mean fitness
        W = mean_fitness(p,w)

        # monitoring and logging

        if tick_interval != 0 and tick % tick_interval == 0:
            print("Tick %d" % tick)
        tick += 1
        ps.append(p)
        Ws.append(W)


    if bool(p[2,:].sum() > 0):
        print("Fixation at tick %d with mean fitness %.4g and AB frequency %.4g" % (tick, W, p[2,:].sum()))
        AB0,AB1,AB2,AB3 = p[2,0],p[2,1],p[2,2],p[2,3]
        print("AB/0 %.4g, AB/1 %.4g, AB/2 %.4g, AB/3 %.4g" % (AB0, AB1, AB2, AB3))
    else:
        print("Extinction at tick %d with mean fitness %.4g" % (tick, W))

    # wrap up 
    print("Simulation finished, %d ticks" % tick)

    return np.array(ps), np.array(Ws)