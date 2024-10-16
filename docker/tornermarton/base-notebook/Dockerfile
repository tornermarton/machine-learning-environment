FROM quay.io/jupyter/base-notebook:latest

USER root
RUN jupyter labextension disable --level=system "@jupyterlab/apputils-extension:announcements"
USER ${NB_USER}

RUN mkdir "/home/${NB_USER}/data"

RUN pip install --no-cache-dir                                                 \
    mlflow-skinny psutil pynvml

RUN fix-permissions "${CONDA_DIR}" && fix-permissions "/home/${NB_USER}"
