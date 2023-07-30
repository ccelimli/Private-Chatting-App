def createPassword(password):
    with open('password.txt', 'wb') as invitationPassword:
        invitationPassword.write(password.encode('utf-8'))