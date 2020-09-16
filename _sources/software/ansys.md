Ansys 
=====
    
Versions of Ansys Fluent and CFX are installed for Leeds researchers who
have access to either their own or a departmental license. This supports
the Infiniband interconnect so can be used for jobs of \>16 (for ARC2)
or \>24 (for ARC3) processors in size.

Information on Ansys can be found on the Ansys web site:\
<http://www.ansys.com/en-GB>

::: {#toc_container .no_bullets}
Contents

-   [[1]{.toc_number .toc_depth_1} Setting up the
    license](#Setting_up_the_license)
    -   [[1.1]{.toc_number .toc_depth_2} Running
        Fluent](#Running_Fluent)
    -   [[1.2]{.toc_number .toc_depth_2} Running CFX](#Running_CFX)
    -   [[1.3]{.toc_number .toc_depth_2} Running
        Chemkin](#Running_Chemkin)
-   [[2]{.toc_number .toc_depth_1} Additional Step for Using Ansys the
    First Time](#Additional_Step_for_Using_Ansys_the_First_Time)
:::

[Setting up the license]{#Setting_up_the_license}
-------------------------------------------------

The license is obtained by setting the
[ANSYSLMD\_LICENSE\_FILE]{.lang:default .decode:true .crayon-inline}
variable. To set it in bash do:\
`$ export ANSYSLMD_LICENSE_FILE=<port>@<host>`\
If accessing for the first time, there is an additional step (see the
next section on this page) required to choose whether you are using
commercial or academic licenses. To get the values of
[\<port\>@\<host\>]{.lang:default .decode:true .crayon-inline} specific
to your group/department please contact the Client IT Team via [Service
Now](https://leeds.service-now.com/it).

To make Ansys Fluent and CFX available for use:

    $ module add ansys

To load a specific version of Ansys, specify this on the module command
i.e.:

    $ module add ansys/17.1

### [[Running Fluent](https://arc.leeds.ac.uk/software/applications/ansys/fluent)]{#Running_Fluent}

Fluent specific information can be found by clicking the link above.

### [[Running CFX](https://arc.leeds.ac.uk/software/applications/ansys/cfx)]{#Running_CFX}

CFX specific information can be found by clicking the link above.

### [[Running Chemkin](https://arc.leeds.ac.uk/?page_id=4521&preview=true)]{#Running_Chemkin}

Chemkin specific information can be found by clicking the link above.

 

[Additional Step for Using Ansys the First Time]{#Additional_Step_for_Using_Ansys_the_First_Time}
-------------------------------------------------------------------------------------------------

Before running the Ansys module for the first time, there is a per-user
setting that chooses whether commercial (default) or academic licenses
should be used.

**For research purposes you should normally be using the academic
licenses, unless you are untertaking commercially funded research.**

**Check with your supervisor of faculty IT if you need clarification on
this.**

You will need a SSH connection with X-forwarding enabled to configure
this setting. Documentation for gaining ssh access to the ARC systems is
in the web pages that describe how to login in from each of the 3 main
operating systems i.e., [Logon from
Linux](https://arc.leeds.ac.uk/using-the-systems/getting-started/logon-from-linux/),
[Logon from Mac OS
X](https://arc.leeds.ac.uk/using-the-systems/getting-started/logon-from-mac-os-x/)
and [Logon from
Windows](https://arc.leeds.ac.uk/using-the-systems/getting-started/logon-from-windows/).

If you have not already done so, set the license server and port:\
`$ export ANSYSLMD_LICENSE_FILE=<port>@<host>`\
Next, ensure that you have the ansys module loaded for the particular
version you wish to configure its licenses, e.g.:

    $ module add ansys/17.1

for ansys version 17.1 (the latest version on the ARC clusters)

You now need to launch the license administration interface. The
simplest way to do this is to start cfx:

    $ cfx5

and select Tools/Ansys client Licensing Utility from the menu.

This will present you with the following window:

![Configuring a license for Ansys using the license
manager.](https://arc.leeds.ac.uk/wp-content/uploads/2016/01/ansys_license.jpg){.size-full
.wp-image-2419 width="840" height="542"
sizes="(max-width: 840px) 100vw, 840px"
srcset="https://arc.leeds.ac.uk/wp-content/uploads/2016/01/ansys_license.jpg 840w, https://arc.leeds.ac.uk/wp-content/uploads/2016/01/ansys_license-300x194.jpg 300w, https://arc.leeds.ac.uk/wp-content/uploads/2016/01/ansys_license-768x496.jpg 768w"}

Select "set license preferences for user abcxyz"

In the next window, select the product you wish to configure (e.g. 12.1)

![Selecting the right license
preferences.](https://arc.leeds.ac.uk/wp-content/uploads/2016/01/ansys_license1.jpg){.size-full
.wp-image-2423 width="372" height="196"
sizes="(max-width: 372px) 100vw, 372px"
srcset="https://arc.leeds.ac.uk/wp-content/uploads/2016/01/ansys_license1.jpg 372w, https://arc.leeds.ac.uk/wp-content/uploads/2016/01/ansys_license1-300x158.jpg 300w"}

In the next window that appears, select the radio button that says Use
academic licenses:

![[]{#longdesc-return-2424} Finally select the academic license
option.](https://arc.leeds.ac.uk/wp-content/uploads/2016/01/ansys_license3.jpg){.size-full
.wp-image-2424 width="925" height="634"
sizes="(max-width: 925px) 100vw, 925px"
srcset="https://arc.leeds.ac.uk/wp-content/uploads/2016/01/ansys_license3.jpg 925w, https://arc.leeds.ac.uk/wp-content/uploads/2016/01/ansys_license3-300x206.jpg 300w, https://arc.leeds.ac.uk/wp-content/uploads/2016/01/ansys_license3-768x526.jpg 768w"}

Select **OK**, then exit the license manager.

This will configure Ansys (both Fluent and CFX) to use Academic licenses
for all future use.
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
