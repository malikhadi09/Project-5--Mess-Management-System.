from tkinter import *

def desi_food():

    import DESI


def fast_food():
    import FAST


def dessert_food():
    import DESSERT


def owner():
    import OWNER


def delivery():
    import DELIVERY


tk=Tk()
tk.geometry("500x300")
tk.title("MENU")
tk.configure(bg='lightblue')
Label(tk, width="300", text="MENU", bg="orange", fg="white").pack()
btn1=Button(tk,text="DESI FOODS",command=desi_food, bg="orange")
btn1.place(relx=0.4,rely=0.2)
btn2=Button(tk,text="FAST FOODS",command=fast_food, bg="orange")
btn2.place(relx=0.4,rely=0.3)
btn3=Button(tk,text="DESSERT",command=dessert_food, bg="orange")
btn3.place(relx=0.4,rely=0.4)
btn4=Button(tk,text="OWNER DETAILS",command=owner, bg="orange")
btn4.place(relx=0.4,rely=0.5)
btn5=Button(tk,text="DELIVERY DETAILS",command=delivery, bg="orange")
btn5.place(relx=0.4,rely=0.6)
def bk():
    tk.destroy()
    import obj
    x = obj.ft

btn7=Button(tk,text="BACK BUTTON",command=bk,bg="black",fg="white")
btn7.place(relx=0.4,rely=0.8)

tk.mainloop()