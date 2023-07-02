from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import datetime
import tkinter
class LibraryManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Library Management System")
        self.root.geometry("1550x800+0+0")
        
        self.member_var=StringVar()
        self.prn_var=StringVar()
        self.id_var=StringVar()
        self.firstname_var=StringVar()
        self.lastname_var=StringVar()
        self.address1_var=StringVar()
        self.address2_var=StringVar()
        self.postcode_var=StringVar()
        self.mobile_var=StringVar()
        self.bookid_var=StringVar()
        self.booktitle_var=StringVar()
        self.author_var=StringVar()
        self.databorrowed=StringVar()
        self.datedue=StringVar()
        self.daysonbook=StringVar()
        self.lateratefine_var=StringVar()
        self.dateoverdue=StringVar()
        self.finallprice=StringVar()
        
        
        lbltitle=Label(self.root,text="LIBRARY MANAGEMENT SYSTEM ",bg="tomato",fg="green", bd=15,relief=RIDGE,font=("times new roman",36,"bold"),padx=2,pady=6)
        lbltitle.pack(side=TOP,fill=X)
        
        frame=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="tomato")
        frame.place(x=0,y=100,width=1530,height=430)
        
        DataFrameLeft=LabelFrame(frame,text="Library Membership Information",bg="powder blue",fg="green", bd=10,relief=RIDGE,font=("times new roman",25,"bold"),padx=2,pady=6)
        DataFrameLeft.place(x=0,y=5,width=900,height=400)
        
        lblMember=Label(DataFrameLeft,bg="powder blue",text="Member Type",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblMember.grid(row=0,column=0,sticky=W)
        
        comMember=ttk.Combobox(DataFrameLeft,font=("times new roman",15,"bold"),textvariable=self.member_var,width=27,state="readonly")
        comMember["value"]=("Admin Staff","Student","Lacturer")
        comMember.grid(row=0,column=1)
        
        lblPRN_No=Label(DataFrameLeft,font=("arial",12,"bold"),text="PRN No:",padx=2,pady=6,bg="powder blue")
        lblPRN_No.grid(row=1,column=0,sticky=W)
        
        txtPRN_NO=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.prn_var,width=29)
        txtPRN_NO.grid(row=1,column=1)
        
        lblTitle=Label(DataFrameLeft,font=("arial",12,"bold"),text="ID No:",padx=2,pady=6,bg="powder blue")
        lblTitle.grid(row=2,column=0,sticky=W)
        
        txtTitle=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.id_var,width=29)
        txtTitle.grid(row=2,column=1)
        
        lblFirstName=Label(DataFrameLeft,font=("arial",12,"bold"),text="FirstName",padx=2,pady=6,bg="powder blue")
        lblFirstName.grid(row=3,column=0,sticky=W)
        
        txtFirstName=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.firstname_var,width=29)
        txtFirstName.grid(row=3,column=1)
        
        lblLastName=Label(DataFrameLeft,font=("arial",12,"bold"),text="LastName",padx=2,pady=6,bg="powder blue")
        lblLastName.grid(row=4,column=0,sticky=W)
        
        txtLastName=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.lastname_var,width=29)
        txtLastName.grid(row=4,column=1)
        
          
        lblAddress1=Label(DataFrameLeft,font=("arial",12,"bold"),text="Address1",padx=2,pady=6,bg="powder blue")
        lblAddress1.grid(row=5,column=0,sticky=W)
        
        txtAddress1=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.address1_var,width=29)
        txtAddress1.grid(row=5,column=1)
        
        lblAddress2=Label(DataFrameLeft,font=("arial",12,"bold"),text="Address2",padx=2,pady=6,bg="powder blue")
        lblAddress2.grid(row=6,column=0,sticky=W)
        
        txtAddress2=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.address2_var,width=29)
        txtAddress2.grid(row=6,column=1)
        
        lblPostCode=Label(DataFrameLeft,font=("arial",12,"bold"),text="PostCode",padx=2,pady=6,bg="powder blue")
        lblPostCode.grid(row=7,column=0,sticky=W)
        
        txtPostCode=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.postcode_var,width=29)
        txtPostCode.grid(row=7,column=1)
        
        lblMobile=Label(DataFrameLeft,font=("arial",12,"bold"),text="Mobile",padx=2,pady=6,bg="powder blue")
        lblMobile.grid(row=8,column=0,sticky=W)
        
        txtMobile=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.mobile_var,width=29)
        txtMobile.grid(row=8,column=1)
        
        lblBookId=Label(DataFrameLeft,font=("arial",12,"bold"),text="BookId",padx=2,pady=6,bg="powder blue")
        lblBookId.grid(row=0,column=2,sticky=W)
        
        txtBookId=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.bookid_var,width=29)
        txtBookId.grid(row=0,column=3)
        
        lblBookTitle=Label(DataFrameLeft,font=("arial",12,"bold"),text="BookTitle",padx=2,pady=6,bg="powder blue")
        lblBookTitle.grid(row=1,column=2,sticky=W)
        
        txtBookTitle=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.booktitle_var,width=29)
        txtBookTitle.grid(row=1,column=3)
        
        lblAuthor=Label(DataFrameLeft,font=("arial",12,"bold"),text="Author Name",padx=2,pady=6,bg="powder blue")
        lblAuthor.grid(row=2,column=2,sticky=W)
        
        txtAuthor=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.author_var,width=29)
        txtAuthor.grid(row=2,column=3)
        
        lblDataBorrowed=Label(DataFrameLeft,font=("arial",12,"bold"),text="DataBorrowed",padx=2,pady=6,bg="powder blue")
        lblDataBorrowed.grid(row=3,column=2,sticky=W)
        
        txtDataBorrowed=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.databorrowed,width=29)
        txtDataBorrowed.grid(row=3,column=3)
        
        lblDateDue=Label(DataFrameLeft,font=("arial",12,"bold"),text="Date Due",padx=2,pady=6,bg="powder blue")
        lblDateDue.grid(row=4,column=2,sticky=W)
        
        txtDateDue=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.datedue,width=29)
        txtDateDue.grid(row=4,column=3)
        
        lblDayOnBook=Label(DataFrameLeft,font=("arial",12,"bold"),text="Days On Book:",padx=2,pady=6,bg="powder blue")
        lblDayOnBook.grid(row=5,column=2,sticky=W)
        
        txtDayOnBook=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.daysonbook,width=29)
        txtDayOnBook.grid(row=5,column=3)
        
        lblLateReturnFine=Label(DataFrameLeft,font=("arial",12,"bold"),text="Late Return Fine:",padx=2,pady=6,bg="powder blue")
        lblLateReturnFine.grid(row=6,column=2,sticky=W)
        
        txtLateReturnFine=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.lateratefine_var,width=29)
        txtLateReturnFine.grid(row=6,column=3)
        
        lblDateOverdate=Label(DataFrameLeft,font=("arial",12,"bold"),text="Date Over Due:",padx=2,pady=6,bg="powder blue")
        lblDateOverdate.grid(row=7,column=2,sticky=W)
        
        txtDateOverdate=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.dateoverdue,width=29)
        txtDateOverdate.grid(row=7,column=3)
        
        lblActualPrice=Label(DataFrameLeft,font=("arial",12,"bold"),text="Actual Price:",padx=2,pady=6,bg="powder blue")
        lblActualPrice.grid(row=8,column=2,sticky=W)
        
        txtActualPrice=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.finallprice,width=29)
        txtActualPrice.grid(row=8,column=3)
        
        DataFrameRight=LabelFrame(frame,text="Book Details",bg="powder blue",fg="green", bd=10,relief=RIDGE,font=("times new roman",25,"bold"),padx=2,pady=6)
        DataFrameRight.place(x=910,y=5,width=550,height=400)
        
       
        
        
        
        self.txtBox=Text(DataFrameRight,font=("arial",12,"bold"),width=32,height=16,padx=2,pady=6)
        self.txtBox.grid(row=0,column=2)
        
        listScrollbar=Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0,column=1,sticky="ns")
        
        
        listBooks=['The Namesake',' Clear Light of Day','Jaya','The God of Small Things','Midnight’s Children','A Suitable Boy','Train to Pakistan','The White Tiger','The Blue Umbrella','The Palace of Illusions','Malgudi Days','Godaan','The Shiva Trilogy','The Great Indian Novel','Gitanjali','Magical Rings','Gaussian']
        
        
        def SelectBook(event=""):
            value=str(listBox.get(listBox.curselection()))
            if(value=='The Namesake'):
                 self.bookid_var.set("BKID5454")
                 self.booktitle_var.set("The Namesake")
                 self.author_var.set("Jhumpa Lahiri")
                  
                 d1=datetime.date.today()
                 d2=datetime.timedelta(days=15)
                 d3=d1+d2
                 self.databorrowed.set(d1)
                 self.datedue.set(d3)
                 self.daysonbook.set(7)
                 self.lateratefine_var.set("Rs.50")
                 self.dateoverdue.set("NO")
                 self.finallprice.set("Rs. 650")
               
            elif(value==' Clear Light of Day'):
                 self.bookid_var.set("BKID5458")
                 self.booktitle_var.set("Clear Light of Day")
                 self.author_var.set("Anita desai")
           
                 d1=datetime.date.today()
                 d2=datetime.timedelta(days=15)
                 d3=d1+d2
                 self.databorrowed.set(d1)
                 self.datedue.set(d3)
                 self.daysonbook.set(10)
                 self.lateratefine_var.set("Rs.50")
                 
                 self.dateoverdue.set("NO")
                 self.finallprice.set("Rs. 900")
            
            elif(value=='Jaya'):
                 self.bookid_var.set("BKID5590")
                 self.booktitle_var.set("Jaya")
                 self.author_var.set(" Devdutt Pattanaik")
           
                 d1=datetime.date.today()
                 d2=datetime.timedelta(days=20)
                 d3=d1+d2
                 self.databorrowed.set(d1)
                 self.datedue.set(d3)
                 self.daysonbook.set(12)
                 self.lateratefine_var.set("Rs.70")
                 self.dateoverdue.set("NO")
                 self.finallprice.set("Rs. 400")
            
            elif(value=='Midnight’s Children'):
                 self.bookid_var.set("BKID560")
                 self.booktitle_var.set("Midnight’s Children")
                 self.author_var.set("Salman Rushdie")
           
                 d1=datetime.date.today()
                 d2=datetime.timedelta(days=20)
                 d3=d1+d2
                 self.databorrowed.set(d1)
                 self.datedue.set(d3)
                 self.daysonbook.set(15)
                 self.lateratefine_var.set("Rs.70")
                 self.dateoverdue.set("NO")
                 self.finallprice.set("Rs. 400")
            
            elif(value=='The God of Small Things'):
                 self.bookid_var.set("BKID578")
                 self.booktitle_var.set("The God of Small Things")
                 self.author_var.set("Michiko kakutani")
           
                 d1=datetime.date.today()
                 d2=datetime.timedelta(days=15)
                 d3=d1+d2
                 self.databorrowed.set(d1)
                 self.datedue.set(d3)
                 self.daysonbook.set(12)
                 self.lateratefine_var.set("Rs.90")
                 self.dateoverdue.set("NO")
                 self.finallprice.set("Rs. 600") 
                 
            elif(value=='A Suitable Boy'):
                 self.bookid_var.set("BKID492")
                 self.booktitle_var.set("A Suitable Boy")
                 self.author_var.set("Vikram seth")
           
                 d1=datetime.date.today()
                 d2=datetime.timedelta(days=20)
                 d3=d1+d2
                 self.databorrowed.set(d1)
                 self.datedue.set(d3)
                 self.daysonbook.set(14)
                 self.lateratefine_var.set("Rs.40")
                 self.dateoverdue.set("NO")
                 self.finallprice.set("Rs. 500") 
                 
            elif(value=='Train to Pakistan'):
                 self.bookid_var.set("BKID361")
                 self.booktitle_var.set("Train to Pakistan")
                 self.author_var.set("Khushwant singh")
           
                 d1=datetime.date.today()
                 d2=datetime.timedelta(days=20)
                 d3=d1+d2
                 self.databorrowed.set(d1)
                 self.datedue.set(d3)
                 self.daysonbook.set(8)
                 self.lateratefine_var.set("Rs.60")
                 self.dateoverdue.set("NO")
                 self.finallprice.set("Rs. 700")  
            
            elif(value=='The White Tiger'):
                 self.bookid_var.set("BKID690")
                 self.booktitle_var.set("The White Tiger")
                 self.author_var.set("Aravind Adiga")
           
                 d1=datetime.date.today()
                 d2=datetime.timedelta(days=20)
                 d3=d1+d2
                 self.databorrowed.set(d1)
                 self.datedue.set(d3)
                 self.daysonbook.set(9)
                 self.lateratefine_var.set("Rs.40")
                 self.dateoverdue.set("NO")
                 self.finallprice.set("Rs. 500")  
                 
            elif(value=='The Blue Umbrella'):
                 self.bookid_var.set("BKID479")
                 self.booktitle_var.set("The Blue Umbrella")
                 self.author_var.set("Ruskin Bond")
           
                 d1=datetime.date.today()
                 d2=datetime.timedelta(days=20)
                 d3=d1+d2
                 self.databorrowed.set(d1)
                 self.datedue.set(d3)
                 self.daysonbook.set(11)
                 self.lateratefine_var.set("Rs.80")
                 self.dateoverdue.set("NO")
                 self.finallprice.set("Rs. 900") 
             
                  
            elif(value=='The Palace of Illusions'):
                 self.bookid_var.set("BKID720")
                 self.booktitle_var.set("The Palace of Illusions")
                 self.author_var.set("Draupadi")
           
                 d1=datetime.date.today()
                 d2=datetime.timedelta(days=20)
                 d3=d1+d2
                 self.databorrowed.set(d1)
                 self.datedue.set(d3)
                 self.daysonbook.set(10)
                 self.lateratefine_var.set("Rs.40")
                 self.dateoverdue.set("NO")
                 self.finallprice.set("Rs. 500") 
               
                  
            elif(value=='Malgudi Days'):
                 self.bookid_var.set("BKID200")
                 self.booktitle_var.set("Malgudi Days")
                 self.author_var.set("R.K. Narayan")
           
                 d1=datetime.date.today()
                 d2=datetime.timedelta(days=20)
                 d3=d1+d2
                 self.databorrowed.set(d1)
                 self.datedue.set(d3)
                 self.daysonbook.set(15)
                 self.lateratefine_var.set("Rs.70")
                 self.dateoverdue.set("NO")
                 self.finallprice.set("Rs. 800")       
             
              
            elif(value=='Godaan'):
                 self.bookid_var.set("BKID375")
                 self.booktitle_var.set("Godaan")
                 self.author_var.set("premchand")
           
                 d1=datetime.date.today()
                 d2=datetime.timedelta(days=20)
                 d3=d1+d2
                 self.databorrowed.set(d1)
                 self.datedue.set(d3)
                 self.daysonbook.set(8)
                 self.lateratefine_var.set("Rs.30")
                 self.dateoverdue.set("NO")
                 self.finallprice.set("Rs. 470")       
             
            elif(value=='The Shiva Trilogy'):
                 self.bookid_var.set("BKID650")
                 self.booktitle_var.set("The Shiva Trilogy")
                 self.author_var.set("Amish Tripathy")
           
                 d1=datetime.date.today()
                 d2=datetime.timedelta(days=20)
                 d3=d1+d2
                 self.databorrowed.set(d1)
                 self.datedue.set(d3)
                 self.daysonbook.set(15)
                 self.lateratefine_var.set("Rs.50")
                 self.dateoverdue.set("NO")
                 self.finallprice.set("Rs. 580")       
             
            elif(value=='The Great Indian Novel'):
                 self.bookid_var.set("BKID728")
                 self.booktitle_var.set("The Great Indian Novel")
                 self.author_var.set("Shashi Tharoor")
           
                 d1=datetime.date.today()
                 d2=datetime.timedelta(days=20)
                 d3=d1+d2
                 self.databorrowed.set(d1)
                 self.datedue.set(d3)
                 self.daysonbook.set(14)
                 self.lateratefine_var.set("Rs.70")
                 self.dateoverdue.set("NO")
                 self.finallprice.set("Rs. 600")       
             
             
            elif(value=='Gitanjali'):
                 self.bookid_var.set("BKID539")
                 self.booktitle_var.set("Gitanjali")
                 self.author_var.set("Rabindranath Tagore")
           
                 d1=datetime.date.today()
                 d2=datetime.timedelta(days=20)
                 d3=d1+d2
                 self.databorrowed.set(d1)
                 self.datedue.set(d3)
                 self.daysonbook.set(8)
                 self.lateratefine_var.set("Rs.45")
                 self.dateoverdue.set("NO")
                 self.finallprice.set("Rs. 475")   
                 
            elif(value=='Gaussian'):
                 self.bookid_var.set("BKID578")
                 self.booktitle_var.set("Gaussian")
                 self.author_var.set("Michiko kakutani")
           
                 d1=datetime.date.today()
                 d2=datetime.timedelta(days=15)
                 d3=d1+d2
                 self.databorrowed.set(d1)
                 self.datedue.set(d3)
                 self.daysonbook.set(12)
                 self.lateratefine_var.set("Rs.90")
                 self.dateoverdue.set("NO")
                 self.finallprice.set("Rs. 600")   
            
            elif(value=='Magical Rings'):
                 self.bookid_var.set("BKID720")
                 self.booktitle_var.set("Magical Rings")
                 self.author_var.set("Draupadi")
           
                 d1=datetime.date.today()
                 d2=datetime.timedelta(days=20)
                 d3=d1+d2
                 self.databorrowed.set(d1)
                 self.datedue.set(d3)
                 self.daysonbook.set(10)
                 self.lateratefine_var.set("Rs.40")
                 self.dateoverdue.set("NO")
                 self.finallprice.set("Rs. 500") 
                    
             
                
        listBox=Listbox(DataFrameRight,font=("arial",12,"bold"),width=20 ,height=16)
        listBox.bind("<<ListboxSelect>>",SelectBook)
        listBox.grid(row=0,column=0,padx=4)
        listScrollbar.config(command=listBox.yview)
        
        for item in listBooks:
            listBox.insert(END,item)
        
        
        #====================================Buttons Frame =======================================
        
        Framebutton=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        Framebutton.place(x=0,y=530,width=1530,height=60)
        
        btnAddData=Button(Framebutton,command=self.adda_data,text="Add Data",font=("arial",12,"bold"),width=20,bg="lightgreen",fg="black")
        btnAddData.grid(row=0,column=0)
        
        btnAddData=Button(Framebutton,command=self.get_curser,text="Fetch data",font=("arial",12,"bold"),width=20,bg="lightgreen",fg="black")
        btnAddData.grid(row=0,column=1)
        
        btnAddData=Button(Framebutton,command=self.showData,text="Show Data",font=("arial",12,"bold"),width=20,bg="lightgreen",fg="black")
        btnAddData.grid(row=0,column=2)
        
        btnAddData=Button(Framebutton,command=self.update,text="Update",font=("arial",12,"bold"),width=20,bg="lightgreen",fg="black")
        btnAddData.grid(row=0,column=3)
        
        btnAddData=Button(Framebutton,text="Delete",command=self.delete,font=("arial",12,"bold"),width=20,bg="lightgreen",fg="black")
        btnAddData.grid(row=0,column=4)
        
        btnAddData=Button(Framebutton,text="Reset",command=self.reset,font=("arial",12,"bold"),width=20,bg="lightgreen",fg="black")
        btnAddData.grid(row=0,column=5)
        
        btnAddData=Button(Framebutton,text="Exit",command=self.iExit,font=("arial",12,"bold"),width=20,bg="lightgreen",fg="black")
        btnAddData.grid(row=0,column=6)
        
        #====================================Buttons Frame =======================================
        
        FrameDetails=Frame(self.root,bd=6,relief=RIDGE,padx=20,bg="powder blue")
        FrameDetails.place(x=0,y=600,width=1530,height=200)
        
        Table_frame=Frame(FrameDetails,bd=6,relief=RIDGE,bg="powder blue")
        Table_frame.place(x=0,y=2,width=1460,height=190)
         
        xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)
        self.library_table=ttk.Treeview(Table_frame,column=("membertype","prnno","title","firstname","lastname","adress1","adress2","postid","mobile","bookid","booktitle","author","databorrowed","datedue","days","latereturfine","dateoverdue","finalprice"),xscrollcommand=xscroll.set,yscrollcommand=xscroll.set)
        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)
        
        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)
        self.library_table.heading("membertype",text="Member Type")
        self.library_table.heading("prnno",text="PRN No.")
        self.library_table.heading("title",text="Roll No.")
        self.library_table.heading("firstname",text="First Name")
        self.library_table.heading("lastname",text="Last Name")
        self.library_table.heading("adress1",text="Address1")
        self.library_table.heading("adress2",text="Address2")
        self.library_table.heading("postid",text="Post ID")
        self.library_table.heading("mobile",text="Mobile Number")
        self.library_table.heading("bookid",text="Book ID")
        self.library_table.heading("booktitle",text="Book Title")
        self.library_table.heading("author",text="Author")
        self.library_table.heading("databorrowed",text="Data Of Borrowed")
        self.library_table.heading("datedue",text="Date Due")
        self.library_table.heading("days",text="DaysOnBook")
        self.library_table.heading("latereturfine",text="LateReturnFine")
        self.library_table.heading("dateoverdue",text="DateOverDue")
        self.library_table.heading("finalprice",text="Final Price")
        
        self.library_table["show"]="headings";
        self.library_table.pack(fill=BOTH,expand=1)
        
        self.library_table.column("membertype",width=100)
        self.library_table.column("prnno",width=100)
        self.library_table.column("title",width=100)
        self.library_table.column("firstname",width=100)
        self.library_table.column("lastname",width=100)
        self.library_table.column("adress1",width=100)
        self.library_table.column("adress2",width=100)
        self.library_table.column("postid",width=100)
        self.library_table.column("mobile",width=100)
        self.library_table.column("bookid",width=100)
        self.library_table.column("booktitle",width=100)
        self.library_table.column("author",width=100)
        self.library_table.column("databorrowed",width=100)
        self.library_table.column("datedue",width=100)
        self.library_table.column("days",width=100)
        self.library_table.column("latereturfine",width=100)
        self.library_table.column("dateoverdue",width=100)
        self.library_table.column("finalprice",width=100)
        
        self.fatch_data()
        self.library_table.bind("<<ButtonRelease-1>>",self.get_curser)
        
    def adda_data(self):
             conn=mysql.connector.connect(host="localhost",username="root",password="root5",database="world")
             my_cursor=conn.cursor()
             my_cursor.execute("insert into library values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.member_var.get(),self.prn_var.get(),self.id_var.get(),self.firstname_var.get(),self.lastname_var.get(),self.address1_var.get(),self.address2_var.get(),self.postcode_var.get(),self.mobile_var.get(),self.bookid_var.get(),self.booktitle_var.get(),self.author_var.get(),self.databorrowed.get(),self.datedue.get(),self.daysonbook.get(),self.lateratefine_var.get(),self.dateoverdue.get(),self.finallprice.get()))
             conn.commit()
             self.fatch_data()
             conn.close()
             
             messagebox.showinfo("Success","Member Has Been inserted successfully")
             
    def update(self):
             conn=mysql.connector.connect(host="localhost",username="root",password="root5",database="world")
             my_cursor=conn.cursor()
             my_cursor.execute("update library set Member=%s,ID=%s,FirstName=%s,LastName=%s,Address1=%s,Address2=%s,Postid=%s,Mobile=%s,Bookid=%s,Booktitle=%s,Author=%s,databorrowed=%s,datedue=%s,daysonbook=%s,lateratefine=%s,dateoverdue=%s,finallprice=%s where PRN_NO=%s",(self.member_var.get(),self.id_var.get(),self.firstname_var.get(),self.lastname_var.get(),self.address1_var.get(),self.address2_var.get(),self.postcode_var.get(),self.mobile_var.get(),self.bookid_var.get(),self.booktitle_var.get(),self.author_var.get(),self.databorrowed.get(),self.datedue.get(),self.daysonbook.get(),self.lateratefine_var.get(),self.dateoverdue.get(),self.finallprice.get(),self.prn_var.get()))
             conn.commit()
             self.fatch_data()
             self.reset()
             conn.close()
             
             messagebox.showinfo("Success","Member has been updated")
             
    def fatch_data(self):
             conn=mysql.connector.connect(host="localhost",username="root",password="root5",database="world")
             my_cursor=conn.cursor()
             my_cursor.execute("select * from library")
             rows=my_cursor.fetchall()
             
             if len(rows)!=0:
               self.library_table.delete(*self.library_table.get_children())
               for i in rows:
                   self.library_table.insert("",END,values=i)
             conn.commit()
             conn.close()  
             
    def get_curser(self,event=""):
        curser_row=self.library_table.focus()
        content=self.library_table.item(curser_row)
        row=content['values']
        
        self.member_var.set(row[0]),
        self.prn_var.set(row[1]),
        self.id_var.set(row[2]),
        self.firstname_var.set(row[3]),
        self.lastname_var.set(row[4]),
        self.address1_var.set(row[5]),
        self.address2_var.set(row[6]),
        self.postcode_var.set(row[7]),
        self.mobile_var.set(row[8]),
        self.bookid_var.set(row[9]),
        self.booktitle_var.set(row[10]),
        self.author_var.set(row[11]),
        self.databorrowed.set(row[12]),
        self.datedue.set(row[13]),
        self.daysonbook.set(row[14]),
        self.lateratefine_var.set(row[15]),
        self.dateoverdue.set(row[16]),
        self.finallprice.set(row[17]) 

    def showData(self):   
        self.txtBox.insert(END,"Member Type\t \t"+self.member_var.get()+"\n")  
        self.txtBox.insert(END,"prn no.\t \t"+self.prn_var.get()+"\n")
        self.txtBox.insert(END,"ID No:\t \t"+self.firstname_var.get()+"\n")
        self.txtBox.insert(END,"FirstName:\t \t"+self.firstname_var.get()+"\n")
        self.txtBox.insert(END,"LastName:\t \t"+self.lastname_var.get()+"\n")
        self.txtBox.insert(END,"Address1: \t \t"+self.address1_var.get()+"\n")
        self.txtBox.insert(END,"Address2: \t \t"+self.address2_var.get()+"\n")
        self.txtBox.insert(END,"Post Code:\t \t"+self.postcode_var.get()+"\n")
        self.txtBox.insert(END,"Mobile No.\t \t"+self.mobile_var.get()+"\n")
        self.txtBox.insert(END,"Book ID: \t \t"+self.bookid_var.get()+"\n")
        self.txtBox.insert(END,"Book Title: \t \t"+self.booktitle_var.get()+"\n")
        self.txtBox.insert(END,"Author:\t \t"+self.author_var.get()+"\n")
        self.txtBox.insert(END,"DataBorrowed:\t \t"+self.databorrowed.get()+"\n")
        self.txtBox.insert(END,"DataDue:\t \t"+self.datedue.get()+"\n")
        self.txtBox.insert(END,"DaysOnBook:\t \t"+self.daysonbook.get()+"\n")
        self.txtBox.insert(END,"LateRateFine:\t \t"+self.lateratefine_var.get()+"\n")
        self.txtBox.insert(END,"DateOverDue: \t \t"+self.dateoverdue.get()+"\n")
        self.txtBox.insert(END,"FinalPrice: \t \t"+self.finallprice.get()+"\n")
    def reset(self):
        self.member_var.set("")
        self.prn_var.set("")
        self.id_var.set("")
        self.firstname_var.set("")
        self.lastname_var.set("")
        self.address1_var.set("")
        self.address2_var.set("")
        self.postcode_var.set("")
        self.mobile_var.set("")
        self.bookid_var.set("")
        self.booktitle_var.set("")
        self.author_var.set("")
        self.databorrowed.set("")
        self.datedue.set("")
        self.daysonbook.set("")
        self.lateratefine_var.set("")
        self.dateoverdue.set("")
        self.finallprice.set("")
        self.txtBox.delete("1.0",END)  
        
    def iExit(self):
        iExit=tkinter.messagebox.askyesno("LIbrary management System","Do you want to exit")
        if iExit>0:
            self.root.destroy()
            return 
    def delete(self):
        if self.prn_var.get()=="" or self.id_var.get=="":
             messagebox.showerror("Error","First Select the Member")
        else:
             conn=mysql.connector.connect(host="localhost",username="root",password="root5",database="world")
             my_cursor=conn.cursor()
             query="delete from library where PRN_No=%s"
             value=(self.prn_var.get(),)
             my_cursor.execute(query,value)

             conn.commit()
             self.fatch_data()
             self.reset()
             conn.close()
             
             messagebox.showinfo("Success","Member has been deleted")
if __name__ == "__main__":
      root=Tk()
      obj=LibraryManagementSystem(root)
      root.mainloop()
      
                                        
     
       

     
     
     
     
    
     
     
  
  
  
  
        
        
        
          