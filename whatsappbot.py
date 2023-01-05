from twilio.rest import Client

account_sid = '<Token>'
auth_token = '<Twilio Token>'
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='whatsapp:+14155238886',
    body='Hello this is whatsapp111111',
    to='whatsapp:+1510'
)

print(message.sid)
