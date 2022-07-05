import mysql.connector as c
con = c.connect(host='localhost',
                user='root',
                password='2210@dbisht',
                database='v')

cursor = con. cursor()

name = input("Enter the name")
age = int(input("Enter the age"))
# marks = int(input("Enter the marks"))

query = "Update school set name = '{}' where age = {}".format(name,age)
cursor.execute(query)
con.commit()

#task-----> update marks on the basis of age.