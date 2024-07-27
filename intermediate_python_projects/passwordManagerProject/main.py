import json
from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    #IT GENERATES RANDOM PASSWORD IMPOSSIBLE TO CRACK BY HACKERS

    password = ""
    password_list = []
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
               "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P",
               "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    random_length_of_password = random.randint(14, 18)
    nbr_letters = random.randint(5, random_length_of_password - 2)
    nbr_numbers = random.randint(1, random_length_of_password - nbr_letters - 1)
    nbr_symbols = random_length_of_password - nbr_letters - nbr_numbers

    for n in range(1, nbr_symbols + 1):
        password_list.append(random.choice(symbols))

    for n in range(1, nbr_numbers + 1):
        password_list.append(random.choice(numbers))
    for n in range(1, nbr_letters + 1):
        password_list.append(random.choice(letters))

    random.shuffle(password_list)

    for item in password_list:
        password += item
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get().lower()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {website: {
        "email": email,
        "password": password}}

    if website == "" or email == "" or password == "":
        messagebox.showinfo("ERROR", "Please enter all fields")
    else:

        if messagebox.askokcancel(title="WARNING",message=f"These are details:\nwebsite: {website}\nemail: {email}\npassword: {password}\nIS IT OK TO SAVE?"):
            try:
                with open('data.json', 'r') as data_file:
                    # Check if the file is empty
                    file_content = data_file.read()
                    if file_content:
                        data = json.loads(file_content)
                    else:
                        data = {}
            except FileNotFoundError:
                data = {}

            # Update data with new_data and write to the file
            data.update(new_data)
            with open('data.json', 'w') as data_file:
                json.dump(data, data_file, indent=4)

            # Clear the entries
            website_entry.delete(0, END)
            email_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- SEARCH ------------------------------- #
def search():
    website = website_entry.get().lower()
    if website=="":
        messagebox.showinfo("ERROR", "Please enter website field for searching data")
    else:
        try:
            with open('data.json', 'r') as data_file:
                file_content = data_file.read()
                if file_content:
                    data = json.loads(file_content)
                    messagebox.showinfo("SUCCESS", f"Here is your data for website:{website}:\n{data[website]}\n")
                else:
                    messagebox.showinfo("ERROR", "Data file is empty ")

        except FileNotFoundError:
            messagebox.showinfo("ERROR", "Data file is empty ")
        except KeyError:
            messagebox.showinfo("ERROR", f"There is no data with key:{website} ")


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=150, pady=150)
canvas = Canvas(window, width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

#Labels

website_label = Label(text="Website")
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username")
email_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

#Entries

website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
password_entry = Entry(width=35)
password_entry.grid(row=3, column=1, columnspan=2)

#Buttons

generate_password_button = Button(text="Generate Password", command=password_generator)
generate_password_button.grid(column=3, row=3)

searching_button = Button(text="Search", command=search)
searching_button.grid(column=3, row=1)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
