import smtplib
from email.mime.text import MIMEText

#####################
mail_host = "smtp.163.com"
mail_user = "wingnotify"
mail_pass = "glmsenwnvukxascb"
mail_postfix = "163.com"


######################
def send_mail(to_list, sub, content):
    '''
    send_mail("aaa@126.com","sub","content")
    '''
    me = mail_user + "<" + mail_user + "@" + mail_postfix + ">"
    msg = MIMEText(content)
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = ";".join(to_list)
    try:
        s = smtplib.SMTP()
        s.connect(mail_host)
        s.login(mail_user, mail_pass)
        s.sendmail(me, to_list, msg.as_string())
        s.close()
        return True
    except Exception, e:
        print str(e)
        return False


if __name__ == '__main__':
    if send_mail(['wing.gao@live.com'], "subject", "content"):
        print "success"
    else:
        print "fail"
