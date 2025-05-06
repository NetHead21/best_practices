from twilio.rest import Client

account_sid = "your account sid here"
auth_token = "your account token here"
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_="insert twilio generated number here",
    body="Hello World",
    to="recipient number",
)

print(message.sid)
