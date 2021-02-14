import subprocess
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import requests
import os
import time

print(start of the program)
def send_mail():

    details = subprocess.getoutput("ifconfig")
    print(details)
    sender_address = 'shreyasarunesh161297@gmail.com'
    receiver_address = 'shreyasarunesh161297@gmail.com'
    sender_pass = 'gyxe wbln pxla jkcn'
    
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'Raspbarri Pi - Login Details'
    message.attach(MIMEText(details, 'plain'))
    
    session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
    session.starttls() #enable security
    session.login(sender_address, sender_pass) #login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    print('Mail Sent')



ADDRESS_FILE = '/tmp/old_ip_address.txt'
def detect_ip_change():
    blnDelta = False
    currIp = requests.get('https://api.ipify.org').text

    if not os.path.isfile(ADDRESS_FILE):
        persist_ip('127.0.0.1')

    oldIp = read_old_ip()

    if currIp != oldIp:
        blnDelta = True

    persist_ip(currIp)
    return (blnDelta, currIp)


def persist_ip(ip):
    f = open(ADDRESS_FILE, 'w')
    f.write(ip)
    f.close()


def read_old_ip():
    f = open(ADDRESS_FILE, 'r')
    oldIp = f.read()
    f.close()
    return oldIp



def main():
    time.sleep(120)
    send_mail()
    while (True):
        try:
            deltaTuple = detect_ip_change()
            if deltaTuple[0] is True:
                send_mail()(deltaTuple[1])
            else:
                print("No change")
            time.sleep(300)
        except:
            continue


if __name__ == '__main__':
    main()


