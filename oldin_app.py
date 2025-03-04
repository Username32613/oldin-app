import psutil
import os
import tkinter as tk
from tkinter import simpledialog
import time

class OldinApp:
    def __init__(self, protected_apps, pin_code):
        self.protected_apps = protected_apps
        self.pin_code = pin_code
        self.running = True

    def prompt_for_pin(self):
        root = tk.Tk()
        root.withdraw()  # Fè fenèt la kache
        pin = simpledialog.askstring("PIN Verification", "Antre PIN ou:")
        if pin != self.pin_code:
            return False
        return True

    def monitor_apps(self):
        while self.running:
            for app in self.protected_apps:
                for proc in psutil.process_iter(['pid', 'name']):
                    if proc.info['name'].lower() == app.lower():
                        if not self.prompt_for_pin():
                            os.system(f"taskkill /f /pid {proc.info['pid']}")
                            print(f"{app} te bloke paske PIN lan pa kòrèk.")
            time.sleep(2)  # Tcheke chak 2 segonn

    def start(self):
        print("Monitoring aplikasyon yo...")
        self.monitor_apps()

# Lis aplikasyon pwoteje
protected_apps = ["whatsapp.exe", "facebook.exe", "tiktok.exe"]

# Kòd PIN
pin_code = "1234"  # Modifye PIN sa a si ou vle

# Kreye objè aplikasyon an
app = OldinApp(protected_apps, pin_code)

# Kòmanse siveyans aplikasyon yo
app.start()
