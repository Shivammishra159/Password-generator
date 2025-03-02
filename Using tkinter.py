from tkinter import *
import string
import random
import pyperclip


def generator():
    all_characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    password_length = int(length_Box.get())

    passwordField.delete(0, END)  # Clear previous password
    passwordField.insert(0, "".join(random.sample(all_characters, password_length)))  # Strongest password


def copy():
    random_password = passwordField.get()
    pyperclip.copy(random_password)


# GUI Setup
root = Tk()
root.config(bg='Black')
root.title("Password Generator")
root.geometry("350x250")

Font = ('arial', 13, 'bold')

# Title Label
passwordLabel = Label(root, text='Password Generator', font=('times new roman', 20, 'bold'), bg='gray20', fg='white')
passwordLabel.grid(row=0, column=1, columnspan=2, pady=10)

# Password Length Label and Spinbox
lengthLabel = Label(root, text='Password Length', font=Font, bg='gray20', fg='white')
lengthLabel.grid(row=1, column=0, columnspan=2, pady=5)

length_Box = Spinbox(root, from_=5, to_=18, width=5, font=Font)
length_Box.grid(row=2, column=0, columnspan=2, pady=5)

# Generate Button
generateButton = Button(root, text='Generate ', font=Font, command=generator)
generateButton.grid(row=3, column=0, columnspan=2, pady=5)

# Password Field
passwordField = Entry(root, width=25, bd=2, font=Font)
passwordField.grid(row=4, column=0, columnspan=2, pady=5)

# Copy Button
copyButton = Button(root, text='Copy', font=Font, command=copy)
copyButton.grid(row=5, column=0, columnspan=2, pady=5)

root.mainloop()
