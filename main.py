import qrcode

# URL or any text you want to encode

print("Hello user. Welcome to QR Code for URL.")
print("Enter the URL here: ")
input_url = input()


# Create QR code instance
qr = qrcode.QRCode(
    version=1,  # controls size of QR code: 1 is smallest
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # error correction level
    box_size=10,  # size of each box in the QR code
    border=4,  # thickness of the border (default 4)
)

# Add data
qr.add_data(input_url)
qr.make(fit=True)

# Create an image
img = qr.make_image(fill_color="black", back_color="white")

img.show() #without saving the image you can also show your image

# Save the image
img.save("output.png")

print("QR Code generated and saved as output.png")
