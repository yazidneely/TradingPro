import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Simple Tkinter GUI")
xclick=0

def on_button_click():
    """Function to be called when the button is clicked."""
    global xclick
    xclick=xclick+1
    print(f"Button was clicked ! {xclick} times")



# Add a label
label = tk.Label(root, text="Welcome to your Python GUI!")
label.pack(pady=10) # Add some padding

# Add a button
button = tk.Button(root, text="Press Me", command=on_button_click)
button.pack(pady=5)

root.update()

# Start the Tkinter event loop
root.mainloop()
