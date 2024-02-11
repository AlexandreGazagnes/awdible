#! /bin/bash


# poetry install
python3 -m poetry install

# activate the virtual environment
python3 -m poetry shell

# install pre-commit hooks
pre-commit install

# run the tests
pytest -vvx --capture=tee-sys --log-cli-level=INFO tests/
