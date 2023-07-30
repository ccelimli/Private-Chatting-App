import re
import smtplib

from PasswordControl import passwordControl


def emailControl(domainInfo, portInfo, members):
    try:
        regexPattern = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
        subject = "Invitation for chat"
        message = "You have been invited for a private chat channel!"
        content = "Subject: {0}\n{1}\nDomain Info: {2}\n" \
                  "Port Number Info: {3}\nPassword: ({4})".format(subject, message, domainInfo, portInfo, passwordControl())

        sender = "salihkpln1@gmail.com"
        password = "mxbdlwrzatdwaciv"
        receiver = []

        for i in range(int(members)):
            i = input('Enter the participants mail: ')
            member = re.match(regexPattern, i)
            if member:
                receiver.append(i)
            else:
                print('Invalid mail address')
                exit(0)

        mail = smtplib.SMTP("smtp.gmail.com", 587)
        mail.ehlo()
        mail.starttls()
        mail.login(sender, password)
        mail.sendmail(sender, receiver, content.encode("utf-8"))
        mail.quit()

        print("Mail sent")

    except Exception as e:
        print("Error", e)
