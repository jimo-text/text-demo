# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
import os
from twilio.rest import Client

# Find these values at https://twilio.com/user/account
# To set up environmental variables, see http://twil.io/secure
# account_sid = os.environ['ACf1b07075c000a6eaf37629fce4a7ba8f']
# auth_token = os.environ['b915e58f46b9d2dbbc641b583c9c11cb']

account_sid = 'ACf1b07075c000a6eaf37629fce4a7ba8f'

auth_token = 'b915e58f46b9d2dbbc641b583c9c11cb'

client = Client(account_sid, auth_token)

# client.api.account.messages.create(
#     to="+18453377216",
#     from_="+14243226407",
#     body="Hello there!")


message = client.api.account.messages.create(
    to="+18453377216",
    from_="+14243226407",
    body="Hello there!",
    media_url=['https://demo.twilio.com/owl.png',
               'https://demo.twilio.com/logo.png'])



# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond and greet the caller by name."""
    # Try adding your own number to this list!
    callers = {
        "+14158675308": "Curious George",
        "+12349013030": "Boots",
        "+12348134522": "Virgil",
    }
    from_number = request.values.get('From', None)
    message = callers[from_number] if from_number in callers else "Monkey"

    resp = MessagingResponse()
    resp.message("{}, thanks for the message!".format(message))

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
