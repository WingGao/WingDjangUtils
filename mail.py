import smtplib
from email.mime.text import MIMEText
import random
import string

#####################
mail_host = "smtp.163.com"
mail_user = "wingnotify"
mail_pass = "glmsenwnvukxascb"
mail_postfix = "163.com"


######################
def send_mail(to_list, sub, content, content_format='plain'):
    '''
    send_mail("aaa@126.com","sub","content")
    '''
    me = mail_user + "<" + mail_user + "@" + mail_postfix + ">"
    msg = MIMEText(content, content_format, 'utf-8')
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
    except Exception as e:
        print(str(e))
        return False


def random_mail():
    method = random.choice(['qq', 'name'])
    acc = ''
    rd = random.SystemRandom()
    if method == 'qq':
        acc = str(rd.randint(1171748, 9159171748))
    elif method == 'name':  # gyy19910101/gyy1010
        acc = ''.join([rd.choice(string.ascii_lowercase) for i in
                       range(rd.randint(2, 3))])
        acc += '{}{:0>2}{:0>2}'.format(rd.choice([2018 - rd.randint(16, 50), ''])
                                       , rd.randint(1, 12), rd.randint(1, 28))
    host = rd.choice(['qq.com', '163.com', 'sina.com', 'sohu.com'])

    return acc + '@' + host


if __name__ == '__main__':
    if send_mail(['wing.gao@live.com'], "subject", "content"):
        print("success")
    else:
        print("fail")
