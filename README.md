# Python Code Quality Continuous Integration (CI)
This repository is a template to provide Continuous Integration (CI) for any kind of Python projects.
The CI by default is triggered on merge on the `main` branch.

## Features
### Overview
If any of the following jobs fail, the push/merge will be rejected.
This ensures that the code meets a certain level of quality.

The CI contains the following jobs:
- `create-virutalenv`: creates a virtual environment with the necessary dependencies.
    Used by the other jobs to run the jobs in parallel and avoid re-defining the Python environment.
- `check-linting`: uses Pylint to check for any linting error. If any is found, the CI triggers and error.
- `check-coding-style`: runs Black to check for any formatting error in the Python code.
- `check-static-types`: uses MyPy to check for type hints errors.
- `check-security-vulnerability`: runs bandit to check for any security vulnerability in the code.

## Setup
Install Python3.11 and VirutalEnvWrapper:
```bash
sudo apt-get install python3.11 python3.11-venv python3-venv
sudo apt-get install python3-virtualenv

python3.11 -m pip install virtualenvwrapper
```

Create Python environment:
```bash
mkvirtualenv myenv -p python3.11
```

Install dependencies:
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Install your custom package in your environment:
```bash
python setup.py install --force
```