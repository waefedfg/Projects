import tkinter as tk
from tkinter import ttk
import os
from cryptography.fernet import Fernet
import json

full_dir = os.path.join("passwords", "key.txt")
just_dir = os.path.join("passwords")
actual_stuff = os.path.join("passwords", "passwords.json")


youre_going_to_the_big_leagues_kid = {
    "credentials": [],
}


try:
	os.makedirs("passwords")
	print("Passwords folder not found, creating one")
except:
	print("Directory Found")

if os.path.isfile(full_dir):
	print("Original key file detected, not making another one")
else:
	print("No key file in passwords folder, creating one")
	with open(full_dir, "wb") as bussin_key:
		bussin_key.write(Fernet.generate_key())

with open(full_dir, "rb") as reading_key:
	key = reading_key.read()

if os.path.isfile(actual_stuff):
	with open(actual_stuff, "r") as credential_file:
		youre_going_to_the_big_leagues_kid = json.load(credential_file)
else:
	with open(actual_stuff, "w") as credential_file:
		json.dump(youre_going_to_the_big_leagues_kid, credential_file, indent=4)


print(key)
def add_file():
	username_unencrypted = username.get()
	user_encrypted = Fernet(key).encrypt(username_unencrypted.encode()).decode()
	password_unencrypted = password.get()
	pass_encrypted = Fernet(key).encrypt(password_unencrypted.encode()).decode()
	youre_going_to_the_big_leagues_kid['credentials'].append({
			"username": user_encrypted,
			"password": pass_encrypted
		})
	with open(actual_stuff, "w") as credentials:
		json.dump(youre_going_to_the_big_leagues_kid, credentials, indent=4)
	



root = tk.Tk()
root.geometry("1000x500")
root.title("Password Saver")


username = tk.Entry(root)
username.pack()
password = tk.Entry(root)
password.pack()

add_creds = tk.Button(root, text="Test", command=add_file)
add_creds.pack()

treeview = ttk.Treeview()

credentials = treeview.insert("", tk.END, text="Credentials")
treeview.insert(credentials, tk.END, text="Test?")
treeview.column("#0", width=1000)

treeview.pack()

def update():
	with open(actual_stuff, "r") as the_json:
		data = json.load(the_json)

	for item in treeview.get_children():
		treeview.delete(item)
	global credentials
	credentials = treeview.insert("", tk.END, text="Credentials")
	for login in data['credentials']:
		real_usernames = Fernet(key).decrypt(login['username'].encode()).decode()
		real_passwords = Fernet(key).decrypt(login['password'].encode()).decode()
		treeview.insert(credentials, tk.END, text=real_usernames + ":" + real_passwords)
		treeview.pack()


update = tk.Button(root, text="Update", command=update)
update.pack()

root.mainloop()
