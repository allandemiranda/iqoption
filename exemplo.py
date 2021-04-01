
import json
import time
import os
import logging
from iqoptionapi.stable_api import IQ_Option
from datetime import datetime
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s')
API = IQ_Option(os.environ.get("LOGIN"), os.environ.get("PASSWORD"))
API.connect()  # connect to iqoption
API.change_balance('PRACTICE')  # PRACTICE / REAL

while True:
    if API.check_connect():
        print('Conectado com sucesso')
        break
    else:
        print('Erro ao se conectar')
        API.connect()

    time.sleep(1)


def perfil():  # Função para capturar informações do perfil
    return json.loads(json.dumps(API.get_profile_ansyc()))


ranking = API.get_leader_board("Worldwide", 1, 10, 0)

for n in ranking['result']['positional']:
    id = ranking['result']['positional'][n]['user_id']

    perfil_info = API.get_user_profile_client(id)
    if perfil_info['status'] == 'online':
        op = API.get_users_availability(id)

        try:
            tipo = op['statuses'][0]['selected_instrument_type']
            par = API.get_name_by_activeId(op['statuses'][0]['selected_asset_id']).replace('/','')

            print('\n [', n, '] ', perfil_info['user_name'])
            print(tipo)
            print(par)
        except:
            pass
