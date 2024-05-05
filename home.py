import customtkinter as ck
import sqlite3
from tkinter import ttk, messagebox
import login

conn = sqlite3.connect('std_manage.db')
cursor = conn.cursor()


def logout(app):
    messagebox.showinfo('Logout', 'Logged out successfully')
    app.destroy()
    login.login()


def home(user_id):
    cursor.execute('SELECT * FROM users WHERE id = ?', (user_id,))
    user = cursor.fetchone()
    username = user[1]

    def enter_button():
        insert_student()
        display_student()

    def insert_student():
        try:
            st_id = s_id.get()
            name = name_entry.get()
            gender = gender_entry.get()
            age = age_entry.get()
            midterm = mid_entry.get()
            final = final_entry.get()
            gpa = gpa_entry.get()

            # Check if any required field is empty
            if st_id == '' or name == '' or gender == '' or age == '' or midterm == '' or final == '' or gpa == '':
                messagebox.showerror('Error', 'Fill all fields before pressing enter button')
            else:
                # Convert age, midterm, final, and gpa to appropriate types
                age = int(age)
                midterm = int(midterm)
                final = int(final)
                gpa = float(gpa)

                # Insert student info into the database
                cursor.execute('INSERT INTO students VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
                               (st_id, name, gender, age, midterm, final, gpa, user_id))
                conn.commit()
                messagebox.showinfo('Success', 'Student information added successfully')

                # Clear all fields after successful insertion
                clear_fields()
        except ValueError:
            messagebox.showerror('Error', 'Please enter valid numeric values for Age, Midterm, Final, and GPA')

    def clear_fields():
        s_id.delete(0, 'end')
        name_entry.delete(0, 'end')
        gender_entry.delete(0, 'end')
        age_entry.delete(0, 'end')
        mid_entry.delete(0, 'end')
        final_entry.delete(0, 'end')
        gpa_entry.delete(0, 'end')


    def display_student():
        # Retrieve student records based on user role
        if user[3] == 'admin':
            cursor.execute('SELECT * FROM students')
        else:
            cursor.execute('SELECT * FROM students WHERE user_id = ?', (user[0],))

        students = cursor.fetchall()
        # Clear all existing rows from the Treeview
        tree.delete(*tree.get_children())
        # Insert student data into the Treeview
        for student in students:
            tree.insert('', 'end', text=student[0],
                        values=(student[1], student[2], student[3], student[4], student[5], student[6], student[7]))

        tree.pack(expand=True, fill='both')

    app = ck.CTk()
    height = 500
    width = 900
    x = (app.winfo_screenwidth() / 2) - (width / 2)
    y = (app.winfo_screenheight() / 2) - (height / 2)
    app.geometry(f'{width}x{height}+{int(x)}+{int(y)}')
    app.title(f'Student Management System: {username}\'s Home')
    ck.set_appearance_mode("system")

    font1 = ('roboto', 24, 'bold')
    # font2 = ('roboto', 15, 'bold')
    font3 = ('roboto', 13, 'bold')

    app.resizable(width=False, height=False)

    frame1 = ck.CTkFrame(master=app, width=200, fg_color="#1e71b3", corner_radius=0)
    frame1.pack(side="left", fill="y")
    frame2 = ck.CTkFrame(master=app)
    frame2.pack(side="left", fill="both", expand="True")

    topic = ck.CTkLabel(master=frame1, text='Students', font=font1)
    topic.place(x=50, y=20)
    s_id = ck.CTkEntry(master=frame1, placeholder_text='Student Id', width=160)
    s_id.place(x=20, y=70)
    name_entry = ck.CTkEntry(master=frame1, placeholder_text='Name', width=160)
    name_entry.place(x=20, y=110)
    gender_entry = ck.CTkEntry(master=frame1, placeholder_text='Gender', width=160)
    gender_entry.place(x=20, y=150)
    age_entry = ck.CTkEntry(master=frame1, placeholder_text='Age', width=160)
    age_entry.place(x=20, y=190)
    mid_entry = ck.CTkEntry(master=frame1, placeholder_text='Mid Term', width=160)
    mid_entry.place(x=20, y=230)
    final_entry = ck.CTkEntry(master=frame1, placeholder_text='Final', width=160)
    final_entry.place(x=20, y=270)
    gpa_entry = ck.CTkEntry(master=frame1, placeholder_text='GPA', width=160)
    gpa_entry.place(x=20, y=310)
    enter_btn = ck.CTkButton(master=frame1, text='Enter', font=font3, fg_color="white", text_color="#1e71b3",
                             command=lambda: enter_button())
    enter_btn.place(x=30, y=360)
    logout_btn = ck.CTkButton(master=frame1, text='Logout', font=font3, text_color="white", border_color="white",
                              border_width=1,
                              command=lambda: logout(app))
    logout_btn.place(x=30, y=400)

    # Create a Treeview widget
    tree = ttk.Treeview(frame2, columns=('Name', 'Gender', 'Age', 'Mid', 'Final', 'GPA'))
    tree.column('#0', width=100)
    tree.column('Name', width=150)
    tree.column('Gender', width=100)
    tree.column('Age', width=50)
    tree.column('Mid', width=80)
    tree.column('Final', width=80)
    tree.column('GPA', width=80)

    tree.heading('#0', text='Student ID')
    tree.heading('Name', text='Name')
    tree.heading('Gender', text='Gender')
    tree.heading('Age', text='Age')
    tree.heading('Mid', text='Midterm')
    tree.heading('Final', text='Final')
    tree.heading('GPA', text='GPA')

    display_student()

    app.mainloop()
