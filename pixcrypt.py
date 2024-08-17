from PIL import Image
import numpy as np
import os

# Banner
print("""
 ____  ____  _  _  ___  ____  _  _  ____  ____ 
(  _ \\(_  _)( \\/ )/ __)(  _ \\( \\/ )(  _ \\(_  _)
 )___/ _)(_  )  (( (__  )   / \\  /  )___/  )(  
(__)  (____)(_/\_)\\___)(_)\_) (__) (__)   (__) 
""")

def validate_extension(file_path):
    valid_extensions = ['.png', '.jpg', '.jpeg', '.bmp', '.tiff']
    ext = os.path.splitext(file_path)[1].lower()
    if ext not in valid_extensions:
        raise ValueError(f"Unsupported file extension: {ext}. Please use one of the following: {', '.join(valid_extensions)}")

def encrypt_image(image_path, output_path, key):
    try:
        # Validate output file extension
        validate_extension(output_path)
        
        # Load image
        img = Image.open(image_path)
        img = img.convert("RGB")
        
        # Convert image to numpy array
        img_array = np.array(img)
        
        # Apply encryption (e.g., adding key value to each pixel)
        encrypted_array = (img_array + key) % 256
        
        # Convert back to image and save
        encrypted_img = Image.fromarray(encrypted_array.astype('uint8'))
        encrypted_img.save(output_path)
        print(f"Encrypted image saved to {output_path}")

    except FileNotFoundError:
        print(f"File not found: {image_path}")
    except ValueError as ve:
        print(ve)
    except Exception as e:
        print(f"An error occurred: {e}")

def decrypt_image(image_path, output_path, key):
    try:
        # Validate output file extension
        validate_extension(output_path)
        
        # Load image
        img = Image.open(image_path)
        img = img.convert("RGB")
        
        # Convert image to numpy array
        img_array = np.array(img)
        
        # Apply decryption (e.g., subtracting key value from each pixel)
        decrypted_array = (img_array - key) % 256
        
        # Convert back to image and save
        decrypted_img = Image.fromarray(decrypted_array.astype('uint8'))
        decrypted_img.save(output_path)
        print(f"Decrypted image saved to {output_path}")

    except FileNotFoundError:
        print(f"File not found: {image_path}")
    except ValueError as ve:
        print(ve)
    except Exception as e:
        print(f"An error occurred: {e}")

# Prompt the user to select the operation
operation = input("Do you want to encrypt or decrypt an image? (enter 'encrypt' or 'decrypt'): ").strip().lower()

# Manually enter the path of the input image
input_image_path = input("Enter the full path of the image: ")

# Manually enter the path of the output image
output_image_path = input("Enter the full path for the output image (with extension): ")

# Manually enter the encryption/decryption key
try:
    key = int(input("Enter the key (a number): "))
except ValueError:
    print("Invalid key. Please enter a valid integer.")
    key = 0  # Default to 0 if invalid key is provided

if input_image_path and output_image_path:
    if operation == 'encrypt':
        encrypt_image(input_image_path, output_image_path, key)
    elif operation == 'decrypt':
        decrypt_image(input_image_path, output_image_path, key)
    else:
        print("Invalid operation. Please enter 'encrypt' or 'decrypt'.")
else:
    print("No file path provided.")
