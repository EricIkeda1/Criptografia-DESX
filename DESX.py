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

def hex_to_bytes(hex_str: str) -> bytes:
    hex_str = hex_str.replace(" ", "")
    return bytes.fromhex(hex_str)

def main():
    key_des = b'8bytekey'
    key1 = b'12345678'
    key2 = b'abcdefgh'

    while True:
        print("\nEscolha a opção:")
        print("1 - Criptografar")
        print("2 - Descriptografar")
        print("0 - Sair")
        opcao = input("> ")

        if opcao == "0":
            print("Encerrando...")
            break
        elif opcao == "1":
            texto = input("Digite o texto para criptografar:\n> ")
            pt = pad(texto.encode('utf-8'))
            ct = b""
            for i in range(0, len(pt), 8):
                bloco = pt[i:i+8]
                ct += desx_encrypt(bloco, key_des, key1, key2)
            print("Texto criptografado (hex):")
            print(ct.hex())
        elif opcao == "2":
            hex_text = input("Digite o texto criptografado em hexadecimal:\n> ")
            try:
                ct_bytes = hex_to_bytes(hex_text)
            except ValueError:
                print("Entrada hexadecimal inválida.")
                continue

            if len(ct_bytes) % 8 != 0:
                print("O texto criptografado deve ter múltiplos de 8 bytes.")
                continue

            dt = b""
            for i in range(0, len(ct_bytes), 8):
                bloco = ct_bytes[i:i+8]
                dt += desx_decrypt(bloco, key_des, key1, key2)
            try:
                dt = unpad(dt)
                print("Texto descriptografado:")
                print(dt.decode('utf-8'))
            except:
                print("Erro ao remover padding ou decodificar o texto.")
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()
