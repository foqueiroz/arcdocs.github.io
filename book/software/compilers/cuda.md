# Cuda

CUDA is a set of tools developed for programming natively on NVIDIA GPUs. You can read more about CUDA on the [NVIDIA website](https://developer.nvidia.com/cuda-zone).

## Usage

CUDA is available as a module on both ARC3 and ARC4. You can find an outline of the available versions and commands to load those modules below:

```{list-table}
:header-rows: 1
:widths: 10 30 10

* - System
  - Version
  - Command
* - ARC4
  - CUDA 11.1.1
  - `module add cuda/11.1.1`
* - ARC4
  - CUDA 10.1.168 (default)
  - `module add cuda`
* - ARC4
  - CUDA 9.0.176
  - `module add cuda/9.0.176`
* - ARC4
  - CUDA 8.0.61
  - `module add cuda/8.0.61`
* - ARC3
  - CUDA 11.1.1
  - `module add cuda/11.1.1`
* - ARC3
  - CUDA 10.1.168 (default)
  - `module add cuda`
* - ARC3
  - CUDA 9.0.176
  - `module add cuda/9.0.176`
* - ARC3
  - CUDA 8.0.61
  - `module add cuda/8.0.61`
* - ARC3
  - CUDA 8.0.44
  - `module add cuda/8.0.44`
```

## Training

The Research Computing team runs the [HPC5: Introduction to GPU programming with CUDA](https://arc.leeds.ac.uk/training/courses/hpc5/) twice a year. This course introduces the fundamentals of GPU programming and how to optimise code to run on GPUs.
