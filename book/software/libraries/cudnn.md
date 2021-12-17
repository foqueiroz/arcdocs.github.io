# Cudnn

The NVIDIA CUDA® Deep Neural Network library (cuDNN) is a GPU-accelerated library of primitives for deep neural networks. cuDNN provides highly tuned implementations for standard routines such as forward and backward convolution, pooling, normalization, and activation layers.

Read more about CUDNN on their [website](https://developer.nvidia.com/cudnn).



## Licensing 

The CUDNN license is available to read on the [NVIDIA website](https://docs.nvidia.com/deeplearning/cudnn/sla/index.html)



## The CUDNN module on the HPC

The CUDNN module can be loaded into your environment with the following command:

```bash
$ module add CUDNN
```

The CUDNN module is available on ARC3 and ARC4:

```{list-table}
:header-rows: 1
:widths: 10 20 10


* - System
  - Version
  - Command

* - ARC4
  - CUDNN 7.6.5
  - `module add cudnn/7.6.5`

```