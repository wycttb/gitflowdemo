import os
import socket

hostname = socket.gethostname()
print(hostname)
print(socket.gethostbyname(hostname))
<<<<<<< HEAD

print('memory')
=======
import psutil
# gives a single float value
cpu = psutil.cpu_percent()
print(cpu)
>>>>>>> 0439b04f5d13f60cba0f993bcaba2f2a74ebe283
