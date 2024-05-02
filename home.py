import customtkinter as ck
from PIL import Image


def log_in(app):
    print('home')


def home():
    app = ck.CTk()
    height = 500
    width = 900
    x = (app.winfo_screenwidth() / 2) - (width / 2)
    y = (app.winfo_screenheight() / 2) - (height / 2)
    app.geometry(f'{width}x{height}+{int(x)}+{int(y)}')
    app.title("Student Management System: Home")
    ck.set_appearance_mode("system")

    font1 = ('roboto', 24, 'bold')
    font2 = ('roboto', 15, 'bold')
    font3 = ('roboto', 13, 'bold')

    app.resizable(width=False, height=False)

    frame1 = ck.CTkFrame(master=app, width=200, fg_color="#1e71b3", corner_radius=0)
    frame1.pack(side="left", fill="y")
    frame2 = ck.CTkFrame(master=app)
    frame2.pack(side="left", fill="both", expand="True")

    # image1 = ck.CTkImage(dark_image=Image.open('images/login.jpg'), size=(200, 400))
    # label1 = ck.CTkLabel(frame1, image=image1, text='')
    # label1.pack()

    topic = ck.CTkLabel(master=frame1, text='Students', font=font1)
    topic.place(x=50, y=20)
    id = ck.CTkEntry(master=frame1, placeholder_text='Student Id', width=160)
    id.place(x=20, y=70)
    name = ck.CTkEntry(master=frame1, placeholder_text='Name', width=160)
    name.place(x=20, y=110)
    gender = ck.CTkEntry(master=frame1, placeholder_text='Gender', width=160)
    gender.place(x=20, y=150)
    age = ck.CTkEntry(master=frame1, placeholder_text='Age', width=160)
    age.place(x=20, y=190)
    e_date = ck.CTkEntry(master=frame1, placeholder_text='En-Date', width=160)
    e_date.place(x=20, y=230)
    mid = ck.CTkEntry(master=frame1, placeholder_text='Mid Term', width=160)
    mid.place(x=20, y=270)
    final = ck.CTkEntry(master=frame1, placeholder_text='Final', width=160)
    final.place(x=20, y=310)
    gpa = ck.CTkEntry(master=frame1, placeholder_text='GPA', width=160)
    gpa.place(x=20, y=350)
    enter_btn = ck.CTkButton(master=frame1, text='Enter', font=font3, fg_color="white", text_color="#1e71b3")
    enter_btn.place(x=30, y=400)

    # username_lb = ck.CTkLabel(master=frame3, text='Username', font=font3)
    # username_lb.place(x=40, y=100)
    # username_en = ck.CTkEntry(master=frame3, )
    # username_en.place(x=125, y=100)
    # password_lb = ck.CTkLabel(master=frame3, text='Password', font=font3)
    # password_lb.place(x=40, y=150)
    # password_en = ck.CTkEntry(master=frame3, )
    # password_en.place(x=125, y=150)
    # login_btn = ck.CTkButton(master=frame3, text='SignUp', font=font3)
    # login_btn.place(x=90, y=200)
    # signup_txt = ck.CTkLabel(master=frame3, text='I already registerd', font=font3)
    # signup_txt.place(x=60, y=250)
    # signup_bt = ck.CTkButton(master=frame3, text='Login', font=font3, text_color="#319ff5", fg_color="transparent",
    #                          width=50, hover_color="#343536", command=lambda: log_in(app))
    # signup_bt.place(x=180, y=250)

    app.mainloop()
