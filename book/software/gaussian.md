DLpoly {#dlpoly .entry-title}
======

To access this software you need to be a member of the DLPOLY group,
please contact <arc-help@lists.leeds.ac.uk> if you wish to be added to
this group.

The licence terms are available through [this
link](https://arc.leeds.ac.uk/software/applications/dlpoly/dlpoly-licence-conditions/).

::: {#toc_container .no_bullets}
Contents

-   [[1]{.toc_number .toc_depth_1} Setting the module
    environment](#Setting_the_module_environment)
-   [[2]{.toc_number .toc_depth_1} Batch execution](#Batch_execution)
    -   [[2.1]{.toc_number .toc_depth_2} Parallel
        execution](#Parallel_execution)
    -   [[2.2]{.toc_number .toc_depth_2} Serial
        execution](#Serial_execution)
:::

[Setting the module environment]{#Setting_the_module_environment}
-----------------------------------------------------------------

When you log in, do:

    $ module add dl_poly/4.05

To add the executables to your environment.

[Batch execution]{#Batch_execution}
-----------------------------------

For the [dl\_poly/4.05]{.lang:default .decode:true .crayon-inline}
module, parallel ( [DLPOLY.Z.MPI]{.lang:default .decode:true
.crayon-inline} ) and serial ( [DLPOLY.Z.SRL1]{.lang:default
.decode:true .crayon-inline} ) executables are available on the system.
For the [dlpoly/2.20]{.lang:default .decode:true .crayon-inline} module
the parallel executable is [DLPOLY.X.parallel]{.lang:default
.decode:true .crayon-inline} and the serial executable is
[DLPOLY.X]{.lang:default .decode:true .crayon-inline} .

### [Parallel execution]{#Parallel_execution}

An example script, [dlpoly.sh]{.lang:default .decode:true
.crayon-inline} , looks like:

    #$ -cwd -V 
    #$ -l h_rt=48:00:00
    #$ -pe ib 16
    mpirun DLPOLY.X.parallel 

This requests 48 hours of runtime on 16 processes. It can be submitted
with:

    $ qsub dlpoly.sh

### [Serial execution]{#Serial_execution}

The serial code is called DLPOLY.X, an example script
[dlpoly\_serial.sh]{.lang:default .decode:true .crayon-inline} can be
used to launch it:

    #$ -cwd -V 
    #$ -l h_rt=48:00:00
    DLPOLY.X 

To submit the above script do:

    % qsub dlpoly_serial.sh 
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
