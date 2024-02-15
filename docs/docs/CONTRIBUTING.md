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

Awdible is an open-source project and is far from perfect. We are constantly aiming to improve, so contribution and feedback from developers with any level of experience is greatly appreciated! Issues are marked with various tag, some of which are good first issues, making it a great place for beginners and new open-source contributors to start. Areas that you could look to contribute towards may range from adding or suggesting new app features, debugging, and documentation revision. Feedback and testing regarding any of the features will help our overall development process, so feel free to suggest anything that you can think of.

If you have any questions about the project or don't know where to start, feel free to reach out and we'll help you get started! Otherwise, you can check out the Issues tab to see the open issues that currently need to be fixed. If you find any bugs or would like to request new features, you can click on "New Issue" and note the deatils accordingly. If there is a bug, please describe the bug in the issue and the steps that are needed to replicate it so that it can be fixed in a timely manner.

For major changes and new requests, please open an issue first so that we can reach out and discuss the changes before implementing it into the project. In the future, we may create other forms of communication through apps such as Slack or Discord, but for now please refer to the Issues tab for project communication purposes. 

For more information, please refer to the [contributing](https://alexandregazagnes.github.io/awdible/CONTRIBUTING/) page.
