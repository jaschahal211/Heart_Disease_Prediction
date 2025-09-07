from tkinter import *
from datetime import date
from tkinter.ttk import Combobox
import datetime
from tkinter import messagebox
import matplotlib
from PIL import Image, ImageTk 
import loginform
matplotlib.use("TkAgg")
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
# from knnback import *
from randomforestback import *
import os
from MySQL import *
from tkinter import PhotoImage,Toplevel ,Button
from loginform import *
from report import *

background="#f0ddd5"
framebg="#62a7ff"
framefg="#fefbfb"

root=Tk()
root.title("Heart Attack Prediction System")
root.geometry("1450x730+60+80")
root.resizable(True,True)
root.config(bg=background)


#-------------------------------------------------Analysis----------------------------------------------------------------------------#
def analysis():
    global prediction

    name=Name.get()
    D1=Date.get()
    today=datetime.date.today()
    A=today.year-DOB.get()

    try:
        B=selection()
    except:
        messagebox.showerror("missing","Please select gender!!")
        return
    
    try:
        F=selection2()
    except:
        messagebox.showerror("missing","Please select fbs!!")
        return
    
    
    try:
        I=selection3()
    except:
        messagebox.showerror("missing","Please select exang!!")
        return
    
    C = selection4()
    if C is None:
        messagebox.showerror("missing", "Please select cp!!")
        return

    try:
        G = int(restecg_combobox.get())
    except ValueError:
        messagebox.showerror("missing", "Please select restecg!!")
        return


    try:
        K=int(selection5())
    except:
        messagebox.showerror("missing","Please select slope!!")
        return    

    try:
        L=int(ca_combobox.get())
    except:
        messagebox.showerror("missing","Please select ca!!")
        return
    
    try:
        M=int(thal_combobox.get())
    except:
        messagebox.showerror("missing","Please select thal!!")
        return
    
    try:
        D=int(trestbps.get())
        E=int(chol.get())
        H=int(thalach.get())
        J=int(oldpeak.get())
    except:
        messagebox.showerror("missing data","Few missing data entry!!")
        return

#lets check all are working or not
    print("A is age:",A)
    print("B is gender:",B)
    print("C is cp:",C)
    print("D is trestbps:",D)
    print("E is chol:",E)
    print("F is fbs:",F)
    print("G is restecg:",G)
    print("H is thalach:",H)
    print("I is Exang:",I)
    print("J is oldpeak:",J)
    print("K is slope:",K)
    print("L is ca:",L)
    print("M is thal:",M)

    #####first graph

# Create the first figure for Sex, fbs, exang
    f1 = Figure(figsize=(5, 5), dpi=100)
    a1 = f1.add_subplot(111)
    categories1 = ["Sex", "fbs", "exang"]
    values1 = [B, F, I]
    a1.plot(categories1, values1, marker='o', linestyle='-', color='blue')
    a1.set_ylabel('Values')
    a1.set_title('Gender and Health Metrics')

    canvas1 = FigureCanvasTkAgg(f1, master=root)
    canvas1.draw()
    canvas1.get_tk_widget().place(width=250, height=250, x=600, y=240)

    # Create the second figure for Age, Trestbps, Chol, Thalach
    f2 = Figure(figsize=(5, 5), dpi=100)
    a2 = f2.add_subplot(111)
    categories2 = ["Age", "Trestbps", "Chol", "Thalach"]
    values2 = [A,D,E,H]
    a2.plot(categories2, values2, marker='o', linestyle='-', color='green')
    a2.set_ylabel('Values')
    a2.set_title('Vital Health Metrics')

    canvas2 = FigureCanvasTkAgg(f2, master=root)
    canvas2.draw()
    canvas2.get_tk_widget().place(width=250, height=250, x=860, y=240)

    # Create the third figure for Oldpeak, CP, Slope
    f3 = Figure(figsize=(5, 5), dpi=100)
    a3 = f3.add_subplot(111)
    categories3 = ["Oldpeak", "CP", "Slope"]
    values3 = [J,C,K]
    a3.plot(categories3, values3, marker='o', linestyle='-', color='red')
    a3.set_ylabel('Values')
    a3.set_title('Exercise Metrics')

    canvas3 = FigureCanvasTkAgg(f3, master=root)
    canvas3.draw()
    canvas3.get_tk_widget().place(width=250, height=250, x=600, y=470)

    # Create the fourth figure for CA and Thal
    f4 = Figure(figsize=(5, 5), dpi=100)
    a4 = f4.add_subplot(111)
    categories4 = ["CA", "Thal"]
    values4 = [L,M]
    a4.plot(categories4, values4, marker='o', linestyle='-', color='purple')
    a4.set_ylabel('Values')
    a4.set_title('Coronary Metrics')

    canvas4 = FigureCanvasTkAgg(f4, master=root)
    canvas4.draw()
    canvas4.get_tk_widget().place(width=250, height=250, x=860, y=470)

    #input data:
    input_data=(A,B,C,D,E,F,G,H,I,J,K,L,M)
    input_data_as_numpy_array=np.asanyarray(input_data)

    #reshape the numpy array as we are predicting for only on instance

    input_data_reshape=input_data_as_numpy_array.reshape(1,-1)
    prediction=model.predict(input_data_reshape)
    print(prediction[0])

    if(prediction[0]==0):
        print("The person does not have a Heart disease")
        report.config(text=f"Report:{0}",fg="#8dc63f")
        report1.config(text=f"{name},you do not have a heart disease")
    else:
        print("The person has Heart disease")
        report.config(text=f"Report:{1}",fg="#ed1c24")
        report1.config(text=f"{name},you have a heart disease")    
    




#--------------------------------------------Info window(operated by window button)----------------------------------------------------#

def Info():
    Icon_window=Toplevel(root)
    Icon_window.title("Info")
    Icon_window.geometry("700x600+100+100")


    #icon image
    icon_image=PhotoImage(file="images/info.png")
    Icon_window.iconphoto(False,icon_image)

    #Heading
    Label(Icon_window,text="Information Related to dataset",font="robot 19 bold").pack(padx=20,pady=20)
    #info
    Label(Icon_window,text="age - age in years",font="arial 11").place(x=20,y=100)
    Label(Icon_window,text="sex - sex (1 = male; 0 = female)",font="arial 11").place(x=20,y=130)
    Label(Icon_window,text="cp - chest pain type (0 = typical angina; 1 = atypical angina; 2 = non-anginal pain; 3 = asymptomatic)",font="arial 11").place(x=20,y=160)
    Label(Icon_window,text="trestbps - resting blood pressure (in mm Hg on admission to the hospital)",font="arial 11").place(x=20,y=190)
    Label(Icon_window,text="chol - serum cholestoral in mg/dl",font="arial 11").place(x=20,y=220)
    Label(Icon_window,text="fbs - fasting blood sugar > 120 mg/dl (1 = true; 0 = false)",font="arial 11").place(x=20,y=250)
    Label(Icon_window,text="restecg - resting electrocardiographic results (0 = normal; 1 = having ST-T; 2 = hypertrophy)",font="arial 11").place(x=20,y=280)
    Label(Icon_window,text="thalach - maximum heart rate achieved",font="arial 11").place(x=20,y=310)
    Label(Icon_window,text="exang - exercise induced angina (1 = yes; 0 = no)",font="arial 11").place(x=20,y=340)
    Label(Icon_window,text="oldpeak - ST depression induced by exercise relative to rest",font="arial 11").place(x=20,y=370)
    Label(Icon_window,text="slope - the slope of the peak exercise ST segment (0 = upsloping; 1 = flat; 2 = downsloping)",font="arial 11").place(x=20,y=400)
    Label(Icon_window,text="ca - number of major vessels (0-3) colored by flourosopy",font="arial 11").place(x=20,y=430)
    Label(Icon_window,text="thal - 0 = normal; 1 = fixed defect; 2 = reversable defect",font="arial 11").place(x=20,y=460)
    Icon_window.mainloop()

def logout():
    root.destroy()   

#-------------------------------------------Clear()-----------------------------------------------------------------------------------#
def Clear():
    Name.get('')
    DOB.get('')
    trestbps.get('')
    chol.get('')
    thalach.set('')
    oldpeak.set('')

#---------------------------------------Save------------------------------------------------------------------------------------------#

def Save():
    B2=Name.get()
    C2=Date.get()
    D2=DOB.get()
    today=datetime.date.today()
    E2=today.year-DOB.get()

    try:
        F2=selection()
    except:
        messagebox.showerror("Missing Data","Please select Gender!")
    try:
        J2=selection2()
    except:
        messagebox.showerror("Missing Data","Please select fbs!")
    try:
        M2=selection3()
    except:
        messagebox.showerror("Missing Data","Please select Exang!")
    try:
        G2=selection4()
    except:
        messagebox.showerror("Missing Data","Please select cp!")
    try:
        K2=restecg_combobox.get()
    except:
        messagebox.showerror("Missing Data","Please select restecg!")
    try:
        O2=selection5()
    except:
        messagebox.showerror("Missing Data","Please select slope!")
    try:
        P2=ca_combobox.get()
    except:
        messagebox.showerror("Missing Data","Please select ca!")
    try:
        Q2=thal_combobox.get()
    except:
        messagebox.showerror("Missing Data","Please select thal!")
    H2= trestbps.get()
    I2=chol.get()
    L2=thalach.get()
    N2=float(oldpeak.get())
    print(B2)
    print(C2)
    print(D2)
    print(E2)
    print(F2)
    print(G2)
    print(H2)
    print(I2)
    print(J2)
    print(K2)
    print(L2)
    print(M2)
    print(N2)
    print(O2)
    print(P2)
    print(Q2)
    Save_Data_MySql(B2,C2,int(D2),int(E2),int(F2),int(G2),int(H2),int(I2),int(J2),int(K2),int(L2),int(M2),float(N2),int(O2),int(P2),int(Q2),int(prediction[0]))

    Clear()
    root.destroy()
    os.system("main.py")



#----------------------------------------------------------------------------------------------------------------------
#icon 1
image_icon=PhotoImage(file="images/icon.png")
root.iconphoto(False,image_icon)


# ##header section 2
logo=PhotoImage(file="images/header.png")
myimage=Label(image=logo,bg=background)
myimage.place(x=0,y=0)


###<<<frame 3

Heading_entry=Frame(root,width=800,height=190,bg="#df2d4b")
Heading_entry.place(x=600,y=20)

Label(Heading_entry,text="Registeration No.",font="arial 13",bg="#df2d4b",fg=framefg).place(x=30,y=0)
Label(Heading_entry,text="Date",font="arial 13",bg="#df2d4b",fg=framefg).place(x=430,y=0)
Label(Heading_entry,text="Patient Name",font="arial 13",bg="#df2d4b",fg=framefg).place(x=30,y=90)
Label(Heading_entry,text="Birth year",font="arial 13",bg="#df2d4b",fg=framefg).place(x=430,y=90)

Entry_image=PhotoImage(file="images/Rounded Rectangle 1.png")
Entry_image=PhotoImage(file="images/Rounded Rectangle 2.png")
Label(Heading_entry,image=Entry_image,bg="#df2d4b").place(x=20,y=30)
Label(Heading_entry,image=Entry_image,bg="#df2d4b").place(x=430,y=30)
Label(Heading_entry,image=Entry_image,bg="#df2d4b").place(x=20,y=120)
Label(Heading_entry,image=Entry_image,bg="#df2d4b").place(x=430,y=120)

Registration=IntVar()
reg_entry=Entry(Heading_entry,textvariable=Registration,width=30,font="arial 15",bg="#0e5363",fg="white",bd=0)
reg_entry.place(x=30,y=45)

Date=StringVar()
today=date.today()
d1=today.strftime("%d/%m/%Y")
date_entry=Entry(Heading_entry,textvariable=Date,width=15,font="arial 15",bg="#0e5363",fg="white",bd=0)
date_entry.place(x=500,y=45)
Date.set(d1)

Name=StringVar()
name_entry=Entry(Heading_entry,textvariable=Name,width=20,font="arial 20",bg="#ededed",fg="#222222",bd=0)
name_entry.place(x=30,y=130)

DOB=IntVar()
dob_entry=Entry(Heading_entry,textvariable=DOB,width=20,font="arial 20",bg="#ededed",fg="#222222",bd=0)
dob_entry.place(x=450,y=130)

#---------------------------------------------Body--------------------------------------------------------------------------------------#
Detail_entry=Frame(root,width=490,height=260,bg="#dbe0e3")
Detail_entry.place(x=30,y=450)

#--------------------------------------------radio button------------------------------------------------------------------------------#
Label(Detail_entry,text="sex:",font="arial 13",bg=framebg,fg=framefg).place(x=10,y=10)
Label(Detail_entry,text="fbs:",font="arial 13",bg=framebg,fg=framefg).place(x=180,y=10)
Label(Detail_entry,text="exang:",font="arial 13",bg=framebg,fg=framefg).place(x=335,y=10)

def selection():
    if gen.get()==1:
        Gender=1
        return(Gender)
        print(Gender)
    elif gen.get()==2:
        Gender=0
        return(Gender)
        print(Gender)
    else:
        print(Gender) 

def selection2():
    if fbps.get()==1:
        Fbps=1
        return(Fbps)
        print(Fbps)
    elif fbps.get()==2:
        Fbps=0
        return(Fbps)
        print(Fbps)
    else:
        print(Fbps)         


    
def selection3():
    if exang.get()==1:
        Exang=1
        return(Exang)
        print(Exang)
    elif exang.get()==2:
        Exang=0
        return(Exang)
        print(Exang)
    else:
        print(Exang)
    
gen=IntVar()
R1=Radiobutton(Detail_entry,text='Male',variable=gen,value=1,command=selection)
R2=Radiobutton(Detail_entry,text='Female',variable=gen,value=2,command=selection)
R1.place(x=43,y=10)
R2.place(x=93,y=10)

fbps=IntVar()
R3=Radiobutton(Detail_entry,text='True',variable=fbps,value=1,command=selection2)
R4=Radiobutton(Detail_entry,text='False',variable=fbps,value=2,command=selection2)
R3.place(x=213,y=10)
R4.place(x=263,y=10)

exang=IntVar()
R5=Radiobutton(Detail_entry,text='Yes',variable=exang,value=1,command=selection3)
R6=Radiobutton(Detail_entry,text='No',variable=exang,value=2,command=selection3)
R5.place(x=387,y=10)
R6.place(x=430,y=10)


#------------------------------------------------------Combobox--------------------------------------------------------------------------#

Label(Detail_entry,text="cp:",font="arial 13",bg=framebg,fg=framefg).place(x=10,y=50)
Label(Detail_entry,text="restecg:",font="arial 13",bg=framebg,fg=framefg).place(x=10,y=90)
Label(Detail_entry,text="slope:",font="arial 13",bg=framebg,fg=framefg).place(x=10,y=130)
Label(Detail_entry,text="ca:",font="arial 13",bg=framebg,fg=framefg).place(x=10,y=170)
Label(Detail_entry,text="thal:",font="arial 13",bg=framebg,fg=framefg).place(x=10,y=210)
def selection4():
    input = cp_combobox.get()
    if input == "0=typical angina":
        return 0
    elif input == "1=atypical angina":
        return 1
    elif input == "2=non-anginal pain":
        return 2
    elif input == "3=asymptomatic":
        return 3
    else:
        return None  # Return None if no valid input

    
def selection5():
    input = slope_combobox.get()
    if input == "0=upsloping":
        return 0
    elif input == "1=flat":
        return 1
    elif input == "2=downsloping":
        return 2
    else:
        return None  # Return None if no valid input

cp_combobox=Combobox(Detail_entry,values=['0=typical angina','1=atypical angina','2=non-anginal pain','3=asymptomatic'],font="arial 12",state="r",width=14)
restecg_combobox=Combobox(Detail_entry,values=['0','1','2'],font="arial 12",state="r",width=11)
slope_combobox=Combobox(Detail_entry,values=['0=upsloping','1=flat','2=downsloping'],font="arial 12",state="r",width=12)
ca_combobox=Combobox(Detail_entry,values=['0','1','2','3','4'],font="arial 12",state="r",width=14)
thal_combobox=Combobox(Detail_entry,values=['0','1','2','3'],font="arial 12",state="r",width=11)

cp_combobox.place(x=50,y=50)
restecg_combobox.place(x=80,y=90)
slope_combobox.place(x=70,y=130)
ca_combobox.place(x=50,y=170)
thal_combobox.place(x=50,y=210)


#----------------------------------------------Data Entry box--------------------------------------------------------------------------------#

Label(Detail_entry,text="Smoking:",font="arial 13",width=7,bg="#dbe0e3",fg="black").place(x=240,y=50)
Label(Detail_entry,text="trestbps:",font="arial 13",width=7,bg=framebg,fg=framefg).place(x=240,y=90)
Label(Detail_entry,text="chol:",font="arial 13",width=7,bg=framebg,fg=framefg).place(x=240,y=130)
Label(Detail_entry,text="thalach:",font="arial 13",width=7,bg=framebg,fg=framefg).place(x=240,y=170)
Label(Detail_entry,text="oldpeak:",font="arial 13",width=7,bg=framebg,fg=framefg).place(x=240,y=210)



trestbps=StringVar()
chol=StringVar()
thalach=StringVar()
oldpeak=StringVar()

trestbps_entry = Entry(Detail_entry,textvariable=trestbps,width=10,font="aerial 15",bg="#ededed",fg="#222222",bd=0)
chol_entry=Entry(Detail_entry,textvariable=chol,width=10,font="aerial 15",bg="#ededed",fg="#222222",bd=0)
thalach_entry=Entry(Detail_entry,textvariable=thalach,width=10,font="aerial 15",bg="#ededed",fg="#222222",bd=0)
oldpeak_entry=Entry(Detail_entry,textvariable=oldpeak,width=10,font="aerial 15",bg="#ededed",fg="#222222",bd=0)
trestbps_entry.place(x=320,y=90)
chol_entry.place(x=320,y=130)
thalach_entry.place(x=320,y=170)
oldpeak_entry.place(x=320,y=210)

# #------------------------------------------------------------------------------------------------------------------------------------#

# #-------------------------------------------------Report------------------------------------------------------------------------------#

square_report_image=PhotoImage(file="images/Report.png")
report_background=Label(image=square_report_image,bg=background)
report_background.place(x=1120,y=340)

report=Label(root,font="arial 25 bold",bg="white",fg="#8dc63f")
report.place(x=1170,y=550)

report1=Label(root,font="arial 10 bold",bg="white")
report1.place(x=1130,y=610)

#--------------------------------------------------Graph------------------------------------------------------------------------------------#

graph_image=PhotoImage(file="images/graph.png")
Label(image=graph_image).place(x=600,y=270)
Label(image=graph_image).place(x=860,y=270)
Label(image=graph_image).place(x=600,y=500)
Label(image=graph_image).place(x=860,y=500)

#--------------------------------------------------Button-------------------------------------------------------------------------------#
analysis_button=PhotoImage(file="images/Analysis.png")
Button(root,image=analysis_button,bd=0,bg=background,cursor="hand2",command=analysis).place(x=1130,y=240)


#--------------------------------------------------Info button-------------------------------------------------------------------------#
info_button=PhotoImage(file="images/info.png")
Button(root,image=info_button,bd=0,bg=background,cursor='hand2',command=Info).place(x=10,y=240)


#-------------------------------------------------------Save Button--------------------------------------------------------------------#

save_button=PhotoImage(file="images/save.png")
Button(root,image=save_button,bd=0,bg=background,cursor='hand2',command=Save).place(x=1370,y=250)

#----------------------------------Smoking and Non_Smoking Button-----------------------------------------------------------------------#

button_mode=True
choice="smoking"

def changemode():
    global button_mode
    global choice
    if button_mode:
        choice="non-smoking"
        mode.config(image=non_smoking_icon,activebackground="white")
        button_mode=False
    else:
        choice="smoking"
        mode.config(image=smoking_icon,activebackground="white")
        button_mode=True
    print(choice) 


smoking_icon=PhotoImage(file="images/smoker.png")
non_smoking_icon=PhotoImage(file="images/non-smoker.png")
mode=Button(root,image=smoking_icon,bg="#dbe0e3",bd=0,cursor="hand2",command=changemode)
mode.place(x=350,y=495)
#----------------------------------------ReportSection----------------------------------------------------------------------------------#
from tkinter import Toplevel, Label, PhotoImage, Button
from PIL import Image, ImageTk
from report import generate_report  # Import the report generation function

def open_report_section():
    report_window = Toplevel(root)  # Create a new top-level window
    report_window.title("Report Section")
    report_window.state("zoomed")  # Open the window in maximized mode

    # Load the original background image
    original_bg_image = Image.open("images/Heartreport.png")

    # Function to resize the background dynamically
    def resize_bg(event):
        new_width, new_height = event.width, event.height
        resized_bg = original_bg_image.resize((new_width, new_height), Image.LANCZOS)
        report_window.bg_image = ImageTk.PhotoImage(resized_bg)  # Prevent garbage collection
        bg_label.config(image=report_window.bg_image)

    # Display background
    resized_bg_image = original_bg_image.resize((report_window.winfo_screenwidth(), report_window.winfo_screenheight()), Image.LANCZOS)
    bg_image = ImageTk.PhotoImage(resized_bg_image)
    
    bg_label = Label(report_window, image=bg_image)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    report_window.bg_image = bg_image  # Keep reference to avoid garbage collection

    # Bind resizing event
    report_window.bind("<Configure>", resize_bg)

    # Generate the report content
    generate_report(report_window)
    

# Load and resize the button image
original_report_img = PhotoImage(file="images/reportSection.png")
report_button_img = original_report_img.subsample(3, 3)  

# Create the button
report_button = Button(root, image=report_button_img, bd=0, bg=background, cursor='hand2', command=open_report_section)
report_button.place(x=1350, y=520)

#---------------------------------------Database section----------------------------------------------------------------------------------#
import mysql.connector
from tkinter import Toplevel, PhotoImage, Button, messagebox
from tkinter import ttk  # Import Treeview for table display

def show_database():
    try:
        # Connect to the database
        mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            password='992922',
            database='Heart_Data'
        )
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM data")  # Fetch all records
        records = mycursor.fetchall()

        # Create a new window for displaying data
        db_window = Toplevel(root)
        db_window.title("Patient Database")
        db_window.geometry("1000x500")  # Adjust size as needed
        db_window.configure(bg="#E066FF")  # Orchid2 background

        # Define columns
        columns = ("ID", "Name", "Date", "DOB", "Age", "Sex", "CP", "Trestbps",
                   "Chol", "FBS", "RestECG", "Thalach", "Exang", "Oldpeak",
                   "Slope", "CA", "Thal", "Result")

        # Create Treeview (table) widget with style
        style = ttk.Style()
        style.configure("Treeview", background="#FFC0CB", foreground="black", font=("Arial", 12))  # Light pink rows
        style.configure("Treeview.Heading", font=("Arial", 12, "bold"), foreground="#C71585")  # Dark pink2 headings

        tree = ttk.Treeview(db_window, columns=columns, show="headings", style="Treeview")

        # Define column headings
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=100, anchor="center")  # Adjust width as needed

        # Insert data into table
        for row in records:
            tree.insert("", "end", values=row)

        tree.pack(expand=True, fill="both")

    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")

    finally:
        if mydb.is_connected():
            mycursor.close()
            mydb.close()

# Create the database button with background color Orchid2
original_database_img = PhotoImage(file="images/database.png")
database_button_img = original_database_img.subsample(3, 3)  

database_button = Button(root, image=database_button_img, bd=0, cursor='hand2', command=show_database)
database_button.place(x=1350, y=400)
#------------------------------------------Appointment Section------------------------------------------------------------------------------#

from tkinter import Toplevel, Label, PhotoImage, Button, Entry, StringVar, ttk, messagebox
from PIL import Image, ImageTk

def open_appointment_section():
    appointment_window = Toplevel(root)
    appointment_window.title("Appointment Section")
    appointment_window.state("zoomed")

    # Load background image
    original_bg_image = Image.open("images/calendar.png")

    def resize_bg(event):
        new_width, new_height = event.width, event.height
        resized_bg = original_bg_image.resize((new_width, new_height), Image.LANCZOS)
        appointment_window.bg_image = ImageTk.PhotoImage(resized_bg)  # Prevent garbage collection
        bg_label.config(image=appointment_window.bg_image)

    resized_bg_image = original_bg_image.resize((appointment_window.winfo_screenwidth(), appointment_window.winfo_screenheight()), Image.LANCZOS)
    bg_image = ImageTk.PhotoImage(resized_bg_image)

    bg_label = Label(appointment_window, image=bg_image)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    appointment_window.bg_image = bg_image  # Keep reference

    appointment_window.bind("<Configure>", resize_bg)

    # ---------------- Appointment Booking UI ----------------
from tkinter import Toplevel, Label, PhotoImage, Button, Entry, StringVar, ttk, messagebox
from PIL import Image, ImageTk
import sqlite3

# Connect to database (or create one if it doesn't exist)
conn = sqlite3.connect("appointments.db")
cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute("""
    CREATE TABLE IF NOT EXISTS appointments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER,
        gender TEXT,
        contact TEXT,
        date TEXT,
        time TEXT,
        doctor TEXT,
        symptoms TEXT
    )
""")
conn.commit()
conn.close()


def open_appointment_section():
    appointment_window = Toplevel(root)
    appointment_window.title("Appointment Section")
    appointment_window.state("zoomed")

    # Load background image
    original_bg_image = Image.open("images/calendar.png")

    def resize_bg(event):
        new_width, new_height = event.width, event.height
        resized_bg = original_bg_image.resize((new_width, new_height), Image.LANCZOS)
        appointment_window.bg_image = ImageTk.PhotoImage(resized_bg)  # Prevent garbage collection
        bg_label.config(image=appointment_window.bg_image)

    resized_bg_image = original_bg_image.resize((appointment_window.winfo_screenwidth(), appointment_window.winfo_screenheight()), Image.LANCZOS)
    bg_image = ImageTk.PhotoImage(resized_bg_image)

    bg_label = Label(appointment_window, image=bg_image)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    appointment_window.bg_image = bg_image  # Keep reference

    appointment_window.bind("<Configure>", resize_bg)

    # ---------------- Modern Appointment Booking UI ----------------
    
    heading_label = Label(appointment_window, text="🩺 Book Your Appointment", font=("Arial", 28, "bold"), fg="darkblue", bg="#ffffff")
    heading_label.place(x=450, y=40)

    form_bg = "#F9F9F9"
    text_color = "black"
    input_bg = "white"

    # Name
    Label(appointment_window, text="Patient Name:", font=("Arial", 14, "bold"), bg=form_bg, fg=text_color).place(x=380, y=120)
    name_var = StringVar()
    name_entry = Entry(appointment_window, textvariable=name_var, font=("Arial", 14), bg=input_bg)
    name_entry.place(x=600, y=120, width=250)

    # Age
    Label(appointment_window, text="Age:", font=("Arial", 14, "bold"), bg=form_bg, fg=text_color).place(x=380, y=170)
    age_var = StringVar()
    age_entry = Entry(appointment_window, textvariable=age_var, font=("Arial", 14), bg=input_bg)
    age_entry.place(x=600, y=170, width=250)

    # Gender
    Label(appointment_window, text="Gender:", font=("Arial", 14, "bold"), bg=form_bg, fg=text_color).place(x=380, y=220)
    gender_var = StringVar()
    gender_dropdown = ttk.Combobox(appointment_window, textvariable=gender_var, values=["Male", "Female", "Other"], font=("Arial", 14), state="readonly")
    gender_dropdown.place(x=600, y=220, width=250)
    gender_dropdown.current(0)

    # Contact Number
    Label(appointment_window, text="Contact Number:", font=("Arial", 14, "bold"), bg=form_bg, fg=text_color).place(x=380, y=270)
    contact_var = StringVar()
    contact_entry = Entry(appointment_window, textvariable=contact_var, font=("Arial", 14), bg=input_bg)
    contact_entry.place(x=600, y=270, width=250)

    # Select Date
    Label(appointment_window, text="Appointment Date:", font=("Arial", 14, "bold"), bg=form_bg, fg=text_color).place(x=380, y=320)
    date_var = StringVar()
    date_entry = Entry(appointment_window, textvariable=date_var, font=("Arial", 14), bg=input_bg)
    date_entry.place(x=600, y=320, width=250)

    # Select Time Slot
    Label(appointment_window, text="Time Slot:", font=("Arial", 14, "bold"), bg=form_bg, fg=text_color).place(x=380, y=370)
    time_var = StringVar()
    time_slots = ["10:00 AM", "11:00 AM", "12:00 PM", "2:00 PM", "3:00 PM", "4:00 PM"]
    time_dropdown = ttk.Combobox(appointment_window, textvariable=time_var, values=time_slots, font=("Arial", 14), state="readonly")
    time_dropdown.place(x=600, y=370, width=250)
    time_dropdown.current(0)

    # Select Doctor
    Label(appointment_window, text="Select Doctor:", font=("Arial", 14, "bold"), bg=form_bg, fg=text_color).place(x=380, y=420)
    doctor_var = StringVar()
    doctor_dropdown = ttk.Combobox(appointment_window, textvariable=doctor_var, values=["Dr. Smith", "Dr. Johnson", "Dr. Brown", "Dr. Adams"], font=("Arial", 14), state="readonly")
    doctor_dropdown.place(x=600, y=420, width=250)
    doctor_dropdown.current(0)

    # Symptoms
    Label(appointment_window, text="Symptoms:", font=("Arial", 14, "bold"), bg=form_bg, fg=text_color).place(x=380, y=470)
    symptoms_var = StringVar()
    symptoms_entry = Entry(appointment_window, textvariable=symptoms_var, font=("Arial", 14), bg=input_bg)
    symptoms_entry.place(x=600, y=470, width=250)

    # Confirm Appointment Function
    def confirm_appointment():
        name = name_var.get()
        age = age_var.get()
        gender = gender_var.get()
        contact = contact_var.get()
        date = date_var.get()
        time = time_var.get()
        doctor = doctor_var.get()
        symptoms = symptoms_var.get()

        if not name or not age or not gender or not contact or not date or not time or not doctor or not symptoms:
            messagebox.showerror("Error", "All fields are required!")
            return
        
        # Save appointment details
        with open("appointments.txt", "a") as file:
            file.write(f"Name: {name}, Age: {age}, Gender: {gender}, Contact: {contact}, Date: {date}, Time: {time}, Doctor: {doctor}, Symptoms: {symptoms}\n")

        messagebox.showinfo("Success", f"Appointment confirmed for {name} on {date} at {time} with {doctor}")

        # Clear fields
        name_var.set("")
        age_var.set("")
        gender_dropdown.current(0)
        contact_var.set("")
        date_var.set("")
        time_dropdown.current(0)
        doctor_dropdown.current(0)
        symptoms_var.set("")

    # Confirm Appointment Button
    confirm_button = Button(appointment_window, text="✔ Confirm Appointment", font=("Arial", 14, "bold"), bg="green", fg="white", cursor="hand2", command=confirm_appointment)
    confirm_button.place(x=500, y=550, width=250, height=40)


# Load and resize the button image
original_appointment_img = PhotoImage(file="images/appointment.png")
appointment_button_img = original_appointment_img.subsample(5, 5)  

# Create the button
appointment_button = Button(root, image=appointment_button_img, bd=0, bg=background, cursor="hand2", command=open_appointment_section)
appointment_button.place(x=1360, y=630)  # Adjust position as needed


 

#-----------------------------------Logout Button--------------------------------------------------------------------------------------#
logout_icon=PhotoImage(file="images/logout.png")
logout_button=Button(root,image=logout_icon,bg="#df2d4b",cursor="hand2",bd=0,command=logout)
logout_button.place(x=1390,y=60)
def logout():
    root.destroy


# Start the Tkinter event loop
root.mainloop()