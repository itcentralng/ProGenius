import os

import africastalking

class SMS:
    def __init__(self):
        # Set your app credentials
        self.username = os.environ.get("SMS_USERNAME")
        self.api_key = os.environ.get("SMS_API_KEY")
        
        # Initialize the SDK
        africastalking.initialize(self.username, self.api_key)
        
        # Get the SMS service
        self.sms = africastalking.SMS
    
    def send(self, recipient, message):
        # Set your shortCode or senderId
        # sender = os.environ.get("SMS_ID")
        try:
            # print(recipient, message, sender)
            # Thats it, hit send and we'll take care of the rest.
            response = self.sms.send(message, [recipient])
            print (response)
        except Exception as e:
            print ('Encountered an error while sending: %s' % str(e))
    
    def send_bulk(self, recipients, message):
        # Set your shortCode or senderId
        sender = os.environ.get("SMS_ID")
        try:
            # Thats it, hit send and we'll take care of the rest.
            response = self.sms.send(message, recipients, sender)
            print (response)
        except Exception as e:
            print ('Encountered an error while sending: %s' % str(e))

def send_ai_message(history):
    recipient = "+2348158962698"
    sms = SMS()
    if len(history) > 2:
        sms.send(recipient, history[-1].content)        