import sqlite3

from tkinter import *
from tkinter import messagebox

def Connection():
    global conn, cursor
    conn = sqlite3.connect("db/db_1640705610.db")
    cursor = conn.cursor()


def Create_Windows():
    root = Tk()
    root.title("Final Test - by Purin Singkaew 1640705610")
    x = root.winfo_screenwidth() / 2 - w / 2
    y = root.winfo_screenheight() / 2 - h / 2
    root.geometry("%dx%d+%d+%d" %(w, h, x, y))

    root.rowconfigure((0), weight=1)
    root.rowconfigure((1), weight=3)
    root.columnconfigure((0,1,2,3), weight=1)
    root.config(bg="#f8a488")

    return root


def LoginPage():
    global login_frm
    login_frm = Frame(root, bg="#ffd3b4")
    login_frm.columnconfigure((0,1,2,3,4,5), weight=1)
    login_frm.rowconfigure(0, weight=1)
    login_frm.grid(row=0, column=1, columnspan=2,sticky="news", padx=20, pady=10)

    Label(
        login_frm,
        bg = "#ffd3b4",
        image = profile_img
    ).grid(row=0, column=0)

    Label(
        login_frm,
        text="Username:",
        fg = "black",
        bg="#ffd3b4",
        font = "verdana 20"
    ).grid(row=0, column=1)

    Entry(
        login_frm,
        font="verdana 20",
        bg = "#e9896a",
        fg = "black",
        textvariable=user_spy
    ).grid(row=0, column=2)
    
    Label(
        login_frm,
        text="Password:",
        fg = "black",
        bg="#ffd3b4",
        font = "verdana 20"
    ).grid(row=0, column=3)

    Entry(
        login_frm,
        font="verdana 20",
        bg = "#e9896a",
        fg = "black",
        textvariable=pwd_spy,
        show = "*"
    ).grid(row=0, column=4)

    Button(
        login_frm,
        text="Login",
        font="verdana 21",
        command=Login_clicked
    ).grid(row=0, column=5)


    Label(
        root,
        image=course_img,
        bg = "#f8a488"
    ).grid(row=1, column=0, columnspan=4, sticky="news")


def MainPage(user):
    global right
    login_frm.destroy()
    top = Frame(root, bg="#d8ac9c")
    top.rowconfigure(0, weight=1)
    top.columnconfigure((0,1), weight=1)
    top.grid(row=0, column=0, columnspan=4, sticky="news")

    left = Frame(root, bg="#e9896a")
    left.rowconfigure((0,1,2,3,4), weight=1)
    left.columnconfigure(0, weight=1)
    left.grid(row=1, column=0, columnspan=2, sticky="news")

    right = Frame(root, bg="#ffd3b4")
    right.rowconfigure(0, weight=1)
    right.columnconfigure(0, weight=1)
    right.grid(row=1, column=2, columnspan=2, sticky="news")

    Label(
        top,
        image=profile_img,
        bg="#d8ac9c",
    ).grid(row=0, column=0, sticky='e')

    Label(
        top,
        text="Login name: %s" %(user[2]),
        font="verdana 20",
        bg="#d8ac9c",
        fg="black"
    ).grid(row=0, column=1, sticky='w')


    Button(
        left,
        text="Find Student",
        font = "verdana 20",
        image=find,
        compound=LEFT,
        command=find_clicked
    ).grid(row=1, column=0, sticky="news", padx=50)
    
    Button(
        left,
        text="Edit Student Data",
        font = "verdana 20",
        image=edit,
        compound=LEFT,
        command=edit_clicked
    ).grid(row=2, column=0, sticky="news", padx=50, pady=10)
    
    Button(
        left,
        text="Close Program",
        font = "verdana 20",
        image=close,
        compound=LEFT,
        command=quit
    ).grid(row=3, column=0, sticky="news", padx=50)

    
def Login_clicked():
    sql = '''
    SELECT * 
    FROM login
    WHERE username = ? AND pwd = ?
    '''
    cursor.execute(sql, [user_spy.get(), pwd_spy.get()])
    res = cursor.fetchone()
    if res:
        messagebox.showinfo("admin:", "Login Successfully.")
        MainPage(res)
    else:
        messagebox.showwarning("admin:", "Username/Password incorrect")
        user_spy.set("")
        pwd_spy.set("")


def find_clicked():
    global bot
    frm = Frame(right, bg="#ffd3b4")
    frm.rowconfigure((0), weight=1)
    frm.rowconfigure((1), weight=3)
    frm.columnconfigure(0, weight=1)
    frm.grid(row=0, column=0, sticky="news")

    top = Frame(frm, bg="#ffd3b4")
    top.rowconfigure(0, weight=1)
    top.columnconfigure((0,1), weight=1)
    top.grid(row=0, column=0, sticky="news")
    
    bot = Frame(frm, bg="#ffd3b4")
    bot.rowconfigure((0,1,2,3), weight=1)
    bot.rowconfigure(4, weight=3)
    bot.columnconfigure(0, weight=1)
    bot.grid(row=1, column=0, sticky="news")
    
    Label(
        top,
        text="Student ID:",
        fg = "black",
        bg="#ffd3b4",
        font = "verdana 15"
    ).grid(row=0, column=0, sticky='e')
    
    Entry(
        top,
        font="verdana 20",
        bg = "#e9896a",
        fg = "black",
        textvariable=sid_spy
    ).grid(row=0, column=1)

    Button(
        top,
        image=find,
        command=find_std
    ).grid(row=0, column=2, sticky='w')


def find_std():
    sql = '''
    SELECT *
    FROM table_1640705610
    WHERE sid = ?
    '''
    cursor.execute(sql, [sid_spy.get()])
    res = cursor.fetchone()
    if res:
        Label(
        bot,
        text="ID: %d" %res[0],
        fg = "blue",
        bg="#ffd3b4",
        font = "verdana 15"
    ).grid(row=0, column=0)
        Label(
        bot,
        text="Name: %s" %res[1],
        fg = "blue",
        bg="#ffd3b4",
        font = "verdana 15"
    ).grid(row=1, column=0)
        Label(
        bot,
        text="Year: %d" %res[2],
        fg = "blue",
        bg="#ffd3b4",
        font = "verdana 15"
    ).grid(row=2, column=0)
        Label(
        bot,
        text="GPA: %.2f" %res[3],
        fg = "blue",
        bg="#ffd3b4",
        font = "verdana 15"
    ).grid(row=3, column=0)

        Label(
            bot,
            image=student,
            bg="#ffd3b4"
        ).grid(row=4, column=0, sticky="news")
    
    else:
        Label(
            bot,
            text = '''Data not found.\n Try again.''',
            font="verdana 20 bold",
            fg = "#d8ac9c",
            bg= "#ffd3b4"
        ).grid(row=0, column=0, rowspan=5, sticky="news")


def edit_clicked():
    frm = Frame(right, bg="#ffd3b4")
    frm.rowconfigure((0,1,2,3,4,5), weight=1)
    frm.columnconfigure((0,1), weight=1)
    frm.grid(row=0, column=0, sticky="news")

    Label(
        frm,
        text="Edit Student Page",
        fg = "#f8a488",
        bg="#ffd3b4",
        font = "verdana 22 bold"
    ).grid(row=0, column=0, columnspan=2)

    Label(
        frm,
        text="Student ID:",
        fg = "#f8a488",
        bg="#ffd3b4",
        font = "verdana 20"
    ).grid(row=1, column=0, sticky='e')

    Entry(
        frm,
        font="verdana 20",
        bg = "#e9896a",
        fg = "black",
        textvariable=sid_spy2
    ).grid(row=1, column=1, sticky='w')
    
    Label(
        frm,
        text="Full Name:",
        fg = "#f8a488",
        bg="#ffd3b4",
        font = "verdana 20"
    ).grid(row=2, column=0, sticky='e')

    Entry(
        frm,
        font="verdana 20",
        bg = "#e9896a",
        fg = "black",
        textvariable=fn_spy
    ).grid(row=2, column=1, sticky='w')
    
    Label(
        frm,
        text="Year:",
        fg = "#f8a488",
        bg="#ffd3b4",
        font = "verdana 20"
    ).grid(row=3, column=0, sticky='e')

    Entry(
        frm,
        font="verdana 20",
        bg = "#e9896a",
        fg = "black",
        textvariable=year_spy
    ).grid(row=3, column=1, sticky='w')
    
    Label(
        frm,
        text="GPA:",
        fg = "#f8a488",
        bg="#ffd3b4",
        font = "verdana 20"
    ).grid(row=4, column=0, sticky='e')

    Entry(
        frm,
        font="verdana 20",
        bg = "#e9896a",
        fg = "black",
        textvariable=gpa_spy
    ).grid(row=4, column=1, sticky='w')

    Button(
        frm,
        image=find,
        command=edit_student
    ).grid(row=1, column=1, sticky='e', padx=20)

    Button(
        frm,
        text="Update Student Data",
        font="verdana 20",
        command=update_clicked
    ).grid(row=5, column=0)

    Button(
        frm,
        text="Reset Data",
        font="verdana 20",
        command=reset
    ).grid(row=5, column=1)


def update_clicked():
    sql = '''
    UPDATE table_1640705610
    SET sname = ?, syear = ?, gpa = ?
    WHERE sid = ?
    '''
    cursor.execute(sql, [fn_spy.get(), year_spy.get(), gpa_spy.get(), sid_spy2.get()])
    conn.commit()
    messagebox.showinfo("Admin:", "Update Successfully.")


def reset():
    sid_spy2.set("")
    fn_spy.set("")
    year_spy.set("")
    gpa_spy.set("")


def edit_student():
    sql = '''
    SELECT *
    FROM table_1640705610
    WHERE sid = ?
    '''
    cursor.execute(sql, [sid_spy2.get()])
    res = cursor.fetchone()
    if res:
        fn_spy.set(res[1])
        year_spy.set(res[2])
        gpa_spy.set(res[3])
    else:
        messagebox.showwarning("admin:", "Student ID Not Found")


w = 1000
h = 600

Connection()
root = Create_Windows()
profile_img = PhotoImage(file="imgset1/profile.png").subsample(5,5)
course_img = PhotoImage(file="imgset1/course.png")
find = PhotoImage(file="imgset1/search.png")
edit = PhotoImage(file="imgset1/edit.png")
close = PhotoImage(file="imgset1/display.png")
student = PhotoImage(file="imgset1/student.png")

user_spy = StringVar()
pwd_spy = StringVar()
sid_spy = StringVar()
sid_spy2 = StringVar()
fn_spy = StringVar()
year_spy = StringVar()
gpa_spy = StringVar()
LoginPage()
root.mainloop()
