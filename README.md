# ![Pyplan](docs/assets/img/logo.png)

**Pyplan** allows consolidating into a single graphical environment all
corporate Data Analytics and Decision Support needs. It is meant to
simplify Business Analyst introduction to Data Science with Python.

Among its most prominent features you will find:

- Assisted drag and drop graphical programming
- Visual Influence Diagram to represent logic flow
- Easy creation of interactive user interfaces
- Empowered collaboration by one click publishing and sharing
- Secure and scalable with corporate standards
- On cloud or on-premise deployment

Screenshots
===========

Influence Diagram

![Influence Diagram](docs/assets/img/diagram.png)

Interfaces (dashboards)

![Interfaces](docs/assets/img/interface.png)

Include lot of tutorials,examples and demos

![Demos](docs/assets/img/demos.png)

Requirements
===========

- [python 3.7](https://www.python.org/downloads/release/python-375/)

Installation
===========

You can install **Pyplan** using pip:

Linux/Mac:

```bash
python3.7 -m venv pyplan
. pyplan/bin/activate
pip install --upgrade pip
pip install pyplan-ide
```

Windows:

```bash
python3.7 -m venv pyplan
pyplan\Scripts\activate.bat
pip install --upgrade pip
pip install pyplan-ide
```

Install **Pyplan** using **conda**:

```bash
conda config --append channels pyplan
conda config --append channels conda-forge
conda create -n pyplan-ide python=3.7
conda activate pyplan-ide
conda install pyplan-ide
```

Or install **Pyplan** using **Anaconda Navigator**:

create and select new environment "pyplan-ide"

add channel pyplan
add channel conda-forge
go to home
find "pyplan-ide" app on Navigator and click Install
then click Launch

Run Pyplan
===========

You can run **Pyplan** with these commands:

Linux/Mac:

```bash
. pyplan/bin/activate
pyplan
```

Windows:

```bash
pyplan\Scripts\activate.bat
pyplan
```

conda:

- Start terminal an type: **pyplan**

Anaconda Navigator:

- Click launch on **pyplan-ide** app

User Guide
===========

For User Guide please visit [docs.pyplan.com](http://docs.pyplan.com/)
