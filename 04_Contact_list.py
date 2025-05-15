import tkinter as tk
from tkinter import messagebox
import csv

# File to store contacts
CONTACTS_FILE = 'contacts.csv'

# Function to load contacts from the CSV file
def load_contacts():
    contacts = []
    try:
        with open(CONTACTS_FILE, mode='r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                contacts.append(row)
    except FileNotFoundError:
        pass
    return contacts

# Function to save contacts to the CSV file
def save_contacts(contacts):
    with open(CONTACTS_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(contacts)

# Function to add a new contact
def add_contact():
    name = entry_name.get()
    phone = entry_phone.get()
    if name and phone:
        contacts.append([name, phone])
        save_contacts(contacts)
        update_contact_list()
        entry_name.delete(0, tk.END)
        entry_phone.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Both name and phone number are required.")

# Function to delete a selected contact
def delete_contact():
    try:
        selected_index = listbox.curselection()[0]
        contacts.pop(selected_index)
        save_contacts(contacts)
        update_contact_list()
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a contact to delete.")

# Function to update the contact list displayed in the listbox
def update_contact_list():
    listbox.delete(0, tk.END)
    for contact in contacts:
        listbox.insert(tk.END, f"{contact[0]} - {contact[1]}")

# Initialize the main window
root = tk.Tk()
root.title("Contact List")

# Load existing contacts
contacts = load_contacts()

# Create and place widgets
label_name = tk.Label(root, text="Name:")
label_name.pack(padx=10, pady=5)
entry_name = tk.Entry(root)
entry_name.pack(padx=10, pady=5)

label_phone = tk.Label(root, text="Phone:")
label_phone.pack(padx=10, pady=5)
entry_phone = tk.Entry(root)
entry_phone.pack(padx=10, pady=5)

button_add = tk.Button(root, text="Add Contact", command=add_contact)
button_add.pack(padx=10, pady=5)

button_delete = tk.Button(root, text="Delete Contact", command=delete_contact)
button_delete.pack(padx=10, pady=5)

listbox = tk.Listbox(root, width=50, height=10)
listbox.pack(padx=10, pady=5)

# Update the listbox with existing contacts
update_contact_list()

# Start the Tkinter event loop
root.mainloop()
