# Batch jobs

Utilising the computational power of the HPC facilities at Leeds is organised through a batch job scheduling system. This involves users submitting a script that outlines the resources required and the program to be run to the scheduler which allocates that job a position in the queue of jobs. The scheduler software run on both ARC3 and ARC4 is [Son of Grid Engine](https://arc.liv.ac.uk/trac/SGE), plus locally developed and implemented patches.

## Job scripts

The scripts submitted are referred to as **job scripts** or **job submission scripts** these are shell scripts (files ending `.sh`) and at a bare minimum specify:

- how long the job needs to run for
- on how many processors to use (assumed 1 unless otherwise specified)

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

The basic useage to create a new job submission file on HPC would be `nano job_submit.sh` or `vim job_submit.sh`. This opens the new empty file in the text editor ready for you to write it's contents.

``` {warning}
Job scripts written on Windows computers contain different invisible line ending characters that lead to job submission failures such as
`/bin/bash^M: bad interpreter: No such file or directory` <br>
You can use the command `dos2unix job_script.sh` on HPC to convert your script to the correct line endings.
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

Once you've submitted a job you can monitor its progress in the queue using the command `qstat JOBID` where `JOBID` is the unique numeric ID of your submitted job.

In the example below we've just submitted a job and want to check its status in the queue.

```bash
$ qstat 54
job-ID  prior   name       user         state submit/start at     queue                          slots ja-task-ID 
-----------------------------------------------------------------------------------------------------------------
 54 0.00000 test_sub.s exuser     qw    08/21/2019 14:09:08                                    1        

```

Using `qstat` returns a table with the following columns:

- the job ID
- the job priority determined by the scheduler [fair share policy](#fair-share-policy)
- the name of the submission script
- the user who submitted the job
- the jobs state in the queue
    (`qw` for waiting; `r` for running; `hqw` for hold waiting, `Eqw` for errored whilst queueing, `t` for transferring state)
- the submission time, or if the job is running the start time
- the number of slots (cores) requested
- the task ID number if the job is a [task array](./taskarrays)

```{note}
If you run `qstat` expecting an output and nothing happens and your prompt is returned it means you have no jobs currently in the queue. This suggests your job has completed.
```

You can also pass the `qstat` command a number of additional arguments to view the queue or other users queues.

```bash
$ qstat -u 'username'
# where username is your own or another username

$ qstat -u '*'
# will return the entire queue
```

#### Deleting jobs

Sometimes a situation might arise where you need to delete one of your submitted jobs from the queue. You can do this with the straightforward command `qdel JOBID` where `JOBID` is the unique numeric ID of the job we wish to delete.

When the job is successfully deleted we get the following output:

```bash
$ qdel 42
exuser has deleted job 42
```

```{note}
You can only use `qdel` to delete your own submitted jobs from the queue, so don't try and be smart and clear the queue just for your jobs as it won't work.
```

### Job output

When a job runs it produces two output files by default even if you haven't specified your code to write a results file. These contain information from the standard output and standard error produced by your job and are are named following the pattern `submission_script.sh.oJOBID` and `submission_script.sh.eJOBID`. Where `submission_script.sh` is the name of your job script and `JOBID` is the unique numeric ID of the job when it was submitted.

For example, if we submitted a job called `test_run.sh` and it was given the job ID `4689` we'd expect the following files produced alongside any results files:

```bash
test_run.sh.o4689
test_run.sh.e4689
```

Both these files contain useful information about how the job progressed and are especially useful if your job encountered an error. You can read more about using these files to help troubleshoot problems in the [troubleshooting section](./troubleshooting).

### Job holding

Often a workflow can involve a number of steps in a process, where each steps requires the outputs of the previous and should only start when the previous step completes. The scheduler has a system of job dependencies built into it that allows you to submit a series of jobs and specify that jobs should be on hold until another job has completed.

For instance you could do this with two submission scripts `job1.sh` and `job2.sh`, where `job2.sh` should only begin once `job1.sh` has finished. You can specify this when submitting jobs as follows:

```bash
$ qsub job1.sh
Your job 626 ("job1.sh") has been submitted

$ qsub -hold_jid 626 job2.sh
Your job 627 ("job2.sh") has been submitted
```

`job2.sh` will then be held in the queue until `job1.sh` is completed.

This allows for developing a workflow of jobs that run one after another to complete long stepwise tasks.

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
