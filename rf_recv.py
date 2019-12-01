from ctypes import cdll, c_long, c_int
from time import sleep
import RPi.GPIO as GPIO

PIN = 2
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(PIN, GPIO.IN)

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
    sleep(1)  # 1 second
