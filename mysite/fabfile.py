from fabric import task, Connection
from invocations.console import confirm

'''
Fabfile con ejemplos de gestión del proyecto

Recuerda instalar fabric e invocations
$ pip install fabric invocations
'''

my_hosts = []

@task
def run(c):
    c.run('python manage.py runserver', pty=True)

@task
def vagup(c):
    c.run('vagrant up --provision', pty=True)

@task
def backup(c):
    c.run('''vagrant ssh -c "cd /vagrant && \
        docker-compose exec db bash -c 'pg_dump -Fc miproyecto -U postgres | gzip >/backups/example_database-$(date +%Y-%m-%d).dump.gz'"''',
        pty=True)

def conexion_vagrant():
    return Connection('localhost', user='vagrant', port=2222,
        connect_kwargs={"password": "vagrant"})
    
@task
def dockerls(ctx):
    c = conexion_vagrant()

    c.run('docker ps -a', pty=True)
    c.run('cd /vagrant && docker-compose ps', pty=True)

@task
def dockerlogs(ctx):
    c = conexion_vagrant()
    c.run('cd /vagrant && docker-compose logs db', pty=True)

@task
def gitpush(ctx):
    ctx.run('git status')
    question = '¿Estás seguro?'
    respuesta = confirm(question, assume_yes=True)
    if respuesta:
        mensaje = input('Mensaje del commit: ')
        ctx.run(f'git add . && git commit -a -m "{mensaje}" && git push')