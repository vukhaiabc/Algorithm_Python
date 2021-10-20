import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="12345",
  database="demsql",
)

def get_popularity(n):
  query = "Select * from demsql.languagetable ORDER BY popularity DESC"
  mycursor = mydb.cursor()
  mycursor.execute(query)
  myresult = mycursor.fetchall()
  return myresult[n-1]


rs = get_popularity(3)
print(rs)
