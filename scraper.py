
from bs4 import BeautifulSoup
import requests
import re
from dbStart import db


def getBible(topic):

    array = []
    strings_array = []
    #mycursor = db()


    page = requests.get("https://www.openbible.info/topics/"+ topic)
    soup = BeautifulSoup(page.content,'html.parser')

    for tags in soup.findAll('div', class_ = 'verse'):
            for tag in (tags.findAll('a', class_ = 'bibleref')):
                array.append(tag.getText())
                
    i = 0

    for tag in soup.findAll('div' , class_ = 'verse'):
            for para in tag.findAll('p'):
                string = re.sub(r"^\s+|\s+$", "", para.getText()) + " - " + str(array[i])
                i += 1
                strings_array.append(string)


    #sql = "INSERT INTO quotes (author,body, mood_id) VALUES (%s, %s, %s)"
    
    #for entry in strings_array:
        #val = ("Bible", entry , 1)
        #mycursor.execute(sql,val)
        #mycursor.commit()
