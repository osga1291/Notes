import mysql.connector
import config
class db:
    
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host = config.location,
            user= config.user,
            password = config.password,
            database = config.database)

    def insertOneQuote(self,author, body, mood):
        mycursor = self.mydb.cursor()
        sql = "INSERT INTO quotes (author,body, mood_id) VALUES (%s, %s, %s)"
        val = (author, body, mood)
        mycursor.execute(sql, val)
        self.mydb.commit()



    def insertManyQuotes(self,insert_list,author_list, mood):
        mycursor = self.mydb.cursor()
        get_mood = "Select id from mood where name = %s"
        string1 = (mood, )
        mycursor.execute(get_mood,string1)
        mood_id = mycursor.fetchone()
        sql = "INSERT INTO quotes (author,body, mood_id) VALUES (%s, %s, %s)"
        i = 0
        if isinstance(author_list, str):
            for entry in insert_list:
                val = (author_list, entry, mood_id[0])
                mycursor.execute(sql, val)
                self.mydb.commit()
        else:
            for entry in insert_list:
                val = (author_list[i], entry, mood_id[0])
                mycursor.execute(sql, val)
                self.mydb.commit()
                i += 1
        print("Done.")
        return

    def getQuoteById(self, m_id):
        mycursor = self.mydb.cursor()
        sql = "SELECT * from quotes where id = %s"
        string = (m_id, )
        mycursor.execute(sql,string)
        results = mycursor.fetchone()
        return results

    def getQuotesByAuthor(self, author):
        mycursor = self.mydb.cursor()
        sql = "SELECT body from quotes where author = %s"
        string = (author, )
        mycursor.execute(sql,string)
        results = mycursor.fetchall()
        return results

    def getQuoteByMood(self, mood):
        mycursor = self.mydb.cursor()
        mood_sql = "Select id from mood where name = %s"
        string1 = (mood, )
        mycursor.execute(mood_sql, string1)
        
        sql = "SELECT body from quotes where mood_id = %s"

        mycursor.execute(sql,mycursor.fetchone())
        return mycursor.fetchall()

    def getQuoteByMoodAndAuthor(self, mood,author):
        mycursor = self.mydb.cursor()
        mood_sql = "select id from mood where name = %s"
        string1= (mood,)
        mycursor.execute(mood_sql, string1)
        mood_id = mycursor.fetchone()
        author_mood = "select body from quotes where mood_id = %s and author = %s"
        string2 = (mood_id[0], author)
        mycursor.execute(author_mood,string2)
        return mycursor.fetchall()


    def insertMessageQuote(self, body, quote):
        mycursor = self.mydb.cursor()
        quote_sql = "select id , mood_id from quotes where body = %s"
        string1 = (quote, )
        mycursor.execute(quote_sql, string1)
        result = mycursor.fetchone()
        if(result is None):
            print("Quote not Found. Insert quote first")
            return 
        sql = "INSERT INTO messages (body,quote_id, mood_id) VALUES (%s, %s, %s)"
        string2 = (body, result[0],result[1])
        mycursor.execute(sql,string2)
        self.mydb.commit()

    def insertMessage(self, body):
        mycursor = self.mydb.cursor()
        sql = "Insert into messages (body) values (%s)"
        string1 = (body, )
        mycursor.execute(sql, string1)
        self.mydb.commit()
        
    
    def getNextEntry(self):
        mycursor = self.mydb.cursor()
        sql = "select * from messages limit 1"
        mycursor.execute(sql)
        result = mycursor.fetchone()
        if(result == None):
            print("DB is empty")
            return
        return result

    def deleteEntry(self, entry_id):
        mycursor = self.mydb.cursor()
        sql = "delete * from messages where id = %s"
        string1 = (entry_id, )
        mycursor.execute(sql,string1)
        self.mydb.commit()

    
    





    





        

        
