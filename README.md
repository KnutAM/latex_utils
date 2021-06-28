# Latex utilities

[![Build Status](https://travis-ci.com/KnutAM/repo_python.svg?branch=main&kill_cache=1)](https://travis-ci.com/KnutAM/repo_python)  [![Coverage Status](https://coveralls.io/repos/github/KnutAM/latex_utils/badge.svg?branch=main&kill_cache=1)](https://coveralls.io/github/KnutAM/latex_utils?branch=main)  [![Documentation Status](https://readthedocs.org/projects/latex-utils/badge/?version=latest&kill_cache=1)](https://latex-utils.readthedocs.io/en/latest/?badge=latest)  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

The repo contains a set of python tools useful when working with latex, e.g.

**Current**

- Reducing data when plotting with pgf

**Future**

- Removing uncessesary data from .bib files
- Replacing all user defined macros before submitting for publication

## Installation

Download repository using git: ``git clone git@github.com:KnutAM/latex_utils.git``

### Using conda (recommended)

For this to work, you need to have conda install (e.g. by downloading anaconda). In order to work with this library, you should then do the following steps in cmd/shell (replace `<my_env>` with the environment name you wish to use.)

1. Create a new environment: `conda create -n <my_env>`  (Only required if you start with a fresh environment, but this is recommended in most cases)
2. Make the folder containing this readme file your current working directory
3. Activate your environment: `conda activate <my_env>`
4. Install pip with conda: `conda install pip`
5. Install this package: `pip install .`

After completing these steps, the modules will be available for importing in python sessions using the environment `<my_env>`. 

**Update package**: If new updates (obtained via `git pull`) are to be included, run `pip install .` from the same directory as this file, while having `<my_env>` as your active conda environment. 

### Using pip (alternative)

In cmd or shell with the current working directory the same as for this readme: `pip install .`

**Update package**: The same procedure is used to update if updates via `git pull` have been obtained. 
