FROM ghcr.io/mlflow/mlflow:latest

RUN apt-get update --fix-missing                                \
    && apt-get install -y --no-install-recommends curl          \
    && apt-get clean                                            \
    && apt-get autoremove -y                                    \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir psycopg2-binary boto3

RUN useradd -m mlflow
RUN mkdir -p /home/mlflow/mlruns /home/mlflow/mlartifacts

WORKDIR /home/mlflow
USER mlflow

ENTRYPOINT ["mlflow"]
CMD ["server"]
