# Database for ChromaZone 
import sqlite3
from bcrypt import hashpw, checkpw, gensalt
from typing import Any
db_connection = sqlite3.connect("app/db/users.db")
cursor = db_connection.cursor()

# Loading / Writing
def create_account(username:str, password:str, email:str, ip:str) -> Any[bool, str]:
    cursor.execute(
        "INSERT INTO accounts (username, password, email, ip, upload, transfer) VALUES ( ?, ?, ?, ?, 0, 0 );",
        (username, hashpw(bytes(password, "utf-8"), gensalt(12)), email, ip)
    )
    db_connection.commit()

def check_account(username:str, password:str, ip:str) -> Any[bool, str]:
    try:
        result = cursor.execute(
            "SELECT password FROM accounts WHERE username=? AND ip=?",
            (username, ip)
        )
        return checkpw(bytes(password, "utf-8"), result.fetchone()[0])

    except TypeError:
        return False

def check_username(username:str) -> Any[bool, str]:
    try:
        result = cursor.execute(
            "SELECT password FROM accounts WHERE username=?",
            (username)
        )
        return result.fetchone()[0]

    except TypeError:
        return False
    


    

    
