# vigenere_cipher.py

def vigenere_cipher(text, key, mode):
    result = ""
    key_index = 0
    key = key.upper()

    for char in text:
        if char.isalpha():
            shift = ord(key[key_index]) - ord('A')
            if mode == 'decrypt':
                shift = -shift

            if char.islower():
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))

            key_index = (key_index + 1) % len(key)
        else:
            result += char

    return result
