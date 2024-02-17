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

### Setting up pre-commit

We strongly recommend you to use [pre-commit](https://pre-commit.com/) to manage your hooks.

Here is the description of the tool from the official documentation :

 > Git hook scripts are useful for identifying simple issues before submission to code review. We run our hooks on every commit to automatically point out issues in code such as missing semicolons, trailing whitespace, and debug statements. 
 
 > By pointing these issues out before code review, this allows a code reviewer to focus on the architecture of a change while not wasting time with trivial style nitpicks.

 Please install it using the following command :

```bash
pre-commit install
```

```pre-commit ``` will now run on every commit. If you want to run it manually, you can use the following command :

```bash
pre-commit run --all-files
```

**```pre-commit``` is not mandatory but it is highly recommended.** 

It is a great tool to ensure that your code is clean and that you are not introducing any new issues. 

It is also a great way to ensure that your code is compliant with the project's standards, and that your pull request will be accepted.



### Using zsh to auto fetch 

If you are using ```zsh``` and ```ohmyzsh```, you can install ```git-auto-fetch``` to automatically fetch the latest changes from the remote repository.

Here an example of a ```.zshrc``` file with the plugin :
```shell
plugins=(git python git-auto-fetch git-prompt vscode)
GIT_AUTO_FETCH_INTERVAL=1200 # in seconds
source $ZSH/oh-my-zsh.sh
```

Find more information on the [official repository](https://github.com/ohmyzsh/ohmyzsh/blob/master/plugins/git-auto-fetch/git-auto-fetch.plugin.zsh)

This is a great way to ensure that you are always working with the latest version of the code.

**Like pre-commit, it is not mandatory but it is highly recommended.**




## Issues
### Reading issues

Please read the [issues page](https://alexandregazagnes.github.io/awdible/issues/) before creating a new issue : 
* Find a new issue to work on in the page. 
* If you want to work on an issue, please comment on the issue to let others know that you are working on it.

### Creating a new issue

Feel free to create a new issue if you have any question, suggestion, or if you want to report a bug : 
* You will find a template to fill in when creating a new issue.
* We have carefully crafted the template to help you provide the information we need to help you.
* We will add relevant labels to your issue to help us keep track of it.


### Finding the good issue to work on  

* Most important issues are tagged with the `good first issue` label
* Find relevant issues to work on by filtering the issues with the `good first issue`, `help wanted`, `urgent`, or `tricky` labels.
* When you find an issue you want to work on, please comment on the issue to let others know that you are working on it.
* You will have to make a comment to the issue in order to block it to other contributors.



## Contributing

### Creating a new branch

⚠️ **WARNING** ⚠️ : 
* Read carefully the following instructions before creating a new branch.


Find bellow the **exact** process to work on a feature : 
* Any feature, bug fix, or improvement should come from an issue.
* When you are ready to start working on an issue, **please create a new branch directly from the issue page**. You will find a button to create a new branch on the right side of the issue page.
* Please **choose `dev` as the base branch** and not `main`. If not you will not be able to create a pull request.
* You will not have to worry about the name of your branch : it will be automatically generated from the issue title : **do not change it**.
* Once you have created the branch, you can start working on the issue.


### Creating a pull request
⚠️ **WARNING** ⚠️ : 
* Read carefully the following instructions before creating a Pull Request.


When you are ready to submit your work : 
* Please create a pull request related to the issue you're working on
* **Refers to the issue** in the pull request description : ie [#12]()
* Fill up the PR template and **do not try to bypass the templat**e
* Please **choose `dev` as the dest branch** and not `main`. If not you will not be able to create a pull request.
* We will review your pull request and give you feedback.

After your pull request : 
* A code review will be done by the maintainers.
* Once your pull request is approved, we will merge it into the `dev` branch.
* We will then close the issue and add the `merged` label to it.
