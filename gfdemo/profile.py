import os
import socket

hostname = socket.gethostname()
print(hostname)
print(socket.gethostbyname(hostname))
import psutil
# gives a single float value
cpu = psutil.cpu_percent()
print(cpu)