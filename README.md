# Evolution on rugged adaptive landscapes

[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/yoavram/UnderTheRug/master)

This repository contains supporting material for

>   Obolski<sup>eq</sup>, Ram<sup>eq</sup>, and Hadany (2018) _[Key issues review: evolution on rugged adaptive landscapes](http://iopscience.iop.org/article/10.1088/1361-6633/aa94d4)_, Reports on Progress in Physics, 81: 12602. 

A preprint is available on [bioRxiv](https://www.biorxiv.org/content/early/2017/03/03/112177).

The notebook files (`.ipynb`) include Python source code for reproduction of Figures 2, 3, 5, and 6.

## View the notebooks

Interact with the notebooks on [binder](https://mybinder.org/v2/gh/yoavram/UnderTheRug/master).

- [nk_model.ipynb](https://github.com/yoavram/UnderTheRug/blob/master/nk_model.ipynb)
  - Contains source code to generate random landscapes from an _NK model_ and visualize their ruggedness to produce Figure 2.
- [holey_landscape.ipynb](https://github.com/yoavram/UnderTheRug/blob/master/holey_landscape.ipynb)
  - Contains source code to generate random _holey landscapes_, analyse their connectedness and produce Figure 3.
- [simulations.ipynb](https://github.com/yoavram/UnderTheRug/blob/master/simulations.ipynb):
  - Contains source code to load empirical adaptive landscape data, simulate evolution on the landscape using a Wright-Fisher model, and visualize the results of simulations to produce Figure 6.
  - Cotains source code to load results of simulations on a two-loci rugged landscape and analyse and visualize the results to produce Figure 5. Source code for running simulations is in [simulation.py](https://github.com/yoavram/UnderTheRug/blob/master/simulation.py).

### Data source

- Data for TEM landscape, `Weinreich2006.csv`, is from [Weinreich, Delaney, Depristo, & Hartl. _Darwinian evolution can follow only very few mutational paths to fitter proteins_. Science (80-. ). 312, 111–114 (2006)](http://www.ncbi.nlm.nih.gov/pubmed/16601193)
- Data for _A. nigeri_ landscape, `Franke2011.csv`, is from [Franke, Klözer, de Visser, & Krug. _Evolutionary Accessibility of Mutational Pathways_. PLoS Comput. Biol. 7, e1002134 (2011).](http://dx.plos.org/10.1371/journal.pcbi.1002134)
- Data for two-loci landscape is from [Ram, & Hadany. _Stress-induced mutagenesis and complex adaptation_. Proc. R. Soc. B Biol. Sci. 281, 20141025–20141025 (2014)](http://www.ncbi.nlm.nih.gov/pubmed/25143032), retrieved from [Dryad](http://datadryad.org/resource/doi:10.5061/dryad.3066j).

## Run the notebook

You can interact with the notebooks on [binder](https://mybinder.org/v2/gh/yoavram/UnderTheRug/master) or on your own machine.
Following are instructions for the latter.

### Install dependencies

The easiest way to install the dependencies is to install [Anaconda](https://store.continuum.io/).
You should use Python 3, preferably with version 3.5 or higher.
The notebooks will probably not work on Python 2.

All required packages should then be available.
However, if you get an `ImportError` due to a package not being installed, the following command will install all requirements using conda:

```sh
conda install jupyter notebook cython ipykernel matplotlib numpy pandas scipy seaborn
```

### Get the source code repository

You can download all the source code by clicking the _Clone or Download_ button and choosing _Download ZIP_. Then extract the ZIP to a folder on your machine.

If you use `git` you can clone the repo using:

```sh
git clone https://github.com/yoavram/UnderTheRug.git
```

### Run the notebook

Start a Jupyter notebook server inside the repo folder:

```sh
cd <path to folder>
jupyter notebook
```

Your browser should open automatically. Choose one of the notebooks (`.ipynb` files).

## Troubleshooting

Use the [Issues](https://github.com/yoavram/UnderTheRug/issues) page to report problems or suggest improvements or contact [Yoav Ram](mailto:yoav@yoavram.com).

License
-------

This work is licensed under a Creative Commons Attribution-ShareAlike 4.0
International License.
