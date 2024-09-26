from PIL import Image


def encrypt_image(input_image_path, output_image_path):
    # Open the input image
    img = Image.open(input_image_path)
    img = img.convert("RGB")  # Ensure image is in RGB mode
    
    # Load image data
    pixels = img.load()
    
    # Get image dimensions
    width, height = img.size
    
    # Encrypt by modifying each pixel
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            
            # Add 50 to each RGB value (this can be adjusted)
            encrypted_pixel = (min(r + 50, 255), min(g + 50, 255), min(b + 50, 255))
            
            # Set the new pixel
            pixels[x, y] = encrypted_pixel
    
    # Save the encrypted image
    img.save(output_image_path)
    print(f"Encrypted image saved as {output_image_path}")

# Function to decrypt an image by reversing the mathematical operation (e.g., subtract 50 from each pixel value)
def decrypt_image(input_image_path, output_image_path):
    # Open the encrypted image
    img = Image.open(input_image_path)
    img = img.convert("RGB")
    
    # Load image data
    pixels = img.load()
    
    # Get image dimensions
    width, height = img.size
    
    # Decrypt by reversing the operation on each pixel
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            
            # Subtract 50 from each RGB value (inverse of encryption)
            decrypted_pixel = (max(r - 50, 0), max(g - 50, 0), max(b - 50, 0))
            
            # Set the new pixel
            pixels[x, y] = decrypted_pixel
    
    # Save the decrypted image
    img.save(output_image_path)
    print(f"Decrypted image saved as {output_image_path}")

# Paths to your images (you mentioned the following paths)
input_image_path = r"E:\python pjt\Prodigy\b9984b85050a8bfa17ce5befc7cfba6b.jpg"
encrypted_image_path = r"E:\python pjt\Prodigy\encrypted_image.jpg"
decrypted_image_path = r"E:\python pjt\Prodigy\decrypted_image.jpg"

# Encrypt the image
encrypt_image(input_image_path, encrypted_image_path)

# Decrypt the image
decrypt_image(encrypted_image_path, decrypted_image_path)
