from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)

website_label = Label(text="Website:")
website_entry = Entry()

email_username_label = Label(text="Email/Username:")
email_username_entry = Entry()

password_label = Label(text="Password:")
password_entry = Entry()
password_button = Button(text="Generate Password")

add_button = Button(text="Add", width=25)

canvas.grid(row=0, column=1)
website_label.grid(row=1, column=0)
website_entry.grid(row=1, column=1)
email_username_label.grid(row=2, column=0)
email_username_entry.grid(row=2, column=1)
password_label.grid(row=3, column=0)
password_entry.grid(row=3, column=1)
password_button.grid(row=3, column=2)
add_button.grid(row=4, column=1)

window.mainloop()
