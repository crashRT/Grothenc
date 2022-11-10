from public_key import *
from secret_key import *


def grothdec(cipher):
    # decode
    string = cipher.lower()
    hex = string.split(' ')
    message = []
    for number in hex:
        number = bytes.fromhex(number)
        number = int.from_bytes(number, 'big')
        m = (number ** d) % 57
        m = m.to_bytes(1, 'big')
        message.append(m.decode('UTF-8'))
    return message
