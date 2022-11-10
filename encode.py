def grothenc(message: str):
    '''
    57を用いてRSA暗号を生成
    '''

    source = message.encode('UTF-8')

    # public key
    n = 57
    e = 29

    # encode

    # 暗号化できるのはn以下の入力
    # -> 16進数化した後一桁ずつ計算する

    c = []
    for hex in source:
        print(hex)
        c.append((hex ** e) % n)
    # return c
    return " ".join(list(map(lambda x: "%02X" % x, c)))
