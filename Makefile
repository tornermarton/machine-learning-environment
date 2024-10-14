# HELP
# This will output the help for each task
# thanks to https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
help: ## This help.
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

.DEFAULT_GOAL := help
.PHONY: help build-jupyterhub build-mlflow build-tensorboard build-base-notebook build-pytorch-notebook build-pytorch-notebook-cuda12

### BASE COMPONENTS ###

build-jupyterhub:  ## Build docker image tornermarton/jupyterhub:latest
	@docker build --push -t tornermarton/jupyterhub ./docker/jupyterhub

build-mlflow:  ## Build docker image tornermarton/mlflow:latest
	@docker build --push -t tornermarton/mlflow ./docker/mlflow

build-tensorboard:  ## Build docker image tornermarton/tensorboard:latest
	@docker build --push -t tornermarton/tensorboard ./docker/tensorboard

### NOTEBOOKS ###

build-base-notebook:  ## Build docker image tornermarton/base-notebook:latest
	@docker build --push -t tornermarton/base-notebook:latest ./docker/base-notebook

build-pytorch-notebook:  ## Build docker image tornermarton/pytorch-notebook:latest
	@docker build --push -t tornermarton/pytorch-notebook:latest ./docker/pytorch-notebook

build-pytorch-notebook-cuda:  ## Build docker image tornermarton/pytorch-notebook:cuda12-latest
	@docker build --push -t tornermarton/pytorch-notebook:cuda12-latest ./docker/pytorch-notebook/cuda12
