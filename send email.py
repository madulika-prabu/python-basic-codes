# email sender
 
import smtplib

def SendEmail(to, content):
  server=smtplib.SMTP('smtp.gmail.com',587)
  server.ehlo()  #ehlo is an smtp command sent by mail server to identify itself when connencting to another email server
  server.starttls() #starttls start negotiation between server and client
  server.login('madulikaprabusankar@gmail.com','ndcstyfoyoslenyl') #your email , third party email login password
  server.sendmail('madulikaprabusankar@gmail.com',to, content)
  server.close()

if __name__=='__main__':
  try:
    content=input('type your text \n')
    to=input('whom to send email? \n')
    SendEmail(to,content)
    print('email has been sent')
  except Exception as e:
    print(e)
    print('sorry, email not sent')
