import mysql.connector
mydb =mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="library"    
)
mycursor= mydb.cursor() 
'''mycursor.execute("create database library")
print("Database created successfully.")'''
'''mycursor.execute("create table library (book_name int(2) primary key Auto_Increment, author varchar (155), genre varchar(155),series_no varchar(10),book_no varchar(120))")
print("Table created successfully.")'''
mycursor= mydb.cursor()
'''sql ="insert into library ( book_name, author,genre,series_no, book_no) values(%s,%s,%s,%s,%s)"
val=('data structure',"Anuradha A. Puntambekar","computer science","34","00")
mycursor.execute(sql,val)
mydb.commit()
print("Data inserted successfully")'''
'''mycursor.execute("select * from library")
result=mycursor.fetchall()
for x in result:
    print(x)'''
'''sql= ("select *from library where author ='Anuradha A. Puntambekar'")
mycursor.execute(sql)
result=mycursor.fetchall()
for x in result:
    print(x)'''
    #update#
'''sql=("update library set author=%s where author=%s")
val =("Narashima Karumanchi","Anuradha A. Puntambekar")
mycursor.execute(sql,val)
mydb.commit()
print(mycursor.rowcount,"record(s) affected")'''
#delete#
'''sql=("delete from library where author ='Anuradha A. Puntambekar'")
mycursor.execute(sql)
mydb.commit()
print("data deleted successfully")'''