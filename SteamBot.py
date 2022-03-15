from cgitb import lookup
from steam.client import SteamClient 
from dota2.client import Dota2Client
import logging
import os

username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')


client = SteamClient()
dota = Dota2Client(client)

logging.basicConfig(format='[%(asctime)s] %(levelname)s %(name)s: %(message)s', level=logging.DEBUG)

@client.on('logged_on')
def start_dota():
    dota.launch()

# @dota.on('ready')
# def do_dota_stuff():
#     jobid = dota.request_profile_card(70388657)
#     profile_card = dota.wait_msg(jobid, timeout=10)

#     if profile_card:
#         print(str(profile_card))

@dota.on('ready')
def create_lobby():
    lobby = dota.create_practice_lobby(password='welcome')
    lobby_name = dota.wait_msg(lobby, timeout=10)

    if lobby_name:
        dota.destroy_lobby()

@dota.on('ready')
def create_lobby():
    delete = dota.destroy_lobby()
    delete_msg = dota.wait_msg(delete, timeout=10)

    if delete_msg:
        print(delete)


client.cli_login(username=username, password=password)
client.run_forever()