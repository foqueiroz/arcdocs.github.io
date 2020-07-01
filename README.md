# Advanced Research Computing Documentation

This is the repository for the documentation for the University of Leeds HPC systems (ARC3 and ARC4). This is managed by the University of Leeds [Research Computing Team](https://arcleeds.github.io).

This repository automatically builds and deploys html content onto the repository github pages domain https://arcdocs.github.io/arcdocs-jupyterbook/

## Working with this project locally

You can get this project working locally by using the environment.yml file to create a conda environment that contains all the dependencies required to get started.

```{bash}
$ conda env create -f environment.yml
```

To build the html content locally you can use the `jupyter-book` command line tool:

```
# navigate to the repository root
$ cd arcdocs-jupyterbook
# sometimes worth running jupyter-book clean book/ to remove old files
$ jupyter-book build book/
```
### Windows

An important note is that the JupyterBook project does not currently support Windows ([see here for more](https://jupyterbook.org/advanced/advanced.html#working-on-windows)).
