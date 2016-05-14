# EvolRugAdaptLand2016

This repository includes Python code in the form of a Jupyter notebook that is used as the supporting material for 

> Obolski, Ram & Hadany (2016) Evolution on rugged adaptive landscapes, Reports on Progress in Physics, *In preparation*.

The notebook includes code to load fitness landscape data, simulate evolution on it using a Wright-Fisher model, and visualize the results of simulations.

## Install

Install [Anaconda](https://store.continuum.io/), then create a new environment and install it as an IPython kernel (do this from inside the repo folder):

```sh
conda create -n EvolRugAdaptLand2016 --file environment.yml
activate EvolRugAdaptLand2016
python -m ipykernel install --name EvolRugAdaptLand2016
```

## Run

Start a Jupyter notebook server inside the repo folder:

```sh
jupyter notebook
```

## License

CC-BY-SA 3


