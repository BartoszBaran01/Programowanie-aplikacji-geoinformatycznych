'''
#dzialania na podstawowym srodowisku python
print("Hello world")
help(print)
import os
current_path = os.getcwd()
print(current_path)
'''
#moduly i przestrzenie nazw 
from czas import aktualny_czas  
import time  
czas_poczatkowy = aktualny_czas()  # Wywołanie funkcji, aby uzyskać obiekt czasu
print("1", czas_poczatkowy.strftime("%Y-%m-%d %H:%M:%S")) # Format daty

time.sleep(20)
czas2= aktualny_czas()  
print("2", czas2.strftime("%Y-%m-%d %H:%M:%S")) 


import importlib #przeladowanie 
importlib.reload(time)
czas3 = aktualny_czas()  #
print("3", czas3.strftime("%Y-%m-%d %H:%M:%S")) 
