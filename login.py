import customtkinter as ck
from PIL import Image
import signup
import home
import sqlite3
from tkinter import messagebox
import hashlib

conn = sqlite3.connect('std_manage.db')
cursor = conn.cursor()


def sign_up(app):
    app.destroy()
    signup.signup()


def change_to_home(app, user_id):
    app.destroy()
    home.home(user_id)


def signin(username_en, password_en, app):
    username = username_en.get()
    password = password_en.get()

    if username != '' and password != '':
        try:
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, hashed_password))
            user = cursor.fetchone()
            user_id = user[0]

            if user is not None:  # Check if user exists
                messagebox.showinfo('Success', f'Welcome! {user[1]}')
                change_to_home(app, user_id)
            else:
                messagebox.showerror('Error', 'Invalid username or password.')

        except Exception as e:
            print(e)  # Print any exception for debugging
            messagebox.showerror('Error', 'Login Unsuccessful')

    else:
        messagebox.showerror('Error', 'Username and Password cannot be empty.')


def login():
    app = ck.CTk()
    height = 400
    width = 600
    x = (app.winfo_screenwidth() / 2) - (width / 2)
    y = (app.winfo_screenheight() / 2) - (height / 2)
    app.geometry(f'{width}x{height}+{int(x)}+{int(y)}')
    app.title("Student Management System: Login")
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
    topic = ck.CTkLabel(master=frame3, text='Login', font=font1)
    topic.place(x=120, y=50)
    username_lb = ck.CTkLabel(master=frame3, text='Username', font=font3)
    username_lb.place(x=40, y=100)
    username_en = ck.CTkEntry(master=frame3, )
    username_en.place(x=125, y=100)
    password_lb = ck.CTkLabel(master=frame3, text='Password', font=font3)
    password_lb.place(x=40, y=150)
    password_en = ck.CTkEntry(master=frame3, )
    password_en.place(x=125, y=150)
    login_btn = ck.CTkButton(master=frame3, text='Login', font=font3,
                             command=lambda: signin(username_en, password_en, app))
    login_btn.place(x=90, y=200)
    signup_txt = ck.CTkLabel(master=frame3, text='I don\'t have account', font=font3)
    signup_txt.place(x=40, y=250)
    signup_bt = ck.CTkButton(master=frame3, text='SignUp', font=font3, text_color="#319ff5", fg_color="transparent",
                             width=60, hover_color="#343536", command=lambda: sign_up(app))
    signup_bt.place(x=180, y=250)

    app.mainloop()
