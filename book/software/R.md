R {#r .entry-title}
=

Contents

-   [[1]{.toc_number .toc_depth_1} Setting up the path and
    environment:](#Setting_up_the_path_and_environment)
-   [[2]{.toc_number .toc_depth_1} Launching on the front
    end](#Launching_on_the_front_end)
-   [[3]{.toc_number .toc_depth_1} Running through an interactive
    shell](#Running_through_an_interactive_shell)
-   [[4]{.toc_number .toc_depth_1} Batch Execution](#Batch_Execution)
-   [[5]{.toc_number .toc_depth_1} Installing R
    packages](#Installing_R_packages)
    -   [[5.1]{.toc_number .toc_depth_2} R 2.15.0 and
        later](#R_2150_and_later)
:::

[Setting up the path and environment:]{#Setting_up_the_path_and_environment}
----------------------------------------------------------------------------

All required environment variables can be set by loading the R module,
to do this issue:

    $ module add R

[Launching on the front end]{#Launching_on_the_front_end}
---------------------------------------------------------

R can be launched by entering its name at the command prompt; i.e.:

    $ R

Please note that this method should not be used apart from for quick
tests. Exit the R console by typing.

    q()

[Running through an interactive shell]{#Running_through_an_interactive_shell}
-----------------------------------------------------------------------------

The following will launch R interactively via the batch queues.

    $ qrsh -cwd -V -l h_rt= R 

The [\<startup\_flag\>]{.lang:default .decode:true .crayon-inline} can
be [--save]{.lang:default .decode:true .crayon-inline} ,
[--no-save]{.lang:default .decode:true .crayon-inline} or
[--vanilla]{.lang:default .decode:true .crayon-inline} . I have used
--vanilla but information on the meaning of these flags can is
[here](https://stat.ethz.ch/R-manual/R-devel/library/base/html/Startup.html).
In the above command, is the length of real-time the shell will exist
for. e.g. to run R for 6 hours:

    $ qrsh -cwd -V -l h_rt=6:00:00 R --vanilla

This will run R from within the terminal from which it was launched.

[Batch Execution]{#Batch_Execution}
-----------------------------------

To run R in batch-mode you must first generate a list of commands for R
to process in a file, e.g. [r.in]{.lang:default .decode:true
.crayon-inline}. You needed to make sure that this file is executable.
You can do this by running the command [chmod u+x .sh]{.lang:default
.decode:true .crayon-inline}. You can check this by running the command
[ls -la]{.lang:default .decode:true .crayon-inline} command and the
information for that line will contain an x for execute like this
[-rwxr--r--]{.lang:default .decode:true .crayon-inline}.

A script must then be created that will request resources from the
queuing system and launch the R executable; script
[runR.sh]{.lang:default .decode:true .crayon-inline} :

    #!/bin/bash
    # Run in current working directory and use current environment
    #$ -cwd -V
    # Set a 6 hour limit
    #$ -l h_rt=6:00:00
    #Request more memory, the default is 1Gb
    #$ -l h_vmem=1536M
    # Load R module
    module add R
    # run R using command file
    # CMD BATCH flag should be given to suppress graphics
    R CMD BATCH r.in r.out

This can be submitted to the queuing system using:

    $ qsub runR.sh

The files for a simple R test example are available to download in this
tar
file,[R.tar](https://arc.leeds.ac.uk/wp-content/uploads/2016/01/R.tar).

[Installing R packages]{#Installing_R_packages}
-----------------------------------------------

Given the large number of R packages available and pace of development,
it is preferable that users install the packages they need as opposed to
using a centrally provided set of packages.

### [R 2.15.0 and later]{#R_2150_and_later}

To install package [foo]{.lang:default .decode:true .crayon-inline} ,
start an R session by entering its name at the command prompt; i.e.:

    $ R

and then from within R, install the package:

    >install.packages('foo')

This will install the package and any dependencies that are required.
The package should then be accessible from subsequent R interactive
sessions and batch jobs.

### 
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
