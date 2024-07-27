import tkinter as tk
from tkinter import messagebox as msg
import sqlite3 as sql
import reg2  # Import the registration script

def lop():
    # Connect to SQLite database
    con = sql.connect("examp.db")
    cur = con.cursor()

    # Create the main form window
    form = tk.Tk()
    form.geometry('400x200')

    # Add labels and entry fields
    lblu = tk.Label(form, text="UUCMS")
    lblu.grid(row=0, column=0, padx=10, pady=10)
    etu = tk.Entry(form, width=30)
    etu.grid(row=0, column=1, padx=10, pady=10)

    lblp = tk.Label(form, text="Password")
    lblp.grid(row=1, column=0, padx=10, pady=10)
    etp = tk.Entry(form, width=30, show="*")
    etp.grid(row=1, column=1, padx=10, pady=10)

    # Function to check login credentials
    def log():
        uname = etu.get()
        pas = etp.get()

        # Query the database for the provided username and password
        cur.execute("SELECT * FROM stu WHERE rno = ? AND pasw = ?", (uname, pas))
        r = cur.fetchall()

        # Check if a matching record was found
        if r:
            msg.showinfo("Message", "Login successful!")
        else:
            msg.showerror("Error", "Invalid username or password")

    # Add login button
    btnlogin = tk.Button(form, text='Login', command=log)
    btnlogin.grid(row=2, column=1, pady=10)

    # Add register button to open the registration page
    def page():
        form.destroy()  # Close the login form
        reg2.reg()      # Call the registration function from reg2.py

    btnreg = tk.Button(form, text='Register', command=page)
    btnreg.grid(row=2, column=2, pady=10)

    # Start the main loop
    form.mainloop()

# Call the login function to start the application
lop()
