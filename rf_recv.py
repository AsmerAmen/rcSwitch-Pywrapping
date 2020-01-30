# Author : Asmer Amen
# Last update: 1 Dec 2019
# To run:
# #  g++ -shared -fPIC RFSniffer.cpp RCSwitch.cpp RCSwitch.h -o rfSniffer.so -lwiringPi -lwiringPiDev -lcrypt
# #  export LD_LIBRARY_PATH=.
# #  python3 rf_recv.py

from ctypes import cdll, c_long, c_int
from time import sleep
import RPi.GPIO as GPIO

# BCM_PIN = 2 #GPIO2
BCM_PIN = 7 #GPIO7
#WPi_PIN = 2
GPIO.setmode(GPIO.BCM)
# GPIO.setwarnings(False)
# GPIO.setup(BCM_PIN, GPIO.IN)

rf_lib = cdll.LoadLibrary("rfSniffer.so")
rfInit = rf_lib.init
rfValue = rf_lib.getValue
rfValue.restype = c_int

# print(1)
if rfInit(BCM_PIN):
    print('success')
else:
    print('7mada')
# print(2)
rfValue.restype = c_long
while True:
    val = rfValue()
    if val > 0:
        print("Recv: :", val)
    #print("Recv: :", rfValue())
    #sleep(1)  # 1 second
