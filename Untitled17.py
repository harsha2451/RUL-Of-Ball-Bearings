import tkinter
from tkinter import messagebox
import pandas as pd
import numpy as np
import math

def cancel():
    t1.delete (0,20)
    t2.delete (0,last=20)
    t3.delete (0,last=20)
    t4.delete (0,last=20)
    t5.delete (0,last=20)  
    

    t1.focus()

def rul():
    bnum = int(t1.get())  #designation
    wr = int(t2.get())
    wa = int(t3.get())
    sh = int(t4.get()) #shift hours 
    n = int(t5.get())  #speed
    k=3

    #from CSV we have to get c and c0 starts from here
    bearings=pd.read_csv("C:/Users/harsh/KL university/MD/bearings_tables XL.csv")
    ind=bearings[bearings["designation"]== bnum].index
    c=int(bearings["C"][ind])
    c0=int(bearings["C0"][ind])
    print("C0=",c0)
    print("C=",c)


    def eqload():
        
        a=(wa/wr)
        b=float(wa/c0)
        X=0
        Y=0
        
        
        factors=pd.read_csv("C:/Users/harsh/KL university/MD/BEARING LOAD FACTORS.csv.xls")
        list_b=factors['b'].to_list()
        list_b.sort()
        for i in list_b:
            if(i > b):
                req_b = i
                break
        else:
            req_b=list_b[-1]
        inde=factors[factors['b']==req_b].index
        req_e=float(factors['e'][inde])
        if (a<=req_e):
            X=int(factors['case1X'][inde])
            Y=int(factors['case1Y'][inde])
        else:
            X=float(factors['case2X'][inde])
            Y=float(factors['case2Y'][inde])
        
        W=(X*wr)+(Y*wa)
        print("X= ",X)
        print("Y= ",Y)
        print("W= ",W)
        return W
        

    W=eqload()

    L = ((c/W)**k)*(10**6)          #life in revolutions 
    print("L=",L)
    Lh = L/(60*n)                   #life in hours
    print("Lh=",Lh)
    if (sh>=2 and sh<=4) :
        maxi=6000
    elif(sh>=6 and sh<=8) :
        maxi=16000
    elif (sh>=21 and sh<=24):
        maxi=60000
    
    rl = int(maxi-Lh)

    day = int(rl/sh)

    l9 = tkinter.Label(root, text = (rl,"Hrs"))   
    l9.place(x=650, y=305)

    l12 = tkinter.Label(root, text = (day,"days"))
    l12.place(x=650, y=345)
    

root = tkinter.Tk()
root.title("Bearing Life Calculation Application")
w=900
h=450
x=50
y=100
root.geometry("%dx%d+%d+%d" % (w,h,x,y))



l1= tkinter.Label(root,text="BEARINGS REMAINING LIFE CALCULATION",font=("Arial Bold",20))
l1.place(x=175,y=30)


l2= tkinter.Label(root,text="Enter Bearing Designation:  ",font=("Arial Bold",15))
l2.place(x=40,y=100)


l3= tkinter.Label(root,text="Enter Radial Load in N (Wr):  ",font=("Arial Bold",15))
l3.place(x=450,y=100)


l4= tkinter.Label(root,text="Enter Axial Load in N (Wa):  ",font=("Arial Bold",15))
l4.place(x=40,y=150)


l5= tkinter.Label(root,text="Enter Shift hours:  ",font=("Arial Bold",15))
l5.place(x=545,y=150)

l6= tkinter.Label(root,text="Enter Speed in RPM:  ",font=("Arial Bold",15))
l6.place(x=520,y=200)



l8= tkinter.Label(root,text="Remaining life of bearing is:  ",font=("Arial Bold",15)) #ans
l8.place(x=350,y=300)

l10= tkinter.Label(root,text="Remaining life in days:  ",font=("Arial Bold",15)) #ans
l10.place(x=350,y=340)




t1 = tkinter.Entry(root,width=20)
t1.place(x=300, y=100)

t2 = tkinter.Entry(root,width=20)
t2.place(x=725, y=100)


t3 = tkinter.Entry(root,width=20)
t3.place(x=300, y=150)

t4 = tkinter.Entry(root,width=20)
t4.place(x=725, y=150)

t5 = tkinter.Entry(root,width=20)
t5.place(x=725, y=200)




b1 = tkinter.Button(root, text="Ok",width=15,height=2,command=rul)
b1.place(x=250, y=375)

b2 = tkinter.Button(root, text="Cancel", width=15,height=2,command=cancel)
b2.place(x=500, y=375)

t1.focus()


    

root.mainloop()
    
rul()
