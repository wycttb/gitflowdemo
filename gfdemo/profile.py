import os
import socket
import psutil


hostname = socket.gethostname()
print(hostname)
print(socket.gethostbyname(hostname))
print('memory')
cpu = psutil.cpu_percent()
print(cpu)


