import matplotlib.pyplot as plt
import database
import sqlite3

conn = sqlite3.connect("app.db")
cur  = conn.cursor()

for session in cur.execute("SELECT * FROM pomodoro"):
    print(session)


