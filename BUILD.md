# pyplan-ide

## Prerequisites

### Local Virtual Environment, using Python venv (for development)

1. Prerequisites

    ```bash
    sudo apt install python3.7 python3-venv python3.7-venv libpq-dev libpython3.7-dev
    ```

2. Create virtual environment and activate it

    ```bash
    python3.7 -m venv venv
    source venv/bin/activate
    pip install --upgrade pip
    ```

3. Install dependencies

    ```bash
    pip install -r requirements/desktop.txt
    ```

## Run

```bash
    source venv/bin/activate
    python run_pyplan.py
```



## Create build for Pypi

1. Install setup packages:

```bash
python3 -m pip install --upgrade setuptools wheel twine
```

2. Build:

Set de version number in setup.cfg and :

```bash
. build_version
```

3. Upload to Pypi:

```bash
. upload_to_pypi
```

## Setup for buils for Conda

1. Install anaconda or miniconda

2. add conda-forge channel

```bash
conda config --append channels conda-forge
```

## Create build for Conda

1. Upload build to pypi

2. Edit conda/meta.yaml

    Set version on:
    ```{% set version = "0.29.7" %}```

    copy sha256 from pypi and paste on :
    ```sha256: 368ec48.............324```
    (the sha256 is in 'https://pypi.org/project/pyplan-ide/#files') and click on view of .gz file

3. build pyplan-ide:

```bash
cd conda
conda build pyplan-ide
```

3. upload to pyplan conda channel
```bash
anaconda upload /my/anaconda3/conda-bld/noarch/pyplan-ide-0.29.7-py_0.tar.bz2
```
