from tkinter import *
from tkinter import messagebox
from random import randint,shuffle,choice
import pyperclip
import json
# -------------------------------- FETCH DATA ----------------------------------- #

def get_data():
    website=website_entry.get().title()
    try:
        with open("PasswordList.json",'r') as l:
            data_dic=json.load(l)
    except FileNotFoundError:
        messagebox.showwarning(title="Empty Data",message="No data file found!\nCreate Records first.")
    else:
        if website in data_dic:
            site_data = data_dic[website]
            email=site_data["email"]
            password=site_data["password"]
            messagebox.showwarning(title="Records Found",message=f"Website: {website}"
                                                                            f"\nEmail: {email}\nPassword: {password}")
        else:
            messagebox.showwarning(title="No Record", message=f"No details for the {website} exists!")


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
    site=website_entry.get().title()
    website_entry.focus()
    email=email_entry.get()
    password=password_entry.get()

    new_data={site:
              {
               "email":email,
                "password":password,
              }
    }

    if len(site)==0 or len(email)==0 or len(password)==0:
        messagebox.showwarning(title="Empty Fields",message="Don't leave any field empty.")

    else:
        try:
            with open("PasswordList.json",'r') as p:
                data = json.load(p)
        except FileNotFoundError:
            with open("PasswordList.json", 'w') as p:
                json.dump(new_data, p, indent=4)
        else:
            data.update(new_data)
            with open("PasswordList.json", 'w') as p:
                json.dump(data, p, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
        messagebox.showwarning(title="Success",message="Details saved successfully!")

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

website_entry=Entry(width=32)
website_entry.grid(column=1,row=1)
website_entry.focus()
email_entry=Entry(width=50)
email_entry.grid(column=1,row=2,columnspan=2)
email_entry.insert(0,"widadabdullah@outlook.com")
password_entry=Entry(width=32)
password_entry.grid(column=1,row=3)

search_btn=Button(text="Search",width=15,command=get_data)
search_btn.grid(column=2,row=1)
add_btn=Button(text="Add",width=43,command=save_data)
add_btn.grid(column=1, row=4, columnspan=2)
generate_btn=Button(text="Generate Password",command=password_generator)
generate_btn.grid(column=2,row=3)


window.mainloop()