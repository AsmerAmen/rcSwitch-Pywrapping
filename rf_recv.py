from ctypes import cdll, c_long

hello_lib = cdll.LoadLibrary("rfSniffer.so")
rfValue = hello_lib.getValue
rfValue.restype = c_long
print(rfValue())
