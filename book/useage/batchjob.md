# Batch jobs

Utilising the computational power of the HPC facilities at Leeds is organised through a batch job scheduling system. This involves users submitting a script that outlines the resources required and the program to be run to the scheduler which allocates that job a position in the queue of jobs. The scheduler software run on both ARC3 and ARC4 is [Son of Grid Engine](https://arc.liv.ac.uk/trac/SGE), plus locally developed and implemented patches.

## Job scripts

The scripts submitted are referred to as **job scripts** or **job submission scripts** these are shell scripts (files ending `.sh`) and at a bare minimum specify:

- how long the job needs to run for
- on how many processors to use (assumed 1 unless otherwise told)

With this information, the scheduler is able to run jobs at some point in the future when the resources become available. Crucially, the queue is **not** a first-come-first-serve and implements a [fair-share policy](#fair-share-policy) to guide the scheduler towards allocating resources fairly between different faculties.

The common commands used on HPC to interact with batch jobs are:

- [`qsub`](#the-hello-world-job-script) - submits a job script to the scheduler
- [`qstat`](#monitoring-jobs) - checks the status of submitted jobs
- [`qdel`](#deleting-jobs) - deletes a specified job from the queue

### Writing jobs scripts on HPC

We encourage users to write their job submission scripts using text editor tools available on ARC3 and ARC4 such as:

- `nano` (recommended for beginners)
- `gedit`
- `vim`
- `emacs`

The basic useage to create a new job submission file on HPC would be `nano job_submit.sh` or `vim job_submit.sh`. This opens the new empty file in the text editor ready for you to write its contents.

``` {warning}
Job scripts written on Windows computers contain different invisible line ending characters that lead to job submission failures such as
`/bin/bash^M: bad interpreter: No such file or directory` <br>
You can use the command `dos2unix job_script.sh` on HPC to convert your script to the correct line ending.
```

### The Hello world job script

In this basic hello world job script example we've got a job script called `job_script1.sh` requests a single core, 1GB of RAM, 15 minutes of run time in order to run some R code.

```shell
#R single core submission script

#Run with current environment (-V) and in the current directory (-cwd)
#$ -V -cwd

#Request some time- min 15 mins - max 48 hours
#$ -l h_rt=00:15:00

#Request some memory per core
#$ -l h_vmem=1G

#Get email at start and end of the job
#$ -m be

#Now run the job
module load R
R CMD BATCH R.in R.out
```

We can submit this script to the scheduler by using `qsub`:

```bash
$ qsub job_script1.sh
Your job 42 ("job_script1.sh") has been submitted
```

This returns some text to confirm our job has been submitted and provides us with the jobs unique ID number (in this case 42).

``` {note} **Array jobs** <br>
If you intend to runs multiple similar jobs with the same resource specification, we recommend using the [task array system](./taskarrays).
```

### Resource specification

### Monitoring jobs

#### Deleting jobs

### Job output

### Job holding

### Fair share policy

The fair-share policy is two-tiered policy that takes into account the useage of a faculty as a whole and the past useage of the user. In the first tier of the policy faculties are allocated a share of the queue space on the basis of funding, meaning that faculties do not have equal shares of system capacity. The fair-share policy then determines an initial faculty level priority based on the faculties share and the total useage by all faculty member users.

```{note}
The fair share policy and levels are set by the ARC management group and cannot be altered by the system’s support team.
```

Next the fair-share policy determines an individual users job priority. Initially, all users from a faculty have the same initial priority which then decreases based on the users useage of the HPC. Essentially, this means that a user with recent (the last 7 days) heavy usage will have their jobs reduced in priority to allow other user’s jobs to run.

The fair-share policy has the following consequences:

- The more useage by members of your faculty, the more jobs submitted by users in the faculty, the longer you have to wait in the queue
- If you submit lots of jobs your subsequent jobs will have a lower priority and you will have to wait longer in the queue and so will jobs submit by other users from your faculty for the next 1 or 2 weeks
- Jobs submitted by people from another faculty may start before yours
- Jobs submitted after your job may start before yours

```{note}
There is no test queue on the ARC service. To help determine your most efficient useage we recommend submit small test jobs.
The smaller the jobs the less time it will wait in the queue and the less impact it will have on your priority.
```
