from apscheduler.schedulers.background import BackgroundScheduler
import time
import subprocess


interval_minutes = 60

def update_dashboard():
    print("Dashboard wird aktualisiert...")
    subprocess.run(["python3", "/home/pi/E-Paper-Layout/main.py"])

scheduler = BackgroundScheduler()
scheduler.add_job(update_dashboard, 'interval', seconds=20)
scheduler.start()
print("Scheduler gestartet. Warte auf Jobs...")

try:
    # Hauptprogramm läuft weiter
    while True:
        time.sleep(1)
except (KeyboardInterrupt, SystemExit):
    scheduler.shutdown()
    print("Scheduler gestoppt.")