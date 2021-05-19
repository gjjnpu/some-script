import smtplib
from email.mime.text import MIMEText



smtpserver = "smtp.163.com" 

sender = "******@163.com" 
psw = "***" # not password, it should be authorization code 

receiver = "******@qq.com"

subject = "this is an example form 163"

msg = MIMEText('hello send by python', "plain", "utf-8")

# below format <>
msg['From'] = 'frome email <%s>'%sender
msg['To'] = "to <"******@qq.com>"
msg['Subject'] = subject

smtp = smtplib.SMTP()
smtp.connect(smtpserver) 
smtp.login(sender, psw) 
smtp.sendmail(sender, [receiver], msg.as_string()) 
smtp.quit() 