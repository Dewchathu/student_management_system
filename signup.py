import customtkinter as ck
from PIL import Image
import sqlite3
from tkinter import messagebox
import hashlib
import login

conn = sqlite3.connect('std_manage.db')
cursor = conn.cursor()


def log_in(app):
    app.destroy()
    login.login()


def register(username_en, password_en, app):
    username = username_en.get()
    password = password_en.get()
    role = 'user'

    if username != '' and password != '':
        cursor.execute('SELECT username FROM users WHERE username=?', [username])
        if cursor.fetchone() is not None:
            messagebox.showerror('Error', 'Username already exists.')
        else:
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            # Specify column names in the INSERT statement
            cursor.execute('INSERT INTO users (username, password, role) VALUES (?, ?, ?)', [username, hashed_password, role])
            conn.commit()
            messagebox.showinfo('Success', 'Account has been created')
            log_in(app)
    else:
        messagebox.showerror('Error', 'Username and Password cannot be empty.')


def signup():
    app = ck.CTk()
    height = 400
    width = 600
    x = (app.winfo_screenwidth() / 2) - (width / 2)
    y = (app.winfo_screenheight() / 2) - (height / 2)
    app.geometry(f'{width}x{height}+{int(x)}+{int(y)}')
    app.title("Student Management System: SignUp")
    ck.set_appearance_mode("system")

    font1 = ('roboto', 24, 'bold')
    font2 = ('roboto', 15, 'bold')
    font3 = ('roboto', 13, 'bold')

    app.resizable(width=False, height=False)

    frame1 = ck.CTkFrame(master=app, width=200, fg_color="purple", corner_radius=0)
    frame1.pack(side="left", fill="y")
    frame2 = ck.CTkFrame(master=app)
    frame2.pack(side="left", fill="both", expand="True")
    frame3 = ck.CTkFrame(master=frame2, width=300, height=300)
    frame3.place(x=50, y=50)

    image1 = ck.CTkImage(dark_image=Image.open('images/login.jpg'), size=(200, 400))
    label1 = ck.CTkLabel(frame1, image=image1, text='')
    label1.pack()

    main_topic = ck.CTkLabel(master=frame3, text='Student Management System', font=font2)
    main_topic.place(x=40, y=20)
    topic = ck.CTkLabel(master=frame3, text='SignUp', font=font1)
    topic.place(x=120, y=50)
    username_lb = ck.CTkLabel(master=frame3, text='Username', font=font3)
    username_lb.place(x=40, y=100)
    username_en = ck.CTkEntry(master=frame3, )
    username_en.place(x=125, y=100)
    password_lb = ck.CTkLabel(master=frame3, text='Password', font=font3)
    password_lb.place(x=40, y=150)
    password_en = ck.CTkEntry(master=frame3, )
    password_en.place(x=125, y=150)
    login_btn = ck.CTkButton(master=frame3, text='SignUp', font=font3,
                             command=lambda: register(username_en, password_en, app))
    login_btn.place(x=90, y=200)
    signup_txt = ck.CTkLabel(master=frame3, text='I already registerd', font=font3)
    signup_txt.place(x=60, y=250)
    signup_bt = ck.CTkButton(master=frame3, text='Login', font=font3, text_color="#319ff5", fg_color="transparent",
                             width=50, hover_color="#343536", command=lambda: log_in(app))
    signup_bt.place(x=180, y=250)

    app.mainloop()
