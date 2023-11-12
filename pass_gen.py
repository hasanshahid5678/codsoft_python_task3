from tkinter import *
from tkinter.ttk import *
from ttkbootstrap.constants import *
import ttkbootstrap
from PIL import Image, ImageTk
import string
import random

uppercase_alpha = list(string.ascii_uppercase)
lowercase_alpha = list(string.ascii_lowercase)
numbers = [i for i in range(10)]

def check_upper():
    global char_list
    if upper_var.get() == 1 and uppercase_alpha not in char_list:
        char_list.append(uppercase_alpha)
        lowercase_check.configure(state="normal")
        digits_check.configure(state="normal")
    elif upper_var.get() == 0 and uppercase_alpha in char_list:
        char_list.remove(uppercase_alpha)
        if lower_var.get() == 0 and digit_var.get() == 1:
            digits_check.configure(state="disabled")
        elif lower_var.get() == 1 and digit_var.get() == 0:
            lowercase_check.configure(state="disabled")
    
def check_lower():
    global char_list
    if lower_var.get() == 1 and lowercase_alpha not in char_list:
        char_list.append(lowercase_alpha)
        uppercase_check.configure(state="normal")
        digits_check.configure(state="normal")
    elif lower_var.get() == 0 and lowercase_alpha in char_list:
        char_list.remove(lowercase_alpha)
        if upper_var.get() == 0 and digit_var.get() == 1:
            digits_check.configure(state="disabled")
        elif upper_var.get() == 1 and digit_var.get() == 0:
            uppercase_check.configure(state="disabled")
            
        
def check_digits():
    global char_list
    if digit_var.get() == 1 and numbers not in char_list:
        char_list.append(numbers)
        uppercase_check.configure(state="normal")
        lowercase_check.configure(state="normal")
    elif digit_var.get() == 0 and numbers in char_list:
        char_list.remove(numbers)
        if upper_var.get() == 0 and lower_var.get() == 1:
            lowercase_check.configure(state="disabled")
        elif upper_var.get() == 1 and lower_var.get() == 0:
            uppercase_check.configure(state="disabled")
    
def generate():
    choice_list = []
    for item in char_list:
        for char in item:
            choice_list += str(char)
    
    if pass_length.get():
        password = ""
        for i in range(int(pass_length.get())):
            password += random.choice(choice_list)
        password_field.delete(0, END)
        password_field.insert(0, password)
    
            
    



root = ttkbootstrap.Window()
root.title("Password Generator")
frame1 = ttkbootstrap.Frame(root)
frame1.grid(row = 0, column = 0, columnspan=20, padx=10, pady=10)
frame2 = ttkbootstrap.Frame(root)
frame2.grid(row = 1, column = 0, columnspan=10, padx=10, pady=10)
frame3 = ttkbootstrap.Frame(root)
frame3.grid(row = 1, column = 11, columnspan=10, padx=10, pady=10)
#Create a input field
password_field = ttkbootstrap.Entry(frame1, width = 60)
password_field.grid(row = 0, column = 0, columnspan = 20, padx=10, pady=10)

generate_logo = Image.open("refresh_logo.png")
img = ImageTk.PhotoImage(generate_logo)
generate_btn = ttkbootstrap.Button(frame1, image=img, bootstyle = "danger", command=generate)
generate_btn.grid(row = 0, column = 20, padx=3, pady=3)


heading_length = ttkbootstrap.Label(frame2, text = "Password Length Between 1 and 50")
heading_length.grid(row = 0, column = 0, columnspan = 10)

def validate(input):
    try:
        return (1 <= int(input) <=50)
    except:
        if input == "":
            return True
        else:
            return False
vcmd = (root.register(validate), "%P")

pass_length = ttkbootstrap.Spinbox(frame2, from_ = 1, to = 50, validate="key", validatecommand=vcmd, width=3)
pass_length.insert(0, 8)
pass_length.grid(row = 1, column = 0, padx=10, pady=10)

upper_var = IntVar()
uppercase_check = ttkbootstrap.Checkbutton(frame3, bootstyle="danger-round-toggle", text="UPPERCASE", variable= upper_var, command=check_upper)
uppercase_check.grid(row = 0, column = 0,padx=5, pady=5, sticky = "W")
upper_var.set(1)

lower_var = IntVar()
lowercase_check = ttkbootstrap.Checkbutton(frame3, bootstyle="danger-round-toggle", text="lowercase", variable= lower_var,  command=check_lower)
lowercase_check.grid(row = 1, column = 0, padx=5, pady=5, sticky = "W")

digit_var = IntVar()
digits_check = ttkbootstrap.Checkbutton(frame3, bootstyle="danger-round-toggle", text="digits", variable= digit_var,  command=check_digits)
digits_check.grid(row = 2, column = 0, padx=5, pady=5, sticky = "W")

char_list = [uppercase_alpha]
uppercase_check.configure(state="disabled")


root.mainloop()