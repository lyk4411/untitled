#!/usr/bin/python
from concurrent.futures import ThreadPoolExecutor

import smtplib
from email.mime.text import MIMEText
#from subprocess import check_output

#log = check_output(['git', 'log', '-1', '--stat', 'HEAD'])
#log = commands.getstatusoutput('git log -1');

def sendmail(to):
    msg = MIMEText("Look, I'm actually doing some work:\n \n  studygit.git setsid")
