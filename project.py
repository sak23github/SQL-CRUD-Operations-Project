import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from tkinter import *

global e1
global e2
global e3
global e4
global listBox


def GetValue(event):
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    row_id = listBox.selection()[0]
    select = listBox.set(row_id)
    e1.insert(0, select['id'])
    e2.insert(0, select['empname'])
    e3.insert(0, select['mobile'])
    e4.insert(0, select['salary'])


def Add():
    id = e1.get()
    empname = e2.get()
    mobile = e3.get()
    salary = e4.get()
    mysqldb = mysql.connector.connect(host="localhost", user="root", password="1234", database="payroll")
    mycursor = mysqldb.cursor()
    try:
        sql = "INSERT INTO registration (id,empname,mobile,salary) VALUES (%s, %s, %s, %s)"
        val = (id, empname, mobile, salary)
        mycursor.execute(sql, val)
        mysqldb.commit()
        lastid = mycursor.lastrowid
        messagebox.showinfo("information", "Employee inserted successfully...")
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e1.focus_set()
    except Exception as e:
        print(e)
        mysqldb.rollback()
        mysqldb.close()

def update():
    id = e1.get()
    empname = e2.get()
    mobile = e3.get()
    salary = e4.get()
    mysqldb = mysql.connector.connect(host="localhost", user="root", password="1234", database="payroll")
    mycursor = mysqldb.cursor()
    try:
        sql = "update `registration` set id=%s, empname=%s,mobile= %s,salary=%s where id= %s"
        val = (id, empname, mobile, salary,id)
        mycursor.execute(sql, val)
        mysqldb.commit()
        lastid = mycursor.lastrowid
        messagebox.showinfo("information", "Record Updateddddd successfully...")
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e1.focus_set()
    except Exception as e:
        print(e)
        mysqldb.rollback()
        mysqldb.close()



def delete():
    id = e1.get()
    mysqldb = mysql.connector.connect(host="localhost", user="root", password="1234", database="payroll")
    mycursor = mysqldb.cursor()
    try:
        sql = "delete from registration where id = %s"
        val = (id,)
        mycursor.execute(sql, val)
        mysqldb.commit()
        lastid = mycursor.lastrowid
        messagebox.showinfo("information", "Record Deleteeeee successfully...")
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e1.focus_set()
    except Exception as e:
        print(e)
        mysqldb.rollback()
        mysqldb.close()


def show():
    for item in listBox.get_children():
        listBox.delete(item)
    mysqldb = mysql.connector.connect(host="localhost", user="root", password="1234", database="payroll")
    mycursor = mysqldb.cursor()
    mycursor.execute("SELECT * FROM registration")
    records = mycursor.fetchall()
    print(records)
    for i, (id, employee_name, mobile, salary) in enumerate(records, start=1):
        listBox.insert("", "end", values=(id, employee_name, mobile, salary))
        mysqldb.close()

root = Tk()
root.geometry("800x500")
cols = ('id', 'empname', 'mobile', 'salary')

listBox = ttk.Treeview(root, columns=cols, show='headings')

for col in cols:
    listBox.heading(col, text=col)
    listBox.grid(row=1, column=0, columnspan=2)
    listBox.place(x=10, y=200)

tk.Label(root, text="Employee Registration", fg="red", font=(None, 30)).place(x=300, y=5)

tk.Label(root, text="Employee ID").place(x=10, y=10)
Label(root, text="Employee Name").place(x=10, y=40)
Label(root, text="Mobile").place(x=10, y=70)
Label(root, text="Salary").place(x=10, y=100)

e1 = Entry(root)
e1.place(x=140, y=10)

e2 = Entry(root)
e2.place(x=140, y=40)

e3 = Entry(root)
e3.place(x=140, y=70)

e4 = Entry(root)
e4.place(x=140, y=100)

Button(root, text="Add", command=Add, height=3, width=13).place(x=30, y=130)
Button(root, text="update", command=update, height=3, width=13).place(x=140, y=130)
Button(root, text="Delete", command=delete, height=3, width=13).place(x=250, y=130)
Button(root, text="Refresh", command=show, height=3, width=13).place(x=360, y=130)

show()

listBox.bind('<Double-Button-1>', GetValue)

root.mainloop()
 