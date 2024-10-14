FROM quay.io/jupyterhub/jupyterhub:latest

RUN pip install --no-cache-dir dockerspawner jupyterhub-nativeauthenticator

RUN mkdir /data

COPY ./jupyterhub_config.py /etc/jupyterhub/jupyterhub_config.py

CMD ["jupyterhub", "-f", "/etc/jupyterhub/jupyterhub_config.py"]
