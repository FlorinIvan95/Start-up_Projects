import tkinter as tk


def add():
    result = float(num1.get()) + float(num2.get())
    result_label.config(text="Result: " + str(result))


def subtract():
    result = float(num1.get()) - float(num2.get())
    result_label.config(text="Result: " + str(result))


def multiply():
    result = float(num1.get()) * float(num2.get())
    result_label.config(text="Result: " + str(result))


def divide():
    result = float(num1.get()) / float(num2.get())
    result_label.config(text="Result: " + str(result))


root = tk.Tk()
root.geometry("400x400")
root.title("Calculator")

num1 = tk.Entry(root)
num1.pack()

num2 = tk.Entry(root)
num2.pack()

add_button = tk.Button(root, text="+", command=add)
add_button.pack(ipadx=200, ipady=10)

subtract_button = tk.Button(root, text="-", command=subtract)
subtract_button.pack(ipadx=200, ipady=10)

multiply_button = tk.Button(root, text="*", command=multiply)
multiply_button.pack(ipadx=200, ipady=10)

divide_button = tk.Button(root, text="/", command=divide)
divide_button.pack(ipadx=200, ipady=10)

result_label = tk.Label(root)
result_label.pack()

root.mainloop()
