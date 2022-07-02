import mysql.connector as c
con = c.connect(host='localhost',
                user='root',
                password='2210@dbisht',
                database='project')
cursor = con.cursor()

#if con.is_connected():
#    print("Connected successfully")

print("Bank Management System")

print("choose any one option to banking with us!!")

while True:

     choice = input("1. Open Account\n2.Cash Deposit\n3.Cash Withdrawl\n4.Account Details\n5.Exit")

     if choice == '1':
         name=input("Enter your name")
         age=int(input("Enter the age"))
         mobile=int(input("Enter your number"))

         query = "insert into customer value ('{}',{},{})".format(name,age,mobile)
         cursor.execute(query)
         con.commit()
         print("Account Open")


       # CASH DEPOSIT
     elif choice == '2':
         name=input("Enter your name")
         amount=int(input("Enter the amount")
         # acc=int(input("Enter your acc no."))

         query = "Update customer set amount = {} where name = '{}'".format(amount,name)
         cursor.execute(query)
         con.commit()
         print("Cash Deposit")

      # CASH WITHDRAWL
     elif choice == '3':
         name=input("Enter your name")
         acc=int(input("Enter your acc no."))
         amount=int(input("Enter the amount"))

         query = "Update customer set amount = {} where name = '{}'".format(amount,name)
         cursor.execute(query)
         con.commit()
         print("Cash Withdrawl")

     # ACCOUNT DETAILS
     elif choice == '4':
         query = "select * from customer"
         cursor.execute(query)
         acc.detail = cursor.fetchall()
         print(acc.detail)
         con.commit()

     # EXIT USE BREAK
     elif choice == '5':
         break

     else:
         print("Invalid command")

# Modify

# 1. Make a relation between withdrawl & deposit
# 2. Make one more choice