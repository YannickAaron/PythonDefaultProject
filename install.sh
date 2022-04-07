#!/bin/sh

poetry env use $(pyenv which python)
poetry install
