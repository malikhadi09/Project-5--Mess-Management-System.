from tkinter import *

import obj
def insert_owners():
    rt=Tk()
    rt.geometry("500x400")
    rt.configure(bg='lightblue')
    rt.title("INSERT OWNERS")
    def prt():

        name=en.get()
        phone_no=int(en1.get())
        #print(var)
        objj= obj.ft
        objj.insert_owner_details(name,phone_no)

    t=Label(rt,text="Name of Owner:")

    t.place(relx=0.1,rely=0.1)
    t1 = Label(rt, text="Phone number:")

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

def fetching_Owners_details():
    rrrt = Tk()
    q = 0
    z = 1

    import obj

    details = obj.ft

    rrrt.title("FETCH OWNER DETAILS")
    rrrt.configure(bg='lightblue')
    rrrt.geometry("800x500")

    rrt = details.fetch_Owners_details()

    tq = Text(rrrt, height=25, width=80)
    d = details.fetch_Owners_details()
    tq.place(relx=0.1, rely=0.2)

    q = 0
    z = 1
    def bk():
        rrrt.destroy()
        import obj
        obj.ft

    tq.insert(END,"NAME")
    tq.insert(END, "\t\t")
    tq.insert(END, "PHONE NUMBER")
    tq.insert(END, "\n\n")

    while (q < len(details.fetch_Owners_details())):
        tq.insert(END, d[q])
        tq.insert(END, "\t\t")
        tq.insert(END, d[z])
        tq.insert(END, "\n")
        q = q + 2
        z = z + 2
    bt1 = Button(rrrt, text="BACK BUTTON", command=bk,bg="black",fg="white")
    bt1.place(rely=0.1, relx=0.2)


    rrrt.mainloop()

def del_owner():
    rt=Tk()
    rt.geometry("500x400")
    rt.configure(bg='lightblue')
    rt.title("DELETE OWNER")
    def prt():
        var=en.get()
        #print(var)
        objj= obj.ft
        objj.delete_data_owner(var)

    t=Label(rt,text="Name of owner to delete: ")

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

def update_owner():
    rt=Tk()
    rt.geometry("500x400")
    rt.configure(bg='lightblue')
    rt.title("UPDATE OWNER DETAILS")
    def prt():
        var = en.get()
        var2 = en1.get()
        phoneno=int(en2.get())

        objj= obj.ft
        objj.update_data_owner(var,var2,phoneno)

    tn = Label(rt, text="Name of old owner:")
    tn.place(relx=0.1, rely=0.1)
    t = Label(rt, text="Name of new owner:")
    t.place(relx=0.1, rely=0.2)
    t1 = Label(rt, text="Phone number:")
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

root=Tk()
root.geometry("500x300")
root.title("OWNER DETAILS")
root.configure(bg='lightblue')
Label(root, width="300", text="OWNER DETAILS", bg="orange", fg="white").pack()
btn1=Button(root,text="INSERT OWNER",command=insert_owners, bg="orange")
btn1.place(relx=0.4,rely=0.2)
btn2=Button(root,text="FETCH OWNER",command=fetching_Owners_details, bg="orange")
btn2.place(relx=0.4,rely=0.3)
btn3=Button(root,text="UPDATE OWNER",command=update_owner, bg="orange")
btn3.place(relx=0.4,rely=0.4)
btn4=Button(root,text="DELETE OWNER",command=del_owner, bg="orange")
btn4.place(relx=0.4,rely=0.5)
def bk():
    root.destroy()
    import obj
    x = obj.ft

btn7=Button(root,text="BACK BUTTON",command=bk,bg="black",fg="white")
btn7.place(relx=0.4,rely=0.8)
root.mainloop()