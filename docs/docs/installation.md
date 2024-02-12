# Installation


## Using regular pip and venv tools

Creating a virtual environment :

```bash
python3 -m venv .venv
source .venv/bin/activate
```

It is recommended to use a virtual environment to install the package.

Installing the package :

```bash
pip install awdible [--upgrade] [--user]

```

## Using poetry or pipenv

It is recommended to use a virtual environment to install the package.

```bash
pip install poetry
poetry init
poetry add awdible
```



## Check the installation

You can check the installation by running the following command :

```bash
pip show awdible
```

or

```bash
pip list | grep awdible
```
