# from openpyxl.workbook import Workbook
# from openpyxl import load_workbook
#or from openpyxl import *

# wb=Workbook() #workbook instance
# wb=load_workbook('mails.xlsx')

# ws=wb.active

# column_a=ws['A']

# column_b=ws['B']

# for cell in column_a:
#     if(cell.value=="ajayjangir0044@gmail.com"):
#         print("Mail found")
import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Aj@12345",
    database="testdb"
)
mycursor=mydb.cursor()
# mycursor.execute("CREATE DATABASE testdb")
# mycursor.execute("SHOW DATABASES")
# for db in mycursor:
#     print(db)
# mycursor.execute("CREATE TABLE students (email VARCHAR(255),pwd VARCHAR(255))")
# mycursor.execute("SHOW TABLES")
# for tb in mycursor:
#     print(tb)

# mycursor.execute("""insert into students values 
# ("ajayjangir0044@gmail.com","ajay123")""")
# mycursor.execute("""insert into students values 
# ("akankshamaurya0044@gmail.com","akanksha123")""")
# mydb.commit()
# mycursor.execute("SELECT * FROM students")
for x in mycursor:
    print(x)