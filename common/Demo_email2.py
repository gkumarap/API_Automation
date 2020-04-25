import imghdr
import smtplib
from email.message import EmailMessage
from common.Demo_email import fromEmail
from common.Demo_email import toEmail
from common.Demo_email import password

toEmailAddresslist ={'anantsmail@gmail.com','mailztoprabha@gmail.com','aravinthdec07@gmail.com','govindec15@gmail.com'}
message = EmailMessage()
message['subject'] = 'enchanced python script using SSL encryption not TLS '
message['FROM'] =  fromEmail
message['TO'] = toEmail
message.set_content('Attachment TEST')

with open('IMG_4732.JPG','rb') as file:
    data = file.read()
    file_type = imghdr.what(file.name)
    print(file_type)
    file_name = file.name
message.add_attachment(data,maintype='image',subtype=file_type,filename = file_name)
with smtplib.SMTP_SSL('smtp.gmail.com',465) as msg:
    msg.login(fromEmail,password)
    msg.send_message(message)
    msg.close()
