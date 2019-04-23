#!/usr/bin/python
from concurrent.futures import ThreadPoolExecutor

import smtplib
from email.mime.text import MIMEText
#from subprocess import check_output

#log = check_output(['git', 'log', '-1', '--stat', 'HEAD'])
#log = commands.getstatusoutput('git log -1');

def sendmail(to):
    msg = MIMEText("Look, I'm actually doing some work:\n \n  studygit.git setsid")

    msg['Subject'] = 'Git post-push hook notification'
    msg['From'] = 'cfets_rm_git@hotmail.com'
    msg['To'] = 'liuyongkai@chinamoney.com.cn;'
    #Password:cfets1234abcd
    SMTP_SERVER = 'smtp.live.com'
    SMTP_PORT = 587

    session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    session.ehlo()
    session.starttls()
    session.ehlo()
    session.login(msg['From'], 'cfets1234abcd')

    session.sendmail(msg['From'], msg['To'], msg.as_string())
    session.quit()


executor = ThreadPoolExecutor(max_workers=4)
mails = 'liuyongkai@chinamoney.com.cn;'
all_task = [executor.submit(sendmail, (to)) for to in mails]
print("abcdefg")
