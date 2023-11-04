import tkinter as tk

# create main window
root = tk.Tk()
root.title("Doctor Appointment")

# function to switch to login screen
def switch_to_login():
    # clear all widgets from main window
    for widget in root.winfo_children():
        widget.destroy()

    # create login screen
    login_label = tk.Label(root, text="Login")
    login_label.pack()

    # TODO: add login fields and button


# create signup screen
signup_label = tk.Label(root, text="Sign Up")
signup_label.pack()

# create personal information fields
first_name_label = tk.Label(root, text="First Name")
first_name_label.pack()
first_name_entry = tk.Entry(root)
first_name_entry.pack()

last_name_label = tk.Label(root, text="Last Name")
last_name_label.pack()
last_name_entry = tk.Entry(root)
last_name_entry.pack()

age_label = tk.Label(root, text="Age")
age_label.pack()
age_entry = tk.Entry(root)
age_entry.pack()

gender_label = tk.Label(root, text="Gender")
gender_label.pack()
gender_var = tk.StringVar(value="Male") # default value
gender_male_radio = tk.Radiobutton(root, text="Male", variable=gender_var, value="Male")
gender_male_radio.pack()
gender_female_radio = tk.Radiobutton(root, text="Female", variable=gender_var, value="Female")
gender_female_radio.pack()

# create address fields
city_label = tk.Label(root, text="City")
city_label.pack()
city_entry = tk.Entry(root)
city_entry.pack()

address_label = tk.Label(root, text="Address")
address_label.pack()
address_entry = tk.Entry(root)
address_entry.pack()

# create account credentials fields
username_label = tk.Label(root, text="Username")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

password_label = tk.Label(root, text="Password")
password_label.pack()
password_entry = tk.Entry(root, show="*") # mask password
password_entry.pack()

verify_password_label = tk.Label(root, text="Verify Password")
verify_password_label.pack()
verify_password_entry = tk.Entry(root, show="*") # mask password
verify_password_entry.pack()

# create signup and clear buttons
signup_button = tk.Button(root, text="Sign Up")
signup_button.pack()
clear_button = tk.Button(root, text="Clear")
clear_button.pack()

# create switch to login button in top right corner
