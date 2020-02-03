import os
import socket

hostname = socket.gethostname()
print(hostname)
print(socket.gethostbyname(hostname))
print('memory')
import psutil
# gives a single float value
cpu = psutil.cpu_percent()
print(cpu)


