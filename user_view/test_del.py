import mysql.connector


cnx2 = mysql.connector.connect(user='root',
                              password='Password@123',
                              host='localhost',
                              database='table_test',)



print("Connected to:", cnx2.get_server_info())

mycursor = cnx2.cursor()
mycursor.execute("SELECT * FROM user_view_news")
cnx2.commit()
cnx2.close()

