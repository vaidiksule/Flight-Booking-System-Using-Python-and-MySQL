from tkinter import *
from tkinter import messagebox, Entry, Checkbutton
import mysql.connector

# =========================================================
# GUI Interface
signup_window = Tk()
signup_window.title("Signup")
signup_window.geometry("1280x720+125+50")
signup_window.maxsize(width=1280, height=720)

# background
backgroundImage = PhotoImage(file="registrationBg.png")
backgroundLabel = Label(signup_window, image=backgroundImage)
backgroundLabel.place(x=0, y=0)


# =========================================================
# FUNCTIONS
def signup_user():
    if usernameEntry.get() == "Username" or usernameEntry.get() == "" or emailEntry.get() == "Email" or \
            emailEntry.get() == "" or passwordEntry.get() == "Password" or conformEntry.get() == "Conform Password" or \
            conformEntry.get() == "":
        messagebox.showerror('Error', 'All Fields Are Required!')
    elif passwordEntry.get() != conformEntry.get():
        messagebox.showerror('Error', 'password Mismatch!')
    elif check.get() == 0:
        messagebox.showerror('Error', 'Please Agree To Our Terms & Condition')
    else:
        try:
            con = mysql.connector.connect(host='localhost', user='root', passwd='9090')
            mycursor = con.cursor()
        except:
            messagebox.showerror("Error", 'Database Connectivity Issue, Please Try Again')
            return

        query = 'use userdata'
        mycursor.execute(query)
        query = 'select * from data where username=%s or email=%s'
        mycursor.execute(query, (usernameEntry.get(), emailEntry.get()))
        row = mycursor.fetchone()
        if row is not None:
            messagebox.showerror("Error", 'Username or Email Already Exist!')
        else:
            query = "insert into data(username,email,password) values(%s,%s,%s)"
            mycursor.execute(query, (usernameEntry.get(), emailEntry.get(), passwordEntry.get()))
            con.commit()
            con.close()
            clear()
            messagebox.showinfo("Success", "Registration Successful, You may now login.")
            login_page()


def clear():
    usernameEntry.delete(0, END)
    emailEntry.delete(0, END)
    passwordEntry.delete(0, END)
    conformEntry.delete(0, END)
    check.set(0)


def login_page():
    signup_window.destroy()
    import Login


def user_enterN(event):
    if usernameEntry.get() == "Username":
        usernameEntry.delete(0, END)


def user_enterE(event):
    if emailEntry.get() == "Email":
        emailEntry.delete(0, END)


def pass_enter(event):
    if passwordEntry.get() == "Password":
        passwordEntry.delete(0, END)


def conform_pass_enter(event):
    if conformEntry.get() == "Conform Password":
        conformEntry.delete(0, END)


# =========================================================
# usernameEntry
usernameEntry = Entry(signup_window, font=('Comic Sans MS', 12), bd=0, fg="gray7", bg="light cyan", width=31)
usernameEntry.place(x=486, y=337, )
usernameEntry.insert(0, "Username")
usernameEntry.bind('<FocusIn>', user_enterN)

# emailEntry
emailEntry = Entry(signup_window, font=('Comic Sans MS', 12), bd=0, fg="gray7", bg="light cyan", width=31)
emailEntry.place(x=486, y=384)
emailEntry.insert(0, "Email")
emailEntry.bind('<FocusIn>', user_enterE)

# passwordEntry
passwordEntry = Entry(signup_window, font=('Comic Sans MS', 12), bd=0, fg="gray7", bg="light cyan", width=31)
passwordEntry.place(x=486, y=430)
passwordEntry.insert(0, "Password")
passwordEntry.bind('<FocusIn>', pass_enter)

# conform passwordEntry
conformEntry = Entry(signup_window, font=('Comic Sans MS', 12), bd=0, fg="gray7", bg="light cyan", width=31)
conformEntry.place(x=486, y=477)
conformEntry.insert(0, "Conform Password")
conformEntry.bind('<FocusIn>', conform_pass_enter)

# terms and condition
check = IntVar()
termsCondition = Checkbutton(signup_window, text='Agree to out Terms and Condition.',
                                          font=('Comic Sans MS', 7), variable=check, width="47")
termsCondition.place(x=486, y=530)

# signup button
signupButton = Button(signup_window, text="Signup", font=('Comic Sans MS', 11, 'bold'),
                      bd=0, fg="white", bg="DarkOrange", width="34", cursor='hand2', command=signup_user)
signupButton.place(x=486, y=550)

# already have an account
loginButton = Button(signup_window, text='Already have an account?', font=('Comic Sans MS', 7, 'bold'),
                     width='51', bd=0, activebackground='white', activeforeground='blue', fg='blue',
                     cursor='hand2', command=login_page)
loginButton.place(x=486, y=584)

# =========================================================
signup_window.mainloop()
