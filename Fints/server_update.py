import sys
import paramiko as pm
sys.stderr = sys.__stderr__
import os


HOST = '213.139.209.18'
USER = 'linux'
PASSWORD = 'acer123'

git_pull = \
    '''
    cd /home/linux/github/MoCertsMe
    git fetch --all
    git reset --hard origin/master
    git pull
    exit

    '''

give_chmod = \
    '''
    cd /home/linux/github/MoCertsMe/bin
    sudo chmod +x start_gunicorn.sh
    sudo chmod +x start_celery.sh
    exit
    '''

migrations = \
    '''
    cd /home/linux/github/MoCertsMe/MoCerts
    python3 manage.py makemigrations
    y
    python3 manage.py migrate
    exit
    '''

supervisor_restart = \
    '''
    sudo supervisorctl restart all
    exit
    '''


class AllowAllKeys(pm.MissingHostKeyPolicy):
    def missing_host_key(self, client, hostname, key):
        return


def init_connect(HOST, USER, PASSWORD):
    client = pm.SSHClient()
    client.load_system_host_keys()
    client.load_host_keys(os.path.expanduser('~/.ssh/known_hosts'))
    client.set_missing_host_key_policy(AllowAllKeys())
    client.connect(HOST, username=USER, password=PASSWORD)
    channel = client.invoke_shell()
    stdin = channel.makefile('wb')
    stdout = channel.makefile('rb')
    return stdin, stdout, client


def send_commands(HOST, USER, PASSWORD, commands):
    client = init_connect(HOST, USER, PASSWORD)
    stdin = client[0]
    stdout = client[1]
    client = client[2]

    stdin.write(commands)

    opt = stdout.readlines()
    for i in opt:
        i = i.rstrip()
        i=str(i,'utf-8')
        print(i)
    print("\n")

    stdout.close()
    stdin.close()
    client.close()


send_commands(HOST, USER, PASSWORD, git_pull)
send_commands(HOST, USER, PASSWORD, give_chmod)
send_commands(HOST, USER, PASSWORD, migrations)
send_commands(HOST, USER, PASSWORD, supervisor_restart)

input('Press enter...')