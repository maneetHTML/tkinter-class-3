
import tkinter as tk
from tkinter import messagebox

def convert_inches_to_cm():
    try:
        inches = float(entry_inches.get())
        cm = inches * 2.54
        label_result.config(text=f"{cm:.2f} cm")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid number.")

# Create the main window
root = tk.Tk()
root.title("Inches to Centimeters Converter")

# Create and place the widgets
label_prompt = tk.Label(root, text="Enter inches:")
label_prompt.pack(pady=5)

entry_inches = tk.Entry(root)
entry_inches.pack(pady=5)

button_convert = tk.Button(root, text="Convert", command=convert_inches_to_cm)
button_convert.pack(pady=5)

label_result = tk.Label(root, text="Result will be shown here")
label_result.pack(pady=5)

# Run the application
root.mainloop()
