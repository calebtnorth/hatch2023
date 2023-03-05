from .db import db
from random import choice
from time import time, ctime
from typing import Any
from hashlib import md5

# Generates the cookie
def get_random_string(length) -> str:
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqurstuvwxyz0123456789!”#$%&\'()*+,-./:;<=>?@[\]^_`{}~.'
    return ''.join(choice(letters) for i in range(length))

# Checks if username, password, and ip address are real ones
def create(username, password, email, ip, imgurl) -> bool:
    return db.create(username, password, email, ip, imgurl)

def login(username, password, ip_address) -> bool:
    if db.check(username, password, ip_address):
        return True
    else:
        return False
