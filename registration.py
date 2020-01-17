from tkinter import Tk, StringVar,ttk
from tkinter import *

import time;
import datetime
import tkinter.messagebox
import sqlite3
#from flask import Flask,render_template,flash,url_for,redirect,session
import os
#from WTForms import Form,BooleanFiled,TextField,passwordFiled,validators
#from Passlib.hash import escape_string as thwart
import gc
#####------------------creating a window---------------------------####3-----------------------------------------
root=Tk()
root.title("BHSBIET")
root.geometry('2050x1050+0+15')
root.configure(background='STEELBLUE')


####-------------------FRAMES---------------------------------######---------------------------------

LeftMayFrame=Frame(root,width=1000,height=650,bd=8,relief="raise")
LeftMayFrame.pack(side=LEFT)

RightMayFrame=Frame(root,width=350,height=650,bd=8,relief="raise")
RightMayFrame.pack(side=RIGHT)


LeftMayFrame1=Frame(LeftMayFrame,width=10000,height=100,bd=7,relief="raise")
LeftMayFrame1.pack(side=TOP)
LeftMayFrame2=Frame(LeftMayFrame,width=10000,height=550,bd=7,relief="raise")
LeftMayFrame2.pack(side=TOP)


RightMayFrame3=Frame(RightMayFrame,width=350,height=215,bd=7,relief="raise")
RightMayFrame3.pack(side=TOP)
RightMayFrame2=Frame(RightMayFrame,width=350,height=415,bd=7,relief="raise")
RightMayFrame2.pack(side=TOP)


#######---------------------------variables for entry--------##### -------------------------######3    -------------------------
######------------------------creating database------------------------######-----------------------------------------------
var = IntVar()
Student_Name = StringVar()
Name_Of_Program = StringVar()
Name_of_department = StringVar()
var1 = IntVar()
phon = StringVar()
reg = StringVar()
date = StringVar()
aadhar = StringVar()
amount = StringVar()
trans = StringVar()

def database():
    S = var.get()
    NProgram = Name_Of_Program.get()
    Sname = Student_Name.get()
    Ndepartment = Name_of_department.get()
    SStudent = var1.get()
    phone = phon.get()
    regi = reg.get()
    datee = date.get() 
    aadharr = aadhar.get()
    pamount = amount.get()
    transn = trans.get()
    conn=sqlite3.connect("lal.db")
    # prepare cursor object using cursor method
    with conn:
        cursor=conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS STUDENTS (Semester TEXT,Program TEXT,Student_Name TEXT,Department TEXT,Status_student TEXT,\
PHONE_NO TEXT, REG_NO TEXT, DATE TEXT, AADHAR TEXT, FEE_AMOUNT TEXT, PAYMENT_ID TEXT)')
    cursor.execute('INSERT INTO STUDENTS(Semester,Program,Student_Name,Department,Status_student, PHONE_NO,REG_NO,DATE,AADHAR,FEE_AMOUNT,PAYMENT_ID) VALUES(?,?,?,?,?,?,?,?,?,?,?)'
                   ,(S,NProgram,Sname,Ndepartment,SStudent,phone,regi,datee,aadharr, pamount, transn ))
    conn.commit()
    conn.close()
        # disconnect from server
















DateofOrder=StringVar()
value0 = StringVar()
value1 = StringVar()
value2 = StringVar()
value3 = StringVar()
value4 = StringVar()
value5 = StringVar()
value6 = StringVar()
value7 = StringVar()
value8 = StringVar()
value9 = StringVar()
value10 = StringVar()
value11 = StringVar()
value12 = StringVar()
value13 = StringVar()
value14 = StringVar()
value15 = StringVar()
value16 = StringVar()
value17 = StringVar()
value18 = StringVar()
value19 = StringVar()
var1=IntVar()
#####----------------------------variables for radio buttons------#####-------------------------------##############---------------------------
radio0=tkinter.IntVar()
radio0.set(1)



####-----------------------------labels -----##########33--------------------------############----------------------------
lblno=Label(LeftMayFrame1,font=('arial',13,'bold'),text="BABA HIRA SINGH BHATTAL INSTITUTE OF ENGINEERING AND TECHNOLOGY\n(ESTABLISH BY: GOVT OF INDIA,DEEMED UNVERSITY)",bd=19)
lblno.grid(row=0,column=0,sticky=S)

#img=ImageTk.PhotoImage(Image.open('logo.gif'))
#panel=tk.label(LeftMayFrame1,image=img)
#panel.grid(row=0,column=0)

#lblno.grid(row=0,column=0,sticky=S)





lblno1=Label(LeftMayFrame2,font=('arial',8,'bold'),text='Semester',bd=9)
lblno1.grid(row=0,column=0,sticky=W)

box=ttk.Combobox(LeftMayFrame2,textvariable=var)
box['values']=('--SELECT--','1','2','3','4','5',"6","7",'8')
box.current(0)
box.grid(row=0,column=1,sticky=W)

#lblno1=tkinter.Entry(LeftMayFrame2,width=25)
#lblno1.grid(row=0,column=1,sticky=W)


lblno2=Label(LeftMayFrame2,font=('arial',8,'bold'),text='Name_Of_Program',bd=9)
lblno2.grid(row=1,column=0,sticky=W)


box=ttk.Combobox(LeftMayFrame2,textvariable=Name_Of_Program)
box['values']=('SELECT-','B.E-2k14',"B.E-2k15","B.E-2k16",'B.E-2k17','B.E-2k18','B.E-2k19')
box.current(0)
box.grid(row=1,column=1,sticky=W)


#lblno2=tkinter.Entry(LeftMayFrame2,width=25)
#lblno2.grid(row=1,column=1,sticky=W)




lblno3=Label(LeftMayFrame2,font=('arial',8,'bold'),text="Name_of_department",bd=9)
lblno3.grid(row=0,column=2,sticky=W)


box=ttk.Combobox(LeftMayFrame2,textvariable=Name_of_department)
box['values']=("-SELECT","GCS","GEC","GME","GINC")
box.current(0)
box.grid(row=0,column=3,sticky=W)

#lblno3=tkinter.Entry(LeftMayFrame2,width=25)
#lblno3.grid(row=0,column=3,sticky=W)



lblno4=Label(LeftMayFrame2,font=('arial',8,'bold'),text="Status_of_student",bd=9)
lblno4.grid(row=1,column=2,sticky=W)



#box=ttk.Combobox(LeftMayFrame2,textvariable=value17,state="readyonly")
#box['values']=('-SELECT-','Hosteller','Day-scholar')
#box.current(0)
#box.grid(row=1,column=3,sticky=W)



#radio0=tkinter.
#lable4=
Radiobutton(LeftMayFrame2, text="Hosteller",padx = 5, variable=var1,value='1').place(x=705,y=40)
#radio0.grid(row=1,column=2)
#radio0=tkinter.
#label4=
Radiobutton(LeftMayFrame2, text="D-scholer",padx = 20, variable=var1,value='2').place(x=780,y=40)
#radio1.grid(row=1,column=3)


#radio0=tkinter.Radiobutton(LeftMayFrame2,text="Day scholar",variable=radio0,value=2)
#radio0.grid(row=1,column=4,sticky=W)

#lblno4=tkinter.Entry(LeftMayFrame2,width=25)
#lblno4.grid(row=1,column=3,sticky=W)


lblno5=Label(LeftMayFrame2,font=('arial',8,'bold'),text='Student_Name',bd=9)
lblno5.grid(row=2,column=0,sticky=W)

lblno5=tkinter.Entry(LeftMayFrame2,width=25,textvariable=Student_Name)
lblno5.grid(row=2,column=1,sticky=W)



lblno6=Label(LeftMayFrame2,font=('arial',8,'bold'),text="Date_of_Registration",bd=9)
lblno6.grid(row=2,column=2,sticky=W)

lblno6=tkinter.Entry(LeftMayFrame2,width=25,textvariable=date)
lblno6.grid(row=2,column=3,sticky=W)


lblno7=Label(LeftMayFrame2,font=('arial',8,'bold'),text="Contact_no",bd=9)
lblno7.grid(row=3,column=0,sticky=W)

lblno7=tkinter.Entry(LeftMayFrame2,width=25,textvariable=phon)
lblno7.grid(row=3,column=1,sticky=W)

#phone= lblno7

#if re.search('\w{3}-\w{3}-\w{4}',lblno7):
    #print ('yeah this is a phone number')




lblno8=Label(LeftMayFrame2,font=('arial',8,'bold'),text="Aadhar_no",bd=9)
lblno8.grid(row=3,column=2,sticky=W)


lblno8=tkinter.Entry(LeftMayFrame2,width=25,textvariable=aadhar)
lblno8.grid(row=3,column=3,sticky=W)



lblno9=Label(LeftMayFrame2,font=('arial',8,'bold'),text="Registration_no",bd=9)
lblno9.grid(row=4,column=0,sticky=W)

lblno9=tkinter.Entry(LeftMayFrame2,width=25,textvariable=reg)
lblno9.grid(row=4,column=1,sticky=W)
#------------------------------------------------------------------------------------------------------
lblno10=Label(LeftMayFrame2,font=('arial',11,'bold'),text="DETAILS OF FEES DEPOSITED",bd=17)
lblno10.grid(row=5,column=1,sticky=W)


lblno11=Label(LeftMayFrame2,font=('arial',8,'bold'),text='Amount paid',bd=9)
lblno11.grid(row=6,column=0,sticky=W)


lblno11=tkinter.Entry(LeftMayFrame2,width=25,textvariable=amount)
lblno11.grid(row=6,column=1,sticky=W)


lblno12=Label(LeftMayFrame2,font=('arial',8,'bold'),text="Transaction no",bd=9)
lblno12.grid(row=6,column=2,sticky=W)


lblno12=tkinter.Entry(LeftMayFrame2,width=25,textvariable=trans)
lblno12.grid(row=6,column=3,sticky=W)




lblno13=Label(LeftMayFrame2,font=('arial',8,'bold'),text="Payment by",bd=9)
lblno13.grid(row=7,column=0,sticky=W)


box=ttk.Combobox(LeftMayFrame2,textvariable=value1)
box['values']=('-SELECT-','Cash','Transfer',"Debit card","Credit card",'Net-banking')
box.current(0)
box.grid(row=7,column=1,sticky=W)

######--------------------------------------##################------------------------------------------##################
lblno14=Label(LeftMayFrame2,font=('arial',11,'bold'),text="Details of Course For Which in Regular semester(Core subject).",bd=9)
lblno14.grid(row=8,column=1,sticky=W)

#lblno4=tkinter.Entry(LeftMayFrame2,width=25)
#lblno4.grid(row=1,column=3,sticky=W)


lblno15=Label(LeftMayFrame2,font=('arial',8,'bold'),text="SNO",bd=9)
lblno15.grid(row=9,column=0,sticky=W)

#lblno5=tkinter.Entry(LeftMayFrame2,width=25)
#lblno5.grid(row=2,column=1,sticky=W)



lblno16=Label(LeftMayFrame2,font=('arial',8,'bold'),text="Subject",bd=9)
lblno16.grid(row=9,column=1,sticky=W)

#lblno6=tkinter.Entry(LeftMayFrame2,width=25)
#lblno6.grid(row=2,column=3,sticky=W)


lblno17=Label(LeftMayFrame2,font=('arial',8,'bold'),text="Code",bd=9)
lblno17.grid(row=9,column=2,sticky=W)

#lblno7=tkinter.Entry(LeftMayFrame2,width=25)
#lblno7.grid(row=3,column=1,sticky=W)



lblno18=Label(LeftMayFrame2,font=('arial',8,'bold'),text="Credit:",bd=9)
lblno18.grid(row=9,column=3,sticky=W)


#lblno8=tkinter.Entry(LeftMayFrame2,width=25)
#lblno8.grid(row=3,column=3,sticky=W)

####----------------------------------------------#########---------------------------------------------------------------

lblno19=Label(LeftMayFrame2,font=('arial',8,'bold'),text="1",bd=9)
lblno19.grid(row=10,column=0,sticky=W)

#lblno5=tkinter.Entry(LeftMayFrame2,width=25)
#lblno5.grid(row=2,column=1,sticky=W)



#lblno20=Label(LeftMayFrame2,font=('arial',10,'bold'),text="Subject",bd=9)
#lblno20.grid(row=10,column=1,sticky=W)

lblno20=tkinter.Entry(LeftMayFrame2,width=55)
lblno20.grid(row=10,column=1,sticky=W)


#lblno17=Label(LeftMayFrame2,font=('arial',10,'bold'),text="Code",bd=9)
#lblno17.grid(row=9,column=2,sticky=W)

lblno21=tkinter.Entry(LeftMayFrame2,width=10)
lblno21.grid(row=10,column=2,sticky=W)



#lblno18=Label(LeftMayFrame2,font=('arial',10,'bold'),text="Credit:",bd=9)
#lblno18.grid(row=9,column=3,sticky=W)


#lblno22=tkinter.Entry(LeftMayFrame2,width=10)
#lblno22.grid(row=10,column=3,sticky=W)

box=ttk.Combobox(LeftMayFrame2,textvariable=value3,state="readyonly")
box['values']=('-Select-','0',"1","2",'3','4','5')
box.current(0)
box.grid(row=10,column=3,sticky=W)
###---------------------------------------------------------############-------------------------------------------------
lblno22=Label(LeftMayFrame2,font=('arial',8,'bold'),text="2",bd=9)
lblno22.grid(row=11,column=0,sticky=W)

#lblno5=tkinter.Entry(LeftMayFrame2,width=25)
#lblno5.grid(row=2,column=1,sticky=W)



#lblno20=Label(LeftMayFrame2,font=('arial',10,'bold'),text="Subject",bd=9)
#lblno20.grid(row=10,column=1,sticky=W)

lblno23=tkinter.Entry(LeftMayFrame2,width=55)
lblno23.grid(row=11,column=1,sticky=W)


#lblno17=Label(LeftMayFrame2,font=('arial',10,'bold'),text="Code",bd=9)
#lblno17.grid(row=9,column=2,sticky=W)

lblno24=tkinter.Entry(LeftMayFrame2,width=10)
lblno24.grid(row=11,column=2,sticky=W)



#lblno18=Label(LeftMayFrame2,font=('arial',10,'bold'),text="Credit:",bd=9)
#lblno18.grid(row=9,column=3,sticky=W)


#lblno22=tkinter.Entry(LeftMayFrame2,width=10)
#lblno22.grid(row=10,column=3,sticky=W)

box=ttk.Combobox(LeftMayFrame2,textvariable=value4,state="readyonly")
box['values']=('-SELECT-','0',"1","2",'3','4','5')
box.current(0)
box.grid(row=11,column=3,sticky=W)

#####-------------------------------------------#########3--------------------------------------------------------
lblno25=Label(LeftMayFrame2,font=('arial',8,'bold'),text="3",bd=9)
lblno25.grid(row=12,column=0,sticky=W)

#lblno5=tkinter.Entry(LeftMayFrame2,width=25)
#lblno5.grid(row=2,column=1,sticky=W)



#lblno20=Label(LeftMayFrame2,font=('arial',10,'bold'),text="Subject",bd=9)
#lblno20.grid(row=10,column=1,sticky=W)

lblno26=tkinter.Entry(LeftMayFrame2,width=55)
lblno26.grid(row=12,column=1,sticky=W)


#lblno17=Label(LeftMayFrame2,font=('arial',10,'bold'),text="Code",bd=9)
#lblno17.grid(row=9,column=2,sticky=W)

lblno27=tkinter.Entry(LeftMayFrame2,width=10)
lblno27.grid(row=12,column=2,sticky=W)



#lblno18=Label(LeftMayFrame2,font=('arial',10,'bold'),text="Credit:",bd=9)
#lblno18.grid(row=9,column=3,sticky=W)


#lblno22=tkinter.Entry(LeftMayFrame2,width=10)
#lblno22.grid(row=10,column=3,sticky=W)

box=ttk.Combobox(LeftMayFrame2,textvariable=value5,state="readyonly")
box['values']=('-SELECT-','0',"1","2",'3','4','5')
box.current(0)
box.grid(row=12,column=3,sticky=W)
#####--------------------------------------------------#####-------------------------------------------------------------

lblno28=Label(LeftMayFrame2,font=('arial',8,'bold'),text="4",bd=9)
lblno28.grid(row=13,column=0,sticky=W)

#lblno5=tkinter.Entry(LeftMayFrame2,width=25)
#lblno5.grid(row=2,column=1,sticky=W)



#lblno20=Label(LeftMayFrame2,font=('arial',10,'bold'),text="Subject",bd=9)
#lblno20.grid(row=10,column=1,sticky=W)

lblno29=tkinter.Entry(LeftMayFrame2,width=55)
lblno29.grid(row=13,column=1,sticky=W)


#lblno17=Label(LeftMayFrame2,font=('arial',10,'bold'),text="Code",bd=9)
#lblno17.grid(row=9,column=2,sticky=W)

lblno30=tkinter.Entry(LeftMayFrame2,width=10)
lblno30.grid(row=13,column=2,sticky=W)



#lblno18=Label(LeftMayFrame2,font=('arial',10,'bold'),text="Credit:",bd=9)
#lblno18.grid(row=9,column=3,sticky=W)


#lblno22=tkinter.Entry(LeftMayFrame2,width=10)
#lblno22.grid(row=10,column=3,sticky=W)

box=ttk.Combobox(LeftMayFrame2,textvariable=value6,state="readyonly")
box['values']=('-SELECT-','0',"1","2",'3','4','5')
box.current(0)
box.grid(row=13,column=3,sticky=W)
####-----------------------------------------------------########-----------------------------------------------


lblno31=Label(LeftMayFrame2,font=('arial',8,'bold'),text="5",bd=9)
lblno31.grid(row=14,column=0,sticky=W)

#lblno5=tkinter.Entry(LeftMayFrame2,width=25)
#lblno5.grid(row=2,column=1,sticky=W)



#lblno20=Label(LeftMayFrame2,font=('arial',10,'bold'),text="Subject",bd=9)
#lblno20.grid(row=10,column=1,sticky=W)

lblno32=tkinter.Entry(LeftMayFrame2,width=55)
lblno32.grid(row=14,column=1,sticky=W)


#lblno17=Label(LeftMayFrame2,font=('arial',10,'bold'),text="Code",bd=9)
#lblno17.grid(row=9,column=2,sticky=W)

lblno33=tkinter.Entry(LeftMayFrame2,width=10)
lblno33.grid(row=14,column=2,sticky=W)



#lblno18=Label(LeftMayFrame2,font=('arial',10,'bold'),text="Credit:",bd=9)
#lblno18.grid(row=9,column=3,sticky=W)


#lblno22=tkinter.Entry(LeftMayFrame2,width=10)
#lblno22.grid(row=10,column=3,sticky=W)

box=ttk.Combobox(LeftMayFrame2,textvariable=value7,state="readyonly")
box['values']=('-SELECT-','0',"1","2",'3','4','5')
box.current(0)
box.grid(row=14,column=3,sticky=W)
####--------------------------------###########3-----------------------------------------------------------


lblno34=Label(LeftMayFrame2,font=('arial',8,'bold'),text="6",bd=9)
lblno34.grid(row=15,column=0,sticky=W)

#lblno5=tkinter.Entry(LeftMayFrame2,width=25)
#lblno5.grid(row=2,column=1,sticky=W)



#lblno20=Label(LeftMayFrame2,font=('arial',10,'bold'),text="Subject",bd=9)
#lblno20.grid(row=10,column=1,sticky=W)

lblno35=tkinter.Entry(LeftMayFrame2,width=55)
lblno35.grid(row=15,column=1,sticky=W)


#lblno17=Label(LeftMayFrame2,font=('arial',10,'bold'),text="Code",bd=9)
#lblno17.grid(row=9,column=2,sticky=W)

lblno36=tkinter.Entry(LeftMayFrame2,width=10)
lblno36.grid(row=15,column=2,sticky=W)



#lblno18=Label(LeftMayFrame2,font=('arial',10,'bold'),text="Credit:",bd=9)
#lblno18.grid(row=9,column=3,sticky=W)


#lblno22=tkinter.Entry(LeftMayFrame2,width=10)
#lblno22.grid(row=10,column=3,sticky=W)

box=ttk.Combobox(LeftMayFrame2,textvariable=value8,state="readyonly")
box['values']=('-SELECT-','0',"1","2",'3','4','5')
box.current(0)
box.grid(row=15,column=3,sticky=W)
#####-------------------------------------------------------------------####################_------------------------

lblno37=Label(LeftMayFrame2,font=('arial',8,'bold'),text="7",bd=9)
lblno37.grid(row=16,column=0,sticky=W)

#lblno5=tkinter.Entry(LeftMayFrame2,width=25)
#lblno5.grid(row=2,column=1,sticky=W)



#lblno20=Label(LeftMayFrame2,font=('arial',10,'bold'),text="Subject",bd=9)
#lblno20.grid(row=10,column=1,sticky=W)

lblno38=tkinter.Entry(LeftMayFrame2,width=55)
lblno38.grid(row=16,column=1,sticky=W)


#lblno17=Label(LeftMayFrame2,font=('arial',10,'bold'),text="Code",bd=9)
#lblno17.grid(row=9,column=2,sticky=W)

lblno39=tkinter.Entry(LeftMayFrame2,width=10)
lblno39.grid(row=16,column=2,sticky=W)



#lblno18=Label(LeftMayFrame2,font=('arial',10,'bold'),text="Credit:",bd=9)
#lblno18.grid(row=9,column=3,sticky=W)


#lblno22=tkinter.Entry(LeftMayFrame2,width=10)
#lblno22.grid(row=10,column=3,sticky=W)

box=ttk.Combobox(LeftMayFrame2,textvariable=value9,state="readyonly")
box['values']=('-SELECT-','0',"1","2",'3','4','5')
box.current(0)
box.grid(row=16,column=3,sticky=W)
##########----------------------------------------------------------------############-------------------------------------

lblno40=Label(RightMayFrame3,font=('arial',10,'bold'),text="\tDetails of Course For Which in Regular semester\n(Elective Subjects).",bd=19)
lblno40.grid(row=0,column=0,sticky=W)


lblno41=Label(RightMayFrame2,font=('arial',8,'bold'),text="SNO.",bd=9)
lblno41.grid(row=1,column=0,sticky=W)


lblno42=Label(RightMayFrame2,font=('arial',8,'bold'),text="Subject\t\t",bd=9)
lblno42.grid(row=2,column=0,sticky=W)


lblno43=Label(RightMayFrame2,font=('arial',8,'bold'),text="Code",bd=9)
lblno43.grid(row=3,column=0,sticky=W)


lblno44=Label(RightMayFrame2,font=('arial',8,'bold'),text="Credit\t",bd=9)
lblno44.grid(row=4,column=0,sticky=W)

####_----------------------------##########------------------------------------------------------------------------------
lblno45=Label(RightMayFrame2,font=('arial',8,'bold'),text="1",bd=9)
lblno45.grid(row=1,column=1,sticky=W)

#lblno5=tkinter.Entry(LeftMayFrame2,width=25)
#lblno5.grid(row=2,column=1,sticky=W)



#lblno20=Label(LeftMayFrame2,font=('arial',10,'bold'),text="Subject",bd=9)
#lblno20.grid(row=10,column=1,sticky=W)

lblno46=tkinter.Entry(RightMayFrame2,width=23)
lblno46.grid(row=2,column=1,sticky=W)


#lblno17=Label(LeftMayFrame2,font=('arial',10,'bold'),text="Code",bd=9)
#lblno17.grid(row=9,column=2,sticky=W)

lblno47=tkinter.Entry(RightMayFrame2,width=15)
lblno47.grid(row=3,column=1,sticky=W)



#lblno18=Label(LeftMayFrame2,font=('arial',10,'bold'),text="Credit:",bd=9)
#lblno18.grid(row=9,column=3,sticky=W)


#lblno22=tkinter.Entry(LeftMayFrame2,width=10)
#lblno22.grid(row=10,column=3,sticky=W)

box=ttk.Combobox(RightMayFrame2,textvariable=value11,state="readyonly")
box['values']=('-SELECT-','0',"1","2",'3','4','5')
box.current(0)
box.grid(row=4,column=1,sticky=W)
#######---------------------------------------------------------_######--------------------------------------
lblno48=Label(RightMayFrame2,font=('arial',8,'bold'),text="2",bd=9)
lblno48.grid(row=1,column=2,sticky=W)

#lblno5=tkinter.Entry(LeftMayFrame2,width=25)
#lblno5.grid(row=2,column=1,sticky=W)



#lblno20=Label(LeftMayFrame2,font=('arial',10,'bold'),text="Subject",bd=9)
#lblno20.grid(row=10,column=1,sticky=W)

lblno49=tkinter.Entry(RightMayFrame2,width=23)
lblno49.grid(row=2,column=2,sticky=W)


#lblno17=Label(LeftMayFrame2,font=('arial',10,'bold'),text="Code",bd=9)
#lblno17.grid(row=9,column=2,sticky=W)

lblno50=tkinter.Entry(RightMayFrame2,width=15)
lblno50.grid(row=3,column=2,sticky=W)



#lblno18=Label(LeftMayFrame2,font=('arial',10,'bold'),text="Credit:",bd=9)
#lblno18.grid(row=9,column=3,sticky=W)


#lblno22=tkinter.Entry(LeftMayFrame2,width=10)
#lblno22.grid(row=10,column=3,sticky=W)

box=ttk.Combobox(RightMayFrame2,textvariable=value12,state="readyonly")
box['values']=('-SELECT-','0',"1","2",'3','4','5')
box.current(0)
box.grid(row=4,column=2,sticky=W)
###########3---------------------------------------$################---------------------------------------------------
lblno51=Label(RightMayFrame2,font=('arial',10,'bold'),text="\nDetails of Courses of \nprevious semesters to\nbe repeated",bd=9)
lblno51.grid(row=5,column=1,sticky=W)


lblno52=Label(RightMayFrame2,font=('arial',8,'bold'),text="SNO.",bd=9)
lblno52.grid(row=6,column=0,sticky=W)


lblno53=Label(RightMayFrame2,font=('arial',8,'bold'),text="Subject\t\t",bd=9)
lblno53.grid(row=7,column=0,sticky=W)


lblno54=Label(RightMayFrame2,font=('arial',8,'bold'),text="Code",bd=9)
lblno54.grid(row=8,column=0,sticky=W)


lblno55=Label(RightMayFrame2,font=('arial',8,'bold'),text="Credit\t",bd=9)
lblno55.grid(row=9,column=0,sticky=W)
######---------------------------------------############----------------------------------------------------------------------

lblno56=Label(RightMayFrame2,font=('arial',8,'bold'),text="1",bd=9)
lblno56.grid(row=6,column=1,sticky=W)

#lblno5=tkinter.Entry(LeftMayFrame2,width=25)
#lblno5.grid(row=2,column=1,sticky=W)



#lblno20=Label(LeftMayFrame2,font=('arial',10,'bold'),text="Subject",bd=9)
#lblno20.grid(row=10,column=1,sticky=W)

lblno57=tkinter.Entry(RightMayFrame2,width=23)
lblno57.grid(row=7,column=1,sticky=W)


#lblno17=Label(LeftMayFrame2,font=('arial',10,'bold'),text="Code",bd=9)
#lblno17.grid(row=9,column=2,sticky=W)

lblno58=tkinter.Entry(RightMayFrame2,width=15)
lblno58.grid(row=8,column=1,sticky=W)



#lblno18=Label(LeftMayFrame2,font=('arial',10,'bold'),text="Credit:",bd=9)
#lblno18.grid(row=9,column=3,sticky=W)


#lblno22=tkinter.Entry(LeftMayFrame2,width=10)
#lblno22.grid(row=10,column=3,sticky=W)

box=ttk.Combobox(RightMayFrame2,textvariable=value16,state="readyonly")
box['values']=('-SELECT-','0',"1","2",'3','4','5')
box.current(0)
box.grid(row=9,column=1,sticky=W)

####3--------------------------------########-------------------------------------------------------------------------------------
lblno59=Label(RightMayFrame2,font=('arial',8,'bold'),text="2",bd=9)
lblno59.grid(row=6,column=2,sticky=W)

#lblno5=tkinter.Entry(LeftMayFrame2,width=25)
#lblno5.grid(row=2,column=1,sticky=W)



#lblno20=Label(LeftMayFrame2,font=('arial',10,'bold'),text="Subject",bd=9)
#lblno20.grid(row=10,column=1,sticky=W)

lblno60=tkinter.Entry(RightMayFrame2,width=23)
lblno60.grid(row=7,column=2,sticky=W)


#lblno17=Label(LeftMayFrame2,font=('arial',10,'bold'),text="Code",bd=9)
#lblno17.grid(row=9,column=2,sticky=W)

lblno61=tkinter.Entry(RightMayFrame2,width=15)
lblno61.grid(row=8,column=2,sticky=W)



#lblno18=Label(LeftMayFrame2,font=('arial',10,'bold'),text="Credit:",bd=9)
#lblno18.grid(row=9,column=3,sticky=W)


#lblno22=tkinter.Entry(LeftMayFrame2,width=10)
#lblno22.grid(row=10,column=3,sticky=W)

box=ttk.Combobox(RightMayFrame2,textvariable=value13,state="readyonly")
box['values']=('-SELECT-','0',"1","2",'3','4','5')
box.current(0)
box.grid(row=9,column=2,sticky=W)
#####-------------------------------------------######-----------------------------------###-------------------------------
lblno62=Label(RightMayFrame2,font=('arial',10,'bold'),text="\nDetails of Courses of\nregular semesters\nto be dropped",bd=9)
lblno62.grid(row=10,column=1,sticky=W)


lblno63=Label(RightMayFrame2,font=('arial',8,'bold'),text="SNO.",bd=9)
lblno63.grid(row=11,column=0,sticky=W)


lblno64=Label(RightMayFrame2,font=('arial',8,'bold'),text="Subject\t\t",bd=9)
lblno64.grid(row=12,column=0,sticky=W)


lblno65=Label(RightMayFrame2,font=('arial',8,'bold'),text="Code",bd=9)
lblno65.grid(row=13,column=0,sticky=W)


lblno66=Label(RightMayFrame2,font=('arial',8,'bold'),text="Credit\t",bd=9)
lblno66.grid(row=14,column=0,sticky=W)
#####---------------------------------------##############------------------------------------------------------------------
lblno67=Label(RightMayFrame2,font=('arial',8,'bold'),text="1",bd=9)
lblno67.grid(row=11,column=1,sticky=W)

#lblno5=tkinter.Entry(LeftMayFrame2,width=25)
#lblno5.grid(row=2,column=1,sticky=W)



#lblno20=Label(LeftMayFrame2,font=('arial',10,'bold'),text="Subject",bd=9)
#lblno20.grid(row=10,column=1,sticky=W)

lblno68=tkinter.Entry(RightMayFrame2,width=23)
lblno68.grid(row=12,column=1,sticky=W)


#lblno17=Label(LeftMayFrame2,font=('arial',10,'bold'),text="Code",bd=9)
#lblno17.grid(row=9,column=2,sticky=W)

lblno69=tkinter.Entry(RightMayFrame2,width=15)
lblno69.grid(row=13,column=1,sticky=W)



#lblno18=Label(LeftMayFrame2,font=('arial',10,'bold'),text="Credit:",bd=9)
#lblno18.grid(row=9,column=3,sticky=W)


#lblno22=tkinter.Entry(LeftMayFrame2,width=10)
#lblno22.grid(row=10,column=3,sticky=W)

box=ttk.Combobox(RightMayFrame2,textvariable=value14,state="readyonly")
box['values']=('-SELECT-','0',"1","2",'3','4','5')
box.current(0)
box.grid(row=14,column=1,sticky=W)
#####------------------------------------------########3-----------------------------------------------------------------
lblno70=Label(RightMayFrame2,font=('arial',8,'bold'),text="2",bd=9)
lblno70.grid(row=11,column=2,sticky=W)

#lblno5=tkinter.Entry(LeftMayFrame2,width=25)
#lblno5.grid(row=2,column=1,sticky=W)



#lblno20=Label(LeftMayFrame2,font=('arial',10,'bold'),text="Subject",bd=9)
#lblno20.grid(row=10,column=1,sticky=W)

lblno71=tkinter.Entry(RightMayFrame2,width=23)
lblno71.grid(row=12,column=2,sticky=W)


#lblno17=Label(LeftMayFrame2,font=('arial',10,'bold'),text="Code",bd=9)
#lblno17.grid(row=9,column=2,sticky=W)

lblno72=tkinter.Entry(RightMayFrame2,width=15)
lblno72.grid(row=13,column=2,sticky=W)

####------------------------------------########---------------------------------------------####
#lblno73=tkinter.Entry(RightMayFrame2,width=15)
#lblno73.grid(row=14,column=0,sticky=W)



#lblno18=Label(LeftMayFrame2,font=('arial',10,'bold'),text="Credit:",bd=9)
#lblno18.grid(row=9,column=3,sticky=W)


#lblno22=tkinter.Entry(LeftMayFrame2,width=10)
#lblno22.grid(row=10,column=3,sticky=W)

box=ttk.Combobox(RightMayFrame2,textvariable=value15,state="readyonly")
box['values']=('-SELECT-','0',"1","2",'3','4','5')
box.current(0)
box.grid(row=14,column=2,sticky=W)

####-----------------------BUTTONS---------##############3------------------------------#####------------------------------------

#def hellocallback():
    #messagebox.showinfo("details saved","Registration Process Is Sucessfull")


B=Button(RightMayFrame2,text="SAVE & SUBMIT",command=database,bg="DARKGREEN",fg="white")
B.grid(row=15,column=1,sticky=W)

def exit():
    tkinter.messagebox.showinfo("Exit","Leave page")
    root.destroy()
B=Button(RightMayFrame2,text="DESCARD & EXIT",bg="CRIMSON",command=exit,fg="WHITE")
B.grid(row=15,column=2,sticky=W)


###3-------------------------------#######--------------------------------------##########-------------------
#lblno73=Label(RightMayFrame2,font=('arial',10,'bold'),text="certifit",bd=16)
#lblno73.grid(row=16,column=0,sticky=W)







root.mainloop()
