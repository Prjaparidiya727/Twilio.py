'''
1-Twilio  client setup
2-user inputs 
3-scheduling logic
4-send message
'''
import os

# setp=1 Install require liabraries.
from twilio.rest import Client
from datetime import datetime,timedelta
import time

# step=2 Twilio Credentials
account_sid='A\c sid'
Token_num='T_num'

client=Client(account_sid,Token_num)

# step=3 Degine send message function
def send_wp_msg(recipient_number,message_body):
    try:
        message=client.messages.create(
            from_='Whatsapp:+Put Yours,
            body=message_body,
            to=f'Whatsapp:{recipient_number}'
        )
        print(f'message sent successfully! Message SID{message.sid}')
    except Exception as e:
        print('An error occurred')
        
# Step=4 User Input
name=input('enter the recipient name=')
recipient_number=input('enter the recipient Whatsapp number with country code(e.g= +91)=')
message_body=input(f'enter the message u want to{name}=')

# step=5 parse date/time and calculate delay
date_str="2025-03-27"
time_str="16:55"


# Datetime 
schedule_datetime=datetime.strptime(f'{date_str} {time_str}','%Y-%m-%d %H:%M')
current_datetime=datetime.now()
print("scheduled date and time=",schedule_datetime)

# calculate delay
time_differ=schedule_datetime-current_datetime
delay_seconds=time_differ.total_seconds()

if delay_seconds<=0:
    print('The specified time is in the past. please enter a future date and time')
else:
    print(f'Message schedule to be sent to {name} at {schedule_datetime}')
    
    # wait untill the schedule time
    time.sleep(delay_seconds)#1000
    
    # send the message
    send_wp_msg(recipient_number,message_body)
    

