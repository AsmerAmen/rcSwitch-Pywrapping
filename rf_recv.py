from ctypes import cdll, c_long

rf_lib = cdll.LoadLibrary("rfSniffer.so")
rfInit = rf_lib.init
rfValue = rf_lib.getValue
rfInit()
rfValue.restype = c_long
print(rfValue())
