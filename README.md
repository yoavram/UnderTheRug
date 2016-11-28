# Evolution on rugged adaptive landscapes
## Obolski, Ram & Hadany
## Key Issues Review for Reports on Progress in Physics, 2016

This repository contains supporting material for

> Obolski, Ram & Hadany (2016) Evolution on rugged adaptive landscapes, Reports on Progress in Physics, In preparation.

The notebook file (`notebook.ipynb`) includes code to load fitness landscape data, simulate evolution on the landscape using a Wright-Fisher model, and visualize the results of simulations.

## View the notebook

You can open a [static view of the notebook](https://github.com/yoavram/EvolRugAdaptLand2016/blob/master/notebook.ipynb).

## Run the notebook

You can open a dynamic view of the notebook on your own machine.

### Install dependencies

The easiest way to install the dependencies is to install [Anaconda](https://store.continuum.io/), then create a new environment and install it as an IPython kernel (do this from inside the repo folder):

```sh
conda env create -f environment.yml
source activate EvolRugAdaptLand2016
```

### Run the notebook

Start a Jupyter notebook server inside the repo folder:

```sh
jupyter notebook
```

## License

<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.