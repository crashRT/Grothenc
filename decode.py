from public_key import *
from secret_key import *


def grothdec(cipher):
    '''
    57を用いてRSA復号化を行う
    '''

    source = cipher.split()
    m = []
    for text in source:
        m.append((int(text) ** d) % n)
    hex = "".join(list(map(lambda x: "%1X" % x, m)))
    return bytes.fromhex(hex).decode('UTF-8')
