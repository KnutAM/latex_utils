# Template for python repositories
[![Build Status](https://travis-ci.com/KnutAM/repo_python.svg?branch=main&kill_cache=1)](https://travis-ci.com/KnutAM/repo_python)  [![Coverage Status](https://coveralls.io/repos/github/KnutAM/repo_python/badge.svg?branch=main&kill_cache=1)](https://coveralls.io/github/KnutAM/repo_python?branch=main)  [![Documentation Status](https://readthedocs.org/projects/repo-python/badge/?version=latest&kill_cache=1)](https://repo-python.readthedocs.io/en/latest/?badge=latest)  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Initial modifications for a new project

The following should be modified:

- Update the package_name to the name of your library
- Update the string "package_name" correspondingly in the following files:
  - ``setup.py`` 
  - ``doc/source/conf.py``
  - `test/test_main.py` (Update ``import package_name.main`` )
  - ``.travis.yml``  (Update ``-cov=package_name``)

### Enabling installation

In order for users and other developers to work with the package, it is vital that the dependencies are documented properly. Furthermore, this is also required for continuous integration and testing. Add minimal requirements (i.e. packages that are imported in your code) to `requirements.txt`. New line for each package, and package specifications can be e.g. 

- `numpy>=1.0`
- `scipy`

Already, requirements for documentation and testing have been added. After this has been done, your environment can be setup to allow you to run locally, see "Creating the environment"

### Documentation (Sphinx)

Documentation using sphinx allows automatic documentation using docstrings in the code. First, set it up to work locally. For open source projects this can be published to ReadTheDocs. Another alternative is using the GitHub pages. 

You should take the badge embed link from your documentation at readthedocs and replace the current (see "Badges" to ensure that it updates correctly)

### Testing

Unit testing can be setup so that it can be run locally. However, the real power and visibility comes when this is run each time the code is pushed to ensure that it works as intended and that nothing has been broken. First, `pytest` is used to create simple tests. Then, `TravisCI` is used to get continuous testing on each push. Finally, code coverage is analyzed. 

#### pytest

With the conda enironment for development active, and in the present folder, run ``pytest``

To get the test coverage, you can, instead, run

- ``coverage run --source=package_name -m pytest`` (where ``package_name`` should be updated to the present project)
- ``coverage report`` 

#### Automatic testing using TravisCI

Please see [Travis CI Documentation](https://docs.travis-ci.com/user/tutorial/)

Note that the `.travis.yml` has already been created and should work if updated according to above. Hence you only need to grant Travis access to your github repository.

You must update the badge with the link provided by Travis CI (see "Badges" to ensure that it updates correctly)

#### Coverage analysis using coverage.io

Make an account on [coveralls.io](www.coveralls.io) and add your repository. 

You must update the badge with the link provided by coveralls.io (see "Badges" to ensure that it updates correctly)

### Badges

A problem that can occur is that the badges don't update correctly, this can be solved by adding `&kill_cache=1` at the end of the badge url. 

# Readme for end users

[![Build Status](https://travis-ci.com/KnutAM/repo_python.svg?branch=main&kill_cache=1)](https://travis-ci.com/KnutAM/repo_python)  [![Coverage Status](https://coveralls.io/repos/github/KnutAM/repo_python/badge.svg?branch=main&kill_cache=1)](https://coveralls.io/github/KnutAM/repo_python?branch=main)  [![Documentation Status](https://readthedocs.org/projects/repo-python/badge/?version=latest&kill_cache=1)](https://repo-python.readthedocs.io/en/latest/?badge=latest)  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Installation

Download repository using git: ``git clone git@github.com:KnutAM/repo_python.git``

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
