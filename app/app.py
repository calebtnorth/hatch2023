from db import *
from random import choice
from time import time, ctime
from typing import Any

# Generates the cookie
def get_random_string(length) -> str:
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqurstuvwxyz0123456789!”#$%&\'()*+,-./:;<=>?@[\]^_`{}~.'
    return ''.join(choice(letters) for i in range(length))

# Checks if username, password, and ip address are real ones
def login_personal(username, password, ip_address) -> bool:
    if check_account(username, password, ip_address):
        return True
    else:
        return False
    
def login_business(username, password, ip_address, photo_url) -> bool:
    pass
