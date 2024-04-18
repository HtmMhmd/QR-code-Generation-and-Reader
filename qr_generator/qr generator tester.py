from QRgenerator import QRCodeGenerator

print("INPUT YOUR STRING TO BE CONVERTED TO QRCODE:")
#data  = input()
data = "https://www.google.com"
qr = QRCodeGenerator()
qr.generate_qr_code(data)
print("THE DECODED STRING IS:")
print(qr.decode_qr_code())
