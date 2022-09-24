from tkinter import *
from tkinter import ttk
from tkinter import messagebox


root = Tk()
screensize=str(root.winfo_screenwidth())+"x"+str(root.winfo_screenheight()) #reading display width and height

#####...................Title...................######
root.title("Blood Bank Management System")
root.geometry(screensize)

#root.wm_iconbitmap("")
root.configure(padx=20, pady=40)

##########.............background image........###################
photo = PhotoImage(file="blood.png")
label1 = Label( root, image = photo)
label1.place(x = 310, y = 50)



###########........................donardictionary......########

donarinformation = {0: {'name': 'Shahadat', 'blood': 'O+', 'gender': 'Male', 'age': '18', 'mobile': '013', 'email': 'shahadat129@gmail.com', 'area': 'sukrabad'}, 1: {'name': 'Farhan', 'blood': 'B+', 'gender': 'Male', 'age': '19', 'mobile': '017', 'email': 'farhan@gmail.com', 'area': 'mirpur'}

}

donarCount = 2
newWindows=[]

#root.geometry("963x749+540+110")
#root.configure(background="#d9d9d9")



def closewindows():
    for i in newWindows:
        i.destroy()


def createdonarid():
    closewindows()

    def getinfo():
        global donarCount
        messagebox.showinfo("Congrats!", "Donar Information created successfully")
        f4 = Frame(borderwidth=6, relief=SUNKEN)
        newWindows.append(f4)
        donarinformation.update({
            donarCount: {
                "name": namevalue.get(),
                "blood": combo_blood.get(),
                "gender": combo_gender.get(),
                "age": agevalue.get(),
                "mobile": mobilevalue.get(),
                "email": emailvalue.get(),
                "area": areavalue.get(),
            }
        })
        donarCount = donarCount + 1

        var1 = Label(f4, text="Donar ID: " + str(donarCount), font=("comicsansms", 16, "bold")).grid(padx=50, pady=15)
        new = Label(f4, text="Donar Name: " + namevalue.get(), font=10).grid(padx=50, pady=10)
        new1 = Label(f4, text="Blood group: " + combo_blood.get(), font=10).grid(padx=50, pady=10)
        new2 = Label(f4, text="Gender: " + combo_gender.get(), font=10).grid(padx=50, pady=10)
        new3 = Label(f4, text="Age: " + agevalue.get(), font=10).grid(padx=50, pady=10)
        new4 = Label(f4, text="Mobile: " + mobilevalue.get(), font=10).grid(padx=50, pady=10)
        new5 = Label(f4, text="Email: " + emailvalue.get(), font=10).grid(padx=50, pady=10)
        new6 = Label(f4, text="Location: " + areavalue.get(), font=10).grid(padx=50, pady=10)


        f4.pack(side=LEFT, padx=50, pady=20)


    frame2 = Frame(borderwidth=6, relief=SUNKEN, padx=40, pady=40)
    newWindows.append(frame2)
    name = Label(frame2, text="Donar name", font=10, padx=10, pady=15).grid(row=0)
    blood = Label(frame2, text="Blood group", font=10, padx=10, pady=15).grid(row=1)
    gender = Label(frame2, text="Gender", font=10, padx=10, pady=15).grid(row=2)
    age = Label(frame2, text="Age", font=10, padx=10, pady=15).grid(row=3)
    mobile = Label(frame2, text="Mobile: ", font=10, padx=10, pady=15).grid(row=4)
    email = Label(frame2, text="Email: ", font=10, padx=10, pady=15).grid(row=5)
    area = Label(frame2, text="Location: ", font=10, padx=10, pady=15).grid(row=6)

    namevalue = StringVar()

    #bloodvalue = StringVar()
    #gendervalue = StringVar()

    agevalue = StringVar()
    mobilevalue = StringVar()
    emailvalue = StringVar()
    areavalue = StringVar()

    nameentry = Entry(frame2, textvariable=namevalue, font=10)

    ##====blood entry by combo===
    combo_blood=ttk.Combobox(frame2, font=10, state="readonly")
    combo_blood['value']= ('A+','A-', 'B+','B-', 'O+', 'O-','AB+','AB-')
    #bloodentry = Entry(frame2, textvariable=bloodvalue, font=10)

    ##====gender entry by combo===
    combo_gender=ttk.Combobox(frame2, font=10, state="readonly")
    combo_gender['value']=('Male','Female','Others')

    #genderentry = Entry(frame2, textvariable=gendervalue, font=10)

    ageentry = Entry(frame2, textvariable=agevalue, font=10)
    mobileentry = Entry(frame2, textvariable=mobilevalue, font=10)
    emailentry = Entry(frame2, textvariable=emailvalue, font=10)
    areaentry = Entry(frame2, textvariable=areavalue, font=10)

    nameentry.grid(row=0, column=1)

    ##====gender grid by combo===
    combo_blood.grid(row=1, column=1)
    #bloodentry.grid(row=1, column=1)

    ##====gender grid by combo===
    combo_gender.grid(row=2, column=1)
    #genderentry.grid(row=2, column=1)

    ageentry.grid(row=3, column=1)
    mobileentry.grid(row=4, column=1)
    emailentry.grid(row=5, column=1)
    areaentry.grid(row=6, column=1)

    b5 = Button(frame2, text="Submit", command=getinfo, font=10)
    b5.grid()
    frame2.pack(side=LEFT, fill="y")


def donardisplay():
    closewindows()
    frame5 = Frame(borderwidth=6, relief=SUNKEN, padx=40, pady=40)

    donar_tree = ttk.Treeview(frame5)

    #define our column
    donar_tree['columns']= ("Donar ID","Donar name","Blood group", "Gender", "Age", "Mobile", "Email", "Location")

    #formate column
    donar_tree.column("#0", width=0, stretch=NO)
    donar_tree.column("Donar ID", anchor="w", width=80)
    donar_tree.column("Donar name", anchor="w", width=150)
    donar_tree.column("Blood group", anchor="w", width=80)
    donar_tree.column("Gender", anchor="w", width=80)
    donar_tree.column("Age", anchor="w", width=80)
    donar_tree.column("Mobile", anchor="w", width=120)
    donar_tree.column("Email", anchor="w", width=150)
    donar_tree.column("Location", anchor="w", width=120)

    #ctreate heading

    donar_tree.heading("#0", text="", anchor="w")
    donar_tree.heading("Donar ID", text="Donar ID", anchor="w")
    donar_tree.heading("Donar name", text="Donar name", anchor="w")
    donar_tree.heading("Blood group", text="Blood group", anchor="w")
    donar_tree.heading("Gender", text="Gender", anchor="w")
    donar_tree.heading("Age", text="Age", anchor="w")
    donar_tree.heading("Mobile", text="Mobile", anchor="w")
    donar_tree.heading("Email", text="Email", anchor="w")
    donar_tree.heading("Location", text="Location", anchor="w")

    count = 1;
    #add data
    #for item,i in map(donarinformation.values(),range(0,donarCount)):
    x=0
    for item in donarinformation.values():
        donar_tree.insert(parent='', index='end', iid=x, text="parent", values=(count, item["name"],  item["blood"],item["gender"], item["age"], item["mobile"],item["email"],item["area"]))
        donar_tree.pack(pady=20)
        x=x+1
        count = count + 1
    frame5.pack(side=LEFT, fill="y")

    newWindows.append(frame5)



def bloodsearch():

    closewindows()
    global combo_nameblood


    f6=Frame(borderwidth=6, relief=SUNKEN, padx=40, pady=40)
    f6.pack(side=LEFT, fill="y")
    bloodname = Label(f6, text="Enter blood group", font=10, padx=10, pady=15).grid(row=0)


    combo_nameblood = ttk.Combobox(f6, font=10, state="readonly")
    combo_nameblood['value'] = ('A+', 'A-', 'B+', 'B-', 'O+', 'O-', 'AB+', 'AB-')
    combo_nameblood.grid(row=0, column=1)
    b6 = Button(f6, text="Search", command=bsearch, font=10)
    b6.grid()

    newWindows.append(f6)

def bsearch():

    frame7 = Frame(borderwidth=6, relief=SUNKEN, padx=40, pady=40)

    donar_tree = ttk.Treeview(frame7)

    # define our column
    donar_tree['columns'] = ("Donar ID", "Donar name", "Blood group", "Gender", "Age", "Mobile", "Email", "Location")

    # formate column
    donar_tree.column("#0", width=0, stretch=NO)
    donar_tree.column("Donar ID", anchor="w", width=80)
    donar_tree.column("Donar name", anchor="w", width=150)
    donar_tree.column("Blood group", anchor="w", width=80)
    donar_tree.column("Gender", anchor="w", width=80)
    donar_tree.column("Age", anchor="w", width=80)
    donar_tree.column("Mobile", anchor="w", width=120)
    donar_tree.column("Email", anchor="w", width=150)
    donar_tree.column("Location", anchor="w", width=120)

    # ctreate heading

    donar_tree.heading("#0", text="", anchor="w")
    donar_tree.heading("Donar ID", text="Donar ID", anchor="w")
    donar_tree.heading("Donar name", text="Donar name", anchor="w")
    donar_tree.heading("Blood group", text="Blood group", anchor="w")
    donar_tree.heading("Gender", text="Gender", anchor="w")
    donar_tree.heading("Age", text="Age", anchor="w")
    donar_tree.heading("Mobile", text="Mobile", anchor="w")
    donar_tree.heading("Email", text="Email", anchor="w")
    donar_tree.heading("Location", text="Location", anchor="w")

    inputblood = combo_nameblood.get()
    count = 1;
    # add data
    # for item,i in map(donarinformation.values(),range(0,donarCount)):
    x = 0
    for item in donarinformation.values():
        if item["blood"] == inputblood:
            donar_tree.insert(parent='', index='end', iid=x, text="parent", values=(
            count, item["name"], item["blood"], item["gender"], item["age"], item["mobile"], item["email"], item["area"]))
            donar_tree.pack(pady=20)
            x = x + 1
            count = count + 1

#    else:
#        messagebox.showerror("Sorry", "Blood group not found")

    frame7.pack(side=LEFT, fill="y")

    newWindows.append(frame7)


def areasearch():
    closewindows()

    global areanam

    f7 = Frame(borderwidth=6, relief=SUNKEN, padx=40, pady=40)
    f7.pack(side=LEFT, fill="y")
    arename = Label(f7, text="Enter location", font=10, padx=10, pady=15).grid(row=0)

    areanam = Entry(f7, font=10)
    areanam.grid(row=0, column=1)
    b7 = Button(f7, text="Search", command=artree, font=10)
    b7.grid()

    newWindows.append(f7)

def artree():

    frame7 = Frame(borderwidth=6, relief=SUNKEN, padx=40, pady=40)

    donar_tree = ttk.Treeview(frame7)

    # define our column
    donar_tree['columns'] = ("Donar ID", "Donar name", "Blood group", "Gender", "Age", "Mobile", "Email", "Location")

    # formate column
    donar_tree.column("#0", width=0, stretch=NO)
    donar_tree.column("Donar ID", anchor="w", width=80)
    donar_tree.column("Donar name", anchor="w", width=150)
    donar_tree.column("Blood group", anchor="w", width=80)
    donar_tree.column("Gender", anchor="w", width=80)
    donar_tree.column("Age", anchor="w", width=80)
    donar_tree.column("Mobile", anchor="w", width=120)
    donar_tree.column("Email", anchor="w", width=150)
    donar_tree.column("Location", anchor="w", width=120)

    # ctreate heading

    donar_tree.heading("#0", text="", anchor="w")
    donar_tree.heading("Donar ID", text="Donar ID", anchor="w")
    donar_tree.heading("Donar name", text="Donar name", anchor="w")
    donar_tree.heading("Blood group", text="Blood group", anchor="w")
    donar_tree.heading("Gender", text="Gender", anchor="w")
    donar_tree.heading("Age", text="Age", anchor="w")
    donar_tree.heading("Mobile", text="Mobile", anchor="w")
    donar_tree.heading("Email", text="Email", anchor="w")
    donar_tree.heading("Location", text="Location", anchor="w")


    count = 1;
    # add data
    # for item,i in map(donarinformation.values(),range(0,donarCount)):
    x = 0
    for item in donarinformation.values():

        if item["area"] == areanam.get():
            donar_tree.insert(parent='', index='end', iid=x, text="parent", values=(
                count, item["name"], item["blood"], item["gender"], item["age"], item["mobile"], item["email"],
                item["area"]))
            donar_tree.pack(pady=20)
            x = x + 1
            count = count + 1
#   else:
#       messagebox.showerror("Sorry", "Location not found")

    frame7.pack(side=LEFT, fill="y")

    newWindows.append(frame7)


def updatebtn():
    messagebox.showinfo("Congrats!", "Donar Information updated successfully")

    f9 = Frame(borderwidth=6, relief=SUNKEN)
    f9.pack(side=LEFT, pady=20)
    inputid = mobilenum.get()
    for i in range(len(donarinformation)):
        if donarinformation[i]["mobile"] == inputid:
            donarinformation[i]["name"] = nameentry.get()
            donarinformation[i]["blood"] = combo_blood2.get()
            donarinformation[i]["gender"] = combo_gender2.get()
            donarinformation[i]["age"] = ageentry.get()
            donarinformation[i]["mobile"] = mobileentry.get()
            donarinformation[i]["area"] = areaentry.get()



def sure():


    global nameentry,ageentry,mobileentry,emailentry,areaentry,combo_blood2,combo_gender2

    f8 = Frame(borderwidth=6, relief=SUNKEN)
    f8.pack(side=LEFT, pady=20)

    name = Label(f8, text="Donar name", font=10, padx=10, pady=15).grid(row=0)
    blood = Label(f8, text="Blood group", font=10, padx=10, pady=15).grid(row=1)
    gender = Label(f8, text="Gender", font=10, padx=10, pady=15).grid(row=2)
    age = Label(f8, text="Age", font=10, padx=10, pady=15).grid(row=3)
    mobile = Label(f8, text="Mobile: ", font=10, padx=10, pady=15).grid(row=4)
    email = Label(f8, text="Email: ", font=10, padx=10, pady=15).grid(row=5)
    area = Label(f8, text="Location: ", font=10, padx=10, pady=15).grid(row=6)

    namevalue = StringVar()

    # bloodvalue = StringVar()
    # gendervalue = StringVar()

    agevalue = StringVar()
    mobilevalue = StringVar()
    emailvalue = StringVar()
    areavalue = StringVar()

    nameentry = Entry(f8, textvariable=namevalue, font=10)

    ##====blood entry by combo===
    combo_blood2 = ttk.Combobox(f8, font=10, state="readonly")
    combo_blood2['value'] = ('A+', 'A-', 'B+', 'B-', 'O+', 'O-', 'AB+', 'AB-')
    # bloodentry = Entry(frame2, textvariable=bloodvalue, font=10)

    ##====gender entry by combo===
    combo_gender2 = ttk.Combobox(f8, font=10, state="readonly")
    combo_gender2['value'] = ('Male', 'Female', 'Others')

    # genderentry = Entry(frame2, textvariable=gendervalue, font=10)

    ageentry = Entry(f8, textvariable=agevalue, font=10)
    mobileentry = Entry(f8, textvariable=mobilevalue, font=10)
    emailentry = Entry(f8, textvariable=emailvalue, font=10)
    areaentry = Entry(f8, textvariable=areavalue, font=10)

    nameentry.grid(row=0, column=1)

    ##====gender grid by combo===
    combo_blood2.grid(row=1, column=1)
    # bloodentry.grid(row=1, column=1)

    ##====gender grid by combo===
    combo_gender2.grid(row=2, column=1)
    # genderentry.grid(row=2, column=1)

    ageentry.grid(row=3, column=1)
    mobileentry.grid(row=4, column=1)
    emailentry.grid(row=5, column=1)
    areaentry.grid(row=6, column=1)

    b8 = Button(f8, text="Submit", command=updatebtn, font=10)
    b8.grid()

    newWindows.append(f8)

def updateinfo():
    global mobilenum

    closewindows()

    f7 = Frame(borderwidth=6, relief=SUNKEN, padx=40, pady=40)
    f7.pack(side=LEFT, fill="y")
    mobilesearch = Label(f7, text="Enter Donar mobile number: ", font=10, padx=10, pady=15).grid(row=0)

    mobilenum = Entry(f7, font=10)
    mobilenum.grid(row=0, column=1)
    b7 = Button(f7, text="Submit", command=sure, font=10)
    b7.grid()

    newWindows.append(f7)



######################........BUTTON.......############################

f = Frame( borderwidth=6, relief=SUNKEN)
f.pack(side=TOP, fill="x")

heading = Label(f, text="Blood Bank Management System", fg="red", font=("comicsansms", 25, "bold"), padx=15, pady=15)
heading.pack()

frame = Frame(root, borderwidth=6, bg="grey", relief=SUNKEN)
frame.pack(side=LEFT, fill="y")

b1 = Button(frame, fg="red", text="1. Create new donar id", font=("comicsansms", 12, "bold"), command=createdonarid)
b1.pack(side=TOP, padx=5, pady=15, anchor="nw")


b2 = Button(frame, fg="red", text="2. Display all donar information", font=("comicsansms", 12, "bold"), command=donardisplay)
b2.pack(side=TOP, padx=5, anchor="nw")

b3 = Button(frame, fg="red", text="3. Search information by blood group", font=("comicsansms", 12, "bold"), command=bloodsearch)
b3.pack(side=TOP, padx=5, pady=15, anchor="nw")

b4 = Button(frame, fg="red", text="4. Search information by area", font=("comicsansms", 12, "bold"), command=areasearch)
b4.pack(side=TOP, padx=5, anchor="nw")

b5 = Button(frame, fg="red", text="5. Update donar information", font=("comicsansms", 12, "bold"), command=updateinfo)
b5.pack(side=TOP, padx=5, pady=15, anchor="nw")

b7 = Button(frame, fg="red", text="6. Clear Windows", font=("comicsansms", 12, "bold"), command=closewindows)
b7.pack(side=TOP, padx=5, anchor="nw")

b6 = Button(frame, fg="red", text="7. Exit", font=("comicsansms", 12, "bold"), command=frame.quit)
b6.pack(side=TOP, padx=5, pady=15, anchor="nw")
############################################

root.mainloop()