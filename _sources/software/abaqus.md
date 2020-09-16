Abaqus
======

Contents

-   [[1]{.toc_number .toc_depth_1} Introduction](#Introduction)
-   [[2]{.toc_number .toc_depth_1} Licence
    Management](#Licence_Management)
-   [[3]{.toc_number .toc_depth_1} Preparation](#Preparation)
-   [[4]{.toc_number .toc_depth_1} Setting Up a Job](#Setting_Up_a_Job)
-   [[5]{.toc_number .toc_depth_1} Parallel
    Processors](#Parallel_Processors)
-   [[6]{.toc_number .toc_depth_1} Submitting a Job](#Submitting_a_Job)
-   [[7]{.toc_number .toc_depth_1} Example Script](#Example_Script)
-   [[8]{.toc_number .toc_depth_1} User Defined Fortran
    subroutines](#User_Defined_Fortran_subroutines)
-   [[9]{.toc_number .toc_depth_1} Checkpointing](#Checkpointing)
:::

#### [Introduction]{#Introduction}

The purpose of this guide is to get the first few models running with
generic options so that you can start getting results back and have a
working system that you can modify to suit the specific needs of your
work. Because of this there will not be an in depth discussion of the
wide range of options and commands available, however there are
extensive help files available from the command line. Typing
[help]{.lang:default .decode:true .crayon-inline} will give a list of
built-in commands, [help \<command\>]{.lang:default .decode:true
.crayon-inline} will then give more specific information on that command
eg. [help help]{.lang:default .decode:true .crayon-inline} gives you
information about the help command. Entering [info info]{.lang:default
.decode:true .crayon-inline} will open a help manual and [info
\<command\>]{.lang:default .decode:true .crayon-inline} will give
specific information about that command eg. [info qsub]{.lang:default
.decode:true .crayon-inline} details the qsub command which submits a
job to the queue.

#### [Licence Management]{#Licence_Management}

Abaqus is a licensed application with a limited number of license
tokens. Running an Abaqus analysis requires more than one token. The
number of tokens needed (T) is given by the formula T = int(5 x
N\^0.422) where N is the number of cpu cores. More simply, for common
job sizes the numbers are:

  Number of cores   Tokens required
  ----------------- -----------------
  1                 5
  4                 8
  8                 12
  12                14
  16                16
  24                19
  32                21
  64                28

**Good practice** would recommend not to run 5 jobs using 12 cpu cores
each (that would require 70 license tokens, i.e. over half the available
number of tokens)

For information, Abaqus scales efficiently to 4 processors, relatively
well to 8 processors but poorly further. Trying to run a job over more
that 8 to 12 cpu cores won't increase the performances (and running over
more than the number of cpu core per node will even decrease the
performance).

#### [Preparation]{#Preparation}

First of all you will need an account on the facility and a suitable
piece of software to access it. I will be using WinSCP to do this so
keep in mind that if you are using an alternative this may have an
effect.

Running an Abaqus job from the command line, which is how you perform an
analysis, uses an input file with the extension [.inp]{.lang:default
.decode:true .crayon-inline} . This can be created from your model file
in the Abaqus CAE by right clicking the job in the model tree and
selecting [Write Input]{.lang:default .decode:true .crayon-inline} .
This can also be done from the job manager. This will create a file
called [\<job\_name\>.inp]{.lang:default .decode:true .crayon-inline}
which is what Abaqus will use.

When logged in you will have a home directory (WinSCP should send you
here automatically). If you select the open directory option above the
remote directory window and select [Add]{.lang:default .decode:true
.crayon-inline} in the [Session bookmarks]{.lang:default .decode:true
.crayon-inline} tab it will save a bookmark to this directory which make
it easier to navigate around. When working on the facility you should
use the /nobackup directory as it has more working space and faster data
speeds. Make a new directory in /nobackup and place the input file you
wish to analyse in there (also bookmark this directory as well).

#### [Setting Up a Job]{#Setting_Up_a_Job}

There are two sections to a job submission, the first describes the job
to the queue system and the second tells Abaqus to perform the analysis
and gives it the information it needs. The information for both is
contained in a script file held in your /nobackup directory. This script
file is a text file with the extension .sh and can be created by
right-clicking in the remote directory window and selecting
[New]{.lang:default .decode:true .crayon-inline} and
[File]{.lang:default .decode:true .crayon-inline} .

In this script starting the line with a hash ( [\#]{.lang:default
.decode:true .crayon-inline} ) symbol followed by a space comments out
the line so that it will be skipped when the program is run. This allows
you to leave notes within the code or save lines that you do not want
active at the time but may need later. Starting with a hash-dollar (
[\#\$]{.lang:default .decode:true .crayon-inline} ) and then a space
tells the system that this is a command to set up the queue. Having
nothing preceding the line means that it will be used by Abaqus to set
up the analysis.

For a simple script that will run an analysis on a single core use the
following, note that the lines have been numbered for clarity but these
numbers are not a part of the code:

    #$ -l h_rt=<run_time>
    #$ -l h_vmem=<amount_of_RAM_queue>
    #$ -m be
    #$ -M your@email_address
    #$ -cwd  -V
    module add abaqus
    export LM_LICENSE_FILE=@:$LM_LICENSE_FILE
    abaqus memory=<amount_of_RAM_abaqus> input=<input_file> job=<job_name> scratch="<nobackup_directory>" int

[\<run\_time\>]{.lang:default .decode:true .crayon-inline} is the amount
of time you are requesting from the queue, entered in the format
[hh:mm:ss]{.lang:default .decode:true .crayon-inline} . If the job
finishes before this it is fine but if the job takes longer it will
cancel when this time runs out so be sure to give more time than you
think you will need to avoid jobs failing midway through, keep in mind
however that requesting more time makes scheduling the jobs more
difficult and the maximum run time is 48 hours.

[\<amount\_of\_RAM\_queue\>]{.lang:default .decode:true .crayon-inline}
is the amount of memory you are requesting from the queue for each core
(one in this case). Entered in megabytes in the format
[\<number\>M]{.lang:default .decode:true .crayon-inline} or gigabytes as
[\<number\>G]{.lang:default .decode:true .crayon-inline} so that to
request 1000Mb you would type [1000M]{.lang:default .decode:true
.crayon-inline} or for 1Gb [1G]{.lang:default .decode:true
.crayon-inline} The default allocation is 1Gb. Note that Abaqus seems to
use between 1-2Gb to run so this needs to be taken into account as well.

    #$ -m be
    #$ -M emailaddress@leeds.ac.uk

requests that an email be sent you your account when the job begins and
finishes.

[-cwd -V]{.lang:default .decode:true .crayon-inline} requests that the
working directory is your current directory, so run this from the
directory you created in /nobackup, and sends the results to the same
place.

ARC2 is configured with 16 cores per node and 32Gb per node. ARC3 has 24
cores per node and 128GB memory.

[\<amount\_of\_RAM\_abaqus\>]{.lang:default .decode:true .crayon-inline}
is the total amount of memory that you wish to allow Aqaqus to use. When
running on a single core this will be the same as the
[\<amount\_of\_RAM\_queue\>]{.lang:default .decode:true .crayon-inline}
, when running on multiple cores it will be that value multiplied by the
number of cores you are running the analysis on. This is entered in a
slightly different format than before, in the format
[\<number\>mb]{.lang:default .decode:true .crayon-inline} to specify the
amount in megabytes. Therefore for 1000Mb enter [1000mb]{.lang:default
.decode:true .crayon-inline} .

**UPDATE**: [\<amount\_of\_RAM\_abaqus\>]{.lang:default .decode:true
.crayon-inline} is the amount of memory Abaqus will devote to the
solver. There are other memory overheads required by Abaqus. Thus, you
will need to define [\<amount\_of\_RAM\_abaqus\>]{.lang:default
.decode:true .crayon-inline} to be less than the total memory requested
from the queues to allow for this. For instance if you request two cores
at [2Gb]{.lang:default .decode:true .crayon-inline} each, then set
[memory=3000m]{.lang:default .decode:true .crayon-inline} for example,
which would allow [1Gb]{.lang:default .decode:true .crayon-inline} for
memory overheads.

[\<input\_file\>]{.lang:default .decode:true .crayon-inline} is the name
of the .inp input file you wish to analyse, therefore if the name of the
file is [analysis1.inp]{.lang:default .decode:true .crayon-inline} you
enter [analysis1.inp]{.lang:default .decode:true .crayon-inline} here.

[\<job\_name\>]{.lang:default .decode:true .crayon-inline} is the name
of the job, the output files will be named
[\<job\_name\>.\<extension\>]{.lang:default .decode:true .crayon-inline}
.

[\<nobackup\_directory\>]{.lang:default .decode:true .crayon-inline} is
the path of the directory you created in /nobackup. For example if you
made a directory on /nobackup called [username]{.lang:default
.decode:true .crayon-inline} the value for would be
[/nobackup/username]{.lang:default .decode:true .crayon-inline} . Note
that the speechmarks surrounding the directory path are to be typed in.

[\<license\_port\>]{.lang:default .decode:true .crayon-inline} is the
port where the Abaqus license you are using is located and
[\<license\_server\>]{.lang:default .decode:true .crayon-inline} is the
server for the same license. These details depend on the departmental
license you are using and should be available from local IT staff.

#### [Parallel Processors]{#Parallel_Processors}

To make use of several cpu cores to run your analysis use a script file
in the form:

    #$ -l h_rt=<run_time>
    #$ -l h_vmem=<amount_of_RAM_queue>
    #$ -m be
    #$ -M your@email_address
    #$ -pe smp 
    #$ -cwd  -V
      
    module add abaqus
    export LM_LICENSE_FILE=@:$LM_LICENSE_FILE
    abaqus memory=<amount_of_RAM_abaqus> cpus=$NSLOTS input=<input_file> job=<job_name> mp_mode=threads scratch="<nobackup_directory>" int

[\<number\_cores\>]{.lang:default .decode:true .crayon-inline} is the
number of cores you are requesting to be used for the analysis.
[\$NSLOTS]{.lang:default .decode:true .crayon-inline} is an
environmental variable, that is automatically set to equal
[\<number\_cores\>]{.lang:default .decode:true .crayon-inline} , and is
used to pass the number of cores to abaqus. Note that there will now be
a difference between the two memory requests, as described above.

**UPDATE**: [\<amount\_of\_RAM\_abaqus\>]{.lang:default .decode:true
.crayon-inline} is the amount of memory Abaqus will devote to the
solver. There are other memory overheads required by Abaqus. Thus, you
will need to define [\<amount\_of\_RAM\_abaqus\>]{.lang:default
.decode:true .crayon-inline} to be less than the total memory requested
from the queues to allow for this. For instance if you request two cores
at [2Gb]{.lang:default .decode:true .crayon-inline} each, then set
[memory=3000m]{.lang:default .decode:true .crayon-inline} for example,
which would allow [1Gb]{.lang:default .decode:true .crayon-inline} for
memory overheads.

#### [Submitting a Job]{#Submitting_a_Job}

To then submit a job you use the command line in WinSCP or the
comparable program that you are using. Enter [qsub
\<script\_file\_name\>]{.lang:default .decode:true .crayon-inline} where
the [\<script\_file\_name\>]{.lang:default .decode:true .crayon-inline}
is the name of the file created above that holds the settings for the
job. Therefore if this file is called [job\_submission.sh]{.lang:default
.decode:true .crayon-inline} then you would type [qsub
job\_submission.sh]{.lang:default .decode:true .crayon-inline} . If the
submission is successful the command line response should confirm this
and give a job ID. The status of your jobs can be queried with the line
[qstat -f]{.lang:default .decode:true .crayon-inline} . When the job
starts and ends you should receive a confirmation email and the results
of the analysis will be placed into your /nobackup directory.

#### [Example Script]{#Example_Script}

Just to provide an example script with some numbers in place, for a
model requesting 12Gb of memory and 4 hours to run an analysis of the
file [input.inp]{.lang:default .decode:true .crayon-inline} :

    #$ -l h_rt=4:00:00
    #$ -l h_vmem=1500M
    #$ -m be
    #$ -M me@leeds.ac.uk
    #$ -pe smp 8
    #$ -cwd  -V
    module add abaqus
    export LM_LICENSE_FILE=@license_server>
    abaqus memory=12000mb cpus=$NSLOTS input=input.inp job=input mp_mode=threads scratch="/nobackup/example-user/" int

#### [User Defined Fortran subroutines]{#User_Defined_Fortran_subroutines}

To include user defined Fortran subroutines, e.g.
[exampleroutine.f]{.lang:default .decode:true .crayon-inline} , you will
need to prepend the licence for the compiler to the licence path,
[export
LM\_LICENSE\_FILE=\<license\_port\>@license\_server\>:\$LM\_LICENSE\_FILE]{.lang:default
.decode:true .crayon-inline} . For example:

    #$ -l h_rt=4:00:00
    #$ -l h_vmem=1500M
    #$ -m be
    #$ -M your@email_address
    #$ -cwd  -V
    module add abaqus
    export LM_LICENSE_FILE=@license_server>:$LM_LICENSE_FILE
    abaqus memory=12000mb input=input.inp job=input user=exampleroutine scratch="/nobackup/example-user" int

This ensures that **both** Abaqus and the system default Intel Fortran
compiler are able to access their relevant licence servers.

#### [Checkpointing]{#Checkpointing}

Users sometimes find that their jobs take longer than the 48 hours
permitted by the scheduler to complete. Providing that your model does
not automatically re-mesh (for example, after a fracture), you may be
able to make use of Abaqus' built-in checkpointing function.

This will create a **restart** file (.res file extension) from which a
job that is killed can be restarted.

1\. Activate the restart feature by adding the line:

    *restart, write

at the top of your input file and run your job as normal. It should
produce a restart file with a [.res]{.lang:default .decode:true
.crayon-inline} file extension.

2\. Run the restart analysis with

    abaqus job=jobName oldjob=oldjobName ...

where [oldJobName]{.lang:default .decode:true .crayon-inline} is the
initial input file and [newJobName]{.lang:default .decode:true
.crayon-inline} is a file which contains only the line:

    *restart, read
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
