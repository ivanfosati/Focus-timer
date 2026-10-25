import matplotlib.pyplot as plt
import database as dt
import sqlite3
import numpy as np

conn = sqlite3.connect("app.db")
cur  = conn.cursor()


current_time = dt.datetime.now() + dt.timedelta(minutes=np.random.randint(0, 50))
iso_time = current_time.isoformat()

def addTime(t):
    delta = current_time + dt.timedelta(minutes=t)
    return delta.isoformat()

t1 = np.random.randint(1,180)
addElements(iso_time, addTime(t1), 'Analisis', t1)

inicio = []
fin = []
etiqueta = []
tiempo = []
for i, f, e, ti in cur.execute("SELECT * FROM pomodoro ORDER BY start_time"):
    inicio.append(i)
    fin.append(f)
    etiqueta.append(e)
    tiempo.append(ti)

print(f'Comienzo: {inicio} \n Finales: {fin} \n Labels: {etiqueta} \n Tiempos: {tiempo}')



hours = []
f_hours = []
for time_str in inicio:
    """ 
    separa fecha y horas, 
    y devulve lista de horas
    en formato HH:MM 
    """
    date, hour = time_str.split("T")
    hours.append(hour[:5])

for time_str in fin:
    """ 
    separa fecha y horas, 
    y devulve lista de horas
    en formato HH:MM 
    """
    date, hour = time_str.split("T")
    f_hours.append(hour[:5])
    
print(hours)
print(f_hours)



fig, ax = plt.subplots()
bar_container = ax.bar(hours, f_hours)
ax.set(ylabel='Tiempo', ylim=(0,24))
plt.show()

