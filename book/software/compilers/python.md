# Python 

Introduction

A number of different versions of Python are available on our systems.

We also provide a library of some of the most common Python packages for numerical work; if you wish to use it, please load the module python-libs . Documentation can be found here.
Usage
Setting the module environment

When you log in, load the appropriate module for the version of Python you wish to use e.g. python/native (for the version supplied by the operating system (2.7.5 on arc3, 2.6.6 on arc2/marc1/polaris)

e.g.


module add python/3.6.0

Python programs/scripts

We recommend that python programs begin with the following line:


#!/bin/env python

This will cause it to be automatically run under the first version of python found in your PATH . e.g. the loaded python module.
Compilers

Those who wish to build their own Python libraries on top of this module may want to use the same compiler for compatibility and so avoid build issues.

The

python

module now sets environment variable PYTHON_BUILD_MODULES . The modules used to build a particular python version can be shown by loading the appropriate module and executing echo $PYTHON_BUILD_MODULES

Please note that, although we previously used the version of GCC bundled with the operating system, this is no longer the case for more recent pythons.
