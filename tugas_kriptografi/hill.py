import numpy as np

def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

def matrix_inverse(matrix, m):
    det = int(np.linalg.det(matrix)) % m
    inverse = mod_inverse(det, m)

    if inverse is None:
        return None

    adj_matrix = np.round(np.linalg.inv(matrix) * det).astype(int) % m
    return (inverse * adj_matrix) % m


def parse_key(key_str):
    key_list = key_str.split('\n')
    try:
        key = [list(map(int, row.split())) for row in key_list if row.strip()]
        return key
    except ValueError:
        return None

def hill_cipher(text, key, mode):
    result = ""
    m = 26  # Size of the alphabet

    key_matrix = np.array(key)

    if key_matrix.shape != (3, 3):
        return "Error: Key must be a 3x3 matrix"

    inverse_matrix = matrix_inverse(key_matrix, m)

    if inverse_matrix is None:
        return "Error: Key matrix is not invertible"

    text = text.upper().replace(" ", "")
    padding = (3 - len(text) % 3) % 3
    text += "X" * padding  # Pad with 'X' if needed

    for i in range(0, len(text), 3):
        block = np.array([ord(char) - ord('A') for char in text[i:i + 3]])
        if mode == 'encrypt':
            result += ''.join([chr(np.sum(block * key_matrix) % m + ord('A'))])
        elif mode == 'decrypt':
            result += ''.join([chr(np.sum(block * inverse_matrix) % m + ord('A'))])

    return result
