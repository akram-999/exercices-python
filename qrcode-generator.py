import qrcode

input_data = input("Enter the data to encode in the QR code: ")
fileName = input("Enter the filename to save the QR code (e.g., 'qrcode.png'): ")

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(input_data)
image = qr.make_image(fill_color="black", back_color="white")
image.save(fileName)
print(f"QR code generated and saved as {fileName}.")