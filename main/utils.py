import qrcode
from RuqsatAl.settings import MEDIA_ROOT


def embed_QR(content):
    qr = qrcode.make(content)
    file = f'{MEDIA_ROOT}/{content}.png'
    qr.save(file)
    return file
