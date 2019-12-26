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
