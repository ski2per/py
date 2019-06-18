import smtplib


sender = 'zhangpeng@cetcxl.com'
receivers = ['67784480@qq.com']

message = """
This is a test e-mail message.
"""

smtpobj = smtplib.SMTP('mail.cetcxl.com',25)

smtpobj.login('luna_help@cetcxl.com', 'zdsys8301')
smtpobj.sendmail(sender, receivers, message)
print("Successfully sent email")