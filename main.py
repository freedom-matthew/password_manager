from tkinter import *


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    pass


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    data = open("data.txt", "a")
    current_website = website_entry.get()
    current_email_username = email_username_entry.get()
    current_password = password_entry.get()
    data.write(f"{current_website} | {current_email_username} | {current_password}\n")
    data.close()


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
website_entry.grid(row=1, column=1, columnspan=2, sticky="ew")
website_entry.focus()
email_username_entry = Entry()
email_username_entry.grid(row=2, column=1, columnspan=2, sticky="ew")
password_entry = Entry()
password_entry.grid(row=3, column=1, columnspan=2, sticky="ew")

generate_password_button = Button(text="Generate")
generate_password_button.grid(row=4, column=0, sticky="ew")
add_button = Button(text="Add", command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky="ew")

window.mainloop()
