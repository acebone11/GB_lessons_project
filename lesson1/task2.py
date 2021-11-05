import time
current_time = int(input("Введите время в секундах  "))
time_format = time.strftime("%H:%M:%S", time.gmtime(current_time))
print(time_format)
import os
os.system("pause")