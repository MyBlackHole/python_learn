import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

my_sender = "1358244533@qq.com"
my_user = "myisblackhole@163.com"
body = "........."
try:
    msg = MIMEText(body, "plain", "utf-8")
    msg["From"] = formataddr(["邮件预警", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
    msg["To"] = formataddr(["收件人昵称", my_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
    msg["Subject"] = "..."  # 邮件的主题，也可以说是标题

    server = smtplib.SMTP_SSL(host="smtp.qq.com", port=465)  # 发件人邮箱中的SMTP服务器，端口是465
    print(
        server.login(user="1358244533@qq.com", password="wettvkqaipkdfgdi")
    )  # 括号中对应的是发件人邮箱账号、邮箱密码
    server.sendmail(
        my_sender,
        [
            my_user,
        ],
        msg.as_string(),
    )  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
    server.quit()  # 关闭连接
except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
    ret = False
