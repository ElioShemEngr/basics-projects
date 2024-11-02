from datetime import datetime
import os, time

while True:
    # Genera hora actual en formato HH:MM:SS
    now = datetime.now().strftime("%H:%M:%S")
    print(now)
    time.sleep(1)
    os.system("cls")
