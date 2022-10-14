from telnetlib import STATUS
from tkinter import *
import connection
import mysql.connector 


conn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Bhavya@hari22",
  database="login_form"
) 
if(conn):
  print("connection",conn)
 
def getval():

 mycursor = conn.cursor()
# sql = "INSERT INTO registration (username, phone_no , password, email) VALUES ('%s',' %s',' %s','%s')" %(name.get(),contact.get(),pwd.get(),email_val.get())
 sql = mycursor.execute("INSERT INTO registration VALUES ('%s',' %s',' %s','%s')" %(name.get(),contact.get(),pwd.get(),email_val.get()))
 print(sql)
 #mycursor.commit()
 mycursor.close()
 STATUS.set("inserted")
 conn.close()

root1 = Tk()
root1.geometry("500x300")
name= StringVar()
contact= IntVar()
pwd= StringVar()
STATUS=StringVar()
email_val= StringVar()

Label(root1,  text = "Username").place(x = 40,  y = 60)  
Label(root1, text="phone_no").place(x=40, y=90)
Label(root1,  text = "Password").place(x = 40, y = 120)  
Label(root1,  text = "",textvariable=STATUS).place(x = 40, y = 150)  
 
#confirm_pwd = Label(root, text="confirm_password").place(x=40, y=120)

Label(root1, text="email").place(x =40, y=150)
#name = Entry(root, width = 30).place(x = 110, y = 60)

Entry(root1, width = 30, textvariable=name).place(x = 110, y = 60)

Entry(root1, width=30, textvariable=contact).place(x=110,y=90)
Entry(root1, width=30, textvariable=pwd).place(x=110,y=120)
Entry(root1 ,width=30,textvariable=email_val).place(x=110,y=150)

Checkbutton(root1, text="remember me").place(x = 40,y = 180)
Button(root1,width=35, text = "Submit",command=getval).place(x=40, y=210)

mainloop()

