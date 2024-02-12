#! /bin/sh


rm -f ./docs/assets/img/cov.svg
# rm -f .coverage
.venv/bin/coverage run -m pytest -vvx --capture=tee-sys --log-cli-level=INFO tests/integration/
.venv/bin/coverage-badge -fo ./docs/assets/img/cov.svg
