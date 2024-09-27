from tkinter import *
from tkinter import messagebox
from random import randint,shuffle,choice
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    l= [choice(letters) for letter in range(nr_letters)]
    s= [choice(symbols) for symbol in range(nr_symbols)]
    n= [choice(numbers) for char in range(nr_numbers)]

    password_list = l+s+n
    shuffle(password_list)

    password = "".join(password_list)
    pyperclip.copy(password)
    password_entry.insert(0,password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_data():
    site=website_entry.get()
    website_entry.focus()
    email=email_entry.get()
    password=password_entry.get()

    if len(site)==0 or len(email)==0 or len(password)==0:
        messagebox.showwarning(title="Empty Fields",message="Don't leave any field empty.")

    else:
        is_ok=messagebox.askyesno(title=site, message=f"The details entered are\nWebsite: {site}\nEmail: {email}\n"
                            f"Password: {password}\nIs it ok to save?")

        if is_ok:
            with open("PasswordList.txt",'a') as p:
                p.write(f"{site} | {email} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)
            messagebox.showwarning(title="Sucess",message="Details saved successfully!")

# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)

canvas=Canvas(width=200,height=200)
img=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=img)
canvas.grid(column=1,row=0)

website_label=Label(text="Website:")
website_label.grid(column=0,row=1)
email_label=Label(text="Email/Username:")
email_label.grid(column=0,row=2)
password_label=Label(text="Password:")
password_label.grid(column=0,row=3)

website_entry=Entry(width=50)
website_entry.grid(column=1,row=1,columnspan=2)
website_entry.focus()
email_entry=Entry(width=50)
email_entry.grid(column=1,row=2,columnspan=2)
email_entry.insert(0,"widadabdullah@outlook.com")
password_entry=Entry(width=32)
password_entry.grid(column=1,row=3)

add_btn=Button(text="Add",width=43,command=save_data)
add_btn.grid(column=1, row=4, columnspan=2)
generate_btn=Button(text="Generate Password",command=password_generator)
generate_btn.grid(column=2,row=3)


window.mainloop()