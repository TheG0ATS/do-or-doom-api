import os
from twilio.rest import Client


account_sid = os.environ['TWILIO_ACCOUNT_SID'] 
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

 

client = Client(account_sid, auth_token) 
 
message = client.messages.create(
    messaging_service_sid = os.environ['MESSAGE_SID'],
    body='hello again',
    to='+18045479926'
    ) 
