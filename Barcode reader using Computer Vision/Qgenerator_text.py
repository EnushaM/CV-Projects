import qrcode
# Link for website
input_data = "Sundar Pichai"
#Creating an instance of qrcode
qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5)
qr.add_data(input_data)
qr.make(fit=True)
img = qr.make_image(fill_color='black', back_color='white')
#img = qr.make_image(fill_color='red', back_color='white')
#img = qr.make_image(fill_color='blue', back_color='white')
img.save('2qrcode.png')
