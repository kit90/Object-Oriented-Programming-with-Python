from twilio.rest import TwilioRestClient

account_sid = "AC838fdc49673606af683e5a6f16f04a50" # Your Account SID from www.twilio.com/console
auth_token  = "946e396ad84e91553bf4899121084d98"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Hello Akkuuse, from Achacha",
    to="+919447536580",    # Replace with your phone number
    from_="+13346506070") # Replace with your Twilio number

print(message.sid)
