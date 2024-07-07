import signal
import time
import os
import psutil  # Install psutil package if not installed
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Restarts the Django server every 60 seconds"

    def handle(self, *args, **kwargs):
        restart_interval = 60  # seconds

        while True:
            self.stdout.write(self.style.SUCCESS("Reloading server..."))

            # Implement server reload mechanism here
            # Example: Reload Django development server

            # Find the Django server process
            for proc in psutil.process_iter(['pid', 'cmdline']):
                if 'python' in proc.info['cmdline'] and 'manage.py runserver' in ' '.join(proc.info['cmdline']):
                    os.kill(proc.pid, signal.SIGHUP)  # Send SIGHUP signal for reload

            time.sleep(restart_interval)

