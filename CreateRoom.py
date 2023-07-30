import itertools
import socket
import sys
import threading
import time

from MailSender import emailControl

done = False


def animate():
    for c in itertools.cycle(['....', '.......', '..........', '............']):
        if done:
            break
        sys.stdout.write('\rCONFIRMING CONNECTION TO SERVER ' + c)
        sys.stdout.flush()
        time.sleep(0.1)


# Connection Data
host = '127.0.0.1'
port = int(input('Enter port number: '))
domainInfo = input('Enter domain address: ')
portInfo = int(input('Enter port number: '))
members = input('How many member will join: ')

emailControl(domainInfo, portInfo, members)

# Starting Server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(int(members))

thread_load = threading.Thread(target=animate)
thread_load.start()

time.sleep(4)
done = True

# Lists For Clients and Their Nicknames
clients = []
nicknames = []


def broadcast(message):
    for client in clients:
        client.send(message)


def handle(client):
    while True:
        try:
            # Broadcasting Messages
            message = client.recv(1024)
            broadcast(message)
        except:
            # Removing And Closing Clients
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast('{} left!'.format(nickname).encode('utf-8'))
            nicknames.remove(nickname)
            break


def receive():
    while True:
        # Accept Connection
        client, address = server.accept()
        print("\nConnected with {}".format(str(address)))

        # Request And Store Nickname
        client.send('NICK'.encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')
        nicknames.append(nickname)
        clients.append(client)

        # Show Public and Private Keys
        publicKey = open('publicKey.pem', 'r')
        privateKey = open('privateKey.pem', 'r')
        print(publicKey.read())
        print(privateKey.read())

        # Print And Broadcast Nickname
        print("Nickname is {}".format(nickname))
        client.send('Connected to server!\n'.encode('utf-8'))
        broadcast("{} joined!".format(nickname).encode('utf-8'))

        # Start Handling Thread For Client
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


receive()
