# Scalasca

Scalasca is a software tool that supports the performance optimization of parallel programs by measuring and analyzing their runtime behavior. The analysis identifies potential performance bottlenecks - in particular those concerning communication and synchronization - and offers guidance in exploring their causes.

Read more about scalasca on their [website](http://www.scalasca.org/).



## Licensing 

The entire code of Scalasca v2 is licensed under the [BSD-style license agreement.](https://www.scalasca.org/scalasca/software/scalasca-2.x/license.html)



## The scalasca module on the HPC

The scalasca module can be loaded into your environment with the following command:

```bash
$ module add scalasca
```

The scalasca module is available on ARC3 and ARC4:

```{list-table}
:header-rows: 1
:widths: 10 20 10


* - System
  - Version
  - Command

* - ARC3
  - scalasca 2.3.1
  - `module add scalasca/2.3.1`

```