from Crypto.PublicKey import RSA 
import pyqrcode
import qrcode
from PIL import Image
import re


def generate_RSA(bits):
    '''
    Generate an RSA keypair with an exponent of 65537 in PEM format
    param: bits The key length in bits
    Return private key and public key
    '''
    
    new_key = RSA.generate(bits, e=65537) 
    public_key = new_key.publickey().exportKey("PEM") 
    private_key = new_key.exportKey("PEM") 
    return private_key, public_key

def QRcode(publicKey, privateKey):

    message_public = pyqrcode.create(publicKey)
   # message_public.svg('public.svg', scale=0.1)
    print(message_public.terminal(quiet_zone=1))
    message_public.show()

    input("Press enter to generate private key: ")
    
    message_private = pyqrcode.create(privateKey)
    #message_private.svg('private.svg', scale=0.1)
    print (message_private.terminal(quiet_zone=2))
    #message_private.show()

    path = "/Users/DariaZahaleanu/Desktop/Capstone/"

def QRCode_2(publicKey, privateKey):
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4,)
    qr.add_data(publicKey)
    qr.make(fit=True)
    img_public = qr.make_image(fill_color="black", back_color="white")
    img_public.save('public_key.png')

    #img.show()

    qr2 = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=3,)
    qr2.add_data(privateKey)
    qr2.make(fit=True)
    img_private = qr2.make_image(fill_color="black", back_color="white")
    img_private.save('private_key.png')
    #img2.show()

def main():
    keySize = input ("Enter the key size (>=1024, in multiples of 256): ")
    #print (keySize)
    privateKey, publicKey = generate_RSA(int(keySize));
    privateKey = privateKey.decode("utf-8") 
    privateKey = re.sub('-----BEGIN RSA PRIVATE KEY-----\n', '', privateKey)
    privateKey = re.sub('-----END RSA PRIVATE KEY-----', '', privateKey)
    print('Private key = ')
    print(privateKey)
    publicKey = publicKey.decode("utf-8") 
    publicKey = re.sub('-----BEGIN PUBLIC KEY-----\n', '', publicKey)
    publicKey = re.sub('-----END PUBLIC KEY-----', '', publicKey)
    print('Public key = ')
    print(publicKey)
    QRCode_2(publicKey, privateKey);
    
    # with Image.open('public.png') as img:
    #     img.show()
    # with Image.open('private.png') as img2:
    #     img2.show()


if __name__ == "__main__":
    main()
