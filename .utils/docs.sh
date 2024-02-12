#! /bin/sh


# update index.md
cp README.md ./docs/index.md

# docs
cd ./docs

# deploy
mkdocs build
mkdocs gh-deploy
