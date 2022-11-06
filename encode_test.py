from encode import *

source = input("enter your message: ")
print("----------")

cipher = grothenc(source)
print(cipher)
