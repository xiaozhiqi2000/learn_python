#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 这是带参数的发邮件的函数

def sendmail(*args, **kwargs):
    """
    :param args: 邮箱地址以逗号分隔
    :param kwargs: 邮件地址，邮件发件人，邮件收件人，邮件内容
    :return:
    """

    try:
        import smtplib
        from email.mime.text import MIMEText
        from email.utils import formataddr

        for i in range(len(args)):
            msg = MIMEText(kwargs['email_content'], 'plain', 'utf-8')
            msg['From'] = formataddr([kwargs['from_email'], 'pythonxiao@126.com'])
            msg['To'] = formataddr([kwargs['to_email'], '329275108@qq.com'])
            msg['Subject'] = kwargs['email_subject']

            server = smtplib.SMTP("smtp.126.com", 25)
            server.login("pythonxiao@126.com", "xiaozhiqi2016")

            server.sendmail('pythonxiao@126.com', [args[i], ], msg.as_string())
            server.quit()
    except:
        return False
    else:
        return True

msg_dic = {"email_content": "邮件内容",
           "from_email": "发件人",
           "to_email": "收件人",
           "email_subject": "邮件主题"}


email = input("input your email,muliti email use ',' split>>>")

email_list = email.split(",")

ret = sendmail(*email_list, **msg_dic)
if ret:
    print("send success")
else:
    print("send faild")
