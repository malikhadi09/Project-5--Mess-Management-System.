from tkinter import *

import obj

def insert_Riders():
    rt=Tk()
    rt.geometry("500x400")
    rt.configure(bg='lightblue')
    rt.title("RIDERS DETAILS")
    def prt():

        name=en.get()
        phone_no=int(en1.get())
        #print(var)
        objj= obj.ft
        objj.insert_Rider_details(name,phone_no)

    t=Label(rt,text="Name of Rider:")

    t.place(relx=0.1,rely=0.1)
    t1 = Label(rt, text="Phone number:")

    t1.place(relx=0.1, rely=0.2)
    en=Entry(rt)
    en.place(relx=0.4,rely=0.1)
    en1 = Entry(rt)
    en1.place(relx=0.4, rely=0.2)
    bt1=Button(rt,text="CLICK",command=prt,bg='orange')
    bt1.place(rely=0.3,relx=0.3)

    def bk():
        rt.destroy()
        #import obj
       # x = obj.ft

    bt1 = Button(rt, text="BACK BUTTON", command=bk,bg="black",fg="white")
    bt1.place(rely=0.5, relx=0.3)

    rt.mainloop()

def fetching_Rider_details():
    rrrt = Tk()
    q = 0
    z = 1

    import obj

    details = obj.ft

    rrrt.title("FETCH RIDER DETAILS")
    rrrt.geometry("800x500")
    rrrt.configure(bg='lightblue')

    rrt = details.fetch_Rider_details()

    tq = Text(rrrt, height=25, width=80)
    d = details.fetch_Rider_details()
    tq.place(relx=0.1, rely=0.1)

    q = 0
    z = 1
    tq.insert(END, "NAME")
    tq.insert(END, "\t\t")
    tq.insert(END, "PHONE NUMBER")
    tq.insert(END, "\n\n")
    while (q < len(details.fetch_Rider_details())):
        tq.insert(END, d[q])
        tq.insert(END, "\t\t")
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


    rrrt.mainloop()

def update_rider():
    rt=Tk()
    rt.geometry("500x400")
    rt.configure(bg='lightblue')
    rt.title("UPDATE RIDER DETAILS")
    def prt():
        var = en.get()
        var2 = en1.get()
        phoneno=int(en2.get())

        objj= obj.ft
        objj.update_data_rider(var,var2,phoneno)

    tn = Label(rt, text="Name of old rider:")
    tn.place(relx=0.1, rely=0.1)
    t = Label(rt, text="Name of new rider:")
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

def del_delivery_boy():
    rt=Tk()
    rt.geometry("500x400")
    rt.configure(bg='lightblue')
    rt.title("DELETE DELIVERY BOY")
    def prt():
        var=en.get()
        #print(var)
        objj= obj.ft
        objj.delete_data_rider_foods(var)

    t=Label(rt,text="Name of rider to delete: ")

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
root.title("DELIVERY")
root.configure(bg='lightblue')
Label(root, width="300", text="DELIVERY DETAILS", bg="orange", fg="white").pack()
btn1=Button(root,text="INSERT RIDER",command=insert_Riders, bg="orange")
btn1.place(relx=0.4,rely=0.2)
btn2=Button(root,text="FETCH RIDER",command=fetching_Rider_details, bg="orange")
btn2.place(relx=0.4,rely=0.3)
btn3=Button(root,text="UPDATE RIDER",command=update_rider, bg="orange")
btn3.place(relx=0.4,rely=0.4)
btn4=Button(root,text="DELETE RIDER",command=del_delivery_boy, bg="orange")
btn4.place(relx=0.4,rely=0.5)
def bk():
    root.destroy()
    import obj
    x = obj.ft

btn7=Button(root,text="BACK BUTTON",command=bk,bg="black",fg="white")
btn7.place(relx=0.4,rely=0.7)

root.mainloop()