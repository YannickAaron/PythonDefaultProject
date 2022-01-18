# Python default project

## Prerequisites

### Install Homebrew
install homebrew

### Install pyenv
install pyenv: brew install pyenv poetry geos gdal node

export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv init -)"

### install prepare: ./husky/prepare
