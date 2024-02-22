def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

def affine_cipher(text, a, b, mode):
    result = ""
    m = 26  # Size of the alphabet

    for char in text:
        if char.isalpha():
            char_num = ord(char) - ord('A') if char.isupper() else ord(char) - ord('a')
            if mode == 'encrypt':
                encrypted_num = (a * char_num + b) % m
            elif mode == 'decrypt':
                inverse_a = mod_inverse(a, m)
                if inverse_a is None:
                    return "Error: 'a' is not coprime with 26"
                encrypted_num = (inverse_a * (char_num - b)) % m

            encrypted_char = chr(encrypted_num + ord('A') if char.isupper() else encrypted_num + ord('a'))
            result += encrypted_char
        else:
            result += char

    return result