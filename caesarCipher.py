def caesar_cipher(text, shift):
    result = ""
    
    # Traverse through each character in the text
    for char in text:
        # Encrypting uppercase letters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypting lowercase letters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        # Non-alphabetic characters remain unchanged
        else:
            result += char
    
    return result

def encrypt(plaintext, shift):
    return caesar_cipher(plaintext, shift)

def decrypt(ciphertext, shift):
    return caesar_cipher(ciphertext, -shift)

if __name__ == "__main__":
    # User input for plaintext and shift value
    plaintext = input("Enter the text to encrypt: ")
    shift = int(input("Enter the shift value (1-25): "))

    encrypted = encrypt(plaintext, shift)
    print("Encrypted:", encrypted)

    # Option to decrypt
    decrypt_choice = input("Do you want to decrypt the text? (y/n): ")
    if decrypt_choice.lower() == 'y':
        decrypted = decrypt(encrypted, shift)
        print("Decrypted:", decrypted)
