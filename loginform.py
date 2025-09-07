from tkinter import *
from tkinter import messagebox
import ast
from main import *

root = Tk()
root.title('Login')
root.geometry('925x500+300+200')
root.configure(bg='#fff')
root.resizable(True, True)

def signin():
    username = user.get()
    password = code.get()
    file=open('datasheet.txt','r')
    d=file.read()
    r=ast.literal_eval(d)
    file.close()

##    print(r.keys())
##    print(r.values())
    if username in r.keys() and password == r[username]:
        messagebox.showinfo('Login Successful', 'Welcome, you have logged in successfully!')
        screen = Toplevel(root)
        screen.title("App")
        screen.geometry('925x500+300+200')
        screen.config(bg="white")

        Label(screen, text='Welcome to the app', bg='#fff', font=('Calibri (Body)', 50, 'bold')).pack(expand=True) 

        screen.mainloop()
    else:
        messagebox.showerror('Invalid','invalid username or password')
########################################################################################################################################################################
def signup_command():
    window = Toplevel(root)
    window.title("SignUp")
    window.geometry('925x500+300+200')
    window.configure(bg='#fff')
    window.resizable(False, False)

    def sign():
        window.destroy()            

    def signup():
        username = user.get()
        password = code.get()
        confirm_password = conform_code.get()

        if password == confirm_password:
            try:
                with open('datasheet.txt', 'r+') as file:
                    d = file.read()
                    r = ast.literal_eval(d) if d else {}
                    dict2 = {username: password}
                    r.update(dict2)
                    file.seek(0)
                    file.truncate(0)
                    file.write(str(r))
                    messagebox.showinfo('Signup', 'Successfully signed up!')
            except FileNotFoundError:
                with open('datasheet.txt', 'w') as file:
                    file.write(str({username: password}))
                messagebox.showinfo('Signup', 'Successfully signed up!')
                window.destroy()
        else:
            messagebox.showerror('Invalid', 'Both passwords must match.')

    def on_enter(entry):
        entry.delete(0, 'end')

    def on_leave(entry, placeholder):
        if entry.get() == "":
            entry.insert(0, placeholder)

    img = PhotoImage(file='images/login.png')  # Ensure the image path is correct
    Label(window, image=img, border=0, bg='white').place(x=50, y=90)

    frame = Frame(window, width=350, height=390, bg='#fff')
    frame.place(x=480, y=50)

    heading = Label(frame, text='Sign Up', fg='#57a1f8', bg='white', font=('Microsoft Yahei UI Light', 23, 'bold'))
    heading.place(x=100, y=5)

    # Username entry
    user = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
    user.place(x=30, y=80)
    user.insert(0, 'Username')
    user.bind('<FocusIn>', lambda e: on_enter(user))
    user.bind('<FocusOut>', lambda e: on_leave(user, 'Username'))
    Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

    # Password entry
    code = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft Yahei UI Light", 11))
    code.place(x=30, y=150)
    code.insert(0, "Password")
    code.bind("<FocusIn>", lambda e: on_enter(code))
    code.bind("<FocusOut>", lambda e: on_leave(code, "Password"))
    Frame(frame, width=295, height=2, bg="black").place(x=25, y=177)

    # Confirm Password entry
    conform_code = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft Yahei UI Light", 11))
    conform_code.place(x=30, y=220)
    conform_code.insert(0, "Confirm Password")
    conform_code.bind("<FocusIn>", lambda e: on_enter(conform_code))
    conform_code.bind("<FocusOut>", lambda e: on_leave(conform_code, "Confirm Password"))
    Frame(frame, width=295, height=2, bg="black").place(x=25, y=247)

    # Sign Up Button
    Button(frame, width=39, pady=7, text="Sign Up", bg="#57a1f8", fg="white", border=0, command=signup).place(x=35, y=300)

    # Already have an account? Link
    label = Label(frame, text="I have an account", fg="black", bg="white", font=("Microsoft Yahei UI Light", 9))
    label.place(x=90, y=340)

    signin = Button(frame, width=6, text="Sign In", border=0, bg="white", cursor="hand2", fg="#57a1f8", command=sign)
    signin.place(x=200, y=340)

    window.mainloop()


####################################################################################################################################################################

    


# Load and display the image
img = PhotoImage(file='images/login.png')  # Make sure 'login.png' is in the same directory
Label(root, image=img, bg='white').place(x=50, y=50)  # Adjust position as needed

frame=Frame(root,width=350,height=350,bg="")
frame.place(x=480,y=70)

heading = Label(frame, text='Sign in', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=100, y=5)
###############################################################
def on_enter(e):
    user.delete(0,'end')
def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,'Username')
user = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
user.place(x=30, y=80)
user.insert(0, 'Username')
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>',on_leave)
Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)
##################################################################
def on_enter(e):
    code.delete(0,'end')
def on_leave(e):
    name=user.get()
    if name=='':
        code.insert(0,'Password')
code = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
code.place(x=30, y=150)
code.insert(0, 'Password')
code.bind('<FocusIn>',on_enter)
code.bind('<FocusOut>',on_leave)
Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)
########################################################
Button(frame, width=39, pady=7, text='Sign in', bg='#57a1f8', fg='white', border=0,command=signin).place(x=35, y=204)
label = Label(frame, text="Don't have an account?", fg='black', bg='white', font=('Microsoft YaHei UI Light', 9))
label.place(x=75, y=270)

sign_up = Button(frame, width=6, text='Sign Up', border=0, bg='white', cursor='hand2', fg='#57a1f8',command=signup_command)
sign_up.place(x=215,y=270)


root.mainloop()



