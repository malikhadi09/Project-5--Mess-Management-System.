from tkinter import *

import obj
def insert_fast():
    rt=Tk()
    rt.geometry("500x400")
    rt.title("FAST FOOD")
    rt.configure(bg='lightblue')
    def prt():
        var=en.get()
        pr=int(en1.get())
        #print(var)
        objj= obj.ft
        objj.insert_data_fast_foods(var,pr)

    t=Label(rt,text="Name of Fast food:")

    t.place(relx=0.1,rely=0.1)
    t1 = Label(rt, text="Price:")

    t1.place(relx=0.1, rely=0.2)
    en=Entry(rt)
    en.place(relx=0.4,rely=0.1)
    en1 = Entry(rt)
    en1.place(relx=0.4, rely=0.2)
    bt1=Button(rt,text="CLICK",command=prt,bg="orange")
    bt1.place(rely=0.3,relx=0.3)
    def bk():
        rt.destroy()
        import obj
        x = obj.ft

    bt1 = Button(rt, text="BACK BUTTON", command=bk,bg="black",fg="white")
    bt1.place(rely=0.5, relx=0.3)

    rt.mainloop()


def fetch_fast():
    rrrt = Tk()
    q = 0
    z = 1
    import obj

    itm = obj.ft

    rrrt.title("FETCH FAST FOOD")
    rrrt.geometry("800x500")
    rrrt.configure(bg='lightblue')

    rrt = itm.fetch_data_fast_foods()

    tq = Text(rrrt, height=25, width=80)
    d = itm.fetch_data_fast_foods()
    tq.insert(END, "FOOD NAME")
    tq.insert(END, "\t\t\t")
    tq.insert(END, "PRICE")
    tq.insert(END, "\n\n")
    tq.place(relx=0.1, rely=0.1)

    q = 0
    z = 1
    print("111")
    while (q < len(itm.fetch_data_fast_foods())):
        tq.insert(END, d[q])
        tq.insert(END, "\t\t\t")
        tq.insert(END, d[z])
        tq.insert(END, "\n")
        q = q + 2
        z = z + 2

    def bk():
        rrrt.destroy()
        import obj
        x = obj.ft

    bt1 = Button(rrrt, text="BACK BUTTON", command=bk,bg="black",fg="white")
    bt1.place(rely=0.0, relx=0.2)

    # tq.insert(1.0,itm.fetch_data_fast_foods())'''

    rrrt.mainloop()

def update_fast():
    rt=Tk()
    rt.geometry("500x400")
    rt.configure(bg='lightblue')
    rt.title("UPDATE FAST FOOD")
    def prt():
        var = en.get()
        var2 = en1.get()
        pr=int(en2.get())

        objj= obj.ft
        objj.update_data_fast_foods(var,var2,pr)

    tn = Label(rt, text="Name of old food:")
    tn.place(relx=0.1, rely=0.1)
    t = Label(rt, text="Name of new food:")
    t.place(relx=0.1, rely=0.2)
    t1 = Label(rt, text="Price:")
    t1.place(relx=0.1, rely=0.3)
    en=Entry(rt)
    en.place(relx=0.4,rely=0.1)
    en1 = Entry(rt)
    en1.place(relx=0.4, rely=0.2)
    en2 = Entry(rt)
    en2.place(relx=0.4, rely=0.3)
    bt1=Button(rt,text="click",command=prt, bg="orange")
    bt1.place(rely=0.4,relx=0.3)
    def bk():
        rt.destroy()
        import obj
        x = obj.ft

    bt1 = Button(rt, text="BACK BUTTON", command=bk,bg="black",fg="white")
    bt1.place(rely=0.5, relx=0.3)
    rt.mainloop()

def del_fast():
    rt=Tk()
    rt.geometry("500x400")
    rt.configure(bg='lightblue')
    rt.title("FAST FOOD")
    def prt():
        var=en.get()
        #print(var)
        objj= obj.ft
        objj.delete_data_fast_foods(var)

    t=Label(rt,text="Name of food to delete: ")

    t.place(relx=0.1,rely=0.1)

    en=Entry(rt)
    en.place(relx=0.4,rely=0.1)

    bt1=Button(rt,text="CLICK",command=prt, bg="orange")
    bt1.place(rely=0.3,relx=0.3)

    def bk():
        rt.destroy()
        import obj
        x = obj.ft

    bt1 = Button(rt, text="BACK BUTTON", command=bk,bg="black",fg="white")
    bt1.place(rely=0.4, relx=0.3)

    rt.mainloop()

def min_show_fast():
    rrrt = Tk()

    rrrt.title("FAST FOOD MINIMUM PRICE FOOD")
    rrrt.geometry("800x500")
    rrrt.configure(bg='lightblue')
    itm=obj.ft
    rtr=itm.min_fast_price()
    tq = Text(rrrt, height=25, width=80)
    tq.place(relx=0.1,rely=0.1)
    tq.insert(END, "MINIMUM PRICE OF FAST FOOD")
    tq.insert(END, "\n")
    tq.insert(END, "\n")
    tq.insert(END, "FOOD")
    tq.insert(END, "\t")
    tq.insert(END, "PRICE")
    tq.insert(END, "\n\n")
    tq.insert(END, rtr)
    def bk():
        rrrt.destroy()
        import obj
        x = obj.ft

    bt1 = Button(rrrt, text="BACK BUTTON", command=bk,bg="black",fg="white")
    bt1.place(rely=0.0, relx=0.2)

def max_show_fast():
    rrrt = Tk()

    rrrt.title("FAST FOOD MAXIMUM PRICE FOOD")
    rrrt.geometry("800x500")
    rrrt.configure(bg='lightblue')
    itm=obj.ft
    rtr=itm.max_fast_price()
    tq = Text(rrrt, height=25, width=80)
    tq.place(relx=0.1,rely=0.1)
    tq.insert(END, "MAXIMUM PRICE OF FAST FOOD")
    tq.insert(END, "\n")
    tq.insert(END, "\n")
    tq.insert(END, "FOOD")
    tq.insert(END, "\t")
    tq.insert(END, "PRICE")
    tq.insert(END, "\n\n")
    tq.insert(END, rtr)
    def bk():
        rrrt.destroy()
        import obj
        x = obj.ft

    bt1 = Button(rrrt, text="BACK BUTTON", command=bk,bg="black",fg="white")
    bt1.place(rely=0.0, relx=0.2)

root=Tk()
root.geometry("500x300")
root.title("FAST FOODS")
root.configure(bg='lightblue')
Label(root, width="300", text="FAST FOOD DETAILS", bg="orange", fg="white").pack()
btn1=Button(root,text="INSERT FAST",command=insert_fast, bg="orange")
btn1.place(relx=0.4,rely=0.2)
btn2=Button(root,text="FETCH FAST",command=fetch_fast, bg="orange")
btn2.place(relx=0.4,rely=0.3)
btn3=Button(root,text="UPDATE FAST",command=update_fast, bg="orange")
btn3.place(relx=0.4,rely=0.4)
btn4=Button(root,text="DELETE FAST",command=del_fast, bg="orange")
btn4.place(relx=0.4,rely=0.5)
btn5=Button(root,text="MIN PRICE FAST",command=min_show_fast, bg="orange")
btn5.place(relx=0.4,rely=0.6)
btn6=Button(root,text="MAX PRICE FAST",command=max_show_fast, bg="orange")
btn6.place(relx=0.4,rely=0.7)
def bk():
    root.destroy()
    import obj
    x = obj.ft

btn7=Button(root,text="BACK BUTTON",command=bk,bg="black",fg="white")
btn7.place(relx=0.4,rely=0.8)

root.mainloop()