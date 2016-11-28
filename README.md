# EvolRugAdaptLand2016

This repository includes Python code in the form of a Jupyter notebook that is used as the supporting material for 

> Obolski, Ram & Hadany (2016) Evolution on rugged adaptive landscapes, Reports on Progress in Physics, *In preparation*.

The notebook includes code to load fitness landscape data, simulate evolution on the landscape using a Wright-Fisher model, and visualize the results of simulations.

## Install

Install [Anaconda](https://store.continuum.io/), then create a new environment and install it as an IPython kernel (do this from inside the repo folder):

```sh
conda env create -f environment.yml
source activate EvolRugAdaptLand2016
```

## Run

Start a Jupyter notebook server inside the repo folder:

```sh
jupyter notebook
```

## License

<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.