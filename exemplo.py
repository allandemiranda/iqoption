import logging
from iqoptionapi.stable_api import IQ_Option

import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s')
I_want_money = IQ_Option(os.environ.get("LOGIN"), os.environ.get("PASSWORD"))
check, reason = I_want_money.connect()  # connect to iqoption
print(check, reason)
