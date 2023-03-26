from public_key import *


def grothenc(message: str):
    '''
    57を用いてRSA暗号化を行う
    '''

    source = message.encode('UTF-8')
    hex = source.hex()
    c = []
    for text in hex:
        c.append((int(text, 16) ** e) % n)
    return " ".join(list(map(lambda x: "%02d" % x, c)))


print(grothenc("にゃーん"))
