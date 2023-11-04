import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Registration Form")

# Create labels and entry boxes for each field
name_label = tk.Label(root, text="Name:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

course_label = tk.Label(root, text="Course:")
course_label.pack()
course_entry = tk.Entry(root)
course_entry.pack()

semester_label = tk.Label(root, text="Semester:")
semester_label.pack()
semester_entry = tk.Entry(root)
semester_entry.pack()

form_number_label = tk.Label(root, text="Form Number:")
form_number_label.pack()
form_number_entry = tk.Entry(root)
form_number_entry.pack()

contact_number_label = tk.Label(root, text="Contact Number:")
contact_number_label.pack()
contact_number_entry = tk.Entry(root)
contact_number_entry.pack()

email_label = tk.Label(root, text="Email:")
email_label.pack()
email_entry = tk.Entry(root)
email_entry.pack()

address_label = tk.Label(root, text="Address:")
address_label.pack()
address_entry = tk.Entry(root)
address_entry.pack()

# Define a function to handle the submission of the form
def submit_form():
    name = name_entry.get()
    course = course_entry.get()
    semester = semester_entry.get()
    form_number = form_number_entry.get()
    contact_number = contact_number_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    # Print the data for verification purposes
    print(f"Name: {name}")
    print(f"Course: {course}")
    print(f"Semester: {semester}")
    print(f"Form Number: {form_number}")
    print(f"Contact Number: {contact_number}")
    print(f"Email: {email}")
    print(f"Address: {address}")

# Create the submit button
submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.pack()

# Run the main loop
root.mainloop()
