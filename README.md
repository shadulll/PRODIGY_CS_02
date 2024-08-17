# PRODIGY_CS_02

PIXCRYPT

PixCrypt is a simple yet effective image encryption and decryption tool that uses pixel manipulation techniques. 
The project allows users to securely encrypt and decrypt images by applying a mathematical operation 
(like adding or subtracting a key value) to the pixel values of the image.

Key Features:

Encryption:

Encrypts an image by modifying each pixel's color values using a user-defined key.
The encryption process ensures that the original image is transformed into an unreadable format.

Decryption:

Decrypts the encrypted image using the same key that was used during encryption.
Restores the original image by reversing the mathematical operation applied during encryption.

User Input:

Manual Path Selection: Users manually enter the full path for both the input and output images.

Key Input: 

Users provide an integer key that is used for the encryption and decryption process.

Operation Selection: 

Users choose between encryption and decryption through a prompt.

Error Handling:

The tool includes error handling for file not found issues, invalid file extensions, and invalid key inputs.

File Format Support:

Supports common image formats including .png, .jpg, .jpeg, .bmp, and .tiff.

How It Works:

User Interface:

The program begins by displaying a banner, which adds a professional and visually appealing touch.
Users are prompted to choose whether they want to encrypt or decrypt an image.

Input Image Path:

Users input the full path of the image they wish to encrypt or decrypt.

Output Image Path:

Users specify the full path where the resulting encrypted or decrypted image will be saved.

Key Input:

Users enter an integer key that will be used to modify the pixel values during encryption or decryption.

Execution:

Depending on the user’s choice, the script either encrypts or decrypts the image and saves the output to the specified path.

Validation:

The script checks if the output file has a valid extension and whether the key provided is a valid integer.
