# Troubleshooting jobs on HPC

Sometimes things go wrong when we use HPC. This is a fact of life. This can be for many reasons, sometimes it can be HPC related, sometimes it might be to do more specifically with the code you're running.

```{note}
Whilst the Research Computing team provide support for the HPC we can't troubleshoot specific problems you might have with individual languages or scientific software packages. In those cases we'll advise you to speak to your supervisor or contact the original developers for support.
```

This page will aim to cover some of the most common problems people encounter when using the HPC and provide you with the tools you'll need to fix things or in some cases work out what's going wrong.

## Failures submitting your job

When you submit a job to the scheduler it performs a number of quick checks to ensure it knows what you're requesting. If you've provided any incorrect parameters you will recieve an error after using the `qsub` command.

If this happens check the following in your submission script:

- Did you request an acceptable amount of time with `#$ -l h_rt=hh:mm:ss`? (e.g. less than 48 hours)
- Did you request an acceptable amount of memory for a given node? (e.g. on ARC4 192GB or less)
- Did you ensure there were no spaces between a scheduler parameter and value?
- Do you have permission to access the resource you're requesting? (e.g. private nodes)

The `qsub` command also includes an option that allows you to verify whether your job script is acceptable to the scheduler. You can use this to check your job will submit as follows:

```bash
$ qsub -w v my_job.sh
verification: found suitable queue(s)
```

This output tells us our job script is acceptable to the scheduler and should enter the queue.

## Failures during the job run

Jobs can fail during the job run for a wide variety of reasons such as:

- insufficient resources, if your job tries to use more memory or run for more time than requested the job is automatically killed by the scheduler
- lack of space in your [home directory](./nobackup#home-directory)
- bad line ending characters in your job submission script
- failure to checkout software licenses

Your first step to try and identify why a job has failed is to check the [job output and error files](./batchjob#job-output) for any of the following:

- code failures and exit codes
- code failures because file or directory do not exist
- syntax errors in your submission script
- permission errors prevent file read or write

## Job output and error files

