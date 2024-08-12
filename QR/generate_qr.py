import qrcode

# Define your domain and token value
domain = "https://www.nhcom.com/enter_pin.php"
token = "abc123"
url = f"{domain}?token={token}"

# Create a QR code instance
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Add the URL to the QR code
qr.add_data(url)
qr.make(fit=True)

# Create an image of the QR code
img = qr.make_image(fill='black', back_color='white')

# Save the QR code image
img.save("qr_with_token.png")
