#Импортируем через терминал команду ( pip install "qrcode[pil]" )

import qrcode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('https://t.me/it_noraa')
qr.make(fit=True)

img = qr.make_image(fill_color="blue", back_color="white")
img.save("it_noraa.jpg","JPEG")