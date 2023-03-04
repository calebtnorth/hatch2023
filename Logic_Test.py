import random
import string
import time

# Generates the cookie
def get_random_string(length) -> str:
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqurstuvwxyz0123456789!”#$%&\'()*+,-./:;<=>?@[\]^_`{}~.'
    return ''.join(random.choice(letters) for i in range(length))

# Checks if username, password, and ip address are real ones
def login_verify(user, password, ip_address):
    print(user + ' ' + password + ' ' + ip_address)
    if user == get_user() and password == get_pass() and ip_address == get_ip():
        return get_random_string(64)
    else:
        return False
    
# Replace "Calcel", "1234". and "17.172" with lists of login material
def get_user():
    return "Calcel"

def get_pass():
    return "1234"

def get_ip():
    return "17.172"

# Logs 
check = login_verify("Calcel", "1234", "17.172")
if check:
    verification = f"Logged in user {get_user()} at {time.ctime(time.time())}"
    print(verification)
    print("Thank you for using our service! ")
else:
    verification = (f"Attempted to log in user {get_user()} with password {get_pass()} at {time.ctime(time.time())}")
    print(verification)
    print("Issue with login.")
