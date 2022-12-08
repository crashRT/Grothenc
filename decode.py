from public_key import *
from secret_key import *


def grothdec(cipher):
    # decode
    string = cipher.lower()
    hex = string.split(' ')
    message = []
    for char in hex:
        m = []
        print(char)
        number = bytes.fromhex(char)
        number = int.from_bytes(number, 'big')
        for i in range(2):
            if (i == 0):
                num = number // 16
            else:
                num = number % 16
            m.append((num ** d) % n)
        text = m[0] * 16 + m[1]
        print(text)
        text = text.to_bytes(1, 'big')
        message.append(text.decode('UTF-8'))
    return message
