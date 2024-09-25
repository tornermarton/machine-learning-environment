FROM python:latest

RUN apt-get update --fix-missing                                \
    && apt-get install -y --no-install-recommends curl          \
    && apt-get clean                                            \
    && apt-get autoremove -y                                    \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir tensorflow tensorflow-io

RUN useradd -m tensorboard
RUN mkdir -p /home/tensorboard/logs

WORKDIR /home/tensorboard
USER tensorboard

ARG LOGDIR='/home/tensorboard/logs'
ENV LOGDIR=${LOGDIR}

ENTRYPOINT [ "sh", "-c", "tensorboard --bind_all --logdir ${LOGDIR}" ]

EXPOSE 6006
