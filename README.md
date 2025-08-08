# Projeto DESX em Python

## Descrição

Este projeto implementa o algoritmo de criptografia **DESX**, uma variação do DES que utiliza técnicas de *whitening* para aumentar a segurança do algoritmo original. O programa é interativo via terminal, permitindo ao usuário escolher entre criptografar ou descriptografar mensagens usando o DESX.

---

## O que é DESX?

O **DESX** é uma modificação do algoritmo DES que adiciona duas chaves extras (pré e pós-whitening) para aumentar a complexidade da chave e dificultar ataques de força bruta.

O funcionamento básico é:

- **Criptografia:**  
  \( C = K_2 \oplus DES_K(P \oplus K_1) \)  
- **Descriptografia:**  
  \( P = K_1 \oplus DES_K^{-1}(C \oplus K_2) \)  

Onde:  
- \( P \) = plaintext (mensagem original)  
- \( C \) = ciphertext (mensagem cifrada)  
- \( K \) = chave DES padrão (56 bits efetivos)  
- \( K_1 \), \( K_2 \) = chaves de 64 bits para whitening

---

## Funcionalidades do Programa

- Menu interativo para escolher entre:  
  - Criptografar uma mensagem (entrada em texto normal)  
  - Descriptografar uma mensagem (entrada em hexadecimal)  
  - Sair do programa  
- Uso de padding PKCS#7 para blocos múltiplos de 8 bytes  
- Entrada e saída amigáveis no terminal  
- Uso da biblioteca `pycryptodome` para funções DES

---

## Pré-requisitos

- Python 3.6 ou superior  
- Biblioteca `pycryptodome`

Instale a biblioteca com:

```
pip install pycryptodome
```

## Como usar

1. Clone ou copie os arquivos do projeto para seu computador.

2. Execute o script Python:

```
python desx_chat.py
```
