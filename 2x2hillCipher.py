import numpy as np
from math import gcd

def mod26(n):
    return n % 26

def create_matrix(key):
    return np.array(key).reshape(2, 2)

def get_inverse_matrix(matrix):
    det = int(np.round(np.linalg.det(matrix)))  # Determinant
    if gcd(det, 26) != 1:
        raise ValueError("The key matrix is not invertible under mod 26.")
    
    det_inv = pow(det, -1, 26)  # Modular inverse of the determinant
    matrix_inv = (det_inv * np.round(det * np.linalg.inv(matrix)).astype(int)) % 26
    return matrix_inv.astype(int)

def process_text(text, key_matrix):
    text = text.replace(" ", "").upper()
    if len(text) % 2 != 0:
        text += 'X'  # Padding if necessary
    
    result = ""
    for i in range(0, len(text), 2):
        block = np.array([ord(text[i]) - 65, ord(text[i + 1]) - 65])
        transformed_block = (key_matrix @ block) % 26
        result += ''.join(chr(x + 65) for x in transformed_block)
    
    return result

def encrypt(plaintext, key):
    key_matrix = create_matrix(key)
    return process_text(plaintext, key_matrix)

def decrypt(ciphertext, key):
    key_matrix = create_matrix(key)
    inv_key_matrix = get_inverse_matrix(key_matrix)
    return process_text(ciphertext, inv_key_matrix)

if __name__ == "__main__":
    key = [6, 24, 1, 13]  # Example key matrix

    try:
        plaintext = input("Enter the text to encrypt (only letters, spaces will be ignored): ")
        
        encrypted = encrypt(plaintext, key)
        print("Encrypted:", encrypted)

        decrypted = decrypt(encrypted, key)
        print("Decrypted:", decrypted)
    except ValueError as e:
        print("Error:", e)
