from fabric.api import env, run, cd, sudo
from fabric.contrib.files import upload_template
import os

env.hosts = [os.environ["FABIC_HOSTS"]]
env.user = os.environ["FABIC_SSH_USER"]
env.password = os.environ["FABIC_SSH_PASS"]
env.port = int(os.environ["FABIC_PORT"])
env.key_filename = os.environ['FABIC_LOCAL_KEY_FILENAME']

project_home = os.environ["FABIC_VIRTUALENV_HOME"]
venv_path = "%s/venv" % project_home
pip = "%s/bin/pip" % venv_path
manage = "%s/bin/python %s/manage.py" % (venv_path, project_home)


# Templates definition
templates = {
    "nginx": {
        "local_path": "deploy/nginx.conf",
        "remote_path": "/etc/nginx/sites-enabled/pythonbc.com",
        "reload_command": "service nginx reload",
    },
    "supervisor": {
        "local_path": "deploy/supervisor.conf",
        "remote_path": "/etc/supervisor/conf.d/pythonbc.conf",
        "reload_command": "supervisorctl reload",
    },
}


def upload_templates():
    for name in templates:
        template = templates.get(name)
        local_path = template.get('local_path')
        remote_path = template.get('remote_path')

        # Upload template to host
        if local_path and remote_path:
            upload_template(local_path, remote_path, env, use_sudo=True, backup=False)


def restart_services():
    for name in templates:
        template = templates.get(name);
        reload_command = template.get('reload_command')

        # Seload Server
        if reload_command:
            sudo(reload_command)

def deploy():
    upload_templates()
    with cd(project_home):
        run("%s migrate --all" % manage)
        run("%s collectstatic --noinput" % manage)
    restart_services()


def fulldeploy():
    upload_templates()

    with cd(project_home):
        run("git pull origin master")
        run("%s install -r requirements/deploy.txt" % pip)
        run("%s syncdb" % manage)
        run("%s migrate --all" % manage)
        run("%s collectstatic --noinput" % manage)
    restart_services()


def statics():
    with cd(env.venv_home):
        run("%s collectstatic --noinput" % env.manage)

def nginx():
    template = templates.get('nginx')
    local_path = template.get('local_path')
    remote_path = template.get('remote_path')
    upload_template(local_path, remote_path, env, use_sudo=True, backup=False)
    sudo(template.get('reload_command'))
