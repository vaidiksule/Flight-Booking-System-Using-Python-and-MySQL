from tkinter import *
from tkinter import messagebox, Entry, filedialog
import mysql.connector

# =========================================================
# GUI Interface
home_window = Tk()
home_window.title("Home Page")
home_window.geometry("1280x720+125+50")
home_window.maxsize(width=1280, height=720)

# background
backgroundImage = PhotoImage(file="mainPageBg.png")
backgroundLabel = Label(home_window, image=backgroundImage)
backgroundLabel.place(x=0, y=0)


# =========================================================
# FUNCTIONS

def submit():
    if toVar.get() == "" or fromVar.get() == "" or nameEntry == "" or classVar.get() == "" or \
            departureEntry == "" or ageEntry == "":
        messagebox.showerror('Error', 'All Fields Are Required!')

    else:
        try:
            con = mysql.connector.connect(host='localhost', user='root', passwd='9090')
            mycursor = con.cursor()
        except:
            messagebox.showerror("Error", 'Database Connectivity Issue, Please Try Again')
            return

        query = 'use userdata'
        mycursor.execute(query)
        query = "insert into flight_details(_FROM,_TO,PASSENGER,DATE,AGE,CLASS) values(%s,%s,%s,%s,%s,%s)"
        mycursor.execute(query, (fromVar.get(), toVar.get(), nameEntry.get(), departureEntry.get(), ageEntry.get(),
                                 classVar.get()))
        con.commit()
        ticket()
        clear()
        messagebox.showinfo("Success", "Ticket Booked Successfully")


def clear():
    fromVar.set(0)
    toVar.set(0)
    nameEntry.delete(0, END)
    departureEntry.delete(0, END)
    ageEntry.delete(0, END)
    classVar.set(0)


def ticket():
    f = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    f.write('-' * 59 + '\n')
    f.write('=' * 18 + 'EASEMYWAY' + '=' * 32 + '\n')
    f.write('-' * 59 + '\n\n')
    f.write('*  PASSENGER NAME         : ' + str(nameEntry.get()) + '\n')
    f.write('~' * 40 + '\n')
    f.write('*  AGE                    : ' + str(ageEntry.get()) + '\n')
    f.write('~' * 40 + '\n')
    f.write('*  CLASS                  : ' + str(classVar.get()) + '\n')
    f.write('~' * 40 + '\n')
    f.write('*  FROM                   : ' + str(fromVar.get()) + '\n')
    f.write('~' * 40 + '\n')
    f.write('*  TO                     : ' + str(toVar.get()) + '\n')
    f.write('~' * 40 + '\n')
    f.write('*  DEPARTURE DATE         : ' + str(departureEntry.get()) + '\n')
    f.write('~' * 40 + '\n\n')
    f.write('``````````````Happy Journey``````````````' + '\n')
    f.write('=' * 59 + '\n')
    f.write('=' * 59 + '\n')
    f.close()


# =========================================================
# from where drop menu
fromPlaceLabel = Label(home_window, text="From where: ")
fromPlaceLabel.place(x=280, y=230)
fromList = ['Indore', 'Bhopal', 'Delhi', 'Chennai', 'Hyderabad', 'Jammu', 'Punjab', 'Mumbai']
fromVar = StringVar()
fromEntry = OptionMenu(home_window, fromVar, *fromList)
fromEntry.place(x=280, y=250)
fromEntry.config(font=("Comic Sans MS", 11, 'bold'), width=25, bg='white', fg='black', borderwidth=0, padx=0, pady=7)

# to where drop menu
toPlaceLabel = Label(home_window, text="To where: ")
toPlaceLabel.place(x=280, y=300)
toPlaces = ['Indore', 'Bhopal', 'Delhi', 'Chennai', 'Hyderabad', 'Jammu', 'Punjab', 'Mumbai']
toVar = StringVar()
toEntry = OptionMenu(home_window, toVar, *toPlaces)
toEntry.place(x=280, y=320)
toEntry.config(font=("Comic Sans MS", 11, 'bold'), width=25, bg='white', fg='black', borderwidth=0, padx=0, pady=7)

# class
flightClass = Label(home_window, text="Class: ")
flightClass.place(x=280, y=370)
ClassList = ['Economy', 'Business', 'First Class']
classVar = StringVar()
ClassEntry = OptionMenu(home_window, classVar, *ClassList)
ClassEntry.place(x=280, y=390)
ClassEntry.config(font=("Comic Sans MS", 11, 'bold'), width=25, bg='white', fg='black', borderwidth=0, padx=0, pady=7)

# passenger name
nameLabel = Label(home_window, text="Passenger Name: ")
nameLabel.place(x=600, y=230)
nameEntry = Entry(home_window, font=("Comic Sans MS", 11, 'bold'), width=28, bg='white', fg='black')
nameEntry.place(x=600, y=250)

# passenger age
ageLabel = Label(home_window, text="Age: ")
ageLabel.place(x=600, y=300)
ageEntry = Entry(home_window, font=("Comic Sans MS", 11, 'bold'), width=28, bg='white', fg='black')
ageEntry.place(x=600, y=320)

# departure date
departureDate = Label(home_window, text="Departure Date:")
departureDate.place(x=600, y=370)
departureEntry = Entry(home_window, font=("Comic Sans MS", 11, 'bold'), width=28, bg='white', fg='black')
departureEntry.place(x=600, y=390)

# submit
submitButton = Button(home_window, text="Submit", font=('Comic Sans MS', 11, 'bold'), bd=0, fg="white", bg="gray",
                      width="20", cursor='hand2', command=submit)
submitButton.place(x=280, y=570)

# =========================================================
home_window.mainloop()
