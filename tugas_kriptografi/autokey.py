def auto_key_vigenere_cipher(text, key, mode):
    result = ""
    key_index = 0
    key = key.upper()
    key_stream = key + text  # Auto-Key: Key stream starts with the key followed by the plaintext

    for char in text:
        if char.isalpha():
            shift = ord(key_stream[key_index]) - ord('A')
            if mode == 'decrypt':
                shift = -shift

            if char.islower():
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))

            key_index += 1
        else:
            result += char

    return result