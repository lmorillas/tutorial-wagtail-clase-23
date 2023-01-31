
from fabric import task

my_hosts = ["my-server"]

@task
def test(c):
    result = c.res("./manage.py test my_app", warn=True)
    if not result and not confirm("Tests failed. Continue anyway?"):
        raise Exit("Aborting at user request.")

@task
def commit(c):
    c.run("git add -p && git commit")

@task
def status(c):
    c.run("git status")

@task
def push(c):
    c.local("git push")

@task
def prepare_deploy(c):
    test(c)
    commit(c)
    push(c)

@task(hosts=my_hosts)
def deploy(c):
    code_dir = "/srv/django/myproject"
    if not c.run("test -d {}".format(code_dir), warn=True):
        cmd = "git clone user@vcshost:/path/to/repo/.git {}"
        c.run(cmd.format(code_dir))
    c.run("cd {} && git pull".format(code_dir))
    c.run("cd {} && touch app.wsgi".format(code_dir))

@task
def host_type(c):
    c.local('uname -s')

@task
def cosa(   c, p):
    c.run('echo {}'.format(p))