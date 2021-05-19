import smtplib
from email.mime.text import MIMEText



smtpserver = "smtp.163.com" 

sender = "gaojunjienpu@163.com" 
psw = "***" # not password, it should be authorization code 

#psw = "suruo123" 
receiver = "463901631@qq.com"

subject = "this is an example form 163"

msg = MIMEText('hello send by python', "plain", "utf-8")
msg['From'] = 'frome email <%s>'%sender
msg['To'] = "to <463901631@qq.com>"
msg['Subject'] = subject

smtp = smtplib.SMTP()
smtp.connect(smtpserver) 
smtp.login(sender, psw) 
smtp.sendmail(sender, [receiver], msg.as_string()) 
smtp.quit() 