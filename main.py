import qrcode
import uuid
import os

url = input("Enter the URL: ").strip()

unique_filename = f"qrcode_{uuid.uuid4().hex}.png"
directory = "/home/turdiali/Projects/qr_codes"
file_path = os.path.join(directory, unique_filename)

os.makedirs(directory, exist_ok=True)

qr = qrcode.QRCode()
qr.add_data(url)

img = qr.make_image()
img.save(file_path)

print(f"QR Code was generated! Saved as: {file_path}")
