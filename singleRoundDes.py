def permute(bits, table):
    return ''.join(bits[i] for i in table)

def xor(bits1, bits2):
    return ''.join('1' if b1 != b2 else '0' for b1, b2 in zip(bits1, bits2))

def sbox_lookup(sbox, bits):
    row = int(bits[0] + bits[3], 2)
    col = int(bits[1] + bits[2], 2)
    return format(sbox[row][col], '02b')

def feistel_function(right, key):
    # Expansion Permutation
    expansion_table = [3, 0, 1, 2, 1, 2, 3, 0]
    expanded = permute(right, expansion_table)
    
    # XOR with the key
    xor_result = xor(expanded, key)
    
    # S-Boxes
    sboxes = [
        [[1, 0, 3, 2], [3, 2, 1, 0]],  # S1
        [[0, 1, 2, 3], [2, 0, 1, 3]],  # S2
    ]
    
    # Apply S-Boxes
    sbox_output = ''
    for i in range(0, len(xor_result), 4):
        sbox_output += sbox_lookup(sboxes[i // 4], xor_result[i:i+4])
    
    # P4 Permutation
    p4_table = [1, 3, 2, 0]
    return permute(sbox_output, p4_table)

def single_round_encrypt(plaintext, key):
    # Initial permutation
    initial_permutation = [1, 3, 2, 0]
    permuted_input = permute(plaintext, initial_permutation)
    
    left, right = permuted_input[:2], permuted_input[2:]
    
    # Feistel function
    f_output = feistel_function(right, key)
    
    # Combine left and right
    new_left = right
    new_right = xor(left, f_output)
    
    # Final permutation (inverse of initial permutation)
    final_permutation = [1, 2, 3, 0]
    combined = new_left + new_right
    return permute(combined, final_permutation)

def single_round_decrypt(ciphertext, key):
    # Similar to encryption but with the Feistel function applied in reverse
    initial_permutation = [1, 3, 2, 0]
    permuted_input = permute(ciphertext, initial_permutation)
    
    left, right = permuted_input[:2], permuted_input[2:]
    
    # Feistel function
    f_output = feistel_function(right, key)
    
    # Combine left and right
    new_left = xor(left, f_output)
    new_right = right
    
    # Final permutation (inverse of initial permutation)
    final_permutation = [1, 2, 3, 0]
    combined = new_left + new_right
    return permute(combined, final_permutation)

def string_to_bits(s):
    return ''.join(format(ord(c), '04b') for c in s)

def bits_to_string(bits):
    chars = [chr(int(bits[i:i+4], 2)) for i in range(0, len(bits), 4)]
    return ''.join(chars)

def pad_bits(bits):
    # Pad the bits to make the length a multiple of 4
    while len(bits) % 4 != 0:
        bits += '0'  # You can choose to pad with '0' or another character
    return bits

if __name__ == "__main__":
    key = "1100"  # Example 4-bit key

    plaintext = input("Enter the text to encrypt (only letters will be converted to 4-bit): ")
    plaintext_bits = string_to_bits(plaintext)
    plaintext_bits = pad_bits(plaintext_bits)  # Pad the bits

    encrypted = ''
    for i in range(0, len(plaintext_bits), 4):
        block = plaintext_bits[i:i+4]
        encrypted_block = single_round_encrypt(block, key)
        encrypted += encrypted_block

    print("Encrypted:", encrypted)

    decrypted = ''
    for i in range(0, len(encrypted), 4):
        block = encrypted[i:i+4]
        decrypted_block = single_round_decrypt(block, key)
        decrypted += decrypted_block

    decrypted_text = bits_to_string(decrypted)
    print("Decrypted:", decrypted_text)
