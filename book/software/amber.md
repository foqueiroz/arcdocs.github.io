AMBER {#amber .entry-title}
=====

Before you are able to access AMBER, you will be asked to read and agree
to the licence terms.

These can be viewed by following [this
link](http://ambermd.org/amber14.license.html). You are recommended to
print out and sign a copy for your own reference.

To access Amber, load its module through:

     
    $ module load amber 

This sets the [AMBERHOME]{.lang:default .decode:true .crayon-inline}
environment variable and your path to include the [bin]{.lang:default
.decode:true .crayon-inline} directory, with common executables as
follows:

  ------------------------------------------------------------------------- ----------------------------------------------------------------------------------
  [\$AMBERHOME/bin/sander]{.lang:default .decode:true .crayon-inline}       Serial version of SANDER
  [\$AMBERHOME/bin/sander.MPI]{.lang:default .decode:true .crayon-inline}   [sander]{.lang:default .decode:true .crayon-inline} built to run over Infiniband
  [\$AMBERHOME/bin/pmemd]{.lang:default .decode:true .crayon-inline}        Serial version of PMEMD
  [\$AMBERHOME/bin/pmemd.MPI]{.lang:default .decode:true .crayon-inline}    [pmemd]{.lang:default .decode:true .crayon-inline} built to run over Infiniband
  ------------------------------------------------------------------------- ----------------------------------------------------------------------------------

Example job submission scripts.
-------------------------------

The following script will run pmemd on 16 cores for 48 hours, the module
command is included in the submission script therefore it is not
necessary to have the environment loaded prior to job submission:
[run.sh]{.lang:default .decode:true .crayon-inline} :

    #!/bin/sh
    #$ -cwd
    #$ -l h_rt=48:00:00
    #$ -pe ib 16
    module add amber

    l=md19
    f=md20
    mpirun pmemd.MPI  -O -i $f.in -o $f.out -inf $f.inf \
            -c gc90turn10wat.$l -ref gc90turn10wat.$l -r gc90turn10wat.$f \
            -p gc90turn10wat.top -x gc90turn10wat$f.x -e gc90turn10wat$f.ene

This script can be submitted to the batch queues with:

    % qsub run.sh
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
