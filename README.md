🌐 URL QR Code Generator using Python

This is a simple and effective QR Code Generator built in Python using the qrcode library. It allows users to generate a QR code from any URL input and both display and save it as an image (output.png).

🛠️ Features
Accepts any valid URL as input

Generates a clean QR code image

Automatically opens the QR code image after creation

Saves the image as output.png in the working directory

Customizable size, border, and error correction level

💡 How It Works
The user is prompted to input a URL.

The QR code is generated using the qrcode library with defined size and settings.

The image is:

Displayed instantly (without needing to save manually).

Saved as output.png in the current folder.

✅ Example Run

Hello user. Welcome to QR Code for URL.
Enter the URL here:
https://google.com
QR Code generated and saved as output.png
🧰 Requirements
Python 3.x

qrcode

Pillow (image processing backend for saving and showing the image)

Install with:

pip install qrcode[pil]
🖼 Output
The QR code will be displayed automatically using your system’s default image viewer.

It will also be saved as output.png.

⚙️ Configuration Details (Inside Code)
Parameter	Description
version=1	Smallest size QR code
box_size=10	Size of each block in the QR
border=4	Standard white border around the code
ERROR_CORRECT_L	Low level error correction
