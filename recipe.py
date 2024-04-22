import mysql.connector



mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password ="",
    database="recipe"
 
)
mycursor=mydb.cursor()
mycursor.execute("Create database recipe")
mycursor.execute("Create table recipe(number_of_recipes int(2) PRIMARY KEY AUTO_INCREMENT, food_name varchar(155), quantity varchar(155), ingredients varchar(10), cook_name varchar(120))")
sql="Insert into recipe(number_of_recipes,food_name,quantity,ingredients,cook_name)values(%s,%s,%s,%s,%s)"
val=[
    ('',"Chicken Butter Masala","250ml","Chicken","priyanka thakuri"),
    ('',"Paneer Lababdar","500ml","Paneer","priyanka thakuri"),
    ('',"Masala Dosa","100ml","Potatoes","sanjeev kapoor"),
    ('',"Uttapam","150ml","Onions","Vikas khanna"),
    ]
mycursor.executemany(sql,val)
mydb.commit()
print("Database created successfully")
