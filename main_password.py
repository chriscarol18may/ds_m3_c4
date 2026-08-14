import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    """Generates a random password based on the user's selected criteria."""
    length = length_var.get()
    
    # Build the pool of characters to choose from
    characters = ""
    if upper_var.get():
        characters += string.ascii_uppercase
    if lower_var.get():
        characters += string.ascii_lowercase
    if num_var.get():
        characters += string.digits
    if sym_var.get():
        characters += string.punctuation
        
    # Ensure at least one character type is selected
    if not characters:
        messagebox.showwarning("Warning", "Please select at least one character type.")
        return
        
    # Generate the password
    password = "".join(random.choice(characters) for _ in range(length))
    password_var.set(password)

def copy_to_clipboard():
    """Copies the generated password to the system clipboard."""
    generated_password = password_var.get()
    if generated_password:
        root.clipboard_clear()
        root.clipboard_append(generated_password)
        messagebox.showinfo("Success", "Password copied to clipboard!")
    else:
        messagebox.showwarning("Warning", "No password to copy.")

# --- GUI Setup using Tkinter ---
root = tk.Tk()
root.title("Random Password Generator")
root.geometry("400x420")
root.resizable(False, False)

# Variables to store user inputs
length_var = tk.IntVar(value=12)
upper_var = tk.BooleanVar(value=True)
lower_var = tk.BooleanVar(value=True)
num_var = tk.BooleanVar(value=True)
sym_var = tk.BooleanVar(value=True)
password_var = tk.StringVar()

# Title
tk.Label(root, text="Password Generator", font=("Helvetica", 16, "bold")).pack(pady=15)

# Length Selector
length_frame = tk.Frame(root)
length_frame.pack(pady=5)
tk.Label(length_frame, text="Password Length: ", font=("Helvetica", 11)).pack(side=tk.LEFT)
tk.Spinbox(length_frame, from_=4, to=100, textvariable=length_var, font=("Helvetica", 11), width=5).pack(side=tk.LEFT)

# Checkboxes for Character Types
options_frame = tk.Frame(root)
options_frame.pack(pady=10)
tk.Checkbutton(options_frame, text="Include Uppercase Letters (A-Z)", variable=upper_var, font=("Helvetica", 10)).pack(anchor="w")
tk.Checkbutton(options_frame, text="Include Lowercase Letters (a-z)", variable=lower_var, font=("Helvetica", 10)).pack(anchor="w")
tk.Checkbutton(options_frame, text="Include Numbers (0-9)", variable=num_var, font=("Helvetica", 10)).pack(anchor="w")
tk.Checkbutton(options_frame, text="Include Symbols (!@#$)", variable=sym_var, font=("Helvetica", 10)).pack(anchor="w")

# Generate Button
tk.Button(root, text="Generate Password", command=generate_password, font=("Helvetica", 12, "bold"), bg="#4CAF50", fg="white", width=20).pack(pady=15)

# Display the Generated Password
password_entry = tk.Entry(root, textvariable=password_var, font=("Helvetica", 14), justify="center", state="readonly")
password_entry.pack(fill="x", padx=40, pady=5)

# Copy to Clipboard Button
tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard, font=("Helvetica", 10), width=20).pack(pady=10)

# Start the application
root.mainloop()