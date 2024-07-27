import sqlite3 as sql
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as msg

def reg():
    # Connect to SQLite database
    con = sql.connect("examp.db")
    cur = con.cursor()

    # Drop table if it exists and create a new one
    cur.execute('DROP TABLE IF EXISTS stu')
    cur.execute('''
        CREATE TABLE stu(
            rno VARCHAR(10),
            name VARCHAR(10),
            course VARCHAR(10),
            sem VARCHAR(10),
            gen VARCHAR(10),
            pasw VARCHAR(10),
            PRIMARY KEY(rno)
        )
    ''')
    con.commit()

    # Create the main form window
    form = tk.Tk()
    form.geometry("500x500")

    # Add labels and entry fields
    lbluno = tk.Label(form, text="UUCMS")
    lbluno.grid(row=1, column=0)
    etuno = tk.Entry(form, width=20)
    etuno.grid(row=1, column=1)

    lbln = tk.Label(form, text="Name")
    lbln.grid(row=2, column=0)
    etun = tk.Entry(form, width=20)
    etun.grid(row=2, column=1)

    lblg = tk.Label(form, text="Gender")
    lblg.grid(row=3, column=0)
    genvar = tk.StringVar()
    genvar.set("male")
    rdbm = tk.Radiobutton(form, variable=genvar, value='male', text="Male")
    rdbf = tk.Radiobutton(form, variable=genvar, value='female', text='Female')
    rdbm.grid(row=3, column=1)
    rdbf.grid(row=3, column=2)

    lblc = tk.Label(form, text="Course")
    lblc.grid(row=4, column=0)
    coursevar = tk.StringVar()
    course = ttk.Combobox(form, textvariable=coursevar, values=['BCA', 'BBA', 'BSC', 'BCOM', 'BA'])
    course.grid(row=4, column=1)

    lbls = tk.Label(form, text="Semester")
    lbls.grid(row=5, column=0)
    semvar = tk.StringVar()
    sem = ttk.Combobox(form, textvariable=semvar, values=['I', 'II', 'III', 'IV', 'V', 'VI'])
    sem.grid(row=5, column=1)

    lblp = tk.Label(form, text="Password")
    lblp.grid(row=6, column=0)
    etp = tk.Entry(form, width=20, show="*")
    etp.grid(row=6, column=1)

    # Function to save data to the database
    def save():
        uno = etuno.get()
        name = etun.get()
        course = coursevar.get()
        sem = semvar.get()
        gen = genvar.get()
        pasw = etp.get()
        
        try:
            cur.execute("INSERT INTO stu(rno, name, course, sem, gen, pasw) VALUES(?, ?, ?, ?, ?, ?)",
                        (uno, name, course, sem, gen, pasw))
            con.commit()
            msg.showinfo("Message", "Data saved successfully")
        except sql.IntegrityError:
            msg.showerror("Error", "Duplicate entry for RNO")

    # Function to display data in a Treeview
    def disp():
        cur.execute("SELECT * FROM stu")
        rows = cur.fetchall()
        
        treeview = ttk.Treeview(form, columns=("RNO", "Name", "Course", "Semester", "Gender", "Password"), show='headings')
        treeview.heading("RNO", text="RNO")
        treeview.heading("Name", text="Name")
        treeview.heading("Course", text="Course")
        treeview.heading("Semester", text="Semester")
        treeview.heading("Gender", text="Gender")
        treeview.heading("Password", text="Password")

        for row in rows:
            treeview.insert("", "end", values=row)
        
        treeview.grid(row=8, column=0, columnspan=3, padx=10, pady=10)

    # Add buttons to the form
    btnsave = tk.Button(form, text="Save", command=save)
    btnsave.grid(row=7, column=0, pady=10)

    btnd = tk.Button(form, text="Display", command=disp)
    btnd.grid(row=7, column=1, pady=10)

    # Start the main loop
    form.mainloop()

# Call the registration function
reg()
