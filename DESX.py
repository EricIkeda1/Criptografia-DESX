from Crypto.Cipher import DES

def xor_bytes(a: bytes, b: bytes) -> bytes:
    return bytes(x ^ y for x, y in zip(a, b))

def desx_encrypt(plaintext: bytes, key_des: bytes, key1: bytes, key2: bytes) -> bytes:
    des = DES.new(key_des, DES.MODE_ECB)
    step1 = xor_bytes(plaintext, key1)
    step2 = des.encrypt(step1)
    return xor_bytes(step2, key2)

def desx_decrypt(ciphertext: bytes, key_des: bytes, key1: bytes, key2: bytes) -> bytes:
    des = DES.new(key_des, DES.MODE_ECB)
    step1 = xor_bytes(ciphertext, key2)
    step2 = des.decrypt(step1)
    return xor_bytes(step2, key1)

def pad(text: bytes) -> bytes:
    pad_len = 8 - (len(text) % 8)
    return text + bytes([pad_len] * pad_len)

def unpad(text: bytes) -> bytes:
    pad_len = text[-1]
    return text[:-pad_len]

if __name__ == "__main__":
    key_des = b'8bytekey'
    key1 = b'12345678'
    key2 = b'abcdefgh'

    print("Digite uma mensagem para criptografar (ou 'sair' para encerrar):")
    while True:
        msg = input("> ")
        if msg.lower() == "sair":
            break

        pt = pad(msg.encode('utf-8'))
        ct = b""

        for i in range(0, len(pt), 8):
            block = pt[i:i+8]
            ct += desx_encrypt(block, key_des, key1, key2)

        print("Criptografado (hex):", ct.hex())

        dt = b""
        for i in range(0, len(ct), 8):
            block = ct[i:i+8]
            dt += desx_decrypt(block, key_des, key1, key2)

        dt = unpad(dt)
        print("Descriptografado:", dt.decode('utf-8'))
