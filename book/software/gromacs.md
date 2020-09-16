Gromacs {#gromacs .entry-title}
=======

Gromacs is freely available and open source software.

::: {#toc_container .no_bullets}
Contents

-   [[1]{.toc_number .toc_depth_1} Setting the module
    environment](#Setting_the_module_environment)
-   [[2]{.toc_number .toc_depth_1} Executable naming
    conventions](#Executable_naming_conventions)
-   [[3]{.toc_number .toc_depth_1} Batch execution](#Batch_execution)
    -   [[3.1]{.toc_number .toc_depth_2} Serial
        execution](#Serial_execution)
    -   [[3.2]{.toc_number .toc_depth_2} Parallel
        execution](#Parallel_execution)
:::

[ Setting the module environment]{#Setting_the_module_environment}
------------------------------------------------------------------

A number of versions of Gromacs are available on the facility.

To set up the environment, when you log in, use (for example):

    $ module add gromacs/4.5.3

To add the executables for this specific version to your environment.

Alternatively:

    $ module add gromacs

Will add the executables for the default 4.6.3 version.

[ Executable naming conventions]{#Executable_naming_conventions}
----------------------------------------------------------------

The main executables available are :

  ------------------------------------------------------------------- ------------------------------------------
  [mdrun]{.lang:default .decode:true .crayon-inline}                  single precision serial executable
  [mdrun\_d]{.lang:default .decode:true .crayon-inline}               double precision serial executable
  [mpirun mdrun\_mpi]{.lang:default .decode:true .crayon-inline}      single precision parallel MPI executable
  [mpirun mdrun\_mpi\_d]{.lang:default .decode:true .crayon-inline}   double precision parallel MPI exectable
  ------------------------------------------------------------------- ------------------------------------------

However, the naming convention for [Gromacs]{.lang:default .decode:true
.crayon-inline} versions below [4.6.3]{.lang:default .decode:true
.crayon-inline} are a little different:

  ----------------------------------------------------------- -------------------------------------------
  [mdrun.MPI]{.lang:default .decode:true .crayon-inline}      single precision, parallel MPI executable
  [mdrun\_d.MPI]{.lang:default .decode:true .crayon-inline}   double precision, parallel MPI executable
  ----------------------------------------------------------- -------------------------------------------

There are also single/double precision versions of the tools that come
with the application, with the same naming scheme as above. For more
information look at the [Gromacs](http://www.gromacs.org/) homepage and
at the [Gromacs documentation](http://www.gromacs.org/Documentation).

[ Batch execution]{#Batch_execution}
------------------------------------

### [ Serial execution]{#Serial_execution}

An example script, [example\_serial.sh]{.lang:default .decode:true
.crayon-inline} , looks like:

    #!/bin/bash
    #$ -cwd -V 
    # request 10 hours of runtime
    #$ -l h_rt=10:00:00
    mdrun_d  [...]

This requests 10 hours of runtime, to run in the current directory(
[-cwd]{.lang:default .decode:true .crayon-inline} ) and using the
current environment ( [-V]{.lang:default .decode:true .crayon-inline} ),
using the double precision version of mdrun, and where
[\[...\]]{.lang:default .decode:true .crayon-inline} represents the
arguments to mdrun. More memory per core can be requested, 2Gb for
instance, by adding the line [\#\$ -l h\_vmem=2G]{.lang:default
.decode:true .crayon-inline} to the script. For more options look at
[qsub
options](https://arc.leeds.ac.uk/using-the-systems/why-have-a-scheduler/qsub-qrsh-usage/).
The script can be submitted with:

    $ qsub example_serial.sh

### [ Parallel execution]{#Parallel_execution}

For the parallel version, an example script,
[example\_parallel.sh]{.lang:default .decode:true .crayon-inline} will
take the form:

    #!/bin/bash
    #$ -cwd -V 
    # request 10 hours of runtime
    #$ -l h_rt=10:00:00
    # request 4 cores
    #$ -pe ib 4
    mpirun mdrun_mpi_d 

This requests 10 hours of runtime, to run in the current directory(
[-cwd]{.lang:default .decode:true .crayon-inline} ), using the current
environment ( [-V]{.lang:default .decode:true .crayon-inline} ), running
on 4 cores ( [-pe ib 4]{.lang:default .decode:true .crayon-inline} ),
using the double precision parallel version of mdrun, and where
[\<options\>]{.lang:default .decode:true .crayon-inline} represents the
arguments to [mdrun]{.lang:default .decode:true .crayon-inline} .

More memory per core can be requested, 2Gb for instance, by adding the
line [\#\$ -l h\_vmem=2G]{.lang:default .decode:true .crayon-inline} to
the script. For more options look at [qsub
options](https://arc.leeds.ac.uk/using-the-systems/why-have-a-scheduler/qsub-qrsh-usage/).
The script can be submitted with:

    $ qsub example_parallel.sh
:::

::: {.entry-meta}
:::
:::
:::
:::

::: {.container}
::: {.site-info}
::: {.footer-credit}
Built with [Make](https://thethemefoundry.com/make/){.theme-name}. Your
friendly WordPress page builder theme.
:::
:::
:::
:::
