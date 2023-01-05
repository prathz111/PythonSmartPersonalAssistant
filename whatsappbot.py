from twilio.rest import Client

account_sid = 'AC9355cdf187a2c833b689c679d404a959'
auth_token = '92aabda01e13bba34a2a3a2e5ce059df'
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='whatsapp:+14155238886',
    body='Hello this is whatsapp111111',
    to='whatsapp:+1510'
)

print(message.sid)