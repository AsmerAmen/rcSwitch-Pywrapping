from ctypes import cdll, c_long

hello_lib = cdll.LoadLibrary("hello.so")
hello = hello_lib.hello
hello.restype = c_long
print (hello())