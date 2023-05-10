# Python Code Quality Continuous Integration (CI)
This repository is a template to provide Continuous Integration (CI) for any kind of Python projects.<br>
The main purpose of this repository is to prevent programmers to waste time re-creating their Python
CI over and over each time they have to create a new project. <br>
GitHub Actions is the CI/CD platform used in this repository. <br>

By default, pushing to the `main` branch is prohibited.<br>
The following workflow is advised using this template:
- Create a branch for your feature
- Create Pull Request once your feature is ready
- The PR will trigger the CI
- Once the CI passed and the PR is resolved, merge your branch to `main`.

This workflow ensure that the CI is the authority enforcing the code quality and that your production code will always pass the tests.

## Installation
Install Python3.10 and virutalenvwrapper.

### Linux
Install dependences:
```bash
sudo apt-get update
sudo apt-get install -y build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev git python3 python3-pip make
```

Install Pyenv:
```bash
curl https://pyenv.run | bash
```

Add Pyenv at startup:
```bash
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init --path)"\nfi' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc
source ~/.bashrc
```

Install Pyenv-virtualenv:
```bash
mkdir -p "$(pyenv root)/plugins"
git clone https://github.com/pyenv/pyenv-virtualenv.git "$(pyenv root)/plugins/pyenv-virtualenv"
```

Install Virtualenvwrapper:
```bash
sudo apt-get install virtualenvwrapper
```

Add environment variables for Virtualenvwrapper:
```bash
echo "export WORKON_HOME=$HOME/.virtualenvs
export PROJECT_HOME=$HOME/Projects
export VIRTUALENVWRAPPER_PYTHON=$(which python3)
source ~/.local/bin/virtualenvwrapper.sh" >> ~/.bashrc

source ~/.bashrc
```

### Mac
```bash
# Install pyenv
brew install pyenv
brew install pyenv-virtualenv
brew install virtualenvwrapper

# Install Python3.10
pyenv install 3.10

# Set Python3.10 as global
pyenv global 3.10

pip install virtualenv
pip install virtualenvwrapper
brew install pyenv-virtualenvwrapper

which virtualenvwrapper.sh

mkdir ~/.virtualenvs
```
Add environment variables to your `~/.zshrc`:
```bash
echo "export WORKON_HOME=$HOME/.virtualenvs
source $(which virtualenvwrapper.sh)

export PYENV_VIRTUALENVWRAPPER_PREFER_PYVENV="true"

if command -v pyenv 1>/dev/null 2>&1; then
 eval "$(pyenv init -)"
fi" >> ~/.zshrc
```

### Create Python Virtual Environment
1. Install a specific Python version with pyenv:
```bash
pyenv install <version>
```
2. Set the desired Python version as the default:
```bash
pyenv global <version>
```
3. Create a new virtual environment with virtualenvwrapper:
```bash
mkvirtualenv <venv_name>
```
4. To work in a virtual environment, use:
```bash
workon <venv_name>
```
5. To deactivate the virtual environment, simply run:
```bash
deactivate
```

### Install Dependencies & Pre-commit
Install dependencies:
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Install your custom package in your environment:
```bash
python setup.py install --force
```

Install pre-commit hooks:
```bash
pre-commit install
```

## Usage
The process is quite simple:
- Create a project from template pointing to this repository. Follow this [link](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template) for further explanation on how to create a project from template.
- Follow the [Protected Branch Configuration](##-Protected-Branch-Configuration) section.
- Follow the [Installation](##-Installation) section.
- Test the CI by running the `main-ci` manually. To run a workflow manually follow this [link](https://docs.github.com/en/actions/managing-workflow-runs/manually-running-a-workflow).
- Create a branch from `main`.
- Remove the `mymodule` example package and create your own at the root of the repository.
- Create your own package with the approriate tests.
- Edit the `setup.py` file, under the `packages` argument add your module path.
- Create a Pull Request and merge your code on `main`.
- By default, each time you try to merge a PR the CI will be triggered and the user will be allowed to merge if all the tests pass.

Congratulation ! You have now a repository with a functional CI to maintain your code standard to a stellar level ;)

## Protected Branch Configuration
- Go to the main Github page of your project created from template.
- Go to Settings > Branches.
- Click on `Add branch protection rule`
- Tick the following boxes:
    - Require a pull request before merging
    - Require status checks to pass before merging
    - Require branches to be up to date before merging
    - Do not allow bypassing the above settings
- Untick the Require Approval box if you are the only maintainer of the project.


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

To change the Python version of the CI, edit the `github/workflows/main-ci.yml` file. <br>
Change the value of the `PYTHON_VERSION` env variable to suit your needs.

