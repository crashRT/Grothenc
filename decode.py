from public_key import *
from secret_key import *


def grothdec(cipher):

    # decode
    hex = bytes.fromhex(cipher)
    int_cipher = int.from_bytes(hex, 'big')
    message = ((int_cipher, 'big') ** d) % 57
    message = message.decode('UTF-8')
    return message
