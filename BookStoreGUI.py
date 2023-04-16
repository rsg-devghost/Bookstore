from tkinter import *
from tkinter import ttk
#import mysql.connector


class BookStoreManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Book Store Management System")
        self.root.geometry("1550x800+0+0") #Dimensions of the GUI

        #Creating the customisation of the title block
        lbltitle = Label(self.root,text="Book Store Management System", bg="light blue",fg="grey", bd=20, relief=RIDGE, font=("Times New Roman",50,"bold"),padx=2,pady=6)
        lbltitle.pack(side=TOP,fill=X)

        #Inner Frame css
        frame = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="light blue")
        frame.place(x=0,y=130,width=1530,height=400)


        # ======================== Data Frame Left ============================#
        DataFrameLeft=LabelFrame(frame,text="Book Store Management System", bg="light blue",fg="grey",bd=12, relief=RIDGE, font=("Times New Roman",12,"bold"))
        DataFrameLeft.place(x=0,y=5,width=900,height=350)

        #Member Type DropDown
        lblMember = Label(DataFrameLeft,font=("arial",12,"bold"),bg="light blue",text="Member Type",padx=2,pady=6)
        lblMember.grid(row=0,column=0,sticky=W)

        #Dropdown options
        comMember=ttk.Combobox(DataFrameLeft,text="Member Type",font=("arial",12,"bold"),width=27,state="readonly")
        comMember["value"]=("Admin Staff","Student","Lecturer")
        comMember.grid(row=0,column=1)

        lblPRN_NO = Label(DataFrameLeft,bg="light blue",text="PRN_NO",font=("arial",12,"bold"),padx=2)
        lblPRN_NO.grid(row=1, column=0, sticky=W)
        #Entry Box
        txtPRN_NO = Entry(DataFrameLeft,font=("aerial", 13, "bold"),width=29)
        txtPRN_NO.grid(row=1,column=1)

        lblTitle = Label(DataFrameLeft,font=("arial", 12, "bold"),text="ID NO:",padx=2,pady=4,bg="light blue")
        lblTitle.grid(row=2, column=0, sticky=W)
        # Entry Box
        txtTitle = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=29)
        txtTitle.grid(row=2, column=1)

        lblFirstName = Label(DataFrameLeft, font=("arial", 12, "bold"), text="First Name", padx=2, pady=6, bg="light blue")
        lblFirstName.grid(row=3, column=0, sticky=W)
        # Entry Box
        txtFirstName = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=29)
        txtFirstName.grid(row=3, column=1)

        lblLastName = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Last Name", padx=2, pady=4, bg="light blue")
        lblLastName.grid(row=4, column=0, sticky=W)
        # Entry Box
        txtLastName = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=29)
        txtLastName.grid(row=4, column=1)

        lblAddress = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Address", padx=2, pady=6, bg="light blue")
        lblAddress.grid(row=5, column=0, sticky=W)
        # Entry Box
        txtAddress = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=29)
        txtAddress.grid(row=5, column=1)

        lblMobileNo = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Mobile NO", padx=2, pady=4, bg="light blue")
        lblMobileNo.grid(row=6, column=0, sticky=W)
        # Entry Box
        txtMobileNo = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=29)
        txtMobileNo.grid(row=6, column=1)

        lblTitle = Label(DataFrameLeft, font=("arial", 12, "bold"), text="ID NO:", padx=2, pady=4, bg="light blue")
        lblTitle.grid(row=0, column=2, sticky=W)
        # Entry Box
        txtPRN_NO = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=29)
        txtPRN_NO.grid(row=0, column=3)

        lblTitle = Label(DataFrameLeft, font=("arial", 12, "bold"), text="ID NO:", padx=2, pady=4, bg="light blue")
        lblTitle.grid(row=1, column=2, sticky=W)
        # Entry Box
        txtPRN_NO = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=29)
        txtPRN_NO.grid(row=1, column=3)

        lblTitle = Label(DataFrameLeft, font=("arial", 12, "bold"), text="ID NO:", padx=2, pady=4, bg="light blue")
        lblTitle.grid(row=2, column=2, sticky=W)
        # Entry Box
        txtPRN_NO = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=29)
        txtPRN_NO.grid(row=2, column=3)

        # =========Add more columns==========#


        #====================data frame right=======================
        DataFrameRight = LabelFrame(frame, text="Book Details", bg="light blue", fg="black", bd=12,relief=RIDGE, font=("arial", 12, "bold"),padx=20)
        DataFrameRight.place(x=870,y=5,width=580,height=350)

        self.txtBox = Text(DataFrameRight,font=("arial", 12, "bold"),width=32,height=16, padx=2, pady=6)
        self.txtBox.grid(row=0,column=2)

        listScrollbar=Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0,column=1,sticky="ns")

        # Books Name list
        listBox=[]
        listBox=Listbox(DataFrameRight,font=("arial", 12, "bold"),width=20,height=16)
        listBox.grid(row=0,column=0,padx=4)
        listScrollbar.config(command=listBox.yview)

        #for loop


        #============================== Buttons Frame ====================================#
        Framebutton=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="light blue")
        Framebutton.place(x=0,y=530,width=1530,height=70)

        btnAddData=Button(Framebutton,text="Add Data",font=("arial", 12, "bold"),width=23,bg="Grey",fg="white")
        btnAddData.grid(row=0,column=0)

        btnAddData = Button(Framebutton, text="Show Data", font=("arial", 12, "bold"), width=23, bg="Grey", fg="white")
        btnAddData.grid(row=0, column=1)

        btnAddData = Button(Framebutton, text="Update Data", font=("arial", 12, "bold"), width=23, bg="Grey", fg="white")
        btnAddData.grid(row=0, column=2)

        btnAddData = Button(Framebutton, text="Delete Data", font=("arial", 12, "bold"), width=23, bg="Grey", fg="white")
        btnAddData.grid(row=0, column=3)

        btnAddData = Button(Framebutton, text="Reset", font=("arial", 12, "bold"), width=23, bg="Grey", fg="white")
        btnAddData.grid(row=0, column=4)

        btnAddData = Button(Framebutton, text="Exit", font=("arial", 12, "bold"), width=23, bg="Grey", fg="white")
        btnAddData.grid(row=0, column=5)

        #============================== Information Frame ================================#
        FrameDetails = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="light blue")
        FrameDetails.place(x=0, y=590, width=1530, height=210)

        Table_frame=Frame(FrameDetails,bd=6,relief=RIDGE,bg="light blue")
        Table_frame.place(x=0,y=2,width=1460,height=190)


        #ScrollBar dim
        xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)
        self.library_table_=ttk.Treeview(Table_frame,column=("Member type","prnno"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set) #All Column Names

        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)

        #scrollbar dim can be viewed after entering data
        xscroll.config(command=self.library_table_.xview)
        yscroll.config(command=self.library_table_.yview)


        self.library_table_.heading("Member type", text="Member Type")
        #Do it for all columns..




        self.library_table_["show"]="headings"
        self.library_table_.pack(fill=BOTH,expand=1)

        self.library_table_.column("Member type",width=100)
        #do for remaining columns with same width









if __name__== "__main__":
    root = Tk()
    obj=BookStoreManagementSystem(root)
    root.mainloop()
