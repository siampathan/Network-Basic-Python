import hashlib

def sha512_hash(message):
    # Create a new sha512 hash object
    sha512 = hashlib.sha512()
    
    # Update the hash object with the bytes-like object (message)
    sha512.update(message.encode('utf-8'))
    
    # Return the hexadecimal representation of the digest
    return sha512.hexdigest()

if __name__ == "__main__":
    message = input("Enter the message to hash: ")
    
    # Generate SHA-512 hash
    hash_value = sha512_hash(message)
    
    print("SHA-512 Hash:", hash_value)
