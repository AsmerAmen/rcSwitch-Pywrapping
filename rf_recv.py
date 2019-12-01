from ctypes import cdll, c_long, c_int
from time import sleep
import RPi.GPIO as GPIO

BCM_PIN = 27
WPi_PIN = 2
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(BCM_PIN, GPIO.IN)

rf_lib = cdll.LoadLibrary("rfSniffer.so")
rfInit = rf_lib.init
rfValue = rf_lib.getValue
rfValue.restype = c_int

# print(1)
if rfInit(WPi_PIN):
    print('success')
else:
    print('7mada')
# print(2)
rfValue.restype = c_long
while True:
    print("Recv: :", rfValue())
    sleep(1)  # 1 second
