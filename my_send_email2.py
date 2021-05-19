import smtplib
from email.mime.text import MIMEText



smtpserver = "smtp.qq.com" 
port = 587
sender = "*****@qq.com" 
#psw = "****" # not password, it should be authorization code 

receiver = "******@163.com"

subject = "this is an example form 163"

msg = MIMEText('hello send by python', "plain", "utf-8")
msg['From'] = 'frome email <%s>'%sender
msg['To'] = "to <*****@163.com>"
msg['Subject'] = subject

smtp = smtplib.SMTP()
smtp.connect(smtpserver,port) 
smtp.login(sender, psw) 
smtp.sendmail(sender, [receiver], msg.as_string()) 
smtp.quit() 