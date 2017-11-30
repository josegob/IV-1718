from fabric.api import *


def instalar_proyecto():
	run('sudo git clone https://github.com/josegob/IV-Proyecto')
	run('cd ./IV-Proyecto && sudo pip3 install -r requirements.txt')

def api_up():
    run('nohup sudo -E python3 home/ubuntu/IV-Proyecto/flask_api.py', pty=False)

def delete_api():
	run('sudo rm -rf ./IV-Proyecto')

def kill_api():
    run('sudo pkill python3')
