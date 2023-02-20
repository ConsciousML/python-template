# Python Code Quality Continuous Integration (CI)
This repository is a template to provide Continuous Integration (CI) for any kind of Python projects.<br>
The main purpose of this repository is to prevent programmers to waste time re-creating their Python
CI over and over each time they have to create a new project. <br>
GitHub Actions is the CI/CD platform used in this repository. <br>

## Usage
The process is quite simple:
- Create a project from template pointing to this repository. Follow this [link](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template) for further explanation on how to create a project from template.
- Follow the Setup section.
- Test the CI by running the `main-ci` manually. To run a workflow manually follow this [link](https://docs.github.com/en/actions/managing-workflow-runs/manually-running-a-workflow).
- Create a branch from `main`.
- Remove the `mymodule` example package and create your own at the root of the repository.
- Create your own package and the approriate tests.
- Create a Pull Request and merge your code on `main`.
- By default, each time you try to merge a PR the CI will be triggered and the user will be allowed to merge if all the tests pass.

Congratulation ! You have now a repository with a functional CI to maintain your code standard to a stellar level ;)

## Features
### Overview
The CI by default is triggered on merge on the `main` branch. <br>
If any of the following job fail, the push/merge will be rejected. <br>
This ensures that the code meets a certain level of quality. <br>

The CI contains the following jobs:
- `create-virutalenv`: creates a virtual environment with the necessary dependencies.
    Used by the other jobs to run in parallel and avoid the re-definition of the Python environment.
- `check-linting`: uses Pylint to check for any linting error. If any is found, the CI triggers and error.
- `check-coding-style`: runs Black to check for any formatting error in the Python code.
- `check-static-types`: uses MyPy to check for type hints errors.
- `check-security-vulnerability`: runs bandit to check for any security vulnerability in the code.
- `run-tests`: uses PyTest to make sure tests pass.

### Customization
This repository comes with multiple configuration file that you can modify as you see fit:
| Package | Description | Configuration file | Job name |
|---------|-------------|--------------------|----------|
| Pylint  | Static code analyzer to enforce best practices | `.pylintrc` | `check-linting` |
| Black   | Code formatter that ensures that every contributor uses the same coding style | `pyproject.toml` under `[tool.black]` section | `check-coding-style` |
| MyPy | Check type hints to improve further code readability | `pyproject.toml` under `[tool.mypy]` section | `check-static-types` |
| Bandit | Checks for security vulnerability in the code | `.bandit` | `check-security-vulnerability` |
| PyTest | Runs a test suite | `pyproject.toml` under `[tool.pytest.ini_options]` section | `run-tests` |

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