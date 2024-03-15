# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : send_email
  Description : 邮件发送
  Summary     : 1、
                2、
                3、
  Author      : chenyushencc@gmail.com
  date        : 2024/3/13 10:20
-------------------------------------------------
"""
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


def set_email():
    """ 设置完直接发送邮件 """
    # 请替换成你的邮箱地址和密码
    sender_email = 'your_email@163.com'
    authentication = ''     # TODO 授权码
    receiver_email = 'your_email@163.com'
    subject = 'Web Catch Email'
    body = 'Web Catch start~\nGood news is coming~'
    attachment_path = 'dedails.txt'  # 附件路径，也决定附件的名称，如果不需要附件可以设置为 None

    send_email(sender_email, authentication, receiver_email, subject, body, attachment_path)


def send_email(sender_email, authentication, receiver_email, subject, body, attachment_path=None):
    """ authentication 163邮箱是使用的授权码 """
    # 创建邮件消息
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # 添加正文内容
    msg.attach(MIMEText(body, 'plain'))

    # 添加附件
    if attachment_path:
        with open(attachment_path, "rb") as attachment:
            part = MIMEApplication(attachment.read(), Name=attachment_path)
            part['Content-Disposition'] = 'attachment; filename="%s"' % attachment_path
            msg.attach(part)

    # 连接到SMTP服务器并发送邮件
    with smtplib.SMTP_SSL('smtp.163.com', 465) as server:       # TODO
        server.login(sender_email, authentication)
        server.sendmail(sender_email, receiver_email, msg.as_string())


if __name__ == "__main__":
    # 请替换成你的邮箱地址和密码
    sender_email = 'your_email@163.com'
    authentication = ''
    receiver_email = 'your_email@163.com'
    subject = 'Web Catch Email'
    body = 'This is a test email sent from ShenYuChen`s Web Catch.'
    attachment_path = 'D:\\my_workspace\\helloshen\\tools\\web_catch\\dedails.txt'  # 附件路径，如果不需要附件可以设置为 None

    send_email(sender_email, authentication, receiver_email, subject, body, attachment_path)
