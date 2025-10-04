import qrcode
import random
import string
import time

def generate_qrcode(input_text):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    qr.add_data(input_text)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.show()
def generate_input_text(no_characters):
    characters = string.ascii_letters + string.digits + string.punctuation
    input_text = ''.join(random.choices(characters,k = no_characters))
    return input_text
    
def dynamic_qrcode(no_characters,no_images):
    for i in range(no_images):
        generate_qrcode(generate_input_text(no_characters))
        time.sleep(5)

dynamic_qrcode(12,5)
