import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password ="",
    database="inventory"
)
mycursor=mydb.cursor()
'''mycursor.execute("Create database inventory")'''
mycursor.execute("Create table Invention(number_of_products int(2) PRIMARY KEY AUTO_INCREMENT, name varchar(155), quantity varchar(155), date varchar(10), contact_number varchar(120))")
sql="Insert into Invention(number_of_products,name,quantity,date,contact_number)values(%s,%s,%s,%s,%s)"
val=[
    ('',"Phone","1000pc","12/04/2021","7001624508"),
    ('',"computer","500pc","1/04/2022","9002627002"),
    ('',"laptops","200pc","2/04/2021","7645324516"),
    ('',"charger","300pc","1/04/2023","8754632415")
    ]
mycursor.executemany(sql,val)
mydb.commit()
print("Database inserted successfully")