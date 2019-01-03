'''
 Program to read data from database and email the data to users.
 This script can be used to set alert on data stored in prodcution database.
'''

# encoding=utf8

import cx_Oracle
import csv
import os
import mimetypes
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from email.mime.image import MIMEImage
from email.mime.audio import MIMEAudio

# write SQL statement - fetch data from database
SQL = "select Count(*) as "count", messege_type from outgoing_messages group by message_type"

# make connection to database
con = cx_Oracle.connect('username/password@SID')

# intiate cursor object
cur = con.cursor()

# call execute method from cursor and pass sql statement to execute it
cur.execute(SQL)

# handle file  in which you want to create save the data from database.
filename = "test.csv"
file1 = open(filename, "w")
file1.write('count'+ ',' 'message_type' + '\n')

# fetch the data and write row one by one in file
for row in cur:
    file1.write(row[0] + ',' + row[1].read() + '\n') #row[1].read() in case of CLOB data to convert it into string

#close the file , the cursor and the database connection
file1.close()
cur.close()
con.close()


''' =======emailing save data to users======'''

# Parameters for sending email
msg = MIMEMultipart()
msg["Subject"] = "test_email"
msg["From"] = "sender's email"
msg["To"] = "Receiver's email"
msg["Cc"] = "in copy receiver person's email id"
body = MIMEText("sending email using python")
msg.attach(body)
textMessage = msg.as_string()

# email attachment part

fileToSend = "test.csv"

ctype, encoding = mimetypes.guess_type(fileToSend)
if ctype is None or encoding is not None:
    ctype = "application/octet-stream"

maintype, subtype = ctype.split("/", 1)

print("Mail attachment start")

if maintype == "text":
    fp= open(fileToSend)
    # Note: we should handle calculating the charset
    attachment = MIMEText(fp.read(), _subtype=subtype)
    fp.close()
elif maintype == "image":
    fp = open(fileToSend, "rb")
    attachment = MIMEImage(fp.read(), _subtype=subtype)
    fp.close()
elif maintype == "audio":
    fp = open(fileToSend, "rb")
    attachment = MIMEAudio(fp.read(), _subtype=subtype)
    fp.close()
else:
    fp = open(fileToSend, "rb")
    attachment = MIMEBase(maintype, subtype)
    attachment.set_payload(fp.read())
    fp.close()

encoders.encode_base64(attachment)
attachment.add_header("Content-Disposition", "attachment", filename=fileToSend)
msg.attach(attachment)


smtp = smtplib.SMTP("hostName", portNumber)
smtp.sendmail(msg["From"], msg["To"].split(",") + msg["Cc"].split(","), msg.as_string())
