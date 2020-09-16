VMD (Visual Molecular Dynamics) {#vmd-visual-molecular-dynamics .entry-title}
===============================

Contents

-   [[1]{.toc_number .toc_depth_1} Description](#Description)
-   [[2]{.toc_number .toc_depth_1} Licensing](#Licensing)
-   [[3]{.toc_number .toc_depth_1} Application
    Homepage](#Application_Homepage)
-   [[4]{.toc_number .toc_depth_1} Basic Usage](#Basic_Usage)
-   [[5]{.toc_number .toc_depth_1} Further
    Resources](#Further_Resources)
:::

#### [Description]{#Description}

VMD (Visual Molecular Dynamics) is a molecular visualization program
with 3-D graphics and built-in scripting for displaying, animating, and
analyzing large biomolecular systems. It is also an effective front end
visualisation and interaction package for simulations running on NAMD.

#### [Licensing]{#Licensing}

UIUC Open Source Licence:\
<http://www.ks.uiuc.edu/Research/vmd/current/LICENSE.html>

Users are required to agree to the terms and conditions of the licence
before access can be granted. For further information contact us.

The authors require that any published work or images created using VMD
include the following reference:

Humphrey, W., Dalke, A. and Schulten, K., "VMD -- Visual Molecular
Dynamics" J. Molec. Graphics 1996, 14.1, 33-38.

#### [Application Homepage]{#Application_Homepage}

<http://www.ks.uiuc.edu/Research/vmd/>

#### [Basic Usage]{#Basic_Usage}

VMD can be run as either an interactive or batch application.

*Interactive Mode:*\
To run in interactive mode, first request an interactive session on one
of the backend compute nodes via the scheduler. If compute facilities
are available at the time of your request then a new terminal window
will be launched.

    qsh -cwd -V -l h_rt=01:00:00

will request an interactive shell with 1 hour of run-time (the -l h\_rt
parameter). Once in the interactive shell, enter these two commands to\
start a graphical session:

    module load vmd
    vmd

After exiting VMD, enter the [exit]{.lang:default .decode:true
.crayon-inline} command in the interactive window to close the session.

*Batch Mode:*\
As VMD has both a GUI and a text interface, scripts can be written to
automate functions such as loading molecules, creating representations,
making animations and analysing data. These commands can be entered in a
batch script and then submitted through the batch queue in the normal
way. An example script to create a movie of a molecular representation:

#### [Further Resources]{#Further_Resources}

**VMD tutorials:**\
<http://www.ks.uiuc.edu/Research/vmd/current/docs.html#tutorials>

**Youtube:**\
<https://www.youtube.com/watch?v=Fl3hmqCHYU4>\
<http://www.youtube.com/watch?v=CJEZydlXQp4>\
<http://www.youtube.com/watch?v=hChPzoEXK2Q>
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
