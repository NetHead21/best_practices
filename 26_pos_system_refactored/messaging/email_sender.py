# """ email client class
#     read more https://www.sitepoint.com/quick-tip-sending-email-via-gmail-with-python/
#     https://mailtrap.io/blog/python-send-email-gmail/
# """

import smtplib
from email.mime.text import MIMEText


class Email:
    def __init__(self):
        self.email: str = "your email address"
        self.password: str = "your password"
        self.smtp_server: str = "smtp.gmail.com"
        self.smtp_port: int = 465

    def send(self, subject: str, body: str, recipients: str) -> None:
        msg = MIMEText(body)
        msg["Subject"] = subject
        msg["From"] = self.email
        msg["To"] = recipients
        with smtplib.SMTP_SSL(self.smtp_server, self.smtp_port) as smtp_server:
            smtp_server.login(self.email, self.password)
            smtp_server.sendmail(self.email, recipients, msg.as_string())
        print("Message sent!")


if __name__ == "__main__":
    subject = "Email Subject"
    body = "This is the body of the text message"
    recipients = "junivensaavedra@gmail.com"
    email = Email()
    email.send(subject, body, recipients)
