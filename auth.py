import streamlit as st
import sqlite3
import hashlib


def create_users_table():
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    
    c.execute('''
        CREATE TABLE IF NOT EXISTS users(
        username TEXT,
        password TEXT
        )
    ''')
    
    conn.commit()
    conn.close()


def add_user(username, password):
    
    conn = sqlite3.connect("users.db")
    c = conn.cursor()

    hashed = hashlib.sha256(password.encode()).hexdigest()

    print("Saving user:", username)
    c.execute("INSERT INTO users VALUES (?,?)",(username, hashed))

    conn.commit()
    conn.close()


def login_user(username, password):

    username = username.strip()
    password = password.strip()

    conn = sqlite3.connect("users.db")
    c = conn.cursor()

    hashed = hashlib.sha256(password.encode()).hexdigest()

    c.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (username, hashed)
    )

    data = c.fetchall()

    conn.close()

    return data