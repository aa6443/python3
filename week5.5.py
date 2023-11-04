import tkinter as tk

# Create a new Tkinter window
window = tk.Tk()

# Set the size of the window
window.geometry("500x500")

# Create two frames to hold the input boxes
frame1 = tk.Frame(window)
frame1.pack(pady=10)
frame2 = tk.Frame(window)
frame2.pack(pady=10)

# Add labels and entry widgets to frame1 for first and last name
tk.Label(frame1, text="First Name: ").grid(row=0, column=0)
first_name = tk.Entry(frame1, width=30)
first_name.grid(row=0, column=1)
tk.Label(frame1, text="Last Name: ").grid(row=1, column=0)
last_name = tk.Entry(frame1, width=30)
last_name.grid(row=1, column=1)

# Add labels and entry widgets to frame2 for street, city, and zip code
tk.Label(frame2, text="Street: ").grid(row=0, column=0)
street = tk.Entry(frame2, width=30)
street.grid(row=0, column=1)
tk.Label(frame2, text="City: ").grid(row=1, column=0)
city = tk.Entry(frame2, width=30)
city.grid(row=1, column=1)
tk.Label(frame2, text="Zip Code: ").grid(row=2, column=0)
zip_code = tk.Entry(frame2, width=30)
zip_code.grid(row=2, column=1)

# Define a function to be called when the submit button is pressed
def submit():
    # Get the values entered by the user
    first = first_name.get()
    last = last_name.get()
    st = street.get()
    ct = city.get()
    zc = zip_code.get()
    
    # Print the values to the console
    print("First Name: " + first)
    print("Last Name: " + last)
    print("Street: " + st)
    print("City: " + ct)
    print("Zip Code: " + zc)

# Add a submit button to the GUI
submit_button = tk.Button(window, text="Submit", command=submit)
submit_button.pack(pady=10)

# Run the Tkinter event loop
window.mainloop()
