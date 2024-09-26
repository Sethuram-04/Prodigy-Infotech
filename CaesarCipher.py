def encrypt(text, shift):
    result = ""
    
    # Loop through each character in the text
    for i in range(len(text)):
        char = text[i]
        
        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        
        # Encrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        
        else:
            result += char
    
    return result

# Function to decrypt the text using Caesar Cipher
def decrypt(text, shift):
    return encrypt(text, -shift)

# Main function
if __name__ == "__main__":
    # Input from the user
    message = input("Enter the message: ")
    shift = int(input("Enter the shift value: "))
    
    # Encrypt the message
    encrypted_message = encrypt(message, shift)
    print(f"Encrypted Message: {encrypted_message}")
    
    # Decrypt the message
    decrypted_message = decrypt(encrypted_message, shift)
    print(f"Decrypted Message: {decrypted_message}")