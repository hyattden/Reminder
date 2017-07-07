import smtplib
from email.mime.text import MIMEText

daily_schedule = ''
file = open("C:\\Users\\Dylan\\Dropbox\\schedule.txt",'r')
msg = MIMEText(file.read())
file.close()

msg['Subject'] = "Things To Do"

smtpObj = smtplib.SMTP('smtp.gmail.com',587)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login('python.hyatt@gmail.com','command and')
value = smtpObj.sendmail('hyatt.denesik@gmail.com','hyatt.denesik@gmail.com',msg.as_string())
if value:
    value = smtpObj.sendmail('hyatt.denesik@gmail.com','hyatt.denesik@gmail.com',msg.as_string())
smtpObj.quit()