# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
import os
from twilio.rest import Client
import csv
import pandas as pd

# Find these values at https://twilio.com/user/account
# To set up environmental variables, see http://twil.io/secure

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']

client = Client(account_sid, auth_token)

raw_invite_google_sheet_invite_list = pd.read_csv('jimo_invite_list.csv',sep=',',header=0)
list_of_people_that_should_be_invited = raw_invite_google_sheet_invite_list[(raw_invite_google_sheet_invite_list['Invite_Flag']=='Y')]
print (list_of_people_that_should_be_invited)
text_dict = {}
for index, row in list_of_people_that_should_be_invited.iterrows():
    print (row[4])
    client.api.account.messages.create(
        to=f"{row[4]}",
        from_="+14243226407",
        body=f"Hello, {row[1]}. You are invited to Access the JIMO beta! Welcome and Enjoy! Click to continue:")
    client.api.account.messages.create(
        to=f"{row[4]}",
        from_="+14243226407",
        body="https://apps.apple.com/us/app/jimo-discover-new-places/id1541360118")
