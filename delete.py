import mysql.connector as c
con = c.connect(host = 'localhost',
                user = 'root',
                password = '2210@dbisht',
                database = 'v')

cursor = con.cursor()

age = int(input("enter the age"))

query = "delete from school where age = '{}'".format(age)
cursor.execute(query)
con.commit()