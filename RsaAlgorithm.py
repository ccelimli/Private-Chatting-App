import rsa

(publicKey, privateKey) = rsa.newkeys(1024)

def writeKeystoFile():
    with open('publicKey.pem', 'wb') as f:
        f.write(publicKey.save_pkcs1('PEM'))

    with open('privateKey.pem', 'wb') as f:
        f.write(privateKey.save_pkcs1('PEM'))


def encode(message):
    encryptedMessage = rsa.encrypt(message, publicKey)
    print('\nEncrypted message: ' + str(encryptedMessage))
    return encryptedMessage


def decode(encryptedMessage):
    decryptedMessage = rsa.decrypt(encryptedMessage, privateKey)
    return decryptedMessage
