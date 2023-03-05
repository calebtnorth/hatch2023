from db import *
from random import choice
from time import time, ctime
from typing import Any

# Generates the cookie
def get_random_string(length) -> str:
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqurstuvwxyz0123456789!”#$%&\'()*+,-./:;<=>?@[\]^_`{}~.'
    return ''.join(choice(letters) for i in range(length))

# Checks if username, password, and ip address are real ones
def login_cookie(username, cookie) -> bool:
    return check_cookie(username, cookie)
cookie = get_random_string(64)
def login_verify(username, password, ip_address) -> bool:
    if check_account(username, password, ip_address):
        stache_cookie(username, cookie)
        return True
    else:
        return False

# Logs 
print(login_verify("calebtnorth", "ctn070206", "194.168.1.2"))
print(check_cookie("calebtnorth", cookie))
# if check:
#     verification = f"Logged in user {get_user()} at {time.ctime(time.time())}"
#     print(verification)
#     print("Thank you for using our service! ")
# else:
#     verification = (f"Attempted to log in user {get_user()} with password {get_pass()} at {ctime(time())}")
#     print(verification)
#     print("Issue with login.")
