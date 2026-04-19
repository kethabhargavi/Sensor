import sqlite3
import matplotlib.pyplot as plt

conn = sqlite3.connect("sensordb.db")
cursor = conn.cursor()

cursor.execute("SELECT temperature FROM sensor_data")
rows = cursor.fetchall()

temps = [r[0] for r in rows]

plt.plot(temps)
plt.title("Temperature Trend")
plt.xlabel("Reading Number")
plt.ylabel("Temperature")
plt.show()