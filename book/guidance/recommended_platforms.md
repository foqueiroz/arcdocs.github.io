# Recommended Platforms

This guide asks a range of questions to consider when deciding which platform to use for your research. The suitable choice depends on your use cases and requirements.

## Considerations

### Are you using {ref}`personal data <personal_data>`?

- [LASER (Leeds Analytic Secure Environment for Research)](https://lida.leeds.ac.uk/about-lida/integrated-research-campus/)

### Does the work need a lot of memory?

- For example, a local laptop / workstation may have 4-64 GB
- There may be tools and methods to reduce memory usage, e.g., [SWD6: High Performance Python](https://arc.leeds.ac.uk/training/courses/swd6/)
- High Performance Computers (HPC)
  - [ARC3](https://arcdocs.leeds.ac.uk/systems/arc3.html#standard-nodes)
    - Standard 128 GB
    - High-memory 768 GB
  - [ARC4](https://arcdocs.leeds.ac.uk/systems/arc4.html#standard-nodes)
    - Standard 192 GB
    - High-memory 768 GB
- Cloud computing
  - Microsoft Azure
    - ...

### Does the work need a lot of storage?

- For example, a local laptop / workstation may have 0.25-2 TB
- Onedrive
  - 5 TB each, for all users
- HPC
  - [ARC3](https://arcdocs.leeds.ac.uk/systems/arc3.html#lustre-storage)
    - 836 TB Lustre storage, at 4GB/s (/nobackup)
  - [ARC4](https://arcdocs.leeds.ac.uk/systems/arc4.html#lustre-storage)
    - 1.2 PB Lustre storage, at 11GB/s (/nobackup)

### Do you need to parallelise the work over many cores?

- For example, a local laptop / workstation may have 4-16 cores
- HPC
  - [ARC3](https://arcdocs.leeds.ac.uk/systems/arc3.html#standard-nodes)
    - 252 standard nodes, each with 24 cores
    - 4 high-memory nodes, each with 24 cores
  - [ARC4](https://arcdocs.leeds.ac.uk/systems/arc4.html#standard-nodes)
    - 149 standard nodes, each with 40 cores
    - 2 high-memory nodes, each with 40 cores
- Cloud computing
  - Microsoft Azure
    - ...

### Do you need to use GPUs?

- Buy a local laptop / workstation with a GPU
  - [Purchase form](https://leeds.service-now.com/it?id=sc_cat_item&sys_id=a649379c0f2f9b40a82247ece1050e25)
- HPC (multiple / more powerful GPUs)
  - [ARC3](https://arcdocs.leeds.ac.uk/systems/arc3.html#gpgpu-nodes)
    - 2 x [general purpose GPU](https://en.wikipedia.org/wiki/General-purpose_computing_on_graphics_processing_units) nodes, each with 2 x [NVIDIA Tesla K80](https://www.nvidia.com/en-gb/data-center/tesla-k80/)
    - 6 x [general purpose GPU](https://en.wikipedia.org/wiki/General-purpose_computing_on_graphics_processing_units) nodes, each with 4 x [NVIDIA Tesla P100](https://www.nvidia.com/en-gb/data-center/tesla-p100/)
  - [ARC4](https://arcdocs.leeds.ac.uk/systems/arc4.html#gpgpu-nodes)
    - 3 x [general purpose GPU](https://en.wikipedia.org/wiki/General-purpose_computing_on_graphics_processing_units) nodes, each with 4 x [NVIDIA Tesla V100](https://www.nvidia.com/en-gb/data-center/tesla-v100/)
  - [Bede](https://bede-documentation.readthedocs.io/en/latest/hardware/index.html)
    - 2 x login GPU nodes each with 4 x [NVIDIA Tesla V100](https://www.nvidia.com/en-gb/data-center/tesla-v100/)
    - 32 x GPU nodes each with 4 x [NVIDIA Tesla V100](https://www.nvidia.com/en-gb/data-center/tesla-v100/)
    - 4 x "inference" GPU nodes each with 4 x [NVIDIA Tesla T4](https://www.nvidia.com/en-gb/data-center/tesla-t4/)
  - [JADE-2](http://docs.jade.ac.uk/en/latest/index.html)
    - 63 x [DGX-MAX-Q](https://www.nvidia.com/en-gb/data-center/dgx-systems/dgx-1/) Nodes, each with 8 x [NVIDIA Tesla V100](https://www.nvidia.com/en-gb/data-center/tesla-v100/)
- Cloud computing
  - Microsoft Azure
    - ...

## Cost

- ...

## Access

### How can I use LASER?

- Contact the Data Analytics Team at dat@leeds.ac.uk.

### How can I get an account on ARC3/4?

- [Request an account on ARC](https://arcdocs.leeds.ac.uk/getting_started/request_hpc_acct.html)

### How can I get an account on Bede?

- Identify an existing project, or [register](https://n8cir.org.uk/supporting-research/facilities/bede/docs/bede_registrations/) a new one.
  - [Application](https://n8cir.org.uk/supporting-research/facilities/bede/bede-application/)
- Register on [EPCC SAFE account](https://safe.epcc.ed.ac.uk/) (to manage your account)
  - Once there, select "Project -> Request access" from the web interface and then register against your project

### How can I get an account on JADE-2?

- Register on Hartree Self Service (for technical support)
  - Click [here](https://stfc.service-now.com/hcssp) and use the register option in the top right-hand corner
- Register on Hartree SAFE (to manage your account)
  - Click [here](https://um.hartree.stfc.ac.uk/hartree/login.jsp) to register
  - Add your public SSH key following the instructions [here](https://stfc.service-now.com/kb?id=kb_article_view&sys_kb_id=318854b7db451410b40c9334ca9619ec)
- Request to join the project  
  - From within SAFE, click "Request join project"
  - Select: J2AD014 - University of Leeds
  - An project administrator, can then provide the access code, accept you onto the project, and add you to the relevant group
- More detail is [here](https://www.jade.ac.uk/access/)
