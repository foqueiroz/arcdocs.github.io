# Anaconda

Anaconda is a distribution of Python and R for scientific computing that includes the conda package manager system which aids with reproducibility. You can read more about Anaconda on their [website](https://www.anaconda.com/products/individual).

Anaconda is our actively supported Python distribution on both ARC3 and ARC4.

## Usage

To access the anaconda module use the command:

```bash
$ module load anaconda
```

This will make available the [Conda package management tool](https://docs.conda.io/en/latest/), but it will not load any environment. You may wish to load and use the `base` environment which has the default Python 3.7.4 and the Python packages made available in the [Anaconda 2019.10 release](https://docs.anaconda.com/anaconda/reference/release-notes/#anaconda-2019-10-october-15-2019).

To enter the `base` environment:

```bash
$ source activate base
```

This will adjust your prompt and add a prefix with the environments name surrounded by parentheses e.g. (base).

You can see the packages and versions available in the base environment:

```bash
$ conda list
```

You can exit an environment after use:

```bash
$ conda deactivate
```

To delete an environment (and all associated files) you no longer need:

```bash
$ conda remove --name my_env --all
```

To view all available environments:

```bash
$ conda env list
```

```{note}
We recommend, however, that you do not use the base environment but create and activate custom environments built to the specifications you need for your projects.
```

### What is a conda environment?

Conda environments are a form of python virtual environments, a self contained directory that contains a particular version of python plus a number of specific python packages. Conda allows us to create and manage several of these separate environments at the same time.

![Conda environment graphic](../../assets/img/software/compilers/anaconda/conda-env2.jpg)
Image Copyright © [geohackweek](https://geohackweek.github.io/datasharing/01-conda-tutorial/)

Each environments packages and installed python versions are isolated from one another preventing notorious package 'dependency hell' situations. Conda also allows us to share environment specifications through the creation of simple text files, aiding reproducibility.

### Creating custom environments

To create a new Python 3 environment with the Pandas, Numpy and Scipy libraries named example_env_1, use the command:

```bash
$ conda create --name example_env_1 python=3 numpy scipy pandas
```

Here we have used the [`conda create`](https://docs.conda.io/projects/conda/en/latest/commands/create.html) command, we specify a name for our environment using the `--name/-n` option and then the packages we want to be installed, and if we require specific versions we include that in the pattern `<package>=<versionNumber>`.

You’ll note that during the installation process that Conda will attempt to install the enviroment and it’s constituent packages in your home directory:

```bash
## Package Plan ##

environment location: /home/home02/issev001/.conda/envs/example_env_1

To load this environment:

source activate example_env_1

and to deactivate it after use:

conda deactivate
```

```{note}
As your home directory has limited storage space you may wish to specify that new environment are built and stored in your [/nobackup directory](../../getting_started/nobackup) instead.
```

To create an environment named `example_env_2` in [`/nobackup`](../../getting_started/nobackup) (here as user issev001 - you should replace this with your own named user directory) then:

```bash
$ conda create -p /nobackup/issev001/example_env_2 python=3 matplotlib pandas numpy
```

Here we've used the `conda create` command but included the `--prefix/-p` option which lets us specify the prefix for the environment (the location where we want the environment files to live).

This time, you’ll note that Conda will install the environment and it’s constituent packages in the directory you specified:

```bash
## Package Plan ##

environment location: /nobackup/issev001/example_env_2

To load this new environment:

source activate /nobackup/issmcal/example_env_2

and to deactivate after use:

conda deactivate
```

At any time, you can list your Conda environments (whether in your home directory or elsewhere):

```bash
$ conda env list
```

For the full conda documentation please consult their [website](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html).


## Example conda environments

Below we cover some examples of more generic conda environments HPC users might wish to create depending on their research.

### Conda channels

Conda 

Add the a number of channels. This step is required so that the conda installer knows where to get the installation files for your applications from. Again, at the command prompt:

conda config --add channels r
conda config --add channels bioconda
conda config --add channels conda-forge

 

That’s it. You can now use Conda to automatically install a range of applications and libraries.

### Bioconda

A number of research domains have repositories that allow the installation of applications and libraries. One example is Bioconda for the Computational Biology community.

The full list of applications that Bioconda is currently able to install is available on the Bioconda Web site:

https://bioconda.github.io
Installing Python packages
Creating environments with Conda

Environments can be though of as standalone, isolated working copies of Python and other packages. They are usually created for specific projects or tasks where a certain configuration is needed that is different than for other projects.

For example, to replicate a workflow used by another researcher in your team you might create an environment with specific applications and versions or you might have a particular part of your workflow that requires a package built for an older version of Python.

Environments can be created, switched on and switched off as required.
Example 1: Environment with older versions of packages

Create an environment with bowtie2 version=2.2.5 and bamhash version=1.0 :

conda create -n project1 bowtie2=2.2.5

 

This creates the environment with the first of the packages, you will see the environment being built.

The next step is to activate this package:

source activate project1

 

The command prompt will change, with the name of the environment in parentheses before the regular prompt:

(project1) [issev001@login2.marc1 ~]$

 

This environment is isolated from the main Bioconda installation. You will need to install the specific applications and packages you need directly into this environment. In our case we still need to install bamhash.

conda install bamhash=1.0

 

You can continue to install packages into this environment and run your scripts and analyses as normal. All your drives, directories and files can be accessed as normal.

When you have finished working in the environment and want to return to the regular prompt and the main Bioconda system:

source deactivate

 

and the command prompt will return to normal:

[issev001@login2.marc1 ~]$

 
### Creating a Python 2 environment

Originally, we downloaded and installed Bioconda built around Python 3 (which is the version of Python we should now be using). Sometimes though, we need to work with a legacy Python 2 package (htseq is an example of a legacy Python 2 package) that has not been updated to work with Python 3, or we need to temporarily revert to Python 2 in order to collaborate with a colleague who has not made the transition.

In these cases, we can create a Python 2 environment:

conda create -n project2 python=2.7

 

activate it as before:

source activate project2

 

and then install the packages we need:

conda install htseq

 

When finished using the environment, as before:

source deactivate

### Example 3: Creating an R environment

Although Conda was originally designed to manage Python, it’s just as happy dealing with R. If you need to have multiple different versions of R available for testing purposes you can create separate R environments for each one.

For example, to create an R environment called r_env (with the latest version of R available):

conda create -n r_env r-base r-essentials

activate as before:

source activate r_env

and deactivate

source deactivate

More information on using R with Conda can be found on the Anaconda documentation site.
