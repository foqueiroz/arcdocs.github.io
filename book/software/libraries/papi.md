# Papi

PAPI provides the tool designer and application engineer with a consistent interface and methodology for use of the performance counter hardware found in most major microprocessors. PAPI enables software engineers to see, in near real time, the relation between software performance and processor events.



Read more about papi on their [website](http://icl.cs.utk.edu/papi/).





## Licensing 

Distributed with a permissive license on the [Bitbucket project page](https://bitbucket.org/icl/papi/wiki/Home).



## The papi module on the HPC

The papi module can be loaded into your environment with the following command:

```bash
$ module add papi
```

The papi module is available on ARC3 and ARC4:

```{list-table}
:header-rows: 1
:widths: 10 20 10


* - System
  - Version
  - Command

* - ARC3
  - papi 5.5.1
  - `module add papi/5.5.1`

```