# Anaconda

Anaconda on ARC4

Anaconda is now our actively supported Python distribution on ARC4. For the moment ARC3 has the ‘old’ Python and python-libs system but as soon as we
can we will install an Anaconda module on ARC3 too.

To use Anaconda, run:

module load anaconda

This will make available the Conda package management tool, but it will not load any environment. You may wish to load and use the ‘base’ environment which has the default Python 3.7.4 and the Python packages made available in the Anaconda 2019.10 release.

You can see the packages and versions available in the base environment:

conda list

and to load this base environment:

source activate base

to deactivate the environment after use:

conda deactivate

We recommend, however, that you do not use the base environment but create and activate custom environments built to the specifications you need for your projects.

For example, if you wish to create a new ‘Python 3’ environment with the Pandas, Numpy and Scipy libraries named example_env_1, run:

conda create -n example_env_1 python=3 numpy scipy pandas

You’ll note that during the installation process that Conda will attempt to install the enviroment and it’s constituent packages in your home directory:

## Package Plan ##

environment location: /home/home02/issev001/.conda/envs/example_env_1

To load this environment:

source activate example_env_1

and to deactivate it after use:

conda deactivate

As your home directory has limited storage space you may wish to specify that new environment are built and stored in your /nobackup directory instead (but note that files are expired from /nobackup if they haven’t been used for 90 days)

To create an environment named example_env_2 in /nobackup (here as user issev001- you should replace this with your own named user directory) then:

conda create -p /nobackup/issev001/example_env_2 python=3 matplotlib pandas numpy

This time, you’ll note that Conda will install the environment and it’s constituent packages in the directory you specified:

## Package Plan ##

environment location: /nobackup/issev001/example_env_2

To load this new environment:

source activate /nobackup/issmcal/example_env_2

and to deactivate after use:

conda deactivate

At any time, you can list your Conda environments (whether in your home directory or elsewhere:

conda env list

For full instructions on using Conda:

https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html
Anaconda on ARC3

Anaconda Python uses a package management system called Conda which allows users to easily download and install a large range of Python, R and other packages and libraries into their own user directories, without having to use environment modules, follow complex installation instructions or to ask us for help.

As it uses the same package management system as Anaconda Python, it will also give you a Python 3 (or Python 2) environment without having to use the system python and python-libs modules.

How do I install it?
On our HPC clusters you have a HOME directory shared across the machines so we recommend that you install into a dedicated /nobackup directory (eg. /nobackup/<username>/conda3 for a Python3 Conda install).

It is also possible to create a shared Bioconda installation across (for example) a research group. Please contact us if you would like to discuss this further.
Installation instructions:

1. Download the Miniconda installer
At a command prompt, enter:

wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh

If you wish to confirm the download is valid, Miniconda provide a set of MD5 checksums for these installers. These are available linked from the Miniconda Homepage

2. Run the installer:

bash Miniconda3-latest-Linux-x86_64.sh

You will be prompted to agree to a set of licence terms (hit [SPACE] to page down) Enter yes when prompted to agree

3. Setting the install directory
Next, you will be prompted for an installation directory. By default this will be your home directory (here for user issev001):

Miniconda3 will now be installed into this location:
/home/marc1_d/issev001/miniconda3

- Press ENTER to confirm the location
- Press CTRL-C to abort the installation
- Or specify a different location below

[/home/marc1_d/issmcal/miniconda3] >>>

To accept this location, hit [ENTER] or specify an alternative installation directory (which is recommended as you will easily fill up your Home directory otherwise!).

For example, you may wish to install into your /nobackup directory so just type the full path to this directory, for example (for user issev001):

[/home/marc1_d/issmcal/miniconda3] >>> /nobackup/issev001/miniconda3

Note:

Files on /nobackup are automatically deleted after 90 days if they have not been accessed. You will need to take steps to make sure that this directory is not expired.

4. Final steps
You will be prompted for the installer to add a line to your ~/.bashrc file. This will allow Conda to be automatically loaded (and thus all of it applications available) every time you log in:

Do you wish the installer to prepend the Miniconda3 install location
to PATH in your /home/marc1_d/issmcal/.bashrc ? [yes|no]
[no] >>>

Reply yes and hit [ENTER]

The installer will finish. Logout and then back in again and the Conda environment is ready for use.
Configuring Conda

Before first use, the conda package management system needs some initial configuration.

Make sure all the components are updated to their latest versions by entering:

conda update conda

at the command prompt. If there are any updates, you will be prompted to agree their installation.

Add the a number of channels. This step is required so that the conda installer knows where to get the installation files for your applications from. Again, at the command prompt:

conda config --add channels r
conda config --add channels bioconda
conda config --add channels conda-forge

 

That’s it. You can now use Conda to automatically install a range of applications and libraries.
Installing applications and libraries

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

 
Example 2: Creating a Python 2 environment

Originally, we downloaded and installed Bioconda built around Python 3 (which is the version of Python we should now be using). Sometimes though, we need to work with a legacy Python 2 package (htseq is an example of a legacy Python 2 package) that has not been updated to work with Python 3, or we need to temporarily revert to Python 2 in order to collaborate with a colleague who has not made the transition.

In these cases, we can create a Python 2 environment:

conda create -n project2 python=2.7

 

activate it as before:

source activate project2

 

and then install the packages we need:

conda install htseq

 

When finished using the environment, as before:

source deactivate

Example 3: Creating an R environment

Although Conda was originally designed to manage Python, it’s just as happy dealing with R. If you need to have multiple different versions of R available for testing purposes you can create separate R environments for each one.

For example, to create an R environment called r_env (with the latest version of R available):

conda create -n r_env r-base r-essentials

activate as before:

source activate r_env

and deactivate

source deactivate

More information on using R with Conda can be found on the Anaconda documentation site.

More environment commands
You can list all of the environments you currently have available:

conda info --envs

 

and delete an environment you no longer need:

conda remove --name  --all

 
