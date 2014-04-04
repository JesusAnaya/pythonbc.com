from fabric.api import env, local, run, cd, sudo
from fabric.contrib.files import upload_template
from config.local_settings import FABRIC as fab

env.hosts = fab.get('HOSTS')
env.user = fab.get('SSH_USER')
env.password = fab.get('SSH_PASS')
env.port = fab.get('SSH_PORT')
env.venv_home = fab.get('VIRTUALENV_HOME')
env.venv_path = "%s/venv" % env.venv_home
env.pip = "%s/bin/pip" % env.venv_path
env.manage = "%s/bin/python %s/manage.py" % (env.venv_path, env.venv_home)


# Templates definition
templates = {
    "nginx": {
        "local_path": "deploy/nginx.conf",
        "remote_path": "/etc/nginx/sites-enabled/pythonbc.co",
        "reload_command": "service nginx reload",
    },
    "local_settings": {
        "local_path": "deploy/live_settings.py",
        "remote_path": "/home/anaya/pythonbc/config/local_settings.py",
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


def init_ssh():
    home_ssh = local("echo $HOME/.ssh/id_rsa", capture=True)
    env.key_filename = home_ssh


def deploy():
    init_ssh()
    upload_templates()

    with cd(env.venv_home):
        run("git pull origin master")
        run("%s migrate --all" % env.manage)
        run("%s collectstatic --noinput" % env.manage)
    restart_services()


def fulldeploy():
    init_ssh()
    upload_templates()

    with cd(env.venv_home):
        run("git pull origin master")
        run("%s install -r requirements/deploy.txt" % env.pip)
        run("%s syncdb" % env.manage)
        run("%s migrate --all" % env.manage)
        run("%s collectstatic --noinput" % env.manage)
    restart_services()


def statics():
    init_ssh()
    with cd(env.venv_home):
        run("%s collectstatic --noinput" % env.manage)


def nginx():
    init_ssh()
    template = templates.get('nginx')
    local_path = template.get('local_path')
    remote_path = template.get('remote_path')
    upload_template(local_path, remote_path, env, use_sudo=True, backup=False)
    sudo(template.get('reload_command'))

