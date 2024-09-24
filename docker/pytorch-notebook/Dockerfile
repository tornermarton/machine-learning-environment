#FROM quay.io/jupyter/pytorch-notebook:cuda12-latest
FROM quay.io/jupyter/pytorch-notebook:latest

USER root

RUN jupyter labextension disable --level=system "@jupyterlab/apputils-extension:announcements"

USER ${NB_USER}

RUN pip install --no-cache-dir mlflow psutil pynvml && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}"
