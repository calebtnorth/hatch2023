# Database for ChromaZone 
import sqlite3
from bcrypt import hashpw, checkpw, gensalt
from hashlib import md5
from typing import Any

db_connection = sqlite3.connect("app/db/users.db", check_same_thread=False)
cursor = db_connection.cursor()

# Loading / Writing
def create(username:str, password:str, email:str, ip:str, imgurl) -> bool:
    try:
        status = cursor.execute(
            "INSERT INTO accounts (username, password, email, ip, imgurl, local, export, approved) VALUES ( ?, ?, ?, ?, ?, 0, 0, 0 );",
            (username, hashpw(bytes(password, "utf-8"), gensalt(16)), email, ip, imgurl)
        )
        db_connection.commit()
        return True
    except Exception as e:
        print(f"[-] {e}")
        return False

def login(username:str, password:str, ip:str) -> bool:
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
    
def get_activity(activity:int):
    """
    True means username is available
    """
    df = pd.read_sql_query(
            "SELECT activity FROM businesses WHERE activity=\""+ activity + "\"", db_connection
        )
    return df.head()
   


def get_local(local:int):
    """
    True means username is available
    """
    df = pd.read_sql_query(
            "select local,export from businesses WHERE owner=" + "", db_connection
        )
    return df.head()
