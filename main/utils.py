import string
import random

import qrcode
from RuqsatAl.settings import MEDIA_ROOT


def embed_QR(content):
    S = 10  # number of characters in the string.
    ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k=S))
    qr = qrcode.make(f'{ran}')
    file = f'{MEDIA_ROOT}/{content}.png'
    qr.save(file)
    return file
