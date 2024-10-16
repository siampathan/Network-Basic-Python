import random
from sympy import isprime, mod_inverse

def generate_prime_candidate(length):
    # Generate an odd integer randomly
    p = random.getrandbits(length)
    return p | (1 << length - 1) | 1  # Ensure it's odd and has the desired length

def generate_prime_number(length):
    p = 4  # Start with a non-prime
    while not isprime(p):
        p = generate_prime_candidate(length)
    return p

def generate_keys(key_size):
    # Generate two distinct prime numbers
    p = generate_prime_number(key_size)
    q = generate_prime_number(key_size)
    
    while p == q:
        q = generate_prime_number(key_size)

    # Calculate n
    n = p * q
    
    # Calculate the totient
    phi = (p - 1) * (q - 1)

    # Choose an integer e such that 1 < e < phi and gcd(e, phi) = 1
    e = random.randrange(1, phi)
    while gcd(e, phi) != 1:
        e = random.randrange(1, phi)

    # Calculate d
    d = mod_inverse(e, phi)
    
    return (e, n), (d, n)  # Public and private keys

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def encrypt(public_key, plaintext):
    e, n = public_key
    # Convert plaintext to numbers
    plaintext_numbers = [ord(char) for char in plaintext]
    # Encrypt each number
    ciphertext = [(pow(char, e, n)) for char in plaintext_numbers]
    return ciphertext

def decrypt(private_key, ciphertext):
    d, n = private_key
    # Decrypt each number
    plaintext_numbers = [(pow(char, d, n)) for char in ciphertext]
    # Convert numbers back to characters
    plaintext = ''.join([chr(num) for num in plaintext_numbers])
    return plaintext

if __name__ == "__main__":
    key_size = 8  # Length of the key in bits
    public_key, private_key = generate_keys(key_size)

    print(f"Public Key: {public_key}")
    print(f"Private Key: {private_key}")

    plaintext = input("Enter the plaintext to encrypt: ")
    ciphertext = encrypt(public_key, plaintext)

    print("Ciphertext:", ciphertext)

    decrypted_text = decrypt(private_key, ciphertext)
    print("Decrypted text:", decrypted_text)
