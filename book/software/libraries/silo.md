# Silo

Silo is a library for reading and writing a wide variety of scientific data to binary, disk files. The files Silo produces and the data within them can be easily shared and exchanged between wholly independently developed applications running on disparate computing platforms. Consequently, Silo facilitates the development of general purpose tools for processing scientific data. One of the more popular tools that process Silo data files is the VisIt visualization tool.



Read more about silo on their [website](https://wci.llnl.gov/simulation/computer-codes/silo/).





## Licensing 

Distributed under a BSD license.



## The silo module on the HPC

The silo module can be loaded into your environment with the following command:

```bash
$ module add silo
```

The silo module is available on ARC3 and ARC4:

```{list-table}
:header-rows: 1
:widths: 10 20 10


* - System
  - Version
  - Command

* - ARC3
  - silo 4.10.2
  - `module add silo/4.10.2`

* - ARC3
  - silo 4.9.1
  - `module add silo/4.9.1`

* - ARC4
  - silo 4.9.1
  - `module add silo/4.9.1`

```