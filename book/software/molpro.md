Molpro {#molpro .entry-title}
======

Contents

-   [[1]{.toc_number .toc_depth_1} Setting up the
    environment](#Setting_up_the_environment)
-   [[2]{.toc_number .toc_depth_1} Scratch files](#Scratch_files)
-   [[3]{.toc_number .toc_depth_1} Example job
    scripts](#Example_job_scripts)
    -   [[3.1]{.toc_number .toc_depth_2} Serial job
        submission](#Serial_job_submission)
:::

[Setting up the environment]{#Setting_up_the_environment}
---------------------------------------------------------

To set up the environment load the version of the software that you want
to use. For example for version [2010.1.25]{.lang:default .decode:true
.crayon-inline} use:

    $ module add molpro/2010.1.25

[Scratch files]{#Scratch_files}
-------------------------------

Molpro writes a larges amount of temporary or scratch files. By default
these are written to [/scratch]{.lang:default .decode:true
.crayon-inline} directory on compute nodes. The [/scratch]{.lang:default
.decode:true .crayon-inline} directories are usually fairly small and
may fill up quickly causing jobs to fail. In this case, to avoid these
failures you may need to change the location of the scratch files. You
can redirect these scratch files to your directory on the high speed
filesystem [/nobackup]{.lang:default .decode:true .crayon-inline} ,
using the [-d]{.lang:default .decode:true .crayon-inline} switch. For
example:

    molpro -d /nobackup/your_scratch_directory 

The directory [/nobackup/your\_scratch\_directory]{.lang:default
.decode:true .crayon-inline} is a directory that you create in the
[/nobackup]{.lang:default .decode:true .crayon-inline} area. This is
most likely to be in your [/nobackup]{.lang:default .decode:true
.crayon-inline} area. Information about our [/nobackup]{.lang:default
.decode:true .crayon-inline} is available
<https://arc.leeds.ac.uk/using-the-systems/getting-started/nobackup/>.

It is best to use the version of molpro installed on the system as it is
installed and tested to run most efficiently but if you do choose to
install your own version of molpro you will need to configure it so that
it uses the [/scratch]{.lang:default .decode:true .crayon-inline} area
or you should use the [-d \$TMPDIR]{.lang:default .decode:true
.crayon-inline} or [-d /scratch]{.lang:default .decode:true
.crayon-inline} in your command line when you submit your job to the
batch system.

[Example job scripts]{#Example_job_scripts}
-------------------------------------------

### [Serial job submission]{#Serial_job_submission}

To run jobs through the batch scheduler, you need to submit them by
using the command [qsub \<script name\>]{.lang:default .decode:true
.crayon-inline} . The command to launch the serial version of molpro is
[molpro]{.lang:default .decode:true .crayon-inline} . Below is an
example job script. The example script below requests 1Gb RAM for 2
hours, using the current environment and running from the current
working directory:

    #!/bin/bash
    #$ -l h_rt=2:0:0
    #$ -l h_vmem=1G
    #$ -V
    #$ -cwd
    molpro -d /nobackup/your_scratch_directory  
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
