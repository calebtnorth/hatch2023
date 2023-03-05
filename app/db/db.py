# Database for ChromaZone 
import sqlite3
from bcrypt import hashpw, checkpw, gensalt
from typing import Any
db_connection = sqlite3.connect("app/db/users.db")
cursor = db_connection.cursor()

# Loading / Writing
def create_account(username:str, password:str, email:str, ip:str) -> bool:
    status = cursor.execute(
        "INSERT INTO accounts (username, password, email, ip, upload, transfer) VALUES ( ?, ?, ?, ?, 0, 0 );",
        (username, hashpw(bytes(password, "utf-8"), gensalt(16)), email, ip)
    )
    db_connection.commit()
    return status

def check_account(username:str, password:str, ip:str) -> bool:
    try:
        result = cursor.execute(
            "SELECT password FROM accounts WHERE username=? AND ip=?",
            (username, ip)
        )
        return checkpw(bytes(password, "utf-8"), result.fetchone()[0])

    except TypeError:
        return False

def check_username(username:str) -> bool:
    """
    True means username is available
    """
    try:
        result = cursor.execute(
            "SELECT username FROM accounts WHERE username=?",
            (username)
        )
        return len(result.fetchone()) == 0

    except TypeError:
        return False
    
def stache_cookie(username:str, cookie:str) -> bool:
    result = cursor.execute(
        "UPDATE accounts SET cookie=? WHERE username=?",
        (cookie, username)
    )
    db_connection.commit()

def check_cookie(username:str, cookie:str) -> bool:
    try:
        result = cursor.execute(
            "SELECT cookie FROM accounts WHERE username=?",
            (username,)
        )
        if result.fetchone[0] > 0:
            return result.fetchone()[0] == cookie
        else:
            return False

    except TypeError:
        return False