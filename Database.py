import mysql.connector as c
con = c.connect(host= 'localhost',
                user = 'root',
                password = '2210@dbisht',
                database = 'v' )

cursor = con. cursor()

#if con. is_connected():
#    print('Connected successfully')

name = input("enter the name")
age = input("enter the age")
marks = input("enter the marks")

query = "Insert into school values( '{}',{},{})".format(name,age,marks)
cursor.execute(query)
con. commit()
print("Data enter successfully")