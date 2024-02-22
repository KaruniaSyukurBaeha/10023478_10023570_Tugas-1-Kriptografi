def extended_vigenere_cipher(text, key, mode):
    result = ""
    key_index = 0

    for char in text:
        if char.isascii():
            key_byte = ord(key[key_index % len(key)])
            char_byte = ord(char)
            
            if mode == 'encrypt':
                encrypted_byte = (char_byte + key_byte) % 256
            elif mode == 'decrypt':
                encrypted_byte = (char_byte - key_byte) % 256

            result += chr(encrypted_byte)
            key_index += 1
        else:
            result += char

    return result