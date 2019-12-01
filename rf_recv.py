from ctypes import cdll, c_long, c_int
from time import time
rf_lib = cdll.LoadLibrary("rfSniffer.so")
rfInit = rf_lib.init
rfValue = rf_lib.getValue
rfValue.restype = c_int
# print(1)
if rfInit():
    print('success')
else:
    print('7mada')
# print(2)
rfValue.restype = c_long
while True:
    print("Recv: :", rfValue())
    time.sleep(0.100)
