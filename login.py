from tkinter import *
import cx_Oracle 


class Main():
    def __init__(self,parent):
        self.parent = parent
        self.parent.title('Hospital Management')

        self.page = StringVar()
        self.loginName = StringVar()
        self.loginPass = StringVar()
        self.signinName = StringVar()
        self.signinPass = StringVar()
        self.sts=StringVar()
        self.searchName = StringVar()
        self.searchwor_no = StringVar()
        self.addName = StringVar()
        self.addroom = StringVar()
        self.addfloor = StringVar()
        self.adddiseas = StringVar()
        self.addage = StringVar()
        self.adddrname = StringVar()
        self.addstatus = StringVar()
        self.adddoa = StringVar()
        self.adddod = StringVar()
        
        
        self.createWidgets()
        self.showLogin()

    def createWidgets(self):
        Label(self.parent, textvariable=self.page, font=("",20)).pack()
        frame1=Frame(self.parent,background='#003333')
        Label(frame1,text='Name',fg="white",background='#003333').grid(sticky = W)
        Entry(frame1,textvariable = self.loginName,fg="green").grid(row=0,column=1,pady=10,padx=10)
        Label(frame1,text='Password',fg="white",background='#003333').grid(sticky= W)
        Entry(frame1,textvariable = self.loginPass, show='*',fg="green").grid(row=1,column=1)
        Button(frame1,text='Login',command=self.login, font=("",15)).grid(row=2,column=1,pady=10,ipadx=20)
        Button(frame1,text='Sign in',command=self.signIn).grid(row=3,column=1,pady=10,ipadx=20)
        frame1.pack(ipadx=100,pady=75)
        frame2=Frame(self.parent,background='#003333')
        Label(frame2,text='Name',fg="white",background='#003333').grid(sticky = W)
        Entry(frame2,textvariable = self.signinName).grid(row=0,column=1,pady=10,padx=10)
        Label(frame2,text='Password',fg="white",background='#003333').grid(sticky= W)
        Entry(frame2,textvariable = self.signinPass, show='*').grid(row=1,column=1)
        Button(frame2,text='Sign in',command=self.create, font=("",13)).grid(row=2,column=1,pady=10,ipadx=20)
        Button(frame2,text='Back',command=self.showLogin).grid(row=3,column=1,pady=10,ipadx=20)
        frame3=Frame(self.parent,background='#003333')
        
        Label(frame3,text='Name',fg="white",background='#003333').grid(sticky = W)
        Entry(frame3,textvariable = self.searchName,fg="green").grid(row=0,column=1,pady=10,padx=10)
        Button(frame3,text='Search',command=self.search, font=("",15)).grid(row=0,column=2,pady=10,ipadx=20)
        Label(frame3,text='Room no',fg="white",background='#003333').grid(sticky = W)
        Label(frame3,text='Floor no',fg="white",background='#003333').grid(sticky = W)
        Label(frame3,text='Diseas',fg="white",background='#003333').grid(sticky = W)
        Label(frame3,text='Age',fg="white",background='#003333').grid(sticky = W)
        Label(frame3,text='Dr Name',fg="white",background='#003333').grid(sticky = W)
        Label(frame3,text='Status',fg="white",background='#003333').grid(sticky = W)
        Label(frame3,text='Date of charged',fg="white",background='#003333').grid(sticky = W)
        Label(frame3,text='Date of discharged',fg="white",background='#003333').grid(sticky = W)
        Button(frame3,text='Add Patient',command=self.add,).grid(row=10,column=1,pady=5,ipadx=10)
        Button(frame3,text='Delete',command=self.delete).grid(row=11,column=1,pady=10,ipadx=20)

        
        frame4=Frame(self.parent,background='#003333')
        Label(frame4,text='Name',fg="white",background='#003333').grid(sticky = W)
        Entry(frame4,textvariable = self.addName,fg="green").grid(row=0,column=1,pady=10,padx=10)
        Label(frame4,text='Room no',fg="white",background='#003333').grid(sticky = W)
        Entry(frame4,textvariable = self.addroom,fg="green").grid(row=1,column=1,pady=10,padx=10)
        Label(frame4,text='Floor no',fg="white",background='#003333').grid(sticky = W)
        Entry(frame4,textvariable = self.addfloor,fg="green").grid(row=2,column=1,pady=10,padx=10)
        Label(frame4,text='Diseas',fg="white",background='#003333').grid(sticky = W)
        Entry(frame4,textvariable = self.adddiseas,fg="green").grid(row=3,column=1,pady=10,padx=10)
        Label(frame4,text='Age',fg="white",background='#003333').grid(sticky = W)
        Entry(frame4,textvariable = self.addage,fg="green").grid(row=4,column=1,pady=10,padx=10)
        Label(frame4,text='Dr Name',fg="white",background='#003333').grid(sticky = W)
        Entry(frame4,textvariable = self.adddrname,fg="green").grid(row=5,column=1,pady=10,padx=10)
        Label(frame4,text='Status',fg="white",background='#003333').grid(sticky = W)
        Entry(frame4,textvariable = self.addstatus,fg="green").grid(row=6,column=1,pady=10,padx=10)
        Label(frame4,text='Date of charged',fg="white",background='#003333').grid(sticky = W)
        Entry(frame4,textvariable = self.adddoa,fg="green").grid(row=7,column=1,pady=10,padx=10)
        Label(frame4,text='Date of discharged',fg="white",background='#003333').grid(sticky = W)
        Entry(frame4,textvariable = self.adddod,fg="green").grid(row=8,column=1,pady=10,padx=10)
        Button(frame4,text='Add',command=self.addele, font=("",15)).grid(row=10,column=1,pady=10,ipadx=20)
        Button(frame4,text='Back',command=self.showLogedagain).grid(row=11,column=1,pady=10,ipadx=20)
        
        
        self.loginFrame=frame1
        self.signinFrame=frame2
        self.LogedFrame=frame3
        self.addFrame=frame4
        Label(self.parent,textvariable=self.sts).pack()




    def login(self):
        
        name=self.loginName.get()
        password=self.loginPass.get()
        try:
            conn = cx_Oracle.connect('keval','pass@123',cx_Oracle.makedsn('localhost',1521,'XE'))
            c = conn.cursor()
            c.execute("select * from login where username ='{}' and password ='{}'".format(name,password) )
            for row in c:
                self.showLoged()
            messagebox.showinfo("Information","Login successfull")
            conn.close()
        except Exception:
             messagebox.showerror("Error","incorrect name or password")

    
    def signIn(self):
        self.page.set('Sign In')
        self.loginFrame.pack_forget()
        self.signinFrame.pack(ipadx=100,pady=75)
        
    def showLogin(self):
        self.page.set('Log in')
        self.signinFrame.pack_forget()
        self.loginFrame.pack(ipadx=100,pady=75)

    def showLoged(self):
        self.page.set('Patient Detail')
        self.loginFrame.pack_forget()
        
        self.LogedFrame.pack(ipadx=100,pady=75)

    def showLogedagain(self):
        self.page.set('Patient Detail')
        self.addFrame.pack_forget()
        
        self.LogedFrame.pack(ipadx=100,pady=75)

    
        

    def create(self):
        name1=self.signinName.get()
        password1=self.signinPass.get()
        try:
            conn = cx_Oracle.connect('keval','pass@123',cx_Oracle.makedsn('localhost',1521,'XE'))
            c = conn.cursor()
            c.execute("insert into login values('{}','{}')".format(name1,password1) )
            conn.commit()
            conn.close()
            messagebox.showinfo("Information","signin successfull")
            self.showLogin()
            
        except Exception:
            messagebox.showerror("error","incorrect name or password")


    def search(self):
        name2=self.searchName.get()
        try:
            conn = cx_Oracle.connect('keval','pass@123',cx_Oracle.makedsn('localhost',1521,'XE'))
            c = conn.cursor()
            c.execute("select room_no from patient where name ='{}' ".format(name2) )
            rows = c.fetchall()
            e1=Entry(self.LogedFrame)
            e1.insert(END,rows[0])
            e1.grid(row=1,column=1,pady=10,padx=10)
            c.execute("select floor_no from patient where name ='{}' ".format(name2) )
            rows = c.fetchall()
            e2=Entry(self.LogedFrame)
            e2.insert(END,rows[0])
            e2.grid(row=2,column=1,pady=10,padx=10)
            c.execute("select diseas from patient where name ='{}' ".format(name2) )
            rows = c.fetchall()
            e3=Entry(self.LogedFrame)
            e3.insert(END,rows[0])
            e3.grid(row=3,column=1,pady=10,padx=10)
            c.execute("select age from patient where name ='{}' ".format(name2) )
            rows = c.fetchall()
            e4=Entry(self.LogedFrame)
            e4.insert(END,rows[0])
            e4.grid(row=4,column=1,pady=10,padx=10)
            c.execute("select dr_name from patient where name ='{}' ".format(name2) )
            rows = c.fetchall()
            e5=Entry(self.LogedFrame)
            e5.insert(END,rows[0])
            e5.grid(row=5,column=1,pady=10,padx=10)
            c.execute("select status from patient where name ='{}' ".format(name2) )
            rows = c.fetchall()
            e6=Entry(self.LogedFrame)
            e6.insert(END,rows[0])
            e6.grid(row=6,column=1,pady=10,padx=10)
            c.execute("select doa from patient where name ='{}' ".format(name2) )
            rows = c.fetchall()
            e7=Entry(self.LogedFrame)
            e7.insert(END,rows[0])
            e7.grid(row=7,column=1,pady=10,padx=10)
            c.execute("select dod from patient where name ='{}' ".format(name2) )
            rows = c.fetchall()
            e8=Entry(self.LogedFrame)
            e8.insert(END,rows[0])
            e8.grid(row=8,column=1,pady=10,padx=10)
            messagebox.showinfo("Information","patient found")
        except Exception:
            messagebox.showerror("error","pateint not found")
    def add(self):
        self.page.set('Add Details')
        
        self.LogedFrame.pack_forget()
        self.addFrame.pack(ipadx=100,pady=75)


    def addele(self):
        name3=self.addName.get()
        room=self.addroom.get()
        floor=self.addfloor.get()
        diseas=self.adddiseas.get()
        age=self.addage.get()
        drname=self.adddrname.get()
        status=self.addstatus.get()
        doa=self.adddoa.get()
        dod=self.adddod.get()
        try:
            conn = cx_Oracle.connect('keval','pass@123',cx_Oracle.makedsn('localhost',1521,'XE'))
            c = conn.cursor()
            c.execute("insert into patient values('{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(name3,room,floor,diseas,age,drname,status,doa,dod) )
            conn.commit()
            conn.close()
            messagebox.showinfo("Information","patient added successfull")
            self.showLogedagain()
            
        except(e):
            self.sts.set("e")
            
    def delete(self):
        name2=self.searchName.get()
        try:
            conn = cx_Oracle.connect('keval','pass@123',cx_Oracle.makedsn('localhost',1521,'XE'))
            c = conn.cursor()
            c.execute("delete from patient where name='{}'".format(name2)) 
            conn.commit()
            conn.close()
            messagebox.showinfo("Information","patient deleted successfull")
            self.showLogedagains()
        except(e):
            self.sts.set("e")

    def showLogedagains(self):
        self.page.set('Patient Detail')
        self.LogedFrame.pack_forget()
        self.LogedFrame.pack(ipadx=100,pady=75)
        

        



root=Tk()
root.configure(background='#003333')
Main(root)
root.mainloop()
    

        
