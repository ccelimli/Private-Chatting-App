from Crypto.Cipher import DES3
from hashlib import md5

key = "0Ax8n5Zizf"
key_hash = md5(key.encode('ascii')).digest()
tdes_key = DES3.adjust_key_parity(key_hash)
cipher = DES3.new(tdes_key, DES3.MODE_EAX, nonce=b'0')


def encryption(filePath):
    path = open(filePath, 'rb')
    fileBytes = path.read()
    writePath = open(filePath, "wb")
    newFileBytes = cipher.encrypt(fileBytes)
    writePath.write(newFileBytes)


def decryption(filePath):
    path = open(filePath, 'rb')
    fileBytes = path.read()
    newFileBytes = cipher.decrypt(fileBytes)
    return newFileBytes.decode('utf-8')


def passwordDecryption(password):
    with open('password.txt', 'w') as invitationPassword:
        invitationPassword.write(password)
    path = open('password.txt', 'rb')
    fileBytes = path.read()
    newFileBytes = cipher.decrypt(fileBytes)
    return newFileBytes.decode('utf-8')
