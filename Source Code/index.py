from tkinter import *

# =========================================================
# GUI Interface
index_window: Tk = Tk()
index_window.title("Welcome")
index_window.geometry("1280x720+125+50")
index_window.maxsize(width=1280, height=720)

# background
backgroundImage = PhotoImage(file="indexBg.png")
backgroundLabel = Label(index_window, image=backgroundImage)
backgroundLabel.place(x=0, y=0)


# =========================================================
# Functions
def join_now():
    index_window.destroy()
    import SignUp


# =========================================================
# login button
joinNow = Button(index_window, text="JOIN NOW", font=('Comic Sans MS', 12, 'bold'), bd=0,
                 fg="white", bg="black", width=16, cursor='hand2', activebackground="black",
                 activeforeground="yellow", command=join_now)
joinNow.place(x=555, y=490)


# =========================================================
index_window.mainloop()


