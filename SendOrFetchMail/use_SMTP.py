
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

# Python对SMTP支持有smtplib和email两个模块，
# email负责构造邮件，smtplib负责发送邮件
# 注意到构造MIMEText对象时，
# 第一个参数就是邮件正文，
# 第二个参数是MIME的subtype，传入'plain'表示纯文本，最终的MIME就是'text/plain'，
# 最后一定要用utf-8编码保证多语言兼容性
msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')

# 发送HTML邮件,把第二个参数由plain变为html就可以了
msg = MIMEText('<html><body><h1>Hello</h1>' +
    '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
    '</body></html>', 'html', 'utf-8')

# 然后通过SMTP发出去
# 输入Email地址和口令
from_addr = input('From:')
password = input('Password:')
# 输入收件人地址
to_addr = input('To:')
# 输入SMIP服务器地址
smtp_server = input('SMTP server:')


import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('来自SMTPDM问候……', 'utf-8').encode()

server = smtplib.SMTP(smtp_server, 25) # SMTP协议默认端口为25
server.starttls() # 创建安全链接
server.set_debuglevel(1) # 打印出和SMTP服务器交互的所有信息
server.login(from_addr, password) # 登录SMTP服务器
server.sendmail(from_addr, [to_addr], msg.as_string()) # 发邮件，由于可以一次发给多个人，所以传入一个list
server.quit()
print('finish')


