#YouTube channel 5starcoder
#subscribe my channel 
#project_11

import qrcode

# Data to encode
data = "https://example.com"

# Create QR code instance
qr = qrcode.QRCode(
    version=1,  # controls the size of the QR Code
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Add data
qr.add_data(data)
qr.make(fit=True)

# Create an image
img = qr.make_image(fill="black", back_color="white")

# Save the image
img.save("qrcode.png")

print("QR code generated and saved as qrcode.png")
