from flask import Flask, render_template, request
import numpy as np
from vigenere_cipher import vigenere_cipher
from autokey import auto_key_vigenere_cipher
from extended_vigenere import extended_vigenere_cipher
from playfair import playfair_cipher
from affine import affine_cipher
from hill import hill_cipher
from super_encryption import super_encryption



app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/vigenere', methods=['GET', 'POST'])
def vigenere():
    result = ""
    if request.method == 'POST':
        text = request.form['text']
        key = request.form['key']
        mode = request.form['mode']

        if text and key:
            result = vigenere_cipher(text.upper(), key.upper(), mode)

    return render_template('vigenere_cipher.html', result=result)

@app.route('/autokey', methods=['GET', 'POST'])
def autokey():
    result = ""
    if request.method == 'POST':
        text = request.form['text']
        key = request.form['key']
        mode = request.form['mode']

        if text and key:
            result = auto_key_vigenere_cipher(text.upper(), key.upper(), mode)

    return render_template('auto_key_vigenere.html', result=result)

@app.route('/extended_vigenere', methods=['GET', 'POST'])
def extended_vigenere():
    result = ""
    if request.method == 'POST':
        text = request.form['text']
        key = request.form['key']
        mode = request.form['mode']

        if text and key:
            result = extended_vigenere_cipher(text, key, mode)

    return render_template('extended_vigenere.html', result=result)

@app.route('/playfair', methods=['GET', 'POST'])
def playfair():
    result = ""
    if request.method == 'POST':
        text = request.form['text']
        key = request.form['key']
        mode = request.form['mode']

        if text and key:
            result = playfair_cipher(text, key, 1 if mode == 'encrypt' else -1)

    return render_template('playfair.html', result=result)

@app.route('/affine', methods=['GET', 'POST'])
def affine():
    result = ""
    if request.method == 'POST':
        text = request.form['text']
        a = int(request.form.get('a', 1))  # Use 1 as default value if 'a' is not present
        b = int(request.form.get('b', 0))  # Use 0 as default value if 'b' is not present
        mode = request.form['mode']

        if text and 0 <= a < 26 and 0 <= b < 26:
            result = affine_cipher(text, a, b, mode)

    return render_template('affine_cipher.html', result=result)

def parse_key(key_str):
    key_list = key_str.split('\n')
    try:
        key = [list(map(int, row.split())) for row in key_list if row.strip()]
        return key
    except ValueError:
        return None

@app.route('/hill', methods=['GET', 'POST'])
def hill():
    result = ""
    example_key = "2 4 5\n9 2 1\n3 17 7"

    if request.method == 'POST':
        text = request.form['text']
        key_str = request.form['key']
        mode = request.form['mode']

        key = parse_key(key_str)

        if key is None:
            return "Error: Invalid key format"

        if text and key:
            result = hill_cipher(text, key, mode)

    return render_template('hill_cipher.html', result=result, example_key=example_key)

@app.route('/super_encryption', methods=['GET', 'POST'])
def super_encryption():
    result = ""

    if request.method == 'POST':
        text = request.form['text']
        key_vigenere = request.form['key_vigenere']
        key_transposition = request.form['key_transposition']
        mode = request.form['mode']

        if text and key_vigenere and key_transposition:
            result = super_encryption(text, key_vigenere, key_transposition, mode)

    return render_template('super_encryption.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)
