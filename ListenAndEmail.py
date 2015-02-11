import subprocess
import smtplib
import socket
from email.mime.text import MIMEText
import RPi.GPIO as GPIO
import datetime
import time
import sys

#GPIO Setup
print("GPIO Setup")
inputPin = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(inputPin,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

# read the to email, from email and from password from config file
emailConfigFile ='/home/pi/tools/email.conf'
params = [line.strip() for line in open(emailConfigFile)]

if len(params) >= 3:
  to = params[0]
  gmail_user = params[1]
  gmail_password = params[2]

print(to)
print(gmail_user)
print(gmail_password)

today = datetime.date.today()
buttonPressed = False

while True:
  #take a reading
  input = GPIO.input(inputPin)

  if (input):
    print("Send Email")
    msg = MIMEText('ROTATE YOUR LAUNDRY')
    msg['Subject'] = 'Pi-Notify on %s' % today.strftime('%b %d %Y')
    msg['From'] = gmail_user
    msg['To'] = to
    smtpserver = smtplib.SMTP('smtp.gmail.com', 587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo
    smtpserver.login(gmail_user, gmail_password)
    smtpserver.sendmail(gmail_user, [to], msg.as_string())
    smtpserver.close()
    time.sleep(60);
      


