# to connect to gmail, you have to allow gmail to access less secure apps.
# reference to above can be found here  https://stackoverflow.com/questions/10147455/how-to-send-an-email-with-gmail-as-provider-using-python/27515833#27515833

# second you have to set the email and password as your system environment variables .
# reference for the above can be found here  https://www.youtube.com/watch?v=IolxqkL7cD8




import smtplib
import os

from email.message import EmailMessage

#Open file from local
currentpath = os.getcwd()


fromEmail = os.environ.get('USER_EMAIL')
print(fromEmail)
toEmail = {'arunamanikarnika@gmail.com'}
password = os.environ.get('EMAIL_PASSWORD')
print(password)





with smtplib.SMTP('smtp.gmail.com',587) as mail:
    mail.ehlo()
    mail.starttls()
    mail.ehlo()
    mail.login(fromEmail,password)
    mail.sendmail(fromEmail,toEmail,'Hello Darling !! \n sent from my python script \n wink wink')
    mail.close()

