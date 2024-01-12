import json
import pyperclip
from random import choice, randint, shuffle
from tkinter import *
from tkinter import messagebox


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------------ #
def save():
    website = website_entry.get()
    email_username = email_username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email_username,
            "password": password,
        }
    }

    if len(website) == 0 or len(email_username) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops!", message="Please make sure you haven't left any fields empty.")
    else:
        user_accept = messagebox.askokcancel(title=website, message=f"These are the details you entered:\n"
                                                                    f"Email/Username:{email_username}\n"
                                                                    f"Password: {password}\n"
                                                                    f"Is it OK to save?")

        if user_accept:
            try:
                with open("data.json", "r") as data_file:
                    old_data = json.load(data_file)

            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)

            else:
                old_data.update(new_data)

                with open("data.json", "w") as data_file:
                    json.dump(old_data, data_file, indent=4)

            finally:
                website_entry.delete(0, END)
                email_username_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------------ #
def find_password():
    website = website_entry.get()

    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showinfo(title="Oops", message="No Data File Found")

    else:
        if website in data.keys():
            messagebox.showinfo(title=website, message=f"Email: {data[website]['email']}\n"
                                                       f"Password: {data[website]['password']}")

        else:
            messagebox.showinfo(title="Oops", message="No details for the website exists")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=80, pady=80)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=0, columnspan=3)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0, sticky="e")
email_username_label = Label(text="Email/Username:")
email_username_label.grid(row=2, column=0, sticky="e")
password_label = Label(text="Password:")
password_label.grid(row=3, column=0, sticky="e")

website_entry = Entry()
website_entry.grid(row=1, column=1, sticky="ew")
website_entry.focus()
email_username_entry = Entry()
email_username_entry.grid(row=2, column=1, columnspan=2, sticky="ew")
password_entry = Entry()
password_entry.grid(row=3, column=1, sticky="ew")

search_button = Button(text="Search", command=find_password)
search_button.grid(row=1, column=2, sticky="ew")
generate_password_button = Button(text="Generate", command=generate_password)
generate_password_button.grid(row=3, column=2, sticky="ew")
add_button = Button(text="Add", command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky="ew")

window.mainloop()
