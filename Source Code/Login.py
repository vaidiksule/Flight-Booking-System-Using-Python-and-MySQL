from tkinter import *
from tkinter import messagebox
import mysql.connector

# =========================================================
# GUI Interface
login_window = Tk()
login_window.title("Login")
login_window.geometry("1280x720+125+50")
login_window.maxsize(width=1280, height=720)

# background
backgroundImage = PhotoImage(file="loginBg.png")
backgroundLabel = Label(login_window, image=backgroundImage)
backgroundLabel.place(x=0, y=0)


# =========================================================
# FUNCTIONS
def login_user():
    if usernameEntry.get() == "Username" or usernameEntry.get() == "":
        messagebox.showerror("Error", "Please Enter Username")
    elif passwordEntry.get() == "Password" or passwordEntry.get() == "":
        messagebox.showerror("Error", "Please Enter Password")
    else:
        try:
            con = mysql.connector.connect(host='localhost', user='root', passwd='9090')
            mycursor = con.cursor()
        except:
            messagebox.showerror("Error", 'Database Connectivity Issue, Please Try Again')
            return

        query = "use userdata"
        mycursor.execute(query)
        query = "select * from data where username=%s  and password=%s"
        mycursor.execute(query, (usernameEntry.get(), passwordEntry.get()))
        row = mycursor.fetchone()
        if row is None:
            messagebox.showerror("Error", "Invalid username or password!")
        else:
            messagebox.showinfo("Success", "Login Successful. Welcome to our Website!")
            login_window.destroy()
            import homePage


def signup_page():
    login_window.destroy()
    import SignUp


def user_enter(event):
    if usernameEntry.get() == "Username":
        usernameEntry.delete(0, END)


def pass_enter(event):
    if passwordEntry.get() == "Password":
        passwordEntry.delete(0, END)


def hide():
    openEye.config(file="closeye.png")
    if passwordEntry.get() != "Password":
        passwordEntry.config(show="*")
    eye_button.config(command=show)


def show():
    openEye.config(file="openeye.png")
    passwordEntry.config(show="")
    eye_button.config(command=hide)


# =========================================================
# username
usernameEntry = Entry(login_window, font=('Comic Sans MS', 12), bd=0, fg="gray7", bg="light cyan", width=31)
usernameEntry.place(x=486, y=357)
usernameEntry.insert(0, "Username")
usernameEntry.bind('<FocusIn>', user_enter)

# password
passwordEntry = Entry(login_window, font=('Comic Sans MS', 12), bd=0, fg="gray7", bg="light cyan", width=31)
passwordEntry.place(x=486, y=410)
passwordEntry.insert(0, "Password")
passwordEntry.bind('<FocusIn>', pass_enter)

# eye button
openEye = PhotoImage(file="openeye.png")
eye_button = Button(login_window, image=openEye, bd=0, cursor="hand2", command=hide, bg='light cyan')
eye_button.place(x=772, y=410)

'''
# forget button
forgetButton = Button(login_window, text='Forget Password?', font=('Comic Sans MS', 7, 'bold'),
                      bd=0, cursor="hand2", bg='white', fg='brown', activeforeground='brown',
                      activebackground='white', width="51")
forgetButton.place(x=486, y=440)
'''

# login button
loginButton = Button(login_window, text="Login", font=('Comic Sans MS', 11, 'bold'), bd=0,
                     fg="white", bg="DarkOrange", width="34", cursor='hand2', command=login_user)
loginButton.place(x=486, y=510)

# don't have an account
signupButton = Button(login_window, text="Don't have an account?", font=('Comic Sans MS', 7, 'bold'),
                      width='51', bd=0, activebackground='white', activeforeground='blue', fg='blue',
                      cursor='hand2', command=signup_page)
signupButton.place(x=486, y=544)

# =========================================================
login_window.mainloop()
