import random
from messaging.email_sender import Email


def authorize_sms() -> bool:
    sms_code = str(random.randint(1000, 9999))
    print(f"Send SMS code: {sms_code}")
    read_sms_code = input("Please enter the code sent to you by SMS: ")
    return read_sms_code == sms_code


def authorize_google() -> bool:
    auth_code = str(random.randint(1000, 9999))
    email = Email()
    recipient_email = input("Please enter your email address: ")
    email_body = f"Your authorization code is {auth_code}"
    email.send("Authorization Code", email_body, recipient_email)
    read_auth_code = input("Please enter the Google Auth code: ")
    return read_auth_code == auth_code


def authorize_robot() -> bool:
    read_auth_code = ""
    while read_auth_code not in ["Y", "N"]:
        read_auth_code = input("Are you a robot (Y/n): ").upper() or "Y"
    return read_auth_code == "N"
