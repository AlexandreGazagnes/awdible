# Contributing

## Local development

- The complete test suite depends on having at least the following installed
  (possibly not a complete list)
  - git (Version 2.24.0 or above is required )
  - python3.10.x (Required by a test which checks different python versions)
  <!-- - tox (or venv) -->
  - poetry, pip, pipenv, virtualenv, or similar
  - poetry is the preferred tool for managing dependencies, highly recommended

### Setting up an environment

The project uses [Poetry](https://python-poetry.org/) to manage its dependencies.
Please install it using the following command :

```bash
pip install poetry
```

Then, please install the dependencies using the following command :

```bash
poetry install
```

Activate the environment using the following command :

```bash
poetry shell
```

And finally, install the pre-commit hooks using the following command :

```bash
pre-commit install
```


### Running a specific test

Running a specific test with the environment activated is as easy as:
`pytest tests -k test_the_name_of_your_test`

### Running all the tests

With the environment activated you can run all of the tests
using:
`pytest tests`



## Contributing

Pull requests are welcome.

For major changes, please open an issue first to discuss what you would like to change.

For more information, please refer to the [contributing](https://alexandregazagnes.github.io/awdible/CONTRIBUTING/) page.
