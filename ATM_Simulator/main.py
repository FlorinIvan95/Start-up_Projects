import tkinter as tk
from tkinter import messagebox
import pymysql

# create a connection to the MySQL database
db = pymysql.connect(
    host="localhost",
    user="root",
    password="python",
    database="atm_simulator_v2"
)

# Define a function to insert line after every four digits


def insert_hyphens(event):
    widget = event.widget
    text = widget.get()
    if len(text) == 4 or len(text) == 9 or len(text) == 14:
        widget.insert('end', "-")
    if len(text) >= 19:
        widget.delete(19, tk.END)

# Create GUI for login


def login_window():
    # Create login window
    login_win = tk.Tk()
    login_win.title('ATM - Login')
    login_win.geometry('1280x700+0+0')
    login_win.resizable(False, False)
    login_win.configure(background='lightblue')
    bg_image = tk.PhotoImage(
        file='D:\Python-Projects\Python\ATM-Simulator\image_bg.png')
    bg_label = tk.Label(login_win, image=bg_image)
    bg_label.place(x=100, y=70)

    # Create frame
    login_frame = tk.Frame(login_win, bg='lightblue')
    login_frame.place(x=780, y=280)

    # Create the login widget for "card number"
    card_image = tk.PhotoImage(
        file='D:\Python-Projects\Python\ATM-Simulator\image_card.png')
    card_label = tk.Label(login_frame, image=card_image, text='Card Number',
                          compound='left', font=('times new roman', 15, 'bold'), bg='lightblue')
    card_label.grid(row=0, column=0, padx=20)
    card_entry = tk.Entry(login_frame, font=(
        'times new roman', 15, 'bold'), bd=5)
    card_entry.grid(row=0, column=1)
    card_entry.bind("<KeyRelease>", insert_hyphens)

    # Create the login widget for "PIN"
    pin_image = tk.PhotoImage(
        file='D:\Python-Projects\Python\ATM-Simulator\image_pin.png')
    pin_label = tk.Label(login_frame, image=pin_image, text='PIN', compound='left',
                         font=('times new roman', 15, 'bold'), bg='lightblue')
    pin_label.grid(row=1, column=0, padx=20)
    pin_entry = tk.Entry(login_frame, show='*',
                         font=('times new roman', 15, 'bold'), bd=5)
    pin_entry.grid(row=1, column=1)

    # Create login validation
    def login():
        card_number = card_entry.get()
        pin = pin_entry.get()
        cursor = db.cursor()
        cursor.execute(
            "SELECT * FROM users WHERE card_number=%s AND pin=%s", (card_number, pin))
        user = cursor.fetchone()
        if user:
            login_win.destroy()
            show_balance(user)
        else:
            messagebox.showerror("Invalid card number or PIN",
                                 "Please enter valid Card Number and PIN")

    # Create login button
    login_button = tk.Button(login_frame, text='Login',
                             font=('times new roman', 12, 'bold'), width=10, fg='white', bg='royalblue',
                             bd=3, activebackground='royalblue', activeforeground='white', cursor='hand2', command=login)
    login_button.grid(row=2, column=1, pady=10)

    login_win.mainloop()


# Create GUI to display balance and allow transactions
def show_balance(user):
    # Create balance/transactions window
    cursor = db.cursor()
    cursor.execute("SELECT balance FROM users WHERE user_id=%s", (user[0]))
    balance = cursor.fetchone()[0]
    trans_win = tk.Tk()
    trans_win.title('ATM - Balance and transactions')
    trans_win.geometry('1280x700+0+0')
    trans_win.resizable(False, False)
    trans_win.configure(background='lightblue')
    bg_image = tk.PhotoImage(
        file='D:\Python-Projects\Python\ATM-Simulator\image_bg.png')
    bg_label = tk.Label(trans_win, image=bg_image)
    bg_label.place(x=100, y=70)

    # Create frame
    login_frame = tk.Frame(trans_win, bg='lightblue')
    login_frame.place(x=780, y=230)

    # Create the balance widget
    money_image = tk.PhotoImage(
        file='D:\Python-Projects\Python\ATM-Simulator\image_money.png')
    pin_label = tk.Label(login_frame, image=money_image, text='Your balance is:', compound='left',
                         font=('times new roman', 15, 'bold'), bg='lightblue')
    pin_label.grid(row=0, column=0)
    trans_label = tk.Label(login_frame, text="${:.2f}".format(balance),
                           font=('times new roman', 15, 'bold'), bd=5, bg='lightblue')
    trans_label.grid(row=0, column=1)

    # Create transaction functions
    def withdraw():
        amount = float(amount_entry.get())
        if amount > user[3]:
            error_label = tk.Label(
                trans_win, text="Insufficient funds. Please enter a valid amount.")
            error_label.pack()
        else:
            cursor = db.cursor()
            cursor.execute(
                "UPDATE users SET balance = balance - %s WHERE user_id=%s", (amount, user[0]))
            db.commit()
            cursor.execute("SELECT CURRENT_TIMESTAMP")
            date_time = cursor.fetchone()[0]
            cursor.execute(
                "INSERT INTO transactions (user_id, transaction_type, amount, date) VALUES (%s, %s, %s, %s)", (user[0], 'withdrawal', amount, date_time))
            db.commit()
            trans_win.destroy()
            show_balance(user)

    def deposit():
        amount = float(amount_entry.get())
        cursor = db.cursor()
        cursor.execute(
            "UPDATE users SET balance = balance + %s WHERE user_id=%s", (amount, user[0]))
        db.commit()
        cursor.execute("SELECT CURRENT_TIMESTAMP")
        date_time = cursor.fetchone()[0]
        cursor.execute(
            "INSERT INTO transactions (user_id, transaction_type, amount, date) VALUES (%s, %s, %s, %s)", (user[0], 'deposit', amount, date_time))
        db.commit()
        trans_win.destroy()
        show_balance(user)

    # Create the transaction widget
    amount_label = tk.Label(login_frame, text="Enter transaction amount:",
                            font=('times new roman', 15, 'bold'), bd=5, bg='lightblue')
    amount_label.grid(row=1, column=0, padx=10, pady=10)
    amount_entry = tk.Entry(login_frame, font=(
                            'times new roman', 15, 'bold'), bd=5)
    amount_entry.grid(row=1, column=1, padx=10)

    # Create withdraw and deposit buttons
    withdraw_button = tk.Button(login_frame, text='Withdraw',
                                font=('times new roman', 12, 'bold'), width=10, fg='white', bg='royalblue',
                                bd=3, activebackground='royalblue', activeforeground='white', cursor='hand2', command=withdraw)
    withdraw_button.grid(row=2, column=0, pady=20)

    deposit_button = tk.Button(login_frame, text='Deposit',
                               font=('times new roman', 12, 'bold'), width=10, fg='white', bg='royalblue',
                               bd=3, activebackground='royalblue', activeforeground='white', cursor='hand2', command=deposit)
    deposit_button.grid(row=2, column=1, pady=20)

    # Define exit function and button
    def exit():
        trans_win.destroy()

    exit_button = tk.Button(trans_win, text='Exit',
                            font=('times new roman', 12, 'bold'), width=10, fg='white', bg='royalblue',
                            bd=3, activebackground='royalblue', activeforeground='white', cursor='hand2', command=exit)
    exit_button.place(x=975, y=450)

    trans_win.mainloop()


login_window()
