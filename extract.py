import mysql.connector as c
con = c.connect(host='localhost',
                user='root',
                password='2210@dbisht',
                database='v')

cursor = con.cursor()
query = 'select * from school'
cursor.execute(query)

#data = cursor.fetchone()
data1 = cursor.fetchmany(2)
#data2 = cursor.fetchall()
print(data1)

# one -----> fetch only one data
# many -----> fetch more than or one data
# all ------> fetch all data