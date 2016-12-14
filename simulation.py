from datetime import datetime 
import json
import click
import numpy as np

time_format = '%Y-%m-%d-%H-%M-%s'

def simulation(N, s, H, u):
    """Simulation a single appearance of double mutant and its extinction or fixation.
    
    Parameters
    ----------
    N : int
        constant population size
    s  : float
        selection coefficient against aB and Ab, 0 < s < 1
    H : float
        ratio of selection coefficeints against aB/Ab and AB, 0 < H < 1
    u : float
        mutation rate, 0 < u < 1
        
    Returns
    -------
    Tw : int
        time of first appearance of AB
    Tfe : int
        time for fixation or extinction of AB
    fix : bool
        if True, AB reached 50% (fixation), otherwise AB reached 0% (extinction)
    n : numpy.ndarray
        n[i,j] if the number of j genotypes at generation i
    """
    N = int(N)
    # n[j][i] is counts of genotype i (ab, aB, Ab, AB) in generation j
    n = [np.array([N, 0, 0, 0])]

    S = np.diag([1, 1-s, 1-s, 1+s*H])
    M = np.array([
        [(1-u)**2, (1-u)*u, (1-u)*u, u**2],
        [(1-u)*u, (1-u)**2, u**2, (1-u)*u],
        [(1-u)*u, u**2, (1-u)**2, (1-u)*u],
        [u**2, (1-u)*u, (1-u)*u, u**2]
    ])
    E = M @ S
    
    # waiting for appearance
    while n[-1][-1] == 0:
        p = n[-1] / N
        p = E @ p
        p = p / p.sum()
        n.append(np.random.multinomial(N, p))
    Tw = len(n) # appearance time
    
    # waiting for fixation (reach 50%) or extinction (reach 0%)
    while 0 < n[-1][-1] < (N*0.5):
        p = n[-1] / N
        p = E @ p
        p = p / p.sum()
        n.append(np.random.multinomial(N, p))
    Tfe = len(n) - Tw # fixation / extinction time
    return Tw, Tfe, bool(n[-1][-1] > 0), np.array(n)

@click.command()
@click.option('--N', default=1000, type=int, help='Population size')
@click.option('--s', default=0.1, type=float, help='Selection coefficient')
@click.option('--H', default=2, type=float, help='Advantage of double mutant')
@click.option('--u', default=1e-5, type=float, help='Mutation rate')
@click.argument('output', default=datetime.now().strftime(time_format)+'.json', type=click.File('wt'))
def main(n, s, h, u, output):
    N = n
    H = h
    filename = output.name
    click.echo("Starting simulation with:")
    click.echo(dict(N=N, s=s, H=H, u=u, filename=filename))
    waiting_time, fixation_time, fixation, n = simulation(N, s, H, u)
    click.echo("Writing results to {}".format(filename))
    json.dump(dict(
            waiting_time=waiting_time,
            fixation_time=fixation_time,
            fixation=fixation,
            n=n.tolist(),
            N=N, 
            s=s, 
            H=H, 
            u=u, 
            filename=filename
        ),
        output,
        sort_keys=True, indent=4, separators=(',', ': ')
    )

if __name__ == '__main__':
    main()