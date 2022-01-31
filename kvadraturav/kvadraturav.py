from tkinter import *
from math import *
import matplotlib.pyplot as plt
import numpy as np


def ochko():
    x1=np.arrange(-9,-1.5,0.5)
    y1=(-1/16)*(x+5)**2+2
    x2=np.arrange(1,9.5,0.5)
    y2=(-1/16)*(x-5)**2+2
    x3=np.arrange(-9,-1.5,0.5)
    y3=1/4*(x+5)**2-3
    x4=np.arrange(1,9.5,0.5)
    y4=1/4*(x-5)**2-3
    x5=np.arrange(-9,-6.5,0.5)
    y5=-(x+7)**2+5
    x6=np.arrange(6,9.5,0.5)
    y6=-(x-7)**2+5
    x7=np.arrange(-1,1.5,0.5)
    y7=-0,5**2+1,5
    fig=plt.figure()
    plt.plot(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7)
    plt.title("Очки")
    plt.ylabel("y")
    plt.xlabel("x")
    plt.grid(True)
    plt.show()

def handler():    
    if (a.get()!="" and b.get()!="" and c.get()!=""):
        a1=int(a.get())
        b1=int(b.get())
        c1=int(c.get())
        D=b1*b1-4*a1*c1
        if D>0:
            xround=round((-1*b1+sqrt(D))/(2*a1),2)
            xround1=round((-1*b1-sqrt(D))/(2*a1),2)
            t=f"X1={xround} \nX2={xround1}"
            flag=True
        elif D==0:
            xround=round((-1*b1)/(2*a1),2)
            t=f"X1={xround}"
            flag=True
        else:
            t="Корней нет"
            flag=False
        answer.configure(text=f"D={D}\n{t}")
    return flag,D,t
def graafik():
    flag,D,t=handler()
    if flag==True:
        a1=int(a.get())
        b1=int(b.get())
        c1=int(c.get())
        x0=(-b1)/(2*a1)
        y0=a1*x0*x0+b1*x0+c1
        x = np.arange(x0-10, x0+10, 0.5)
        y=a1*x*x+b1*x+c1
        fig = plt.figure()
        plt.plot(x, y,'b:o', x0, y0,'g-d')
        plt.title('Квадратное уравнение')
        plt.ylabel('y')
        plt.xlabel('x')
        plt.grid(True)
        plt.show()
        text=f"Вершина параболлы ({x0},{y0})"
    else:
        text=f"График нет возможности построить"
    answer.configure(text=f"D={D}\n{t}\n{text}")
window=Tk()
window.geometry("640x240")
window.title("Квадратные уравнения")
f1=Frame(width=640,h)
f2=Frame(width=640,height=)


label=Label(window,text="Решение квадратного уравнения",font="Calibri 26", fg="black",bg="white")
label.pack()
answer=Label(window,height=4,width=60,bg="white")
answer.pack(side=BOTTOM)
a=Entry(window,font="Calibri 26",fg="black",bg="white",width=3)
a.pack(side=LEFT)
x2=Label(window,text="x**2+",font="Calibri 26",fg="black")
x2.pack(side=LEFT)
b=Entry(window,font="Calibri 26",fg="black",bg="white",width=3)
b.pack(side=LEFT)
x=Label(window,text="x+",font="Calibri 26",fg="black")
x.pack(side=LEFT)
c=Entry(window,font="Calibri 26",fg="black",bg="white",width=3)
c.pack(side=LEFT)
y=Label(window,text="=0",font="Calibri 26",fg="black")
y.pack(side=LEFT)

btn=Button(window,text="Решить",font="Calibri 26",bg="white",command=handler)
btn.pack(side=LEFT)
btn_g=Button(window,text="График",font="Calibri 26",bg="white",command=graafik)
btn_g.pack(side=LEFT)

window.mainloop()