import smtplib
from email.mime.application import MIMEApplication
from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import time
import re

host_server = 'smtp.163.com'
#sender_163 = 'chuikokching@163.com'
pwd = 'Xiaerdaren520'

sender_163_mail = 'chuikokching@163.com'
receiver = '455344883@qq.com'
sender_in_sent_box = re.search("(.*)@",receiver)
print(sender_in_sent_box.group(1))
sender_in_sent_box = sender_in_sent_box.group(1)

mail_title= 'AutoEmail-Test'
mail_content = """
chuikokching auto-email test
"""f'{time.localtime().tm_year} {time.localtime().tm_mon} {time.localtime().tm_mday}'

#添加附件 word
# wordFile = ''
# word = MIMEApplication(open(wordFile,'rb').read())
# word.add_header('Content-Disposition','attachment',filename='word') #设置附件信息
#
# #添加附件 pdf
# pdfFile = ''
# pdf = MIMEApplication(open(pdfFile,'rb').read())
# pdf.add_header('Content-Disposition','attachment',filename='pdf') #设置附件信息


#添加附件 pic
picFile = 'G:\Genshin Impact Mainland\Genshin Impact\Genshin Impact Game\ScreenShot\/1650869114446.jpg'
pic = MIMEApplication(open(picFile,'rb').read())
pic.add_header('Content-Disposition','attachment',filename='img') #设置附件信息


msg = MIMEMultipart() #邮件主体
msg["Subject"] = Header(mail_title,'utf-8')
msg["From"] = sender_163_mail
msg["To"] = Header(sender_in_sent_box,'utf-8')
msg.attach(MIMEText(mail_content,'plain','utf-8')) #如果content含有html 则plain需要改成html
msg.attach(pic)

try:
    smtp = smtplib.SMTP_SSL(host_server)
    smtp.set_debuglevel(0) #关闭debug
    smtp.ehlo(host_server)
    smtp.login(sender_163_mail,pwd)
    smtp.sendmail(sender_163_mail,receiver,msg.as_string())
    smtp.quit()
    print("Sent successfully!")
except smtplib.SMTPException:
    raise Exception("Failed!")