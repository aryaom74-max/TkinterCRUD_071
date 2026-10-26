import sqlite3
import tkinter as tk
from tkinter import messagebox

DB_NAME = "school.db"

def run_query(sql, params=()):
    conn = sqlite3.connect(DB_NAME)
    try:
        with conn:
            return conn.execute(sql, params).fetchall()
    finally:
        conn.close()
