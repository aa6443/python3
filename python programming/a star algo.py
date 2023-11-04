import tkinter as tk

def submit_form():
    name = name_entry.get()
    course = course_entry.get()
    semester = semester_entry.get()
    form_number = form_number_entry.get()
    contact_number = contact_number_entry.get()
    email_address = email_address_entry.get()
    address = address_entry.get()
    # Print the form data to the console
    print(f"Name: {name}")
    print(f"Course: {course}")
    print(f"Semester: {semester}")
    print(f"Form Number: {form_number}")
    print(f"Contact Number: {contact_number}")
    print(f"Email Address: {email_address}")
    print(f"Address: {address}")
    # Clear the form fields
    name_entry.delete(0, tk.END)
    course_entry.delete(0, tk.END)
    semester_entry.delete(0, tk.END)
    form_number_entry.delete(0, tk.END)
    contact_number_entry.delete(0, tk.END)
    email_address_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)
# Create the main window
root = tk.Tk()
root.title("Registration Form")
# Create the form fields
name_label = tk.Label(root, text="Name:")
name_label.grid(row=0, column=0, sticky=tk.W)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

course_label = tk.Label(root, text="Course:")
course_label.grid(row=1, column=0, sticky=tk.W)
course_entry = tk.Entry(root)
course_entry.grid(row=1, column=1)

semester_label = tk.Label(root, text="Semester:")
semester_label.grid(row=2, column=0, sticky=tk.W)
semester_entry = tk.Entry(root)
semester_entry.grid(row=2, column=1)

form_number_label = tk.Label(root, text="Form Number:")
form_number_label.grid(row=3, column=0, sticky=tk.W)
form_number_entry = tk.Entry(root)
form_number_entry.grid(row=3, column=1)

contact_number_label = tk.Label(root, text="Contact Number:")
contact_number_label.grid(row=4, column=0, sticky=tk.W)
contact_number_entry = tk.Entry(root)
contact_number_entry.grid(row=4, column=1)

email_address_label = tk.Label(root, text="Email Address:")
email_address_label.grid(row=5, column=0, sticky=tk.W)
email_address_entry = tk.Entry(root)
email_address_entry.grid(row=5, column=1)

address_label = tk.Label(root, text="Address:")
address_label.grid(row=6, column=0, sticky=tk.W)
address_entry = tk.Entry(root)
address_entry.grid(row=6, column=1)

# Create the submit button
submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.grid(row=7, column=1)

# Start the main event loop
root.mainloop()
