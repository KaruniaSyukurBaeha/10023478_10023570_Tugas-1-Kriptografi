from itertools import cycle

def extended_vigenere_cipher(text, key, mode):
    result = ""
    for char, key_char in zip(text, cycle(key)):
        if char.isalpha():
            char_code = ord(char)
            key_code = ord(key_char)
            if mode == 'encrypt':
                result += chr((char_code + key_code) % 256)
            elif mode == 'decrypt':
                result += chr((char_code - key_code + 256) % 256)
        else:
            result += char
    return result

def transposition_cipher(text, key, mode):
    order = sorted(range(len(key)), key=lambda k: key[k])
    if mode == 'decrypt':
        order = sorted(order)
    result = ''
    for col in order:
        result += ''.join(text[col::len(key)])
    return result

def super_encryption(text, key_vigenere, key_transposition, mode):
    vigenere_result = extended_vigenere_cipher(text, key_vigenere, mode)
    transposition_result = transposition_cipher(vigenere_result, key_transposition, mode)
    return transposition_result