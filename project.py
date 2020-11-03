from tkinter import *
from tkcalendar import *
root= Tk()
root.title("Timetable")
root.geometry("600x700")
root.configure(bg='#F5F5F5')

def fun1():
    val=cal.get_date()
    print(val)
    
  
    
    if(val=='10/5/20' or val=='10/12/20' or val=='10/19/20' or val=='10/26/20'):
        l1['text']="Monday"
        l1['fg']="black"
        l2['text']="10-11: MTH 705"
        l3['text']="11-12: CSE 205"
        l5['text']="04-05: CSE 000"
        l6['text']="04-05: PES 319"
        
        l4['text']="02-03: PEL 999"
        l2['bg']="#E08686"
        l6['bg']="#E08686"
                
        
        l3['bg']="#E08686"
        
        l4['bg']="#E08686"
        
        l5['bg']="#E08686"
    if(val=='10/6/20' or val=='10/13/20' or val=='10/20/20' or val=='10/27/20'):
        l1['text']="Tuesday"
        l1['fg']="black"
        l2['text']="09-10: CSE 000"
        
        l3['text']="10-11: CSE 999"
        
        l4['text']="01-02: PEL 231"
        
        l5['text']="02-04: MTH 555"
        l6['text']=""
        l6['bg']="#F5F5F5"
        l2['bg']="#E08686"
        
        
        l3['bg']="#E08686"
        
        l4['bg']="#E08686"
        
        l5['bg']="#E08686"
        
    if(val=='10/7/20' or val=='10/14/20' or val=='10/21/20' or val=='10/28/20'):
        l1['text']="Wednesday"
        l1['fg']="black"
        l2['text']="11-12: PES 319"
        
        l3['text']="02-03: MGN 231"
        
        l4['text']="03-04: ASP 380"
        
        l5['text']="04-05: RES 760"
        l6['text']="05-06: MTH 444"
        l6['bg']="#E08686"
        l2['bg']="#E08686"
        
        
        l3['bg']="#E08686"
        
        l4['bg']="#E08686"
        
        l5['bg']="#E08686"
        
    if(val=='10/8/20' or val=='10/15/20' or val=='10/22/20' or val=='10/29/20' or val=='10/1/20'):
        l1['text']="Thursday"
        l1['fg']="black"
        l2['text']="10-12: CSE 250"
        
        l3['text']="01-02: PAS 487"
        
        l4['text']="03-04: CSE 320"
        
        l5['text']="04-05: CSE 211"
        l2['bg']="#E08686"
        
        
        l3['bg']="#E08686"
        
        l4['bg']="#E08686"
        
        l5['bg']="#E08686"
        l6['text']=""
        l6['bg']="#F5F5F5"
        
        
    if(val=='10/9/20' or val=='10/16/20' or val=='10/23/20' or val=='10/30/20' or val=='10/2/20'):
        l1['text']="Friday"
        l1['fg']="black"
        l2['text']="10-11: CSE 700"
        
        l3['text']="11-12: CSE 999"
        
        l4['text']="12-01: PEL 231"
        
        l5['text']="02-04: PES 320"
        l6['text']="05-06: MTH 440"
        l6['bg']="#E08686"
        l2['bg']="#E08686"
        
        
        l3['bg']="#E08686"
        
        l4['bg']="#E08686"
        
        l5['bg']="#E08686"
        
    if(val=='10/10/20' or val=='10/17/20' or val=='10/24/20' or val=='10/3/20'):
        l1['text']="Saturday"
        l1['fg']="#CC5D5D"
        l2['text']=""
        l2['bg']="#F5F5F5"
        l6['text']=""
        l6['bg']="#F5F5F5"
        
        l3['text']=""
        l3['bg']="#F5F5F5"
        
        l4['text']=""
        l4['bg']="#F5F5F5"
        l5['text']=""
        l5['bg']="#F5F5F5"
    if(val=='10/11/20' or val=='10/18/20' or val=='10/25/20' or val=='10/4/20'):
        l1['text']="Sunday"
        l6['text']=""
        l6['bg']="#F5F5F5"
        
        l1['fg']="#CC5D5D"
        l2['text']=""
        l2['bg']="#F5F5F5"
        
        l3['text']=""
        l3['bg']="#F5F5F5"
        
        l4['text']=""
        l4['bg']="#F5F5F5"
        l5['text']=""
        l5['bg']="#F5F5F5"

f1=Frame(root,bg="#F5F5F5")
f1.pack(padx=20,pady=70,side=LEFT,anchor="center")

f2=Frame(root,bg="#F5F5F5")
f2.pack(padx=20,pady=70,side=TOP)


cal=Calendar(f1,selectmode="day",year=2020,month=10,day=5,font="Montserrat 11")
cal.pack( pady=30,padx=30)

b1= Button(f1,text="Get Timetable",fg="#E08686",font="Montserrat 11 bold",command=fun1,relief=SUNKEN,borderwidth=4)
b1.pack(padx=20,pady=20)

l1=Label(f2,text="Monday", font="Montserrat 18",bg="#F5F5F5")
l1.pack(padx=20,pady=40)

l2=Label(f2,text="10-11 : MTH 705",bg="#E08686",padx=200,pady=10, font="Montserrat 11")
l2.pack(padx=20,pady=20,side=TOP)

l3=Label(f2,text="11-12 : CSE 205",bg="#E08686",padx=200,pady=10,font="Montserrat 11")
l3.pack(padx=20,pady=20,side=TOP)

l4=Label(f2,text="02-03 : PEL 999",bg="#E08686",padx=195,pady=10, font="Montserrat 11")
l4.pack(padx=20,pady=20,side=TOP)

l5=Label(f2,text="04-05 : CSE 000",bg="#E08686",padx=193,pady=10,font="Montserrat 11")
l5.pack(padx=20,pady=20,side=TOP)

l6=Label(f2,text="05-06 : PES 319",bg="#E08686",padx=193,pady=10,font="Montserrat 11")
l6.pack(padx=20,pady=20,side=TOP)

root.mainloop()