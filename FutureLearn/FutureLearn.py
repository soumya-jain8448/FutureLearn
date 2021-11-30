import tkinter
import webbrowser
import jwt
import requests
import json
from time import time
import pymysql
import os
import math
import calendar
# import socket
# import threading
from tkinter import *
from tkinter.filedialog import *
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
import subprocess
from tkinter import messagebox

root1 = Tk()
root1.title("LOGIN AS")
root1.geometry("300x200")
root1.config(bg="#dec8ab")
root1.eval('tk::PlaceWindow . center')
l = Label(text="LOGIN FORM", bg="#dec8ab", font="Verdana 10 underline")
l.pack()

def admin():
    root = Toplevel()
    root.title("ADMIN PANEL")
    root.config(bg="#dec8ab")
    root.geometry("300x250")
    def fac():
        master = Toplevel()
        master.title("Faculty Management")
        master.geometry("300x250")
        master.config(bg="#dec8ab")
        l = Label(master, text="FACULTY MANAGEMENT", bg="#dec8ab", font="Verdana 8 underline")
        l1 = Label(master, text="Faculty_id", bg="#dec8ab", font="Verdana 8")
        l2 = Label(master, text="Faculty_name", bg="#dec8ab", font="Verdana 8")
        l3 = Label(master, text="Contact_no", bg="#dec8ab", font="Verdana 8")
        l4 = Label(master, text="Email_ID", bg="#dec8ab", font="Verdana 8")
        l5 = Label(master, text="Department", bg="#dec8ab", font="Verdana 8")
        l6 = Label(master, text="Gender", bg="#dec8ab", font="Verdana 8")
        l.grid(row=0, column=1)
        l1.grid(row=1, column=0)
        l2.grid(row=2, column=0)
        l3.grid(row=3, column=0)
        l4.grid(row=4, column=0)
        l5.grid(row=5, column=0)
        l6.grid(row=6, column=0)
        t1 = Entry(master)
        t2 = Entry(master)
        t3 = Entry(master)
        t4 = Entry(master)
        t1.grid(row=1, column=1)
        t2.grid(row=2, column=1)
        t3.grid(row=3, column=1)
        t4.grid(row=4, column=1)
        x = StringVar()
        v1 = ['CSE', 'IT', 'EEE', 'AUTOMOBILE', 'ETC', 'AGRI', 'MINING']
        c1 = OptionMenu(master, x, *v1)
        c1.grid(row=5, column=1)
        y = StringVar()
        v2 = ['Male', 'Female', 'Other']
        c2 = OptionMenu(master, y, *v2)
        c2.grid(row=6, column=1)

        def a():
            a = t1.get()
            b = t2.get()
            c = t3.get()
            d = t4.get()
            e = x.get()
            f = y.get()
            db = pymysql.connect(host='localhost', user='root', password='stuart@2002', db='hackathon')
            if a == "" or b == "" or c == "" or d == "" or a.isdigit() is False or c.isdigit() is False:
                messagebox.showwarning("Alert!", "Invalid Input, Please try again!")
            else:
                db = pymysql.connect(host='localhost', user='root', password='stuart@2002', db='hackathon')
                sql = "insert into faculty values(%s,%s,%s,%s,%s,%s)"
                val = (a, b, c, d, e, f)
                cur = db.cursor()
                cur.execute(sql, val)
                db.commit()
                messagebox.showinfo("Success", "Values added successfully.")

        def u():
            master = Toplevel()
            master.title("Update details")
            master.geometry("300x250")
            master.config(bg="#dec8ab")
            l = Label(master, text="UPDATE DETAILS", bg="#dec8ab", font="Verdana 8 underline")
            l.grid(row=0, column=1)
            l1 = Label(master, text="Faculty_id", bg="#dec8ab", font="Verdana 8")
            l1.grid(row=1, column=0)
            l2 = Label(master, text="Name", bg="#dec8ab", font="Verdana 8 ")
            l2.grid(row=2, column=0)
            l3 = Label(master, text="Contact", bg="#dec8ab", font="Verdana 8")
            l3.grid(row=3, column=0)
            l4 = Label(master, text="Email_ID", bg="#dec8ab", font="Verdana 8")
            l4.grid(row=4, column=0)
            l5 = Label(master, text="Department", bg="#dec8ab", font="Verdana 8")
            l5.grid(row=5, column=0)
            t1 = Entry(master)
            t2 = Entry(master)
            t3 = Entry(master)
            t4 = Entry(master)
            t5 = Entry(master)
            t1.grid(row=1, column=1)
            t2.grid(row=2, column=1)
            t3.grid(row=3, column=1)
            t4.grid(row=4, column=1)
            t5.grid(row=5, column=1)

            def u2():
                db = pymysql.connect(host='localhost', user='root', password='stuart@2002', db='hackathon')
                a = t1.get()
                b = t2.get()
                c = t3.get()
                d = t4.get()
                e = t5.get()
                sql = "update faculty set faculty_name = %s , contact_no = %s , email_id = %s , deptt = %s where faculty_id = %s"
                val = (b, c, d, e, a)
                cur = db.cursor()
                cur.execute(sql, val)
                db.commit()
                messagebox.showinfo("", "Updated Successfully!")

            b1 = Button(master, text="update", bg="yellow", fg="black", command=u2)
            b1.grid(row=6, column=1)

        def de():
            master = Toplevel()
            master.title("Delete details")
            master.geometry("300x250")
            master.config(bg="#dec8ab")
            l = Label(master, text="DELETE DETAILS", bg="#dec8ab", font="Verdana 8 underline")
            l.grid(row=0, column=1)
            l1 = Label(master, text="Enter faculty_id", bg="#dec8ab")
            l1.grid(row=1, column=0)
            t1 = Entry(master)
            t1.grid(row=1, column=1)

            def d1():
                a = t1.get()
                db = pymysql.connect(host='localhost', user='root', password='stuart@2002', db='hackathon')
                sql = "delete from faculty where faculty_id = %s"
                val = (a)
                cur = db.cursor()
                cur.execute(sql, val)
                db.commit()
                messagebox.showinfo(" ", "Deleted Successfully!")

            b1 = Button(master, text="delete", bg="red",fg='white',command=d1)
            b1.grid(row=2, column=1)

        b1 = Button(master, text="add", bg="green", fg="white", command=a)
        b2 = Button(master, text="update", bg="yellow", fg="black", command=u)
        b3 = Button(master, text="delete", bg="red", fg="white", command=de)
        b1.grid(row=8, column=0)
        b2.grid(row=8, column=1)
        b3.grid(row=8, column=2)

    def stu():
        master = Toplevel()
        master.title("Student Management")
        master.geometry("300x250")
        master.config(bg="#dec8ab")
        l = Label(master, text="STUDENT MANAGEMENT", bg="#dec8ab", font="Verdana 8 underline")
        l1 = Label(master, text="University_rno", bg="#dec8ab", font="Verdana 8")
        l2 = Label(master, text="Student_name", bg="#dec8ab", font="Verdana 8")
        l3 = Label(master, text="Contact_no", bg="#dec8ab", font="Verdana 8")
        l4 = Label(master, text="Email_ID", bg="#dec8ab", font="Verdana 8")
        l5 = Label(master, text="Branch", bg="#dec8ab", font="Verdana 8")
        l6 = Label(master, text="Semester", bg="#dec8ab", font="Verdana 8")
        l.grid(row=0, column=1)
        l1.grid(row=1, column=0)
        l2.grid(row=2, column=0)
        l3.grid(row=3, column=0)
        l4.grid(row=4, column=0)
        l5.grid(row=5, column=0)
        l6.grid(row=6, column=0)
        t1 = Entry(master)
        t2 = Entry(master)
        t3 = Entry(master)
        t4 = Entry(master)
        t1.grid(row=1, column=1)
        t2.grid(row=2, column=1)
        t3.grid(row=3, column=1)
        t4.grid(row=4, column=1)
        x = StringVar()
        v1 = ['CSE', 'IT', 'EEE', 'AUTOMOBILE', 'ETC', 'AGRI', 'MINING']
        c1 = OptionMenu(master, x, *v1)
        c1.grid(row=5, column=1)
        y = IntVar()
        v2 = []
        for i in range (1,9):
            v2.append(i)
        c2 = OptionMenu(master, y, *v2)
        c2.grid(row=6, column=1)

        def ad():
            a = t1.get()
            b = t2.get()
            c = t3.get()
            d = t4.get()
            e = x.get()
            f = y.get()
            if a == "" or b == "" or c == "" or d == "" or a.isdigit() is False or c.isdigit() is False:
                messagebox.showwarning("Alert!", "Invalid Input, Please try again!")
            else:
                db = pymysql.connect(host='localhost', user='root', password='stuart@2002', db='hackathon')
                sql = "insert into student values(%s,%s,%s,%s,%s,%s)"
                val = (a, b, c, d, e, f)
                cur = db.cursor()
                cur.execute(sql, val)
                db.commit()
                messagebox.showinfo(" ", "Values added successfully.")
        def up():
            master = Toplevel()
            master.title("Update details")
            master.geometry("300x250")
            master.config(bg="#dec8ab")
            l = Label(master, text="UPDATE DETAILS", bg="#dec8ab", font="Verdana 8 underline")
            l.grid(row=0, column=1)
            l1 = Label(master, text="University_rno", bg="#dec8ab", font="Verdana 8")
            l1.grid(row=1, column=0)
            l2 = Label(master, text="Name", bg="#dec8ab", font="Verdana 8 ")
            l2.grid(row=2, column=0)
            l3 = Label(master, text="Contact", bg="#dec8ab", font="Verdana 8")
            l3.grid(row=3, column=0)
            l4 = Label(master, text="Email_ID", bg="#dec8ab", font="Verdana 8")
            l4.grid(row=4, column=0)
            l5 = Label(master, text="Branch", bg="#dec8ab", font="Verdana 8")
            l5.grid(row=5, column=0)
            l6 = Label(master, text="Semester", bg="#dec8ab", font="Verdana 8")
            l6.grid(row=6, column=0)
            t1 = Entry(master)
            t2 = Entry(master)
            t3 = Entry(master)
            t4 = Entry(master)
            t5 = Entry(master)
            t6 = Entry(master)
            t1.grid(row=1, column=1)
            t2.grid(row=2, column=1)
            t3.grid(row=3, column=1)
            t4.grid(row=4, column=1)
            t5.grid(row=5, column=1)
            t6.grid(row=6, column=1)

            def u3():
                db = pymysql.connect(host='localhost', user='root', password='stuart@2002', db='hackathon')
                a = t1.get()
                b = t2.get()
                c = t3.get()
                d = t4.get()
                e = t5.get()
                f = t6.get()
                sql = "update faculty set student_name = %s , contact = %s , email_id = %s , branch = %s , semester = %s where university_rno = %s"
                val = (a, b, c, d, e, f)
                cur = db.cursor()
                cur.execute(sql, val)
                db.commit()
                messagebox.showinfo("", "Updated Successfully!")

            b1 = Button(master, text="update", bg="yellow", fg="black", command=u3)
            b1.grid(row=7, column=1)

        def de1():
            master = Toplevel()
            master.title("Delete details")
            master.geometry("300x250")
            master.config(bg="#dec8ab")
            l = Label(master, text="DELETE DETAILS", bg="#dec8ab", font="Verdana 8 underline")
            l.grid(row=0, column=1)
            l1 = Label(master, text="Enter University_rno", bg="#dec8ab")
            l1.grid(row=1, column=0)
            t1 = Entry(master)
            t1.grid(row=1, column=1)

            def d2():
                a = t1.get()
                db = pymysql.connect(host='localhost', user='root', password='stuart@2002', db='hackathon')
                sql = "delete from student where university_rno = %s"
                val = (a)
                cur = db.cursor()
                cur.execute(sql, val)
                db.commit()
                messagebox.showinfo(" ", "Deleted Successfully!")

            b1 = Button(master, text="delete", bg="red",fg='white',command=d2)
            b1.grid(row=2, column=1)

        b1 = Button(master, text="add", bg="green", fg="white",command=ad)
        b2 = Button(master, text="update", bg="yellow", fg="black",command=up)
        b3 = Button(master, text="delete", bg="red", fg="white",command=de1)
        b1.grid(row=8, column=0)
        b2.grid(row=8, column=1)
        b3.grid(row=8, column=2)
    def sub():
        def a2():
            db = pymysql.connect(host='localhost', user='root', password='stuart@2002', db='hackathon')
            br = t1.get()
            sem = t2.get()
            sub = t3.get()
            if br == " " or sem == " " or sub == " " :
                messagebox.showwarning(" ","Enter valid values")
            else:
                sql = "insert into subject values(%s,%s,%s)"
                val = (sub, sem, br)
                cur = db.cursor()
                cur.execute(sql, val)
                db.commit()
                messagebox.showinfo("","added successfully!")
        def delet():
            db = pymysql.connect(host='localhost', user='root', password='stuart@2002', db='hackathon')
            rn1 = t3.get()

            sql = "delete from Subject where sub_name=%s"
            val = (rn1)
            cur = db.cursor()
            cur.execute(sql, val)
            db.commit()
            messagebox.showinfo("","successfully deleted")

        d = Toplevel()
        d.config(bg="#dec8ab")
        d.title("SUBJECT")
        d.geometry("300x200")
        l1 = Label(d, text="Branch", bg="#dec8ab", font="Verdana 10")
        l2 = Label(d, text="Semester", bg="#dec8ab", font="Verdana 10")
        l3 = Label(d, text="Subject", bg="#dec8ab", font="Verdana 10")
        t1 = Entry(d)
        t2 = Entry(d)
        t3 = Entry(d)
        l1.grid(row=1, column=0)
        l2.grid(row=2, column=0)
        l3.grid(row=3, column=0)
        t1.grid(row=1, column=1)
        t2.grid(row=2, column=1)
        t3.grid(row=3, column=1)
        b1 = Button(d, text="add", bg="green", fg="white", command=a2)
        b2 = Button(d, text="delete", bg="red", fg="white", command=delet)
        b1.grid(row=4, column=0)
        b2.grid(row=4, column=1)

    def lout():
        val = messagebox.askyesno("Are you sure?", "Are you sure you want to logout?")
        if val == True:
            root.destroy()
        else:
            return

    b1 = Button(root, text="Faculty Management", padx=3, bg="#2e0000", fg="white", font="Verdana 8", command=fac)
    b2 = Button(root, text="Student Management", bg="#2e0000", fg="white", font="Verdana 8",command=stu)
    b3 = Button(root, text="Subjects", padx=37, bg="#2e0000", fg="white", font="Verdana 8",command=sub)
    b4 = Button(root, text="Logout", padx=43, bg="#2e0000", fg="white", font="Verdana 8",command=lout)
    b1.pack()
    b2.pack()
    b3.pack()
    b4.pack()

def faculty():
    master = Toplevel()
    master.title("Faculty panel")
    master.geometry("300x200")
    master.config(bg="#dec8ab")
    l1 = Label(master, text="FACULTY LOGIN", bg="#dec8ab", font="Verdana 12 underline")
    l1.pack()

    def flogin():
        master = Toplevel()
        master.title("FACULTY")
        master.geometry("300x200")
        master.config(bg="#dec8ab")

        def activity():
            master = Toplevel()
            master.title("Create Account")
            master.geometry("300x200")
            master.config(bg="#dec8ab")
            l = Label(master, text="ACTIVITY", bg="#dec8ab", font="Verdana 10 underline")
            l.pack()

            def lab():
                master = Toplevel()
                master.geometry("300x200")
                master.title("VIRTUAL LAB")
                master.config(bg="#dec8ab")
                l = Label(master, text="Vitrual Lab", bg="#dec8ab", font="Verdana 10 underline")
                l.pack()

                def calc():

                    root2 = Toplevel()
                    root2.title("Scientific Calculator")
                    root2.configure(background='black')
                    root2.resizable(width=True, height=True)
                    root2.geometry("645x345")
                    calc = Frame(root2)
                    calc.config(bg="black")
                    calc.grid()

                    class Calc():
                        def __init__(self):
                            self.total = 0
                            self.current = ''
                            self.input_value = True
                            self.check_sum = False
                            self.op = ''
                            self.result = False

                        def numberEnter(self, num):
                            self.result = False
                            firstnum = txtDisplay.get()
                            secondnum = str(num)
                            if self.input_value:
                                self.current = secondnum
                                self.input_value = False
                            else:
                                if secondnum == '.':
                                    if secondnum in firstnum:
                                        return
                                self.current = firstnum + secondnum
                            self.display(self.current)

                        def sum_of_total(self):
                            self.result = True
                            self.current = float(self.current)
                            if self.check_sum == True:
                                self.valid_function()
                            else:
                                self.total = float(txtDisplay.get())

                        def display(self, value):
                            txtDisplay.delete(0, END)
                            txtDisplay.insert(0, value)

                        def valid_function(self):
                            if self.op == "add":
                                self.total += self.current
                            if self.op == "sub":
                                self.total -= self.current
                            if self.op == "multi":
                                self.total *= self.current
                            if self.op == "divide":
                                self.total /= self.current
                            if self.op == "mod":
                                self.total %= self.current
                            self.input_value = True
                            self.check_sum = False
                            self.display(self.total)

                        def operation(self, op):
                            self.current = float(self.current)
                            if self.check_sum:
                                self.valid_function()
                            elif not self.result:
                                self.total = self.current
                                self.input_value = True
                            self.check_sum = True
                            self.op = op
                            self.result = False

                        def Clear_Entry(self):
                            self.result = False
                            self.current = "0"
                            self.display(0)
                            self.input_value = True

                        def All_Clear_Entry(self):
                            self.Clear_Entry()
                            self.total = 0

                        def pi(self):
                            self.result = False
                            self.current = math.pi
                            self.display(self.current)

                        def tau(self):
                            self.result = False
                            self.current = math.tau
                            self.display(self.current)

                        def e(self):
                            self.result = False
                            self.current = math.e
                            self.display(self.current)

                        def mathPM(self):
                            self.result = False
                            self.current = -(float(txtDisplay.get()))
                            self.display(self.current)

                        def squared(self):
                            self.result = False
                            self.current = math.sqrt(float(txtDisplay.get()))
                            self.display(self.current)

                        def cos(self):
                            self.result = False
                            self.current = math.cos(math.radians(float(txtDisplay.get())))
                            self.display(self.current)

                        def cosh(self):
                            self.result = False
                            self.current = math.cosh(math.radians(float(txtDisplay.get())))
                            self.display(self.current)

                        def tan(self):
                            self.result = False
                            self.current = math.tan(math.radians(float(txtDisplay.get())))
                            self.display(self.current)

                        def tanh(self):
                            self.result = False
                            self.current = math.tanh(math.radians(float(txtDisplay.get())))
                            self.display(self.current)

                        def sin(self):
                            self.result = False
                            self.current = math.sin(math.radians(float(txtDisplay.get())))
                            self.display(self.current)

                        def sinh(self):
                            self.result = False
                            self.current = math.sinh(math.radians(float(txtDisplay.get())))
                            self.display(self.current)

                        def log(self):
                            self.result = False
                            self.current = math.log(float(txtDisplay.get()))
                            self.display(self.current)

                        def exp(self):
                            self.result = False
                            self.current = math.exp(float(txtDisplay.get()))
                            self.display(self.current)

                        def acosh(self):
                            self.result = False
                            self.current = math.acosh(float(txtDisplay.get()))
                            self.display(self.current)

                        def asinh(self):
                            self.result = False
                            self.current = math.asinh(float(txtDisplay.get()))
                            self.display(self.current)

                        def expm1(self):
                            self.result = False
                            self.current = math.expm1(float(txtDisplay.get()))
                            self.display(self.current)

                        def lgamma(self):
                            self.result = False
                            self.current = math.lgamma(float(txtDisplay.get()))
                            self.display(self.current)

                        def degrees(self):
                            self.result = False
                            self.current = math.degrees(float(txtDisplay.get()))
                            self.display(self.current)

                        def log2(self):
                            self.result = False
                            self.current = math.log2(float(txtDisplay.get()))
                            self.display(self.current)

                        def log10(self):
                            self.result = False
                            self.current = math.log10(float(txtDisplay.get()))
                            self.display(self.current)

                        def log1p(self):
                            self.result = False
                            self.current = math.log1p(float(txtDisplay.get()))
                            self.display(self.current)

                    added_value = Calc()

                    txtDisplay = Entry(calc, font=('Verdana', 20, 'bold'),
                                       bg='white', fg='black', bd=3,
                                       width=15, justify=RIGHT)
                    txtDisplay.grid(row=0, column=0, columnspan=4)
                    txtDisplay.insert(0, "0")

                    numberpad = "789456123"
                    i = 0
                    btn = []
                    for j in range(2, 5):
                        for k in range(3):
                            btn.append(Button(calc, width=6, height=2,
                                              bg='black', fg='white',
                                              font=('Verdana', 12, 'bold'),
                                              text=numberpad[i]))
                            btn[i].grid(row=j, column=k, pady=1)
                            btn[i]["command"] = lambda x=numberpad[i]: added_value.numberEnter(x)
                            i += 1

                    btnClear = Button(calc, text=chr(67), width=3,
                                      height=1, bg='powder blue',
                                      font=('Verdana', 20, 'bold'), padx=5
                                      , command=added_value.Clear_Entry
                                      ).grid(row=1, column=0)

                    btnAllClear = Button(calc, text=chr(67) + chr(69),
                                         width=3, height=1,
                                         bg='powder blue',
                                         font=('Verdana', 20, 'bold'), padx=5,
                                         command=added_value.All_Clear_Entry
                                         ).grid(row=1, column=1)

                    btnsq = Button(calc, text="\u221A", width=3, height=1,
                                   bg='powder blue', font=('Verdana',
                                                           20, 'bold'), padx=5,
                                   command=added_value.squared
                                   ).grid(row=1, column=2)

                    btnAdd = Button(calc, text="+", width=3, height=1,
                                    bg='powder blue',
                                    font=('Veradana', 19, 'bold'), padx=6, pady=2,
                                    command=lambda: added_value.operation("add")
                                    ).grid(row=1, column=3)

                    btnSub = Button(calc, text="-", width=4,
                                    height=1, bg='powder blue',
                                    font=('Veradana', 0, 'bold'), padx=4, pady=5,
                                    command=lambda: added_value.operation("sub")
                                    ).grid(row=2, column=3)

                    btnMul = Button(calc, text="x", width=3,
                                    height=1, bg='powder blue',
                                    font=('Verdana', 16, 'bold'), padx=6, pady=4,
                                    command=lambda: added_value.operation("multi")
                                    ).grid(row=3, column=3)

                    btnDiv = Button(calc, text="/", width=3,
                                    height=1, bg='powder blue',
                                    font=('Verdana', 16, 'bold'), padx=6, pady=4,
                                    command=lambda: added_value.operation("divide")
                                    ).grid(row=4, column=3)

                    btnZero = Button(calc, text="0", width=6,
                                     height=3, bg='black', fg='white',
                                     font=('Verdana', 12, 'bold'),
                                     command=lambda: added_value.numberEnter(0)
                                     ).grid(row=5, column=0)

                    btnDot = Button(calc, text=".", width=3,
                                    height=1, bg='powder blue',
                                    font=('Verdana', 16, 'bold'), pady=13, padx=10,
                                    command=lambda: added_value.numberEnter(".")
                                    ).grid(row=5, column=1)

                    btnPM = Button(calc, text=chr(177), width=3,
                                   height=1, bg='powder blue', pady=13, padx=10, font=('Verdana', 16, 'bold'),
                                   command=added_value.mathPM
                                   ).grid(row=5, column=2)

                    btnEquals = Button(calc, text="=", width=3,
                                       height=1, bg='powder blue',
                                       font=('Verdana', 16, 'bold'), pady=13, padx=8,
                                       command=added_value.sum_of_total
                                       ).grid(row=5, column=3)
                    # ROW 1 :
                    btnPi = Button(calc, text="pi", width=3,
                                   height=1, bg='black', fg='white',
                                   font=('Verdana', 16), padx=10, pady=4,
                                   command=added_value.pi
                                   ).grid(row=1, column=4)

                    btnCos = Button(calc, text="cos", width=3,
                                    height=1, bg='black', fg='white',
                                    font=('Verdana', 16), padx=10, pady=4,
                                    command=added_value.cos
                                    ).grid(row=1, column=5)

                    btntan = Button(calc, text="tan", width=3,
                                    height=1, bg='black', fg='white',
                                    font=('Verdana', 16), padx=10, pady=4,
                                    command=added_value.tan
                                    ).grid(row=1, column=6)

                    btnsin = Button(calc, text="sin", width=3,
                                    height=1, bg='black', fg='white',
                                    font=('Verdana', 16), padx=10, pady=4,
                                    command=added_value.sin
                                    ).grid(row=1, column=7)

                    # ROW 2 :
                    btn2Pi = Button(calc, text="2pi", width=3,
                                    height=1, bg='black', fg='white',
                                    font=('Verdana', 16), padx=10, pady=4,
                                    command=added_value.tau
                                    ).grid(row=2, column=4)

                    btnCosh = Button(calc, text="cosh", width=3,
                                     height=1, bg='black', fg='white',
                                     font=('Verdana', 16), padx=10, pady=4,
                                     command=added_value.cosh
                                     ).grid(row=2, column=5)

                    btntanh = Button(calc, text="tanh", width=3,
                                     height=1, bg='black', fg='white',
                                     font=('Verdana', 16), padx=10, pady=4,
                                     command=added_value.tanh
                                     ).grid(row=2, column=6)

                    btnsinh = Button(calc, text="sinh", width=3,
                                     height=1, bg='black', fg='white',
                                     font=('Verdana', 16), padx=10, pady=4,
                                     command=added_value.sinh
                                     ).grid(row=2, column=7)

                    # ROW 3 :
                    btnlog = Button(calc, text="log", width=3,
                                    height=1, bg='black', fg='white',
                                    font=('Verdana', 16), padx=10, pady=4,
                                    command=added_value.log
                                    ).grid(row=3, column=4)

                    btnExp = Button(calc, text="exp", width=3, height=1,
                                    bg='black', fg='white',
                                    font=('Verdana', 16), padx=10, pady=4,
                                    command=added_value.exp
                                    ).grid(row=3, column=5)

                    btnMod = Button(calc, text="Mod", width=3,
                                    height=1, bg='black', fg='white',
                                    font=('Verdana', 16), padx=10, pady=4,
                                    command=lambda: added_value.operation("mod")
                                    ).grid(row=3, column=6)

                    btnE = Button(calc, text="e", width=3,
                                  height=1, bg='black', fg='white',
                                  font=('Verdanaa', 16), padx=10, pady=4,
                                  command=added_value.e
                                  ).grid(row=3, column=7)

                    # ROW 4 :
                    btnlog10 = Button(calc, text="log10", width=3,
                                      height=1, bg='black', fg='white',
                                      font=('Verdana', 16), padx=10, pady=4,
                                      command=added_value.log10
                                      ).grid(row=4, column=4)

                    btncos = Button(calc, text="log1p", width=3,
                                    height=1, bg='black', fg='white',
                                    font=('Verdana', 15), padx=10, pady=4,
                                    command=added_value.log1p
                                    ).grid(row=4, column=5)

                    btnexpm1 = Button(calc, text="expm1", width=3,
                                      height=1, bg='black', fg='white',
                                      font=('Verdana', 14), padx=10, pady=8,
                                      command=added_value.expm1
                                      ).grid(row=4, column=6)

                    btngamma = Button(calc, text="gamma", width=3,
                                      height=1, bg='black', fg='white',
                                      font=('Verdana', 12), padx=12, pady=12,
                                      command=added_value.lgamma
                                      ).grid(row=4, column=7)
                    # ROW 5 :
                    btnlog2 = Button(calc, text="log2", width=3,
                                     height=1, bg='black', fg='white',
                                     font=('Verdana', 16), padx=10, pady=4,
                                     command=added_value.log2
                                     ).grid(row=5, column=4, pady=1)

                    btndeg = Button(calc, text="deg", width=3,
                                    height=1, bg='black', fg='white',
                                    font=('Verdana', 16), padx=10, pady=4,
                                    command=added_value.degrees
                                    ).grid(row=5, column=5, pady=1)

                    btnacosh = Button(calc, text="acosh", width=3,
                                      height=1, bg='black', fg='white',
                                      font=('Verdana', 16), padx=10, pady=4,
                                      command=added_value.acosh
                                      ).grid(row=5, column=6, pady=1)

                    btnasinh = Button(calc, text="asinh", width=3,
                                      height=1, bg='black', fg='white',
                                      font=('Verdana', 16), padx=10, pady=4,
                                      command=added_value.asinh
                                      ).grid(row=5, column=7, pady=1)

                    lblDisplay = Label(calc, text="Scientific Calculator",
                                       font=('Verdana', 24, 'underline'),
                                       bg='black', fg='white', justify=CENTER)

                    lblDisplay.grid(row=0, column=4, columnspan=4)

                    def iExit():
                        iExit = messagebox.askyesno("Scientific Calculator",
                                                    "Do you want to exit ?")
                        if iExit > 0:
                            root2.destroy()
                            return

                    def Scientific():
                        root2.resizable(width=False, height=False)
                        root2.geometry("944x568+0+0")

                    def Standard():
                        root2.resizable(width=False, height=False)
                        root2.geometry("480x568+0+0")

                    menubar = Menu(calc)

                    # ManuBar 1 :
                    filemenu = Menu(menubar, tearoff=0)
                    menubar.add_cascade(label='File', menu=filemenu)
                    filemenu.add_command(label="Standard", command=Standard)
                    filemenu.add_command(label="Scientific", command=Scientific)
                    filemenu.add_separator()
                    filemenu.add_command(label="Exit", command=iExit)

                    # ManuBar 2 :
                    editmenu = Menu(menubar, tearoff=0)
                    menubar.add_cascade(label='Edit', menu=editmenu)
                    editmenu.add_command(label="Cut")
                    editmenu.add_command(label="Copy")
                    editmenu.add_separator()
                    editmenu.add_command(label="Paste")

                    root2.config(menu=menubar)

                    root2.mainloop()

                def lab1():

                    class Notepad:
                        __root = Toplevel()

                        # default window width and height
                        __thisWidth = 300
                        __thisHeight = 300
                        __thisTextArea = Text(__root)
                        __thisMenuBar = Menu(__root)
                        __thisFileMenu = Menu(__thisMenuBar, tearoff=0)
                        __thisEditMenu = Menu(__thisMenuBar, tearoff=0)
                        __thisHelpMenu = Menu(__thisMenuBar, tearoff=0)

                        # To add scrollbar
                        __thisScrollBar = Scrollbar(__thisTextArea)
                        __file = None

                        def __init__(self, **kwargs):

                            # Set icon
                            try:
                                self.__root.wm_iconbitmap("Notepad.ico")
                            except:
                                pass

                            # Set window size (the default is 300x300)

                            try:
                                self.__thisWidth = kwargs['width']
                            except KeyError:
                                pass

                            try:
                                self.__thisHeight = kwargs['height']
                            except KeyError:
                                pass

                            # Set the window text
                            self.__root.title("Untitled - Notepad")

                            # Center the window
                            screenWidth = self.__root.winfo_screenwidth()
                            screenHeight = self.__root.winfo_screenheight()

                            # For left-alling
                            left = (screenWidth / 2) - (self.__thisWidth / 2)

                            # For right-allign
                            top = (screenHeight / 2) - (self.__thisHeight / 2)

                            # For top and bottom
                            self.__root.geometry('%dx%d+%d+%d' % (self.__thisWidth,
                                                                  self.__thisHeight,
                                                                  left, top))

                            # To make the textarea auto resizable
                            self.__root.grid_rowconfigure(0, weight=1)
                            self.__root.grid_columnconfigure(0, weight=1)

                            # Add controls (widget)
                            self.__thisTextArea.grid(sticky=N + E + S + W)

                            # To open new file
                            self.__thisFileMenu.add_command(label="New",
                                                            command=self.__newFile)

                            # To open a already existing file
                            self.__thisFileMenu.add_command(label="Open",
                                                            command=self.__openFile)

                            # To save current file
                            self.__thisFileMenu.add_command(label="Save",
                                                            command=self.__saveFile)

                            # To create a line in the dialog
                            self.__thisFileMenu.add_separator()
                            self.__thisFileMenu.add_command(label="Exit",
                                                            command=self.__quitApplication)
                            self.__thisMenuBar.add_cascade(label="File",
                                                           menu=self.__thisFileMenu)

                            # To give a feature of cut
                            self.__thisEditMenu.add_command(label="Cut",
                                                            command=self.__cut)

                            # to give a feature of copy
                            self.__thisEditMenu.add_command(label="Copy",
                                                            command=self.__copy)

                            # To give a feature of paste
                            self.__thisEditMenu.add_command(label="Paste",
                                                            command=self.__paste)

                            # To give a feature of editing
                            self.__thisMenuBar.add_cascade(label="Edit",
                                                           menu=self.__thisEditMenu)

                            # To create a feature of description of the notepad
                            self.__thisHelpMenu.add_command(label="About Notepad",
                                                            command=self.__showAbout)
                            self.__thisMenuBar.add_cascade(label="Help",
                                                           menu=self.__thisHelpMenu)

                            self.__root.config(menu=self.__thisMenuBar)

                            self.__thisScrollBar.pack(side=RIGHT, fill=Y)

                            # Scrollbar will adjust automatically according to the content
                            self.__thisScrollBar.config(command=self.__thisTextArea.yview)
                            self.__thisTextArea.config(yscrollcommand=self.__thisScrollBar.set)

                        def __quitApplication(self):
                            self.__root.destroy()
                            # exit()

                        def __showAbout(self):
                            messagebox.showinfo("Notepad", "...")

                        def __openFile(self):

                            self.__file = askopenfilename(defaultextension=".txt",
                                                          filetypes=[("All Files", "*.*"),
                                                                     ("Text Documents", "*.txt")])

                            if self.__file == "":

                                # no file to open
                                self.__file = None
                            else:

                                # Try to open the file
                                # set the window title
                                self.__root.title(os.path.basename(self.__file) + " - Notepad")
                                self.__thisTextArea.delete(1.0, END)

                                file = open(self.__file, "r")

                                self.__thisTextArea.insert(1.0, file.read())

                                file.close()

                        def __newFile(self):
                            self.__root.title("Untitled - Notepad")
                            self.__file = None
                            self.__thisTextArea.delete(1.0, END)

                        def __saveFile(self):

                            if self.__file == None:
                                # Save as new file
                                self.__file = asksaveasfilename(initialfile='Untitled.txt',
                                                                defaultextension=".txt",
                                                                filetypes=[("All Files", "*.*"),
                                                                           ("Text Documents", "*.txt")])

                                if self.__file == "":
                                    self.__file = None
                                else:

                                    # Try to save the file
                                    file = open(self.__file, "w")
                                    file.write(self.__thisTextArea.get(1.0, END))
                                    file.close()

                                    # Change the window title
                                    self.__root.title(os.path.basename(self.__file) + " - Notepad")


                            else:
                                file = open(self.__file, "w")
                                file.write(self.__thisTextArea.get(1.0, END))
                                file.close()

                        def __cut(self):
                            self.__thisTextArea.event_generate("<<Cut>>")

                        def __copy(self):
                            self.__thisTextArea.event_generate("<<Copy>>")

                        def __paste(self):
                            self.__thisTextArea.event_generate("<<Paste>>")

                        def run(self):

                            # Run main application
                            self.__root.mainloop()

                        # Run main application

                    notepad = Notepad(width=600, height=400)
                    notepad.run()

                def lab2():
                    window = Toplevel()
                    # set title for window
                    window.title("Python IDE")
                    # create and configure menu
                    menu = Menu(window)
                    window.config(menu=menu)
                    # create editor window for writing code
                    editor = ScrolledText(window, font=("Verdana 10 bold"), wrap=None)
                    editor.pack(fill=BOTH, expand=1)
                    editor.focus()
                    file_path = ""

                    # function to open files
                    def open_file(event=None):
                        global code, file_path
                        # code = editor.get(1.0, END)
                        open_path = askopenfilename(filetypes=[("Python File", "*.py")])
                        file_path = open_path
                        with open(open_path, "r") as file:
                            code = file.read()
                            editor.delete(1.0, END)
                            editor.insert(1.0, code)

                    window.bind("<Control-o>", open_file)

                    # function to save files
                    def save_file(event=None):
                        global code, file_path
                        if file_path == '':
                            save_path = asksaveasfilename(defaultextension=".py", filetypes=[("Python File", "*.py")])
                            file_path = save_path
                        else:
                            save_path = file_path
                        with open(save_path, "w") as file:
                            code = editor.get(1.0, END)
                            file.write(code)

                    window.bind("<Control-s>", save_file)

                    # function to save files as specific name
                    def save_as(event=None):
                        global code, file_path
                        # code = editor.get(1.0, END)
                        save_path = asksaveasfilename(defaultextension=".py", filetypes=[("Python File", "*.py")])
                        file_path = save_path
                        with open(save_path, "w") as file:
                            code = editor.get(1.0, END)
                            file.write(code)

                    window.bind("<Control-S>", save_as)

                    # function to execute the code and
                    # display its output
                    def run(event=None):
                        global code, file_path
                        '''
                        code = editor.get(1.0, END)
                        exec(code)
                        '''
                        cmd = f"python (file_path)"
                        process = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                                                   stderr=subprocess.PIPE, shell=True)
                        output, error = process.communicate()
                        # delete the previous text from
                        # output_windows
                        output_window.delete(1.0, END)
                        # insert the new output text in
                        # output_windows
                        output_window.insert(1.0, output)
                        # insert the error text in output_windows
                        # if there is error
                        output_window.insert(1.0, error)

                    window.bind("<F5>", run)

                    # function to close IDE window
                    def close(event=None):
                        window.destroy()

                    window.bind("<Control-q>", close)

                    # define function to cut
                    # the selected text
                    def cut_text(event=None):
                        editor.event_generate(("<<Cut>>"))

                    # define function to copy
                    # the selected text
                    def copy_text(event=None):
                        editor.event_generate(("<<Copy>>"))

                    # define function to paste
                    # the previously copied text
                    def paste_text(event=None):
                        editor.event_generate(("<<Paste>>"))

                    # create menus
                    file_menu = Menu(menu, tearoff=0)
                    edit_menu = Menu(menu, tearoff=0)
                    run_menu = Menu(menu, tearoff=0)
                    view_menu = Menu(menu, tearoff=0)
                    theme_menu = Menu(menu, tearoff=0)
                    # add menu labels
                    menu.add_cascade(label="File", menu=file_menu)
                    menu.add_cascade(label="Edit", menu=edit_menu)
                    menu.add_cascade(label="Run", menu=run_menu)
                    menu.add_cascade(label="View", menu=view_menu)
                    menu.add_cascade(label="Theme", menu=theme_menu)
                    # add commands in flie menu
                    file_menu.add_command(label="Open", accelerator="Ctrl+O", command=open_file)
                    file_menu.add_separator()
                    file_menu.add_command(label="Save", accelerator="Ctrl+S", command=save_file)
                    file_menu.add_command(label="Save As", accelerator="Ctrl+Shift+S", command=save_as)
                    file_menu.add_separator()
                    file_menu.add_command(label="Exit", accelerator="Ctrl+Q", command=close)
                    # add commands in edit menu
                    edit_menu.add_command(label="Cut", command=cut_text)
                    edit_menu.add_command(label="Copy", command=copy_text)
                    edit_menu.add_command(label="Paste", command=paste_text)
                    run_menu.add_command(label="Run", accelerator="F5", command=run)
                    # function to display and hide status bar
                    show_status_bar = BooleanVar()
                    show_status_bar.set(True)

                    def hide_statusbar():
                        global show_status_bar
                        if show_status_bar:
                            status_bars.pack_forget()
                            show_status_bar = False
                        else:
                            status_bars.pack(side=BOTTOM)
                            show_status_bar = True

                    view_menu.add_checkbutton(label="Status Bar", onvalue=True, offvalue=0, variable=show_status_bar,
                                              command=hide_statusbar)
                    # create a label for status bar
                    status_bars = ttk.Label(window, text="www.codershubb.com \t\t\t\t\t\t characters: 0 words: 0")
                    status_bars.pack(side=BOTTOM)
                    # function to display count and word characters
                    text_change = False

                    def change_word(event=None):
                        global text_change
                        if editor.edit_modified():
                            text_change = True
                            word = len(editor.get(1.0, "end-1c").split())
                            chararcter = len(editor.get(1.0, "end-1c").replace(" ", ""))
                            status_bars.config(
                                text=f"www.codershubb.com \t\t\t\t\t\t characters: {chararcter} words: {word}")
                        editor.edit_modified(False)

                    editor.bind("<<Modified>>", change_word)

                    # function for light mode window
                    def light():
                        editor.config(bg="white")
                        output_window.config(bg="white")

                    # function for dark mode window
                    def dark():
                        editor.config(fg="white", bg="black")
                        output_window.config(fg="white", bg="black")

                    # add commands to change themes
                    theme_menu.add_command(label="light", command=light)
                    theme_menu.add_command(label="dark", command=dark)
                    # create output window to display output of written code
                    output_window = ScrolledText(window, height=10)
                    output_window.pack(fill=BOTH, expand=1)
                    window.mainloop()

                b1 = Button(master, text="Notepad", padx=7, bg="#2e0000", fg="white", command=lab1)
                b1.pack()
                b2 = Button(master, text="Python IDE", bg="#2e0000", fg="white", command=lab2)
                b2.pack()
                b3 = Button(master, text="Calculator", padx=3, bg="#2e0000", fg="white", command=calc)
                b3.pack()

            def result():
                master = Toplevel()
                master.title("Result")
                master.geometry("400x300")
                master.config(bg="#dec8ab")
                l1 = Label(master, text="Select:", bg="#dec8ab", font="Verdana 8")
                l1.grid(row=0, column=0)
                x = ["MCQ", "Assignment"]
                a = StringVar()
                c1 = OptionMenu(master, a, *x)
                c1.grid(row=0, column=1)
                l2 = Label(master, text="Roll_No:", bg="#dec8ab", font="Verdana 8")
                l2.grid(row=1, column=0)
                t = Entry(master)
                t.grid(row=1, column=1)
                l3 = Label(master, text="Branch:", bg="#dec8ab", font="Verdana 8")
                l3.grid(row=2, column=0)
                y = ["CSE", "IT", "MECH"]
                b = StringVar()
                c1 = OptionMenu(master, b, *y)
                c1.grid(row=2, column=1)
                l6 = Label(master, text="Semester:", bg="#dec8ab", font="Verdana 8")
                l6.grid(row=2, column=2)
                z = []
                for i in range(1, 9):
                    z.append(i)
                c = IntVar()
                c1 = OptionMenu(master, c, *z)
                c1.grid(row=2, column=3)
                l4 = Label(master, text="Subject", bg="#dec8ab", font="Verdana 8")
                l4.grid(row=3, column=0)
                l5 = Label(master, text="Marks", bg="#dec8ab", font="Verdana 8")
                l5.grid(row=3, column=1)
                t1 = Entry(master)
                t2 = Entry(master)
                t3 = Entry(master)
                t4 = Entry(master)
                t5 = Entry(master)
                t6 = Entry(master)
                t7 = Entry(master)
                t8 = Entry(master)
                t9 = Entry(master)
                t10 = Entry(master)
                t1.grid(row=5, column=0)
                t2.grid(row=6, column=0)
                t3.grid(row=7, column=0)
                t4.grid(row=8, column=0)
                t5.grid(row=9, column=0)
                t6.grid(row=5, column=1)
                t7.grid(row=6, column=1)
                t8.grid(row=7, column=1)
                t9.grid(row=8, column=1)
                t10.grid(row=9, column=1)

                def clear():
                    t1.delete(0, END)
                    t2.delete(0, END)
                    t3.delete(0, END)
                    t4.delete(0, END)
                    t5.delete(0, END)
                    t6.delete(0, END)
                    t7.delete(0, END)
                    t8.delete(0, END)
                    t9.delete(0, END)
                    t10.delete(0, END)

                def add():
                    z = a.get()
                    p = t.get()
                    x = b.get()
                    y = c.get()
                    e = t1.get()
                    f = t2.get()
                    g = t3.get()
                    h = t4.get()
                    i = t5.get()
                    j = t6.get()
                    k = t7.get()
                    l = t8.get()
                    m = t9.get()
                    n = t10.get()
                    db = pymysql.connect(host='localhost', user='root', password='stuart@2002', db='hackathon')
                    if p == "" or e == "" or f == "" or g == "" or h == "" or i == "" or j == "" or k == "" or l == "" or m == "" or n == "" or j.isdigit() is False or \
                            p.isdigit() is False or k.isdigit() is False or l.isdigit() is False or m.isdigit() is False or n.isdigit() is False:
                        messagebox.showwarning("Alert!", "Enter valid values.")
                    else:
                        sql = "insert into result values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                        val = (z,p, x, y, e, f, g, h, i, j, k, l, m, n)
                        cur = db.cursor()
                        cur.execute(sql, val)
                        db.commit()
                        messagebox.showinfo("AddedSuccessfully!")

                def update():
                    i = t5.get()
                    j = t6.get()
                    k = t7.get()
                    l = t8.get()
                    m = t9.get()
                    n = t10.get()

                b1 = Button(master, text="add", bg="green", fg="white", padx=48, command=add)
                b2 = Button(master, text="update", bg="yellow", padx=40,command = update)
                b3 = Button(master, text="clear", bg="gray", fg="white", padx=45, command=clear)
                b4 = Button(master, text="delete", bg="red", fg="white", padx=42)
                b1.grid(row=10, column=0)
                b2.grid(row=11, column=0)
                b3.grid(row=10, column=1)
                b4.grid(row=11, column=1)

            def classroom():
                gui = Toplevel()
                gui.config(background="#dec8ab")
                gui.title("CALENDAR")
                gui.geometry("850x850")
                f = Frame(gui)
                f.config(bg="#dec8ab")
                f.grid(row=0, column=0)
                cal = Label(f, text="CALENDAR", bg="#dec8ab",
                            font=("Verdana", 14, 'underline'))
                year = Label(f, text="Enter Year", font="Verdana 8", bg="#dec8ab")
                year_field = Entry(f)
                cal.grid(row=1, column=1)
                year.grid(row=2, column=1)
                year_field.grid(row=3, column=1)

                f1 = Frame(gui)
                f1.grid(row=0, column=2)
                f1.config(bg="#dec8ab")

                def n1():
                    # Enter your API key and your API secret
                    API_KEY = 'MIswLGxeQk-glrzt3iDnQQ'
                    API_SEC = 'ANmqR4NVPKAHSJZEW8DRROQiBkhB8tKpwb4F'

                    # create a function to generate a token
                    # using the pyjwt library
                    def generateToken():
                        token = jwt.encode(

                            # Create a payload of the token containing
                            # API Key & expiration time
                            {'iss': API_KEY, 'exp': time() + 5000},

                            # Secret used to generate token signature
                            API_SEC,

                            # Specify the hashing alg
                            algorithm='HS256'
                        )
                        return token

                    # create json data for post requests
                    meetingdetails = {"topic": "The title of your zoom meeting",
                                      "type": 2,
                                      "start_time": "2019-06-14T10: 21: 57",
                                      "duration": "45",
                                      "timezone": "Europe/Madrid",
                                      "agenda": "test",

                                      "recurrence": {"type": 1,
                                                     "repeat_interval": 1
                                                     },
                                      "settings": {"host_video": "true",
                                                   "participant_video": "true",
                                                   "join_before_host": "False",
                                                   "mute_upon_entry": "False",
                                                   "watermark": "true",
                                                   "audio": "voip",
                                                   "auto_recording": "cloud"
                                                   }
                                      }

                    # send a request with headers including
                    # a token and meeting details
                    def createMeeting():

                        headers = {'authorization': 'Bearer %s' % generateToken(),
                                   'content-type': 'application/json'}
                        r = requests.post(
                            f'https://api.zoom.us/v2/users/me/meetings',
                            headers=headers, data=json.dumps(meetingdetails))

                        # converting the output into json and extracting the details
                        y = json.loads(r.text)
                        join_URL = y["join_url"]
                        meetingPassword = y["password"]

                        def callback(url):
                            webbrowser.open_new_tab(url)

                        link = Label(f1, text='join_URL', bg='blue', fg='white', cursor="hand2")
                        link.grid(row=2, column=0)
                        link.bind("<Button-1>", lambda e: callback(f"{join_URL}"))
                        pswrd = Label(f1, text=f"password:{meetingPassword}")
                        pswrd.grid(row=3, column=0)

                        # l = Label.config(gui,f'here is your zoom meeting link {join_URL} and your password: "{meetingPassword}')
                        # l.pack()

                    # run the create meeting function
                    createMeeting()

                b = Button(f1, text="New Meeting",bg="#2e0000",fg='white', command=n1)
                b.grid(row=0, column=0)

                def showCal():
                    fetch_year = int(year_field.get())
                    cal_content = calendar.calendar(fetch_year)
                    cal_year = Label(f, text=cal_content, font="Consolas 10 bold")
                    cal_year.grid(row=5, column=1, padx=20)
                    year_field.delete(0, END)

                Show = Button(f, text="Show Calendar", fg="white",
                              bg="#2e0000", command=showCal)
                Show.grid(row=4, column=1)
                Exit = Button(f, text="Exit", fg="white", bg="Red", command=exit)
                Exit.grid(row=6, column=1)

            b1 = Button(master, text="Classroom", padx=5, bg="#2e0000", fg="white", command=classroom)
            b1.pack()
            b2 = Button(master, text="Assignment", bg="#2e0000", fg="white")
            b2.pack()
            b3 = Button(master, text="Tests", padx=20, bg="#2e0000", fg="white")
            b3.pack()
            b4 = Button(master, text="Attendance", padx=3, bg="#2e0000", fg="white")
            b4.pack()
            b5 = Button(master, text="Virtual Lab", padx=6, bg="#2e0000", fg="white", command=lab)
            b5.pack()
            b6 = Button(master, text="Results", padx=16, bg="#2e0000", fg="white", command=result)
            b6.pack()

        def profile1():
            s = Toplevel()
            s.title("FACULTY PROFILE")
            s.geometry("300x250")
            s.config(bg="#dec8ab")
            l = Label(s,text="PROFILE",font="Verdana 10 underline",bg="#dec8ab")
            l.grid(row=0,column=1)
            l1 = Label(s,text="Faculty_ID",font="Verdana 10 underline",bg="#dec8ab")
            l1.grid(row=1,column=0)
            l2 = Label(s,text="Name",font="Verdana 10 underline",bg="#dec8ab")
            l3 = Label(s,text="Contact",font="Verdana 10 underline",bg="#dec8ab")
            l4 = Label(s,text="EMail_ID",font="Verdana 10 underline",bg="#dec8ab")
            l5 = Label(s,text="Department",font="Verdana 10 underline",bg="#dec8ab")
            l6 = Label(s,text="Gender",font="Verdana 10 underline",bg="#dec8ab")
            l2.grid(row=2,column=0)
            l3.grid(row=3,column=0)
            l4.grid(row=4,column=0)
            l5.grid(row=5,column=0)
            l6.grid(row=6,column=0)
            t = Entry(s)
            t.grid(row=1,column=1)

            def go2():
                a = t.get()
                db = pymysql.connect(host='localhost',user='root',password='stuart@2002',db='hackathon')
                sql = "select * from faculty where faculty_id = %s"
                val = (a)
                cur = db.cursor()
                cur.execute(sql,val)
                i = 1
                for row in cur.fetchall():
                    a1 = Label(s,text=" ",bg="#dec8ab")
                    a2 = Label(s,text=" ",bg="#dec8ab")
                    a3 = Label(s,text=" ",bg="#dec8ab")
                    a4 = Label(s,text=" ",bg="#dec8ab")
                    a5 = Label(s,text=" ",bg="#dec8ab")
                    a1.config(text=row[1])
                    a2.config(text=row[2])
                    a3.config(text=row[3])
                    a4.config(text=row[4])
                    a5.config(text=row[5])
                    a1.grid(row=2,column=i)
                    a2.grid(row=3,column=i)
                    a3.grid(row=4,column=i)
                    a4.grid(row=5,column=i)
                    a5.grid(row=6,column=i)
                    i = i + 1

            b = Button(s,text="go",bg="green",fg="white",command=go2)
            b.grid(row=1,column=2)
        b1 = Button(master, text="PROFILE", bg="#2e0000", fg="white", padx=4,command=profile1)
        b1.pack()
        b2 = Button(master, text="ACTIVITY", bg="#2e0000", fg="white", command=activity)
        b2.pack()

    def createacc():
        master = Toplevel()
        master.title("Create Account")
        master.geometry("300x200")
        master.config(bg="#dec8ab")
        l = Label(master, text="FACULTY LOGIN", bg="#dec8ab", font="Verdana 10 underline")
        l.grid(row=0, column=1)
        l1 = Label(master, text="User_ID", bg="#dec8ab", font="Verdana 8")
        l1.grid(row=1, column=0)
        t1 = Entry(master)
        t1.grid(row=1, column=1)
        l2 = Label(master, text="Name", bg="#dec8ab", font="Verdana 8")
        l2.grid(row=2, column=0)
        t2 = Entry(master)
        t2.grid(row=2, column=1)
        l3 = Label(master, text="Contact_no", bg="#dec8ab", font="Verdana 8")
        l3.grid(row=3, column=0)
        t3 = Entry(master)
        t3.grid(row=3, column=1)
        l4 = Label(master, text="Email_ID", bg="#dec8ab", font="Verdana 8")
        l4.grid(row=4, column=0)
        t4 = Entry(master)
        t4.grid(row=4, column=1)
        l5 = Label(master, text="Department", bg="#dec8ab", font="Verdana 8")
        l5.grid(row=5, column=0)
        t5 = ["CSE", "MECH", "IT"]
        v = StringVar()
        c2 = OptionMenu(master, v, *t5)
        c2.grid(row=5, column=1)
        l6 = Label(master, text="Gender", bg="#dec8ab", font="Verdana 8")
        l6.grid(row=6, column=0)
        x1 = ["Male", "Female", "Other"]
        s = StringVar()
        c1 = OptionMenu(master, s, *x1)
        c1.grid(row=6, column=1)

        def save():
            a = t1.get()
            b = t2.get()
            c = t3.get()
            d = t4.get()
            e = v.get()
            f = s.get()
            db = pymysql.connect(host='localhost', user='root', password='stuart@2002', db='hackathon')
            if (a == "" or b == "" or c == "" or d == "" or c.isdigit() is False or a.isdigit() is False):
                messagebox.showwarning("Alert!", "Enter valid values.")
            else:
                sql = "insert into faculty values(%s,%s,%s,%s,%s,%s)"
                val = (a, b, c, d, e, f)
                cur = db.cursor()
                cur.execute(sql, val)
                db.commit()
                print("Successful")
                messagebox.showinfo("Successfully Registered!",
                                    "Congratulations! You have successfully been registered.")
                master.destroy()

        def clear1():
            t1.delete(0, END)
            t2.delete(0, END)
            t3.delete(0, END)
            t4.delete(0, END)

        b1 = Button(master, text="Save", bg="green", fg="white", command=save)
        b1.grid(row=7, column=1)
        b2 = Button(master, text="clear", command=clear1)
        b2.grid(row=7, column=0)

    b1 = Button(master, text="Login", bg="green", fg="white", padx=26, command=flogin)
    b1.pack()
    b2 = Button(master, text="Create Account", bg="blue", fg="white", command=createacc)
    b2.pack()


def student():
    m = Toplevel()
    m.title("STUDENT LOGIN")
    m.config(bg="#dec8ab")
    m.geometry("300x200")
    l = Label(m,text="STUDENT LOGIN",font="Verdana 10 underline",bg="#dec8ab")
    l.grid(row=0,column=1)
    l1 = Label(m, text="Email_ID:", bg="#dec8ab")
    l1.grid(row=1, column=0)
    l2 = Label(m, text="Contact_no:", bg="#dec8ab")
    l2.grid(row=2, column=0)
    t1 = Entry(m)
    t1.grid(row=1, column=1)
    t2 = Entry(m)
    t2.grid(row=2, column=1)

    # STUDENT LOGIN CHECK
    def check():
        a = t1.get()
        b = t2.get()
        db = pymysql.connect(host='localhost', user='root', password='stuart@2002', db='hackathon')
        sql = "select * from student where email = %s and contact = %s"
        i = 0
        val = (a, b)
        cur = db.cursor()
        cur.execute(sql, val)
        for row in cur.fetchall():
            i = i + 1
        if i == 0:
            messagebox.showwarning("", "Invalid login")
        else:
            t1.delete(0,END)
            t2.delete(0,END)
            d = Toplevel(m)
            d.config(bg="#dec8ab")
            d.title("STUDENT PANEL")
            d.geometry("300x200")
            l = Label(d, text="STUDENT", bg="#dec8ab", font="Verdana 10 underline")
            l.pack()

            def profile():
                a = Toplevel(d)
                a.title("PROFILE")
                a.config(bg="#dec8ab")
                a.geometry("400x300")
                l1 = Label(a, text="University_rno", bg="#dec8ab")
                l1.grid(row=0, column=0)
                l2 = Label(a, text="Name", bg="#dec8ab")
                l2.grid(row=1, column=0)
                l3 = Label(a, text="Contact_no", bg="#dec8ab")
                l3.grid(row=2, column=0)
                l4 = Label(a, text="Email_ID", bg="#dec8ab")
                l4.grid(row=3, column=0)
                l5 = Label(a, text="Branch", bg="#dec8ab")
                l5.grid(row=4, column=0)
                l6 = Label(a, text="Semester", bg="#dec8ab")
                l6.grid(row=5, column=0)
                t = Entry(a)
                t.grid(row=0, column=1)

                def goo():
                    m = t.get()
                    db = pymysql.connect(host='localhost', user='root', password='stuart@2002', db='hackathon')
                    i = 1
                    sql = 'select * from student where university_rno = %s'
                    val = (m)
                    cur = db.cursor()
                    cur.execute(sql, val)
                    for row in cur.fetchall():
                        a1 = Label(a, text=" ", bg="#dec8ab")
                        a2 = Label(a, text=" ", bg="#dec8ab")
                        a3 = Label(a, text=" ", bg="#dec8ab")
                        a4 = Label(a, text=" ", bg="#dec8ab")
                        a5 = Label(a, text=" ", bg="#dec8ab")
                        a1.config(text=row[1])
                        a2.config(text=row[2])
                        a3.config(text=row[3])
                        a4.config(text=row[4])
                        a5.config(text=row[5])
                        a1.grid(row=1, column=i)
                        a2.grid(row=2, column=i)
                        a3.grid(row=3, column=i)
                        a4.grid(row=4, column=i)
                        a5.grid(row=5, column=i)
                        i = i + 1

                b = Button(a, text="go", bg="green", fg="white", command=goo)
                b.grid(row=0, column=2)

                def logout():
                    val = messagebox.askyesno("", "Are you sure you want to logout?")
                    if val == True:
                        a.destroy()
                    else:
                        return

                b1 = Button(a, text="Logout", fg="white", bg="red", command=logout)
                b1.grid(row=6, column=1)

            b1 = Button(d,text="PROFILE",padx=3,bg="#2e0000",fg="white",command=profile)
            b1.pack()

            def activity():
                q = Toplevel(d)
                q.config(bg="#dec8ab")
                q.geometry("400x300")
                q.title("ACTIVITY")

                def class1():
                    gui1 = Toplevel()
                    gui1.config(background="#dec8ab")
                    gui1.title("CLASSROOM")
                    gui1.geometry("650x650")
                    f = Frame(gui1)
                    f.config(bg="#dec8ab")
                    f.grid(row=0, column=0)
                    cal = Label(f, text="CALENDAR", bg="#dec8ab",
                                font=("Verdana", 14, 'underline'))
                    year = Label(f, text="Enter Year", font="Verdana 8", bg="#dec8ab")
                    year_field = Entry(f)
                    cal.grid(row=1, column=1)
                    year.grid(row=2, column=1)
                    year_field.grid(row=3, column=1)

                    def showCal1():
                        fetch_year = int(year_field.get())
                        cal_content = calendar.calendar(fetch_year)
                        cal_year = Label(f, text=cal_content, font="Consolas 10 bold")
                        cal_year.grid(row=5, column=1, padx=20)
                        year_field.delete(0, END)

                    Show = Button(f, text="Show Calendar", fg="white",
                                  bg="#2e0000", command=showCal1)
                    Show.grid(row=4, column=1)
                    Exit = Button(f, text="Exit", fg="white", bg="Red", command=exit)
                    Exit.grid(row=6, column=1)

                b1 = Button(q, text="CLASSROOM", padx=2, fg="white", bg="#2e0000", command=class1)
                b1.pack()
                b2 = Button(q, text="ASSIGNMENT", fg="white", bg="#2e0000")
                b2.pack()
                b3 = Button(q, text="TEST", fg="white", bg="#2e0000", padx=25)
                b3.pack(padx=10)
                b4 = Button(q, text="ATTENDANCE", fg="white", bg="#2e0000")
                b4.pack()

                def lab():
                    master = Toplevel()
                    master.title("VIRTUAL LAB")
                    master.geometry("300x200")
                    master.config(bg="#dec8ab")

                    def calc():
                        root2 = Toplevel()
                        root2.title("Scientific Calculator")
                        root2.configure(background='black')
                        root2.resizable(width=True, height=True)
                        root2.geometry("645x345")
                        calc = Frame(root2)
                        calc.config(bg="black")
                        calc.grid()

                        class Calc():
                            def __init__(self):
                                self.total = 0
                                self.current = ''
                                self.input_value = True
                                self.check_sum = False
                                self.op = ''
                                self.result = False

                            def numberEnter(self, num):
                                self.result = False
                                firstnum = txtDisplay.get()
                                secondnum = str(num)
                                if self.input_value:
                                    self.current = secondnum
                                    self.input_value = False
                                else:
                                    if secondnum == '.':
                                        if secondnum in firstnum:
                                            return
                                    self.current = firstnum + secondnum
                                self.display(self.current)

                            def sum_of_total(self):
                                self.result = True
                                self.current = float(self.current)
                                if self.check_sum == True:
                                    self.valid_function()
                                else:
                                    self.total = float(txtDisplay.get())

                            def display(self, value):
                                txtDisplay.delete(0, END)
                                txtDisplay.insert(0, value)

                            def valid_function(self):
                                if self.op == "add":
                                    self.total += self.current
                                if self.op == "sub":
                                    self.total -= self.current
                                if self.op == "multi":
                                    self.total *= self.current
                                if self.op == "divide":
                                    self.total /= self.current
                                if self.op == "mod":
                                    self.total %= self.current
                                self.input_value = True
                                self.check_sum = False
                                self.display(self.total)

                            def operation(self, op):
                                self.current = float(self.current)
                                if self.check_sum:
                                    self.valid_function()
                                elif not self.result:
                                    self.total = self.current
                                    self.input_value = True
                                self.check_sum = True
                                self.op = op
                                self.result = False

                            def Clear_Entry(self):
                                self.result = False
                                self.current = "0"
                                self.display(0)
                                self.input_value = True

                            def All_Clear_Entry(self):
                                self.Clear_Entry()
                                self.total = 0

                            def pi(self):
                                self.result = False
                                self.current = math.pi
                                self.display(self.current)

                            def tau(self):
                                self.result = False
                                self.current = math.tau
                                self.display(self.current)

                            def e(self):
                                self.result = False
                                self.current = math.e
                                self.display(self.current)

                            def mathPM(self):
                                self.result = False
                                self.current = -(float(txtDisplay.get()))
                                self.display(self.current)

                            def squared(self):
                                self.result = False
                                self.current = math.sqrt(float(txtDisplay.get()))
                                self.display(self.current)

                            def cos(self):
                                self.result = False
                                self.current = math.cos(math.radians(float(txtDisplay.get())))
                                self.display(self.current)

                            def cosh(self):
                                self.result = False
                                self.current = math.cosh(math.radians(float(txtDisplay.get())))
                                self.display(self.current)

                            def tan(self):
                                self.result = False
                                self.current = math.tan(math.radians(float(txtDisplay.get())))
                                self.display(self.current)

                            def tanh(self):
                                self.result = False
                                self.current = math.tanh(math.radians(float(txtDisplay.get())))
                                self.display(self.current)

                            def sin(self):
                                self.result = False
                                self.current = math.sin(math.radians(float(txtDisplay.get())))
                                self.display(self.current)

                            def sinh(self):
                                self.result = False
                                self.current = math.sinh(math.radians(float(txtDisplay.get())))
                                self.display(self.current)

                            def log(self):
                                self.result = False
                                self.current = math.log(float(txtDisplay.get()))
                                self.display(self.current)

                            def exp(self):
                                self.result = False
                                self.current = math.exp(float(txtDisplay.get()))
                                self.display(self.current)

                            def acosh(self):
                                self.result = False
                                self.current = math.acosh(float(txtDisplay.get()))
                                self.display(self.current)

                            def asinh(self):
                                self.result = False
                                self.current = math.asinh(float(txtDisplay.get()))
                                self.display(self.current)

                            def expm1(self):
                                self.result = False
                                self.current = math.expm1(float(txtDisplay.get()))
                                self.display(self.current)

                            def lgamma(self):
                                self.result = False
                                self.current = math.lgamma(float(txtDisplay.get()))
                                self.display(self.current)

                            def degrees(self):
                                self.result = False
                                self.current = math.degrees(float(txtDisplay.get()))
                                self.display(self.current)

                            def log2(self):
                                self.result = False
                                self.current = math.log2(float(txtDisplay.get()))
                                self.display(self.current)

                            def log10(self):
                                self.result = False
                                self.current = math.log10(float(txtDisplay.get()))
                                self.display(self.current)

                            def log1p(self):
                                self.result = False
                                self.current = math.log1p(float(txtDisplay.get()))
                                self.display(self.current)

                        added_value = Calc()

                        txtDisplay = Entry(calc, font=('Verdana', 20, 'bold'),
                                           bg='white', fg='black', bd=3,
                                           width=15, justify=RIGHT)
                        txtDisplay.grid(row=0, column=0, columnspan=4)
                        txtDisplay.insert(0, "0")

                        numberpad = "789456123"
                        i = 0
                        btn = []
                        for j in range(2, 5):
                            for k in range(3):
                                btn.append(Button(calc, width=6, height=2,
                                                  bg='black', fg='white',
                                                  font=('Verdana', 12, 'bold'),
                                                  text=numberpad[i]))
                                btn[i].grid(row=j, column=k, pady=1)
                                btn[i]["command"] = lambda x=numberpad[i]: added_value.numberEnter(x)
                                i += 1

                        btnClear = Button(calc, text=chr(67), width=3,
                                          height=1, bg='powder blue',
                                          font=('Verdana', 20, 'bold'), padx=5
                                          , command=added_value.Clear_Entry
                                          ).grid(row=1, column=0)

                        btnAllClear = Button(calc, text=chr(67) + chr(69),
                                             width=3, height=1,
                                             bg='powder blue',
                                             font=('Verdana', 20, 'bold'), padx=5,
                                             command=added_value.All_Clear_Entry
                                             ).grid(row=1, column=1)

                        btnsq = Button(calc, text="\u221A", width=3, height=1,
                                       bg='powder blue', font=('Verdana',
                                                               20, 'bold'), padx=5,
                                       command=added_value.squared
                                       ).grid(row=1, column=2)

                        btnAdd = Button(calc, text="+", width=3, height=1,
                                        bg='powder blue',
                                        font=('Veradana', 19, 'bold'), padx=6, pady=2,
                                        command=lambda: added_value.operation("add")
                                        ).grid(row=1, column=3)

                        btnSub = Button(calc, text="-", width=4,
                                        height=1, bg='powder blue',
                                        font=('Veradana', 0, 'bold'), padx=4, pady=5,
                                        command=lambda: added_value.operation("sub")
                                        ).grid(row=2, column=3)

                        btnMul = Button(calc, text="x", width=3,
                                        height=1, bg='powder blue',
                                        font=('Verdana', 16, 'bold'), padx=6, pady=4,
                                        command=lambda: added_value.operation("multi")
                                        ).grid(row=3, column=3)

                        btnDiv = Button(calc, text="/", width=3,
                                        height=1, bg='powder blue',
                                        font=('Verdana', 16, 'bold'), padx=6, pady=4,
                                        command=lambda: added_value.operation("divide")
                                        ).grid(row=4, column=3)

                        btnZero = Button(calc, text="0", width=6,
                                         height=3, bg='black', fg='white',
                                         font=('Verdana', 12, 'bold'),
                                         command=lambda: added_value.numberEnter(0)
                                         ).grid(row=5, column=0)

                        btnDot = Button(calc, text=".", width=3,
                                        height=1, bg='powder blue',
                                        font=('Verdana', 16, 'bold'), pady=13, padx=10,
                                        command=lambda: added_value.numberEnter(".")
                                        ).grid(row=5, column=1)

                        btnPM = Button(calc, text=chr(177), width=3,
                                       height=1, bg='powder blue', pady=13, padx=10, font=('Verdana', 16, 'bold'),
                                       command=added_value.mathPM
                                       ).grid(row=5, column=2)

                        btnEquals = Button(calc, text="=", width=3,
                                           height=1, bg='powder blue',
                                           font=('Verdana', 16, 'bold'), pady=13, padx=8,
                                           command=added_value.sum_of_total
                                           ).grid(row=5, column=3)
                        # ROW 1 :
                        btnPi = Button(calc, text="pi", width=3,
                                       height=1, bg='black', fg='white',
                                       font=('Verdana', 16), padx=10, pady=4,
                                       command=added_value.pi
                                       ).grid(row=1, column=4)

                        btnCos = Button(calc, text="cos", width=3,
                                        height=1, bg='black', fg='white',
                                        font=('Verdana', 16), padx=10, pady=4,
                                        command=added_value.cos
                                        ).grid(row=1, column=5)

                        btntan = Button(calc, text="tan", width=3,
                                        height=1, bg='black', fg='white',
                                        font=('Verdana', 16), padx=10, pady=4,
                                        command=added_value.tan
                                        ).grid(row=1, column=6)

                        btnsin = Button(calc, text="sin", width=3,
                                        height=1, bg='black', fg='white',
                                        font=('Verdana', 16), padx=10, pady=4,
                                        command=added_value.sin
                                        ).grid(row=1, column=7)

                        # ROW 2 :
                        btn2Pi = Button(calc, text="2pi", width=3,
                                        height=1, bg='black', fg='white',
                                        font=('Verdana', 16), padx=10, pady=4,
                                        command=added_value.tau
                                        ).grid(row=2, column=4)

                        btnCosh = Button(calc, text="cosh", width=3,
                                         height=1, bg='black', fg='white',
                                         font=('Verdana', 16), padx=10, pady=4,
                                         command=added_value.cosh
                                         ).grid(row=2, column=5)

                        btntanh = Button(calc, text="tanh", width=3,
                                         height=1, bg='black', fg='white',
                                         font=('Verdana', 16), padx=10, pady=4,
                                         command=added_value.tanh
                                         ).grid(row=2, column=6)

                        btnsinh = Button(calc, text="sinh", width=3,
                                         height=1, bg='black', fg='white',
                                         font=('Verdana', 16), padx=10, pady=4,
                                         command=added_value.sinh
                                         ).grid(row=2, column=7)

                        # ROW 3 :
                        btnlog = Button(calc, text="log", width=3,
                                        height=1, bg='black', fg='white',
                                        font=('Verdana', 16), padx=10, pady=4,
                                        command=added_value.log
                                        ).grid(row=3, column=4)

                        btnExp = Button(calc, text="exp", width=3, height=1,
                                        bg='black', fg='white',
                                        font=('Verdana', 16), padx=10, pady=4,
                                        command=added_value.exp
                                        ).grid(row=3, column=5)

                        btnMod = Button(calc, text="Mod", width=3,
                                        height=1, bg='black', fg='white',
                                        font=('Verdana', 16), padx=10, pady=4,
                                        command=lambda: added_value.operation("mod")
                                        ).grid(row=3, column=6)

                        btnE = Button(calc, text="e", width=3,
                                      height=1, bg='black', fg='white',
                                      font=('Verdanaa', 16), padx=10, pady=4,
                                      command=added_value.e
                                      ).grid(row=3, column=7)

                        # ROW 4 :
                        btnlog10 = Button(calc, text="log10", width=3,
                                          height=1, bg='black', fg='white',
                                          font=('Verdana', 16), padx=10, pady=4,
                                          command=added_value.log10
                                          ).grid(row=4, column=4)

                        btncos = Button(calc, text="log1p", width=3,
                                        height=1, bg='black', fg='white',
                                        font=('Verdana', 15), padx=10, pady=4,
                                        command=added_value.log1p
                                        ).grid(row=4, column=5)

                        btnexpm1 = Button(calc, text="expm1", width=3,
                                          height=1, bg='black', fg='white',
                                          font=('Verdana', 14), padx=10, pady=8,
                                          command=added_value.expm1
                                          ).grid(row=4, column=6)

                        btngamma = Button(calc, text="gamma", width=3,
                                          height=1, bg='black', fg='white',
                                          font=('Verdana', 12), padx=12, pady=12,
                                          command=added_value.lgamma
                                          ).grid(row=4, column=7)
                        # ROW 5 :
                        btnlog2 = Button(calc, text="log2", width=3,
                                         height=1, bg='black', fg='white',
                                         font=('Verdana', 16), padx=10, pady=4,
                                         command=added_value.log2
                                         ).grid(row=5, column=4, pady=1)

                        btndeg = Button(calc, text="deg", width=3,
                                        height=1, bg='black', fg='white',
                                        font=('Verdana', 16), padx=10, pady=4,
                                        command=added_value.degrees
                                        ).grid(row=5, column=5, pady=1)

                        btnacosh = Button(calc, text="acosh", width=3,
                                          height=1, bg='black', fg='white',
                                          font=('Verdana', 16), padx=10, pady=4,
                                          command=added_value.acosh
                                          ).grid(row=5, column=6, pady=1)

                        btnasinh = Button(calc, text="asinh", width=3,
                                          height=1, bg='black', fg='white',
                                          font=('Verdana', 16), padx=10, pady=4,
                                          command=added_value.asinh
                                          ).grid(row=5, column=7, pady=1)

                        lblDisplay = Label(calc, text="Scientific Calculator",
                                           font=('Verdana', 24, 'underline'),
                                           bg='black', fg='white', justify=CENTER)

                        lblDisplay.grid(row=0, column=4, columnspan=4)

                        def iExit():
                            iExit = tkinter.messagebox.askyesno("Scientific Calculator",
                                                                "Do you want to exit ?")
                            if iExit > 0:
                                root2.destroy()
                                return

                        def Scientific():
                            root2.resizable(width=False, height=False)
                            root2.geometry("944x568+0+0")

                        def Standard():
                            root2.resizable(width=False, height=False)
                            root2.geometry("480x568+0+0")

                        menubar = Menu(calc)

                        # ManuBar 1 :
                        filemenu = Menu(menubar, tearoff=0)
                        menubar.add_cascade(label='File', menu=filemenu)
                        filemenu.add_command(label="Standard", command=Standard)
                        filemenu.add_command(label="Scientific", command=Scientific)
                        filemenu.add_separator()
                        filemenu.add_command(label="Exit", command=iExit)

                        # ManuBar 2 :
                        editmenu = Menu(menubar, tearoff=0)
                        menubar.add_cascade(label='Edit', menu=editmenu)
                        editmenu.add_command(label="Cut")
                        editmenu.add_command(label="Copy")
                        editmenu.add_separator()
                        editmenu.add_command(label="Paste")

                        root2.config(menu=menubar)

                        root2.mainloop()

                    def lab1():

                        class Notepad:
                            __root = Toplevel()

                            # default window width and height
                            __thisWidth = 300
                            __thisHeight = 300
                            __thisTextArea = Text(__root)
                            __thisMenuBar = Menu(__root)
                            __thisFileMenu = Menu(__thisMenuBar, tearoff=0)
                            __thisEditMenu = Menu(__thisMenuBar, tearoff=0)
                            __thisHelpMenu = Menu(__thisMenuBar, tearoff=0)

                            # To add scrollbar
                            __thisScrollBar = Scrollbar(__thisTextArea)
                            __file = None

                            def __init__(self, **kwargs):

                                # Set icon
                                try:
                                    self.__root.wm_iconbitmap("Notepad.ico")
                                except:
                                    pass

                                # Set window size (the default is 300x300)

                                try:
                                    self.__thisWidth = kwargs['width']
                                except KeyError:
                                    pass

                                try:
                                    self.__thisHeight = kwargs['height']
                                except KeyError:
                                    pass

                                # Set the window text
                                self.__root.title("Untitled - Notepad")

                                # Center the window
                                screenWidth = self.__root.winfo_screenwidth()
                                screenHeight = self.__root.winfo_screenheight()

                                # For left-alling
                                left = (screenWidth / 2) - (self.__thisWidth / 2)

                                # For right-allign
                                top = (screenHeight / 2) - (self.__thisHeight / 2)

                                # For top and bottom
                                self.__root.geometry('%dx%d+%d+%d' % (self.__thisWidth,
                                                                      self.__thisHeight,
                                                                      left, top))

                                # To make the textarea auto resizable
                                self.__root.grid_rowconfigure(0, weight=1)
                                self.__root.grid_columnconfigure(0, weight=1)

                                # Add controls (widget)
                                self.__thisTextArea.grid(sticky=N + E + S + W)

                                # To open new file
                                self.__thisFileMenu.add_command(label="New",
                                                                command=self.__newFile)

                                # To open a already existing file
                                self.__thisFileMenu.add_command(label="Open",
                                                                command=self.__openFile)

                                # To save current file
                                self.__thisFileMenu.add_command(label="Save",
                                                                command=self.__saveFile)

                                # To create a line in the dialog
                                self.__thisFileMenu.add_separator()
                                self.__thisFileMenu.add_command(label="Exit",
                                                                command=self.__quitApplication)
                                self.__thisMenuBar.add_cascade(label="File",
                                                               menu=self.__thisFileMenu)

                                # To give a feature of cut
                                self.__thisEditMenu.add_command(label="Cut",
                                                                command=self.__cut)

                                # to give a feature of copy
                                self.__thisEditMenu.add_command(label="Copy",
                                                                command=self.__copy)

                                # To give a feature of paste
                                self.__thisEditMenu.add_command(label="Paste",
                                                                command=self.__paste)

                                # To give a feature of editing
                                self.__thisMenuBar.add_cascade(label="Edit",
                                                               menu=self.__thisEditMenu)

                                # To create a feature of description of the notepad
                                self.__thisHelpMenu.add_command(label="About Notepad",
                                                                command=self.__showAbout)
                                self.__thisMenuBar.add_cascade(label="Help",
                                                               menu=self.__thisHelpMenu)

                                self.__root.config(menu=self.__thisMenuBar)

                                self.__thisScrollBar.pack(side=RIGHT, fill=Y)

                                # Scrollbar will adjust automatically according to the content
                                self.__thisScrollBar.config(command=self.__thisTextArea.yview)
                                self.__thisTextArea.config(yscrollcommand=self.__thisScrollBar.set)

                            def __quitApplication(self):
                                self.__root.destroy()
                                # exit()

                            def __showAbout(self):
                                messagebox.showinfo("Notepad", "...")

                            def __openFile(self):

                                self.__file = askopenfilename(defaultextension=".txt",
                                                              filetypes=[("All Files", "*.*"),
                                                                         ("Text Documents", "*.txt")])

                                if self.__file == "":

                                    # no file to open
                                    self.__file = None
                                else:

                                    # Try to open the file
                                    # set the window title
                                    self.__root.title(os.path.basename(self.__file) + " - Notepad")
                                    self.__thisTextArea.delete(1.0, END)

                                    file = open(self.__file, "r")

                                    self.__thisTextArea.insert(1.0, file.read())

                                    file.close()

                            def __newFile(self):
                                self.__root.title("Untitled - Notepad")
                                self.__file = None
                                self.__thisTextArea.delete(1.0, END)

                            def __saveFile(self):

                                if self.__file == None:
                                    # Save as new file
                                    self.__file = asksaveasfilename(initialfile='Untitled.txt',
                                                                    defaultextension=".txt",
                                                                    filetypes=[("All Files", "*.*"),
                                                                               ("Text Documents", "*.txt")])

                                    if self.__file == "":
                                        self.__file = None
                                    else:

                                        # Try to save the file
                                        file = open(self.__file, "w")
                                        file.write(self.__thisTextArea.get(1.0, END))
                                        file.close()

                                        # Change the window title
                                        self.__root.title(os.path.basename(self.__file) + " - Notepad")


                                else:
                                    file = open(self.__file, "w")
                                    file.write(self.__thisTextArea.get(1.0, END))
                                    file.close()

                            def __cut(self):
                                self.__thisTextArea.event_generate("<<Cut>>")

                            def __copy(self):
                                self.__thisTextArea.event_generate("<<Copy>>")

                            def __paste(self):
                                self.__thisTextArea.event_generate("<<Paste>>")

                            def run(self):

                                # Run main application
                                self.__root.mainloop()

                            # Run main application

                        notepad = Notepad(width=600, height=400)
                        notepad.run()

                    def lab2():
                        window = Toplevel()
                        # set title for window
                        window.title("Python IDE")
                        # create and configure menu
                        menu = Menu(window)
                        window.config(menu=menu)
                        # create editor window for writing code
                        editor = ScrolledText(window, font=("Verdana 10 bold"), wrap=None)
                        editor.pack(fill=BOTH, expand=1)
                        editor.focus()
                        file_path = ""

                        # function to open files
                        def open_file(event=None):
                            global code, file_path
                            # code = editor.get(1.0, END)
                            open_path = askopenfilename(filetypes=[("Python File", "*.py")])
                            file_path = open_path
                            with open(open_path, "r") as file:
                                code = file.read()
                                editor.delete(1.0, END)
                                editor.insert(1.0, code)

                        window.bind("<Control-o>", open_file)

                        # function to save files
                        def save_file(event=None):
                            global code, file_path
                            if file_path == '':
                                save_path = asksaveasfilename(defaultextension=".py",
                                                              filetypes=[("Python File", "*.py")])
                                file_path = save_path
                            else:
                                save_path = file_path
                            with open(save_path, "w") as file:
                                code = editor.get(1.0, END)
                                file.write(code)

                        window.bind("<Control-s>", save_file)

                        # function to save files as specific name
                        def save_as(event=None):
                            global code, file_path
                            # code = editor.get(1.0, END)
                            save_path = asksaveasfilename(defaultextension=".py", filetypes=[("Python File", "*.py")])
                            file_path = save_path
                            with open(save_path, "w") as file:
                                code = editor.get(1.0, END)
                                file.write(code)

                        window.bind("<Control-S>", save_as)

                        # function to execute the code and
                        # display its output
                        def run(event=None):
                            global code, file_path
                            '''
                            code = editor.get(1.0, END)
                            exec(code)
                            '''
                            cmd = f"python (file_path)"
                            process = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                                                       stderr=subprocess.PIPE, shell=True)
                            output, error = process.communicate()
                            # delete the previous text from
                            # output_windows
                            output_window.delete(1.0, END)
                            # insert the new output text in
                            # output_windows
                            output_window.insert(1.0, output)
                            # insert the error text in output_windows
                            # if there is error
                            output_window.insert(1.0, error)

                        window.bind("<F5>", run)

                        # function to close IDE window
                        def close(event=None):
                            window.destroy()

                        window.bind("<Control-q>", close)

                        # define function to cut
                        # the selected text
                        def cut_text(event=None):
                            editor.event_generate(("<<Cut>>"))

                        # define function to copy
                        # the selected text
                        def copy_text(event=None):
                            editor.event_generate(("<<Copy>>"))

                        # define function to paste
                        # the previously copied text
                        def paste_text(event=None):
                            editor.event_generate(("<<Paste>>"))

                        # create menus
                        file_menu = Menu(menu, tearoff=0)
                        edit_menu = Menu(menu, tearoff=0)
                        run_menu = Menu(menu, tearoff=0)
                        view_menu = Menu(menu, tearoff=0)
                        theme_menu = Menu(menu, tearoff=0)
                        # add menu labels
                        menu.add_cascade(label="File", menu=file_menu)
                        menu.add_cascade(label="Edit", menu=edit_menu)
                        menu.add_cascade(label="Run", menu=run_menu)
                        menu.add_cascade(label="View", menu=view_menu)
                        menu.add_cascade(label="Theme", menu=theme_menu)
                        # add commands in flie menu
                        file_menu.add_command(label="Open", accelerator="Ctrl+O", command=open_file)
                        file_menu.add_separator()
                        file_menu.add_command(label="Save", accelerator="Ctrl+S", command=save_file)
                        file_menu.add_command(label="Save As", accelerator="Ctrl+Shift+S", command=save_as)
                        file_menu.add_separator()
                        file_menu.add_command(label="Exit", accelerator="Ctrl+Q", command=close)
                        # add commands in edit menu
                        edit_menu.add_command(label="Cut", command=cut_text)
                        edit_menu.add_command(label="Copy", command=copy_text)
                        edit_menu.add_command(label="Paste", command=paste_text)
                        run_menu.add_command(label="Run", accelerator="F5", command=run)
                        # function to display and hide status bar
                        show_status_bar = BooleanVar()
                        show_status_bar.set(True)

                        def hide_statusbar():
                            global show_status_bar
                            if show_status_bar:
                                status_bars.pack_forget()
                                show_status_bar = False
                            else:
                                status_bars.pack(side=BOTTOM)
                                show_status_bar = True

                        view_menu.add_checkbutton(label="Status Bar", onvalue=True, offvalue=0,
                                                  variable=show_status_bar,
                                                  command=hide_statusbar)
                        # create a label for status bar
                        status_bars = ttk.Label(window, text="www.codershubb.com \t\t\t\t\t\t characters: 0 words: 0")
                        status_bars.pack(side=BOTTOM)
                        # function to display count and word characters
                        text_change = False

                        def change_word(event=None):
                            global text_change
                            if editor.edit_modified():
                                text_change = True
                                word = len(editor.get(1.0, "end-1c").split())
                                chararcter = len(editor.get(1.0, "end-1c").replace(" ", ""))
                                status_bars.config(
                                    text=f"www.codershubb.com \t\t\t\t\t\t characters: {chararcter} words: {word}")
                            editor.edit_modified(False)

                        editor.bind("<<Modified>>", change_word)

                        # function for light mode window
                        def light():
                            editor.config(bg="white")
                            output_window.config(bg="white")

                        # function for dark mode window
                        def dark():
                            editor.config(fg="white", bg="black")
                            output_window.config(fg="white", bg="black")

                        # add commands to change themes
                        theme_menu.add_command(label="light", command=light)
                        theme_menu.add_command(label="dark", command=dark)
                        # create output window to display output of written code
                        output_window = ScrolledText(window, height=10)
                        output_window.pack(fill=BOTH, expand=1)
                        window.mainloop()

                    b1 = Button(master, text="Notepad", padx=7, bg="#2e0000", fg="white", command=lab1)
                    b1.pack()
                    b2 = Button(master, text="Python IDE", bg="#2e0000", fg="white", command=lab2)
                    b2.pack()
                    b3 = Button(master, text="Calculator", padx=3, bg="#2e0000", fg="white", command=calc)
                    b3.pack()

                b5 = Button(q, text="VIRTUAL LAB", command=lab, fg="white", bg="#2e0000", padx=3)
                b5.pack(padx=10)

                def result():
                    y = Toplevel(q)
                    y.title("RESULT")
                    y.geometry("400x200")
                    y.config(bg="#dec8ab")
                    l = Label(y, text="RESULT", bg="#dec8ab", font="Verdana 10 underline")
                    l.grid(row=0, column=1)
                    l1 = Label(y, text="University_rno", bg="#dec8ab")
                    l1.grid(row=1, column=0)
                    t1 = Entry(y)
                    t1.grid(row=1, column=1)
                    l2 = Label(y, text="Branch", bg="#dec8ab")
                    l2.grid(row=1, column=2)
                    x = StringVar()
                    v1 = ["CSE", "IT", "AUTOMOBILE", "MINING", "EEE"]
                    c1 = OptionMenu(y, x, *v1)
                    c1.grid(row=1, column=3)
                    l3 = Label(y, text="Select", bg="#dec8ab")
                    l3.grid(row=2, column=0)
                    y1 = StringVar()
                    v2 = ["MCQ", "Assignment"]
                    c2 = OptionMenu(y, y1, *v2)
                    c2.grid(row=2, column=1)
                    l4 = Label(y, text="Sem", bg="#dec8ab")
                    l4.grid(row=2, column=2)
                    y2 = IntVar()
                    v3 = []
                    for i in range(1, 9):
                        v3.append(i)
                    c3 = OptionMenu(y, y2, *v3)
                    c3.grid(row=2, column=3)
                    l4 = Label(y,text="Subject",bg="#dec8ab")
                    l4.grid(row=3,column=0)
                    l5 = Label(y,text="Marks",bg="#dec8ab")
                    l5.grid(row=3,column=1)

                    # def go1():
                    #     a = t1.get()
                    #     b = x.get()
                    #     c = y1.get()
                    #     d = y2.get()
                    #     db = pymysql.connect(host='localhost',user='root',password='stuart@2002',db='hackathon')
                    #     sql = "select * from result where "

                    b = Button(y, text="go", bg="green", fg="white")
                    b.grid(row=2, column=4)



                    # b1 = Button(y, text="Exit", fg="white", bg="red", command=exit)
                    # b1.grid(row=7, column=0)

                b6 = Button(q, text="RESULT", fg="white", padx=18, bg="#2e0000", command=result)
                b6.pack(padx=10)

            b2 = Button(d,text="ACTIVITY",bg="#2e0000",fg="white",command=activity)
            b2.pack()

    b = Button(m, text="LOGIN", fg="white", bg="green",command=check)
    b.grid(row=3, column=1)


#CREATE ACCOUNT
    def ca():
            c = Toplevel()
            c.title("CREATE ACCOUNT")
            c.geometry("400x200")
            c.config(bg="#dec8ab")
            l = Label(c, text="CREATE ACCOUNT", bg="#dec8ab", font="Verdana 10 underline")
            l.grid(row=0, column=1)
            l1 = Label(c, text="Roll_no", bg="#dec8ab")
            l1.grid(row=1, column=0)
            t1 = Entry(c)
            t1.grid(row=1, column=1)
            l2 = Label(c, text="Student_name", bg="#dec8ab")
            l2.grid(row=2, column=0)
            t2 = Entry(c)
            t2.grid(row=2, column=1)
            l3 = Label(c, text="Contact_no", bg="#dec8ab")
            l3.grid(row=3, column=0)
            t3 = Entry(c)
            t3.grid(row=3, column=1)
            l4 = Label(c, text="E-mail", bg="#dec8ab")
            l4.grid(row=4, column=0)
            t4 = Entry(c)
            t4.grid(row=4,column=1)
            l5 = Label(c,text="Branch", bg ="#dec8ab")
            l5.grid(row=5,column=0)
            x  = StringVar()
            v1 = ["CSE", "IT", "MECH"]
            c1 = OptionMenu(c, x, *v1)
            c1.grid(row=5, column=1)
            l6 = Label(c, text="Semester", bg="#dec8ab")
            l6.grid(row=5, column=2)
            y = IntVar()
            v2 = []
            for i in range(1,9):
                v2.append(i)
            c2 = OptionMenu(c, y, *v2)
            c2.grid(row=5, column=3)
            def stuca():
                a = t1.get()
                b = t2.get()
                c = t3.get()
                d = t4.get()
                e = x.get()
                f = y.get()
                db = pymysql.connect(host="localhost", user="root", password="stuart@2002", db="hackathon")
                if a == "" or b == "" or c == "" or d == "" or a.isdigit() is False or c.isdigit() is False:
                    messagebox.showwarning("", "Enter valid values!")
                else:
                    sql = "insert into student values (%s,%s,%s,%s,%s,%s)"
                    val = (a, b, c, d, e, f)
                    cur = db.cursor()
                    cur.execute(sql, val)
                    db.commit()
                    messagebox.showinfo("Success", "Account created successfully.")


            b = Button(c, text="register", fg="white", bg="green", command=stuca)
            b.grid(row=6, column=1)

    b1 = Button(m, text="create account", fg="white", bg="blue", command=ca)
    b1.grid(row=3, column=0)

b1 = Button(text="ADMIN", fg="white", bg="#2e0000", padx=6, command=admin)
b1.pack()
b2 = Button(text="FACULTY", fg="white", bg="#2e0000", command=faculty)
b2.pack()
b3 = Button(text="STUDENT", fg="white", bg="#2e0000", command=student)
b3.pack()
mainloop()