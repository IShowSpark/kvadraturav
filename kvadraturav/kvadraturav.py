from tkinter import *
from math import sqrt

def answer(a,b,c):
    D=b*b-4*a*c
    if D>=0:
        x1=(-b+sqrt(D))/(2*a)
        x2=(-b-sqrt(D))/(2*a)
        text="Дискриминант:%s\nX1: %s\nX2: %s\n"%(D,x1,x2)        
    else:
        text="Дискриминант:%s\n Это уравнение не имеет решений"%D 
    return text

def inserter(value):
    label5.delete("0.0","end")
    label5.insert("0.0",value)


def handler():
    try:
        a_vibor=float(a.get())
        b_vibor=float(b.get())
        c_vibor=float(c.get())
        inserter(answer(a_vibor,b_vibor,c_vibor))
    except ValueError:
        inserter("Надо ввести всего 3 числа")
    
    





window=Tk()
window.resizable(width=False, height=False)
window.minsize(800,300)

window.title("Квадратные уравнения")
button1=Button(window,text="Решить",font="Arial 20",height=2,bg="white",fg="#00BFFF",relief=SOLID,command=handler)
button1.place(x=480,y=80)
button2=Button(window,text="График",font="Arial 20",height=2,bg="white",fg="#00BFFF",relief=SOLID,command=handler)
button2.place(x=600,y=80)


label1=Label(window,text="Решение квадратного уравнения",height=2,width=40,font="Arial 20",bg="white",fg="#00BFFF",relief="solid")
label1.pack()
a=Entry(window,font="Arial 30",width=3,bg="white",fg="#00BFFF",justify=CENTER)
a.place(x=100,y=100)
label2=Label(window,text="x**2+",height=3,font="Arial 20",fg="#00BFFF")
label2.place(x=180,y=75)
b=Entry(window,font="Arial 30",width=3,bg="white",fg="#00BFFF",justify=CENTER)
b.place(x=260,y=100)
label3=Label(window,text="x+",height=3,font="Arial 20",fg="#00BFFF")
label3.place(x=320,y=75)
c=Entry(window,font="Arial 30",width=3,bg="white",fg="#00BFFF",justify=CENTER)
c.place(x=360,y=100)
label4=Label(window,text="=0",height=3,font="Arial 20",fg="#00BFFF")
label4.place(x=420,y=75)
label5=Text(window,height=4,width=40,font="Arial 20",bg="white",fg="#00BFFF")
label5.place(x=80,y=180)




























































window.mainloop()