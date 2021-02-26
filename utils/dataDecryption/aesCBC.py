try:
    from crypto.Cipher import AES
except ModuleNotFoundError:
    from Crypto.Cipher import AES
from binascii import a2b_hex
from os import getenv
import json


def decrypt(cipher, mode=AES.MODE_CBC):
    plain_text = AES.new(key=getenv('INTERFACE_KEY'),
                         mode=mode,
                         IV='Wv1rN6#cv5Zwl8Tc').decrypt(a2b_hex(cipher))
    try:
        return json.loads(bytes.decode(plain_text).rstrip('\0'))
    except json.decoder.JSONDecodeError as e:
        return bytes.decode(plain_text).rstrip('\0')


print(decrypt('ca42f3c003f675fb5b71da3d0b0990d19f0539b99d42f8f9901740d9c5ac64f8'))
