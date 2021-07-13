# Advanced Job Examples

## Submitting Mixed Mode Jobs
The ‘mixed mode’ (MPI+OpenMP) programming model is currently only supported on ARC2. This typically involves MPI processes running across nodes and OpenMP threads upon each node with the total number of processes (MPI*OpenMP) equalling the number of physical processor cores.

Your code will need to call MPI_Init and make use of OpenMP directives. You will compile your code using an MPI wrapper and enabling OpenMP support, for example

`mpif90 -openmp example.f90 -o mixed.exe`

You will need to determine ppn, the number of MPI processes per node, and tpp, the number of OpenMP threads per MPI process.

Additionally, you can either ask for a given number of nodes nodes or for the total number of MPI processes np. Note that ppn is related to np since ppn = np/nodes.

Your submission script would then need to contain:

```bash
#$ -V 
#$ -l hr_t=01:00:00 
#$ -l nodes=$nodes, ppn=$ppn, tpp=$tpp
mpirun ./a.out
```
or

```bash
#$ -V
#$ -l hr_t=01:00:00 
#$ -l np=$np, ppn=$ppn, tpp=$tpp 
mpirun ./a.out
```
Given there are 16 cores per node, you would typically ensure `ppn*tpp=16`

### Example
To run an MPI+OpenMP executable mixed.exe with 64 MPI processes each launching 4 OpenMP threads, the following submission script would be needed:
```bash
#$ -V 
#$ -cwd 
#$ -b y 
#$ -l hr_t=01:00:00 
#$ -l np=64, ppn=4, tpp=4 
mpirun ./mixed.exe
```
This will allocate 16 nodes (=16*16=256 cores).
Each node will have 4 MPI processes, each of which will have 4 OpenMP threads (so 4\*4=16 processes per node in total, and 16\*16=256 (=64MPI\*4OpenMP) processes in total.

Alternatively, the same effect can be achieved by:
```bash
#$ -V 
#$ -cwd 
#$ -b y 
#$ -l hr_t=01:00:00 
#$ -l nodes=16, ppn=4, tpp=4 
mpirun ./mixed.exe
```
Note that the OMP_NUM_THREADS environment variable is automatically set by the batch system and so you do not need to set this in your environment.

## Job Dependencies
The SGE scheduler allows you to submit a job but then hold them in the queue until certain job dependencies are met, ie. it will hold the job until a previous job (or number of jobs have completed).

To do this, submit the first job as normal:

`qsub job1.sh`

As usual, the scheduler will give you a job ID `<jobid>`.

if you then want to submit another job that is dependent on the first one completing, use the `-hold_jid` option for qsub:

`qsub -hold_jid <jobid> job2.sh`

Job 2 will remain in the queue until job 1 has completed.

Alternatively, if you have given the job a name (using the -N option), then you can put a hold on subsequent jobs using the name instead:

`qsub -hold_jid <jobname> job2.sh`

If you give several jobs the same name, then the job will be held until all the named jobs have been completed.
