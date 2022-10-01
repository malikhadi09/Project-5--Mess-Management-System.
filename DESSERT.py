from tkinter import *

import obj

def insert_Dessert():
    rt=Tk()
    rt.geometry("500x400")
    rt.configure(bg='lightblue')
    rt.title("DESSERT")
    def prt():

        food=en.get()
        price=int(en1.get())
        #print(var)
        objj= obj.ft
        objj.insert_dessert_details(food,price)

    t=Label(rt,text="Name of food:")

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
def fetching_Dessert_details():
    rrrt = Tk()
    q = 0
    z = 1

    import obj

    details = obj.ft

    rrrt.title("FETCH Dessert DETAILS")
    rrrt.geometry("800x500")
    rrrt.configure(bg='lightblue')

    rrt = details.fetch_Dessert_details()

    tq = Text(rrrt, height=25, width=80)
    d = details.fetch_Dessert_details()
    tq.place(relx=0.1, rely=0.2)
    tq.insert(END,"DESSERT NAME")
    tq.insert(END,"\t\t\t")
    tq.insert(END, "PRICE")
    tq.insert(END, "\n\n")

    def bk():
        rrrt.destroy()
        import obj
        x = obj.ft
    bt1 = Button(rrrt, text="BACK BUTTON", command=bk,bg="black",fg="white")
    bt1.place(rely=0.1, relx=0.2)


    q = 0
    z = 1
    while (q < len(details.fetch_Dessert_details())):
        tq.insert(END, d[q])
        tq.insert(END, "\t\t\t")
        tq.insert(END, d[z])
        tq.insert(END, "\n")
        q = q + 2
        z = z + 2



    rrrt.mainloop()
def min_dessert():
    rrrt = Tk()

    rrrt.title("MINIMUM PRICE DESSERT")
    rrrt.geometry("800x500")
    rrrt.configure(bg='lightblue')
    itm=obj.ft
    rtr=itm.min_dessert_price()
    tq = Text(rrrt, height=25, width=80)
    tq.place(relx=0.1,rely=0.1)
    tq.insert(END, "MINIMUM PRICE OF DESSERTS AVAILABLE")
    tq.insert(END, "\n")
    tq.insert(END, "\n")
    tq.insert(END, "DESSERT")
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


def update_dessert():
    rt = Tk()
    rt.geometry("500x400")
    rt.configure(bg='lightblue')
    rt.title("UPDATE DESSERT")

    def prt():
        var = en.get()
        var2 = en1.get()
        pr = int(en2.get())

        objj = obj.ft
        objj.update_data_dessert_foods(var, var2, pr)

    tn = Label(rt, text="Name of old dessert:")
    tn.place(relx=0.1, rely=0.1)
    t = Label(rt, text="Name of new dessert:")
    t.place(relx=0.1, rely=0.2)
    t1 = Label(rt, text="Price:")
    t1.place(relx=0.1, rely=0.3)
    en = Entry(rt)
    en.place(relx=0.4, rely=0.1)
    en1 = Entry(rt)
    en1.place(relx=0.4, rely=0.2)
    en2 = Entry(rt)
    en2.place(relx=0.4, rely=0.3)
    bt1 = Button(rt, text="CLICK", command=prt, bg="orange")
    bt1.place(rely=0.4, relx=0.3)

    def bk():
        rt.destroy()
        import obj
        x = obj.ft

    bt1 = Button(rt, text="BACK BUTTON", command=bk,bg="black",fg="white")
    bt1.place(rely=0.5, relx=0.3)

    rt.mainloop()

def max_Dessert():
    rrrt = Tk()

    rrrt.title("MAXIMUM PRICE DESSERT")
    rrrt.geometry("800x500")
    rrrt.configure(bg='lightblue')
    itm=obj.ft
    rtr=itm.max_dessert_price()
    tq = Text(rrrt, height=25, width=80)
    tq.place(relx=0.1,rely=0.1)
    tq.insert(END, "MAXIMUM PRICE OF DESSERTS AVAILABLE")
    tq.insert(END, "\n")
    tq.insert(END, "\n")
    tq.insert(END, "DESSERT")
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

def del_dessert():
    rt=Tk()
    rt.geometry("500x400")
    rt.configure(bg='lightblue')
    rt.title("DELETE DESERT")
    def prt():
        var=en.get()
        #print(var)
        objj= obj.ft
        objj.delete_data_dessert_foods(var)

    t=Label(rt,text="Name of dessert to delete: ")

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

root=Tk()
root.geometry("500x300")
root.title("DESSERT")
root.configure(bg='lightblue')
Label(root, width="300", text="DESSERT DETAILS", bg="orange", fg="white").pack()
btn1=Button(root,text="INSERT DESSERT",command=insert_Dessert, bg="orange")
btn1.place(relx=0.4,rely=0.2)
btn2=Button(root,text="FETCH DESSERT",command=fetching_Dessert_details, bg="orange")
btn2.place(relx=0.4,rely=0.3)
btn3=Button(root,text="UPDATE DESSERT",command=update_dessert, bg="orange")
btn3.place(relx=0.4,rely=0.4)
btn4=Button(root,text="DELETE DESSERT",command=del_dessert, bg="orange")
btn4.place(relx=0.4,rely=0.5)
btn5=Button(root,text="MIN PRICE DESSERT",command=min_dessert, bg="orange")
btn5.place(relx=0.4,rely=0.6)
btn6=Button(root,text="MAX PRICE DESSERT",command=max_Dessert, bg="orange")
btn6.place(relx=0.4,rely=0.7)
def bk():
    root.destroy()
    import obj
    x = obj.ft

btn7=Button(root,text="BACK BUTTON",command=bk,bg="black",fg="white")
btn7.place(relx=0.4,rely=0.8)

root.mainloop()