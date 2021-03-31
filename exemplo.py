import logging
from iqoptionapi.stable_api import IQ_Option

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s')
I_want_money = IQ_Option("email", "senha")
check, reason = I_want_money.connect()  # connect to iqoption
print(check, reason)
