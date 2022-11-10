def grothdec(cipher):
    # public key
    n = 57
    e = 5
    # secret key
    d = 19

    # decode
    hex = bytes.fromhex(cipher)
    int_cipher = int.from_bytes(hex, 'big')
    message = ((int_cipher, 'big') ** d) % 57
    message = message.decode('UTF-8')
    return message
