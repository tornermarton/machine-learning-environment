import os, nativeauthenticator

def get_environment(key):
    def _substitute_spawner_context(value, spawner):
        context = {
            "username": spawner.user.name
        }

        for k, v in context.items():
            value = value.replace(f"{{{k}}}", v)

        return value

    _value = os.environ.get(key)

    return lambda spawner: _substitute_spawner_context(_value, spawner)

c = get_config()  # noqa: F821

c.JupyterHub.ip = '0.0.0.0'
c.JupyterHub.port = 8888

c.JupyterHub.allow_named_servers = True
c.JupyterHub.redirect_to_server = False

c.JupyterHub.db_url = "sqlite:////data/jupyterhub.sqlite"
c.JupyterHub.upgrade_db = True

c.JupyterHub.cookie_secret_file = "/data/jupyterhub_cookie_secret"

c.JupyterHub.spawner_class = "dockerspawner.DockerSpawner"

docker_host_name = os.environ.get("DOCKER_HOST_NAME", "jupyterhub")
c.JupyterHub.hub_connect_ip = docker_host_name

docker_image = os.environ.get("DOCKER_IMAGE", "quay.io/jupyter/base-notebook:latest")
c.DockerSpawner.image = docker_image

docker_allowed_images = os.environ.get("DOCKER_ALLOWED_IMAGES", "").split(',')
c.DockerSpawner.allowed_images = docker_allowed_images

docker_environment = os.environ.get("DOCKER_ENVIRONMENT", "").split(',')
c.DockerSpawner.environment = {key: get_environment(key) for key in docker_environment}

c.DockerSpawner.network_name = os.environ.get("DOCKER_NETWORK_NAME", "default")
c.DockerSpawner.use_internal_ip = True

c.DockerSpawner.notebook_dir = "/home/jovyan"
c.DockerSpawner.volumes = { "jupyter-{username}": c.DockerSpawner.notebook_dir }

c.DockerSpawner.remove = True
c.DockerSpawner.debug = True

c.JupyterHub.authenticator_class = "native"

c.JupyterHub.template_paths = [f"{os.path.dirname(nativeauthenticator.__file__)}/templates/"]

# Create default admin user
c.Authenticator.admin_users = {"admin"}
# Allow all signed-up users to login
c.Authenticator.allow_all = True

# c.NativeAuthenticator.check_common_password = True
# c.NativeAuthenticator.minimum_password_length = 10
