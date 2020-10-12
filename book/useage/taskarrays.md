# Task arrays

## When to use task arrays

Situations often arise when you want to run many almost identical jobs simultaneously, perhaps running the same program many times but changing the input data or some argument or parameter. One possible solution is to write a Python or Perl script to create all the qsub files and then write a BASH script to execute them. This is very time consuming and might end up submitting many more jobs to the queue than you actually need to. This is a typical problem suited to an SGE task array.

- only one qsub command is issued (and only one qdel command would be required to delete all jobs)
- only one entry appears in qstat
- the load on the SGE submit node is much less than that of submitting many separate jobs
- it is much easier for the user (you) to keep track of your related jobs

## How to use task arrays

The easiest way to think of a task array is as a job script with a built-in FOR loop. It makes use of an environment variable created by Sun Grid Engine- `$SGE_TASK_ID` . Consider this simple job submission script ( my_script.sh ):

```bash
# Use current working directory and current modules
#$ -cwd -V
# Request Wallclock time of 6 hours
#$ -l h_rt=06:00:00

# Tell SGE that this is an array job, with "tasks" numbered from 1 to 150
#$ -t 1-150

# Run the application passing in the input and output filenames
./myprog < data.$SGE_TASK_ID > results.$SGE_TASK_ID
```

It would be executed through the queues as normal using qsub my_script.sh .

As far as SGE is concerned, this is equivalent to 150 individual queue submissions in which `$SGE_TASK_ID` takes all the
values between 1 and 150 (inclusive), and where input and output files are indexed by the same ID.

In this example, the ‘input files’ would take the form data.1 , data.2 , data.3 etc. and the program would create output files of the form results.1 , results.2 , results.3 etc. (all in the current working directory). The example would require all input
files and put all output files into the same directory (the current working directory, defined by -cwd ).

As the script executes, the variable `$SGE_TASK_ID` will be replaced by the values indicated in the #$ -t 1-150 clause. So in this case, 1,2,3…150.

A small adjustment to the script would allow each job to run from a separate directory:

```bash
# Use current working directory and current modules
#$ -cwd -V
# Request Wallclock time of 6 hours
#$ -l h_rt=06:00:00

#$ -t 1-150

#create directory based on jobID
mkdir myjob-$SGE_TASK_ID

#change directory into the one just created
cd myjob-$SGE_TASK_ID

#execute a program from the folder above this one, putting the results here
../myprog-one > one.output

#execute a different program from the folder above this taking the file created (one.output) as input and putting the results here
../myprog-two < one.output > two.output
```

## The SGE ‘loop counter’

These examples use `$SGE_TASK_ID` starting at 1 and incrementing by 1 to some upper bound. It is a little more flexible than this however.

```bash
#$ -t 200-445:5
```

would allow `$SGE_TASK_ID` to take values from 200 (lower bound) to 445 (upper bound), incrementing by 5.

## Further examples

### Random filenames

The previous examples require all input files to be neatly indexed by number, but often this is not the case. If you have a list of randomly named files, then it is still possible to use `$SGE_TASK_ID` . Assume that you have a text file files.txt listing all of your input filenames (one per line) and that you know how many files you have (50 in the example below):

```bash
# Use current working directory and current modules
#$ -cwd -V
# Request Wallclock time of 6 hours
#$ -l h_rt=06:00:00

#$ -t 1-150

infile=$(sed -n -e "$SGE_TASK_ID p" jobfile1.txt)

./myprog < $infile
```

As the ‘loop’ in the script executes, it will read the filenames one by one from files.txt , assign them to the variable $infile and direct them into your program.

### Restricting the maximum number of concurrent tasks

In some situations it might be necessary to restrict the maximum number of tasks running at any point in time. This is a useful feature to ensure that your jobs don’t restrict other user jobs running.

To do this, add a -tc clause to the submission script:

```bash
#$ -t 1-5000
#$ -tc 50
```

This would run 5000 tasks but limit just 50 to run at any point in time.

## Using the SGE environment variables

The scheduler sets a number of environment variables during array jobs: `$SGE_TASK_FIRST` , `$SGE_TASK_LAST` and `$SGE_STEP_SIZE`. If you need your script to make things happen at the start or end of an array job, then this script shows how this can be done:

```bash
# Use current working directory and current modules
#$ -cwd -V
# Request Wallclock time of 6 hours
#$ -l h_rt=06:00:00

#$ -t 1-50

if[ $SGE_TASK_ID == $SGE_TASK_FIRST ]; then
  # do first-task stuff here
fi

# do normal job processing tasks here

if [ $SGE_TASK_ID == $SGE_TASK_LAST ]; then
  # do last-task stuff here
fi
```
