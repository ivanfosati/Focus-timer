import sqlite3

def createTable():
    conn = sqlite3.connect("app.db")
    cur  = conn.cursor()
    cur.execute("""
                        CREATE TABLE IF NOT EXISTS 
                        pomodoro(
                            start_time INTEGER, 
                            end_time   INTEGER,
                            modo       TEXT,
                            duration   REAL 
                        )""")
    conn.commit()
    conn.close()

def addElements(start_time, end_time, label, time):
    conn = sqlite3.connect("app.db")
    cur  = conn.cursor()

    cur.execute("""
            INSERT INTO pomodoro VALUES (?, ?, ?, ?)""",
            (start_time, end_time, label, time))

    conn.commit()

    print(f"""Datos añadidos a la base de datos: 
            Inicio:     {start_time}, 
            Fin:        {end_time}, 
            Duración:   {time}, 
            Modo:       {label}
          """)
    conn.close()

def showTable():
    conn = sqlite3.connect("app.db")
    cur  = conn.cursor()

    cur.execute("SELECT * FROM pomodoro")
    results = cur.fetchall()
    print(results)
    conn.commit()
    conn.close()
