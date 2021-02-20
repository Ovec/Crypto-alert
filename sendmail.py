import smtplib
from smtplib import SMTP_SSL as SMTP 
from email.mime.text import MIMEText

def sendEmail(pair, value, config):
    try:
        msgText = config["Body"].replace("X", pair).replace("Y", value)
        Msg = MIMEText(msgText, 'plain')
        Msg['Subject']= config["Subject"]
        Msg['From'] = config["From"]

        conn = SMTP(config["address"])
        conn.set_debuglevel(False)
        conn.login(config["username"], config["password"])
        try:
            conn.sendmail(config["From"], config["To"], Msg.as_string())
        finally:
            conn.quit()

    except Exception as e:
        print(e)