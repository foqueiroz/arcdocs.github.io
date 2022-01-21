# Intelmpi

Intel&reg; MPI Library is a multifabric message-passing library that implements the open-source MPICH specification. Use the library to create, maintain, and test advanced, complex applications that perform better on high-performance computing (HPC) clusters based on Intel&reg; processors.

Read more about intelmpi on their [website](https://www.intel.com/content/www/us/en/developer/tools/oneapi/mpi-library.html).



## The intelmpi module on the HPC

The intelmpi module can be loaded into your environment with the following command:

```bash
$ module add intelmpi
```

The intelmpi module is available on ARC3 and ARC4:

```{list-table}
:header-rows: 1
:widths: 10 20 10


* - System
  - Version
  - Command

* - ARC3
  - intelmpi 2018.2.199
  - `module add intelmpi/2018.2.199`

* - ARC3
  - intelmpi 2017.1.132(default)
  - `module add intelmpi/2017.1.132(default)`

* - ARC4
  - intelmpi 2019.4.243
  - `module add intelmpi/2019.4.243`

```