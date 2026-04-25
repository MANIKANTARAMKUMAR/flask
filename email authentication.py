import smtplib

from email.message import EmailMessage

#email details

senderemaild="manikantaramkumar760@gmail.com"

receiveremailid="rammpandalaneni@gmail.com"

password="mnbp rqvs qjcr bxzw"

#email content 

subject ="invitation"

body="""

hello world
"""
#create email path 

msg=EmailMessage()

msg["Subject"]=subject

msg["From"]=senderemaild

msg["To"]=receiveremailid

msg.set_content(body)

#send email
try:
  
  with smtplib.SMTP_SSL("smtp.gmail.com",465) as smtp:
    smtp.login(senderemaild,password)
    smtp.send_message(msg)
    print("email sent successfully")
except Exception as e:
  print("exeption is :",e)
