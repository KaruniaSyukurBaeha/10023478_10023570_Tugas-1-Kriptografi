def prepare_playfair_key(key):
    key = key.upper().replace("J", "I")  # Replace 'J' with 'I'
    unique_chars = []
    for char in key:
        if char not in unique_chars:
            unique_chars.append(char)
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    for char in alphabet:
        if char not in unique_chars:
            unique_chars.append(char)
    playfair_key = [unique_chars[i:i+5] for i in range(0, 25, 5)]
    return playfair_key

def find_char_position(matrix, char):
    for i, row in enumerate(matrix):
        for j, col in enumerate(row):
            if col == char:
                return i, j
    return -1, -1

def playfair_cipher(text, key, mode):
    playfair_key = prepare_playfair_key(key)
    result = ""
    text = text.upper().replace("J", "I")

    for i in range(0, len(text), 2):
        pair = text[i:i+2]
        row1, col1 = find_char_position(playfair_key, pair[0])
        row2, col2 = find_char_position(playfair_key, pair[1])

        if row1 == row2:
            result += playfair_key[row1][(col1 + mode) % 5] + playfair_key[row2][(col2 + mode) % 5]
        elif col1 == col2:
            result += playfair_key[(row1 + mode) % 5][col1] + playfair_key[(row2 + mode) % 5][col2]
        else:
            result += playfair_key[row1][col2] + playfair_key[row2][col1]

    return result