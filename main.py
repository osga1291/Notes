from datetime import datetime,timedelta
from messenger import User
from dbStart import db


def main(event = None , context = None):
    
    newDb = db()
    user = User("Oscar", "+18458672629",newDb)
    user.sendNextMessage("+17203981130")


    
    



if __name__ == "__main__":
    main()