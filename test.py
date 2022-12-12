import mysql.connector

mydb = mysql.connector.connect(
    host="52.79.45.187",
    user="hello",
    passwd="mysqlserver",
    database="coffee"
)
mycursor = mydb.cursor()

# 삭제
id_give = 'test'
pw_give = 'test'

sql = "DELETE FROM user WHERE user_id = %s AND user_pw = %s"
mycursor.execute(sql, (id_give, pw_give))
mydb.commit()