from db import *
from random import choice
from time import time, ctime
from typing import Any
from hashlib import md5

# Generates the cookie
def get_random_string(length) -> str:
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqurstuvwxyz0123456789!”#$%&\'()*+,-./:;<=>?@[\]^_`{}~.'
    return ''.join(choice(letters) for i in range(length))

# Checks if username, password, and ip address are real ones
def create_admin_login(username, password, email, ip, imgurl) -> bool:
    return create_account(username, password, email, ip) and create_business(username, imgurl)

def create_personal_login(username, password, email, ip):
    return create_account(username, password, email, ip)

def login_personal(username, password, ip_address) -> bool:
    if check_account(username, password, ip_address):
        return True
    else:
        return False

def login_business(username, password, ip_address, photo_url) -> bool:
    pass

create_admin_login("robert", "robthegenie", "rob@gene.edu", "192.168.1.2", "path/to/url")
