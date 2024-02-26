import mysql.connector

dataBase = mysql.connector.connect(
  host = 'localhost',
  user = 'root',
  passwd = 'Mithun@2003'

)

cursorObject = dataBase.cursor()
cursorObject.execute("Create DataBase elderco")
print('All Done! :)')