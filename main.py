from tkinter import *
from tkinter import messagebox
FONT = ("Arial", 10, "bold")
from random import shuffle, randint, choice
import pyperclip
import json
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = wentry.get()
    email_a = eentry.get()
    password_a = pentry.get()
    new_data = {
        website: {
            "email": email_a,
            "password": password_a,
        }
    }
    if len(website) == 0 or len(password_a) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any of fields empty.")
    else:
        try:
            with open("data.json", mode="r") as data_file:
                data = json.load(data_file)
        except:
            with open("data.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", mode="w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            wentry.delete(0, END)
            pentry.delete(0, END)

def find_password():
    website = wentry.get()
    if len(website)== 0:
        messagebox.showerror(title= "Error", message= "Please write a website. ")
    try:
        with open("data.json", mode="r") as data_file:
            data = json.load(data_file)
    except:
        messagebox.showerror(title= "Error", message= "Data file not found.")
    else:
        if website in data:
            w_email = data[website]["email"]
            w_password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {w_email}\nPassword: {w_password}")
        else:
            messagebox.showerror(title="Error", message= "This website doesn't exist.")
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []
    # numbers = [1, 2, 3]
    # new_list = [n + 1 for n in numbers]
    l = [password_list.append(choice(letters))for _ in range(randint(8, 10) )]
    s = [password_list.append(choice(symbols))for _ in range(randint(2, 4) )]
    n = [password_list.append(choice(numbers))for _ in range(randint(2, 4) )]
    shuffle(password_list)
    password = "".join(password_list)
    pentry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady= 50)

canvas = Canvas(width=200, height=200)
photo = PhotoImage(file= "logo.png")
canvas.create_image(100, 100, image= photo)
canvas.grid(column=2, row= 1)


wentry= Entry(width= 30)
eentry = Entry(width= 49)
pentry = Entry( width= 30)

wentry.grid(column=2, row= 2)
website_l = Label(text= "Website: ", font= FONT)
website_l.grid(column=1, row= 2)
wentry.focus()


eentry.grid(column=2, row= 3, columnspan= 2)
email = Label(text= "Email/Username: ", font= FONT)
email.grid(column=1, row= 3)
eentry.insert(0, "asal@gmail.com")


pentry.grid(column=2, row= 4)
password = Label(text= "Password: ", font= FONT)
password.grid(column=1, row= 4)
generation = Button(text= "Generate Password", width= 15, command= generate_password)
generation.grid(column=3, row= 4)

add = Button(text= "Add", width= 49, command= save)
add.grid(column=2, row= 5, columnspan= 2)
search = Button(text= "Search", width= 15, command= find_password)
search.grid(column= 3, row= 2)




window.mainloop()