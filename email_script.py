import smtplib
import os
from email.mime.text import MIMEText

#find email body in text file
daily_schedule = ''
file = open(os.getcwd() + "\\schedule.txt",'r')
msg = MIMEText(file.read())
file.close()

#set up subject line
msg['Subject'] = "Things To Do"

#do SMTP mumbo jumbo
smtpObj = smtplib.SMTP('smtp.gmail.com',587)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login('python.hyatt@gmail.com','command and')
value = smtpObj.sendmail('hyatt.denesik@gmail.com','hyatt.denesik@gmail.com',msg.as_string())

#if value dictionary not empty try again, indicates failure
if value:
    value = smtpObj.sendmail('hyatt.denesik@gmail.com','hyatt.denesik@gmail.com',msg.as_string())
smtpObj.quit()