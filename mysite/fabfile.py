from fabric import task, Connection
from invocations.console import confirm
from dotenv import load_dotenv
import os

'''
Fabfile con ejemplos de gestión del proyecto

Recuerda instalar fabric e invocations
$ pip install fabric invocations
'''
load_dotenv()
POSTGRES_DB = os.getenv('POSTGRES_DB')
POSTGRES_USER = os.getenv('POSTGRES_USER')


my_hosts = []

@task
def run(c):
    '''Ejecuta el servidor de desarrollo'''
    c.run('python manage.py runserver', pty=True)

@task
def vagup(c):
    '''Inicia la máquina virtual con provisionamiento'''
    c.run('vagrant up --provision', pty=True)

@task
def backup(c):
    '''Crea un backup de la base de datos'''
    c.run(f'''vagrant ssh -c "cd /vagrant && \
        docker-compose exec db bash -c 'pg_dump -Fc {POSTGRES_DB} \
            -U {POSTGRES_USER} | \
                gzip >/backup/{POSTGRES_DB}-$(date +%Y-%m-%d).dump.gz'"''',
        pty=True)

def conexion_vagrant():
    '''Devuelve una conexión a la máquina virtual'''
    return Connection('localhost', user='vagrant', port=2222,
        connect_kwargs={"password": "vagrant"})
    
@task
def dockerls(ctx):
    '''Lista los contenedores'''
    c = conexion_vagrant()

    c.run('docker ps -a', pty=True)
    c.run('cd /vagrant && docker-compose ps', pty=True)

@task
def dockerlogs(ctx):
    '''Muestra los logs del contenedor de la base de datos'''
    c = conexion_vagrant()
    c.run('cd /vagrant && docker-compose logs db', pty=True)

@task
def gitpush(ctx):
    '''Hace un commit y un push'''
    ctx.run('git status')
    question = '¿Estás seguro?'
    respuesta = confirm(question, assume_yes=True)
    if respuesta:
        mensaje = input('Mensaje del commit: ')
        ctx.run(f'git add . && git commit -a -m "{mensaje}" && git push')