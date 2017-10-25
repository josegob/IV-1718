from fabric.api import *


def instalar_bot():
	run('sudo git clone https://github.com/josegob/IV-Proyecto')
	run('cd ./IV-Proyecto && sudo pip3 install -r requirements.txt')

def bot_up():
    with shell_env(token_bot='token_bot', DATABASE_URL='DATABASE_URL'):
        run('nohup sudo -E python3 ./IV-Proyecto/bot_metacritic/bot_metacritic.py', pty=False)

def delete_bot():
	run('sudo rm -rf ./IV-Proyecto')

def kill_bot():
    run('sudo pkill python3')
