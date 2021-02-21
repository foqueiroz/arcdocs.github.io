# Advisor

The Intel Advisor is a design assistance and analysis tool for SIMD vectorization, threading, memory use, and GPU offload optimization. You can read more about it at the [Intel Advisor website](https://software.intel.com/content/www/us/en/develop/documentation/get-started-with-advisor/top.html).

## The Advisor module on the HPC

The Intel Advisor module can be loaded into your environment with the following command and is only available on ARC3:

```bash
$ module add advisor
```

There are several different versions of the Intel Advisor available on ARC3:

```{list-table}
:header-rows: 1
:widths: 10 20 10

* - System
  - Version
  - Command
* - ARC3
  - Intel Advisor 2018.2.0.551025
  - `module add advisor/2018.2.0.551025`
* - ARC3
  - Intel Advisor 2017.1.5.527008
  - `module add advisor/2017.1.5.527008`
* - ARC3
  - Intel Advisor 2017.1.1.486553
  - `module add advisor/2017.1.1.486553`
```

A guide to using the Advisor CLI can be found on the [Intel Advisor User Guide](https://software.intel.com/content/www/us/en/develop/documentation/advisor-user-guide/top/launch-the-intel-advisor/intel-advisor-cli.html).
