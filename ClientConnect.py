import socket
import threading

from FileEncryption import passwordDecryption

encryptedPassword = input('Encrypted password: ')
decryptedPasswordData = passwordDecryption(encryptedPassword)
print(decryptedPasswordData)

# Connecting Part
domain = input('Domain: ')
port = int(input('Port number: '))
nickname = input('Nickname: ')
password = input('Password: ')

if password != decryptedPasswordData:
    print("Error")
    exit(0)
else:
    # Connecting To Server
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((domain, port))

    def receive():
        while True:
            try:
                # Receive Message From Server
                # If 'NICK' Send Nickname
                message = client.recv(1024).decode('utf-8')
                if message == 'NICK':
                    client.send(nickname.encode('utf-8'))
                else:
                    print(message)
            except:
                # Close Connection When Error
                print("An error occured!")
                client.close()
                break

    def write():
        while True:
            from RsaAlgorithm import encode, decode

            message = '{}: {}\n'.format(nickname, input(''))
            encodedMessage = message.encode('utf-8')
            encryptedText = encode(encodedMessage)
            decryptedText = decode(encryptedText).decode('utf-8')
            client.send(decryptedText.encode('utf-8'))


    receive_thread = threading.Thread(target=receive)
    receive_thread.start()

    write_thread = threading.Thread(target=write)
    write_thread.start()