# Chemkin

## Running Chemkin (ARC4 only)

ANSYS Chemkin provides all the tools for fast, accurate combustion and reaction flow simulations.

### Developer Website

More information about Chemkin can be found on the [Ansys Website](https://www.ansys.com/en-gb/products/fluids/ansys-chemkin-pro).

### Getting started

To use Chemkin, you must have connected to ARC using [X graphical forwarding](../../../getting_started/logon.md#Graphics-forwarding-(X11)), loaded ansys/19.2 and assigned licence server information.

```{note}
More details about using Ansys for the first time and setting license server details can be found on the [Ansys page](../ansys.md#Additional-Step-for-Using-Ansys-the-First-Time).
```

Then run the `run_chemkin.sh` script passing it the argument Pro to start up Chemkin.

```bash
$ module load ansys

$ run_chemkin.sh Pro
```
