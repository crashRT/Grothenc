def grothenc(message: str):
    '''
    57を用いてRSA暗号を生成
    '''

    source = message.encode('UTF-8')

    # public key
    n = 57
    e = 5

    # encode
    c = (int.from_bytes(source, 'big') ** e) % n
    return c
