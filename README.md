# Python Code Quality Continuous Integration (CI)
This repository is a template to provide Continuous Integration (CI) for any kind of Python projects

# Setup
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