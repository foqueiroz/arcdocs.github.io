# XPLOR-NIH

## Introduction

XPLOR-NIH is a powerful protein structure determination software that supports incorporation of sophisticated NMR data but also SAXS, EM, Xray data and ensemble calculations. You can find extensive documentation for XPLOR’s many functions on the [official documentation page](https://nmr.cit.nih.gov/xplor-nih/doc/current/).

## Licensing

Using XPLOR-NIH means you agree to the following license terms:

```
         LICENSE FOR NON-PROFIT INSTITUTIONS TO USE XPLOR-NIH
                         Terms of Agreement
By downloading or using the Xplor-NIH software you agree to the
following terms:
- You shall not use the software for any purpose (research or
  otherwise) that is supported by a "for profit" organization without
  prior written authorization.
- You agree that the software is furnished on an "as is" basis and
  that the authors in no way warrant the software or any of its
  results and is in no way liable for any use you make of the software.
- Ownership of software and documentation is retained by the
  appropriate, respective organizations.
- You shall not disclose in any form either the delivered software or
  documentation to third parties without prior written authorization.
```

The authors require that any published work or images created using VMD include the following reference:

> C.D. Schwieters, J.J. Kuszewski, N. Tjandra, G.M. Clore, ``The
>Xplor-NIH NMR Molecular Structure Determination Package,''
>J. Magn. Res., 160, 66-74 (2003).

## Basic usage

To run a python style xplor script using 10 cores:

```bash
$ pyXplor script.py -smp 10
```
