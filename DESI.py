from tkinter import *

import obj
def insert_desi():
    rt=Tk()
    rt.geometry("500x400")
    rt.configure(bg='lightblue')
    rt.title("Desi FOOD")
    def prt():
        var=en.get()
        pr=int(en1.get())
        #print(var)
        objj= obj.ft
        objj.insert_data_desi_foods(var,pr)

    t=Label(rt,text="Name of Desi food:")

    t.place(relx=0.1,rely=0.1)
    t1 = Label(rt, text="Price:")

    t1.place(relx=0.1, rely=0.2)
    en=Entry(rt)
    en.place(relx=0.4,rely=0.1)
    en1 = Entry(rt)
    en1.place(relx=0.4, rely=0.2)
    bt1=Button(rt,text="click",command=prt, bg="orange")
    bt1.place(rely=0.3,relx=0.3)
    def bk():
        rt.destroy()
        import obj
        x = obj.ft

    bt1 = Button(rt, text="BACK BUTTON", command=bk,bg="black",fg="white")
    bt1.place(rely=0.4, relx=0.3)

    rt.mainloop()

def fetch_desi():
    rrrrt=Tk()

    rrrrt.title("FETCH DESI FOOD")
    rrrrt.geometry("800x500")
    rrrrt.configure(bg='lightblue')
    itm = obj.ft
    rrt=itm.fetch_data_desi_foods()


    tq=Text(rrrrt,height=25,width=80)
    d=itm.fetch_data_desi_foods()
    tq.insert(END, "FOOD NAME")
    tq.insert(END, "\t\t\t")
    tq.insert(END, "PRICE")
    tq.insert(END, "\n\n")
    tq.place(relx=0.1,rely=0.1)
    '''for x in range (0,len(itm.fetch_data_fast_foods())):

        tq.insert(END,d[x])
        tq.insert(END,"\t")
        tq.insert(END,d[x-1])
        tq.insert(END,"\n")
        x=x+2
        q=0'''
    q=0
    z=1
    while(q<len(itm.fetch_data_desi_foods())):
        tq.insert(END, d[q])
        tq.insert(END, "\t\t\t")
        tq.insert(END, d[z])
        tq.insert(END, "\n")
        q=q+2
        z=z+2

    def bk():
        rrrrt.destroy()
        import obj
        x = obj.ft

    bt1 = Button(rrrrt, text="BACK BUTTON", command=bk,bg="black",fg="white")
    bt1.place(rely=0.0, relx=0.2)

    rrrrt.mainloop()

def min_show_desi():
    rrrt = Tk()

    rrrt.title("DESI FOOD MINIMUM PRICE FOOD")
    rrrt.geometry("800x500")
    rrrt.configure(bg='lightblue')
    itm=obj.ft
    rtr=itm.min_desi_price()
    tq = Text(rrrt, height=25, width=80)
    tq.place(relx=0.1,rely=0.1)
    tq.insert(END,"MINIMUM PRICE OF DESI FOOD")
    tq.insert(END, "\n")
    tq.insert(END, "\n")
    tq.insert(END, "FOOD")
    tq.insert(END, "\t\t")
    tq.insert(END, "PRICE")
    tq.insert(END, "\n\n")
    tq.insert(END, rtr)
    def bk():
        rrrt.destroy()
        import obj
        x = obj.ft

    bt1 = Button(rrrt, text="BACK BUTTON", command=bk,bg="black",fg="white")
    bt1.place(rely=0.0, relx=0.2)

def max_show_desi():
    rrrt = Tk()

    rrrt.title("DESI FOOD MAXIMUM PRICE FOOD")
    rrrt.geometry("800x500")
    rrrt.configure(bg='lightblue')
    itm=obj.ft
    rtr=itm.max_desi_price()
    tq = Text(rrrt, height=25, width=80)

    tq.place(relx=0.1,rely=0.1)
    tq.insert(END, "MAXIMUM PRICE OF DESI FOOD")
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

def update_desi():
    rt=Tk()
    rt.geometry("500x400")
    rt.configure(bg='lightblue')
    rt.title("UPDATE DESI FOOD")
    def prt():
        var = en.get()
        var2 = en1.get()
        pr=int(en2.get())

        objj= obj.ft
        objj.update_data_desi_foods(var,var2,pr)

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
    bt1=Button(rt,text="CLICK",command=prt, bg="orange")
    bt1.place(rely=0.4,relx=0.3)
    def bk():

        import obj
        x = obj.ft


    bt1 = Button(rt, text="BACK BUTTON", command=bk,bg="black",fg="white")
    bt1.place(rely=0.5, relx=0.3)

    rt.mainloop()

def del_desi():
    rt=Tk()
    rt.geometry("500x400")
    rt.configure(bg='lightblue')
    rt.title("Desi FOOD")
    def prt():
        var=en.get()
        #print(var)
        objj= obj.ft
        objj.delete_data_desi_foods(var)

    t=Label(rt,text="Name of food to delete: ")

    t.place(relx=0.1,rely=0.1)

    en=Entry(rt)
    en.place(relx=0.4,rely=0.1)
    bt1 = Button(rt, text="CLICK", command=prt, bg="orange")
    bt1.place(rely=0.3, relx=0.3)
    def bk():
        rt.destroy()
        import obj
        x = obj.ft

    bt1 = Button(rt, text="BACK BUTTON", command=bk,bg="black",fg="white")
    bt1.place(rely=0.4, relx=0.3)



    rt.mainloop()

root=Tk()
root.geometry("500x300")
root.title("DESI FOODS")
root.configure(bg='lightblue')
Label(root, width="300", text="DESI FOOD DETAILS", bg="orange", fg="white").pack()
btn1=Button(root,text="INSERT DESI",command=insert_desi, bg="orange")
btn1.place(relx=0.4,rely=0.2)
btn2=Button(root,text="FETCH DESI",command=fetch_desi, bg="orange")
btn2.place(relx=0.4,rely=0.3)
btn3=Button(root,text="UPDATE DESI",command=update_desi, bg="orange")
btn3.place(relx=0.4,rely=0.4)
btn4=Button(root,text="DELETE DESI",command=del_desi, bg="orange")
btn4.place(relx=0.4,rely=0.5)
btn5=Button(root,text="MIN PRICE DESI",command=min_show_desi, bg="orange")
btn5.place(relx=0.4,rely=0.6)
btn6=Button(root,text="MAX PRICE DESI",command=max_show_desi, bg="orange")
btn6.place(relx=0.4,rely=0.7)

def bk():
    root.destroy()

    import obj
    x = obj.ft

btn7=Button(root,text="BACK BUTTON",command=bk,bg="black",fg="white")
btn7.place(relx=0.4,rely=0.8)
root.mainloop()