import random
import string
import tkinter as tk


def generate_password(length):
    letters_and_numbers = string.ascii_letters + string.digits
    password = "".join(random.choice(letters_and_numbers)
                       for i in range(length))
    return password


def show_password():
    length = int(entry_length.get())
    password = generate_password(length)
    label_password.config(text="Generated password: " + password)


app = tk.Tk()
app.geometry("400x200")
app.title("Password Generator")

label_length = tk.Label(text="Enter password length:")
entry_length = tk.Entry()
button_generate = tk.Button(text="Generate", command=show_password)
label_password = tk.Label(text="")

label_length.pack()
entry_length.pack()
button_generate.pack()
label_password.pack()

app.mainloop()
