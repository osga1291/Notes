from twilio.rest import Client 
from config import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN
from dbStart import db


class User:

    def __init__(self,name,number,data):
        self.client = Client(TWILIO_ACCOUNT_SID,TWILIO_AUTH_TOKEN)
        self.name = name
        self.number = number
        self.data = data


    def sendNextMessage(self, to):
        n_message = self.data.getNextEntry()

        if n_message[2] is None:
            message = self.client.messages.create(
            from_=self.number,
            body = n_message[1],
            to = to
        )

            
            
        else:
            quote = self.data.getQuoteById(n_message[2])
            message = self.client.messages.create(
            from_=self.number,
            body = quote[2] + "-" + quote[1] + "/n" + n_message[1],
            to = to
        )
        print(message.sid)
        self.data.deleteEntry(n_message[0])

        return


        






