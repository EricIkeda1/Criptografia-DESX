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

if __name__ == "__main__":
    key_des = b'8bytekey'
    key1 = b'12345678'
    key2 = b'abcdefgh'
    plaintext = b'testdata'
    ciphertext = desx_encrypt(plaintext, key_des, key1, key2)
    print(ciphertext.hex())
    decrypted = desx_decrypt(ciphertext, key_des, key1, key2)
    print(decrypted)
