import mysql.connector
mydb =mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="student"
    
)
mycursor= mydb.cursor() 
'''mycursor.execute("create database student")
print("Database created successfully.")'''
'''mycursor.execute("create table students (id int(2) primary key Auto_Increment, name varchar (155), address varchar(155), phone varchar(10), contact_person varchar(120))")
print("Table created successfully.")'''
mycursor= mydb.cursor()
'''sql ="insert into students ( id, name, address, phone, contact_person) values(%s,%s,%s,%s,%s)"
val=('',"Mr.manav jain","uttar pradesh","9001624508","Mr.Adrash jain")
mycursor.execute(sql,val)
mydb.commit()
print("Data inserted successfully")'''
'''mycursor.execute("select * from students")
result=mycursor.fetchall()
for x in result:
    print(x)'''
'''sql= ("select *from students where name ='Mr.manav jain'")
mycursor.execute(sql)
result=mycursor.fetchall()
for x in result:
    print(x)'''
    #update#
'''sql=("update students set name=%s where name=%s")
val =("Miss priyanka thakuri","Mr.manav jain")
mycursor.execute(sql,val)
mydb.commit()
print(mycursor.rowcount,"record(s) affected")'''
#delete#
'''sql=("delete from students where contact_person ='Mr.manav jain'")
mycursor.execute(sql)
mydb.commit()
print("data deleted successfully")'''