import random
import string
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pyperclip  # Import the pyperclip library

# Function to generate the password
def generate_password(minlen, maxlen, minuchars, minlchars, minnumbers, minschars):
    # Define character sets
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special_characters = string.punctuation

    # Ensure minimum characters from each category
    password = [
        random.choice(uppercase) for _ in range(minuchars)
    ] + [
        random.choice(lowercase) for _ in range(minlchars)
    ] + [
        random.choice(digits) for _ in range(minnumbers)
    ] + [
        random.choice(special_characters) for _ in range(minschars)
    ]

    # Fill the rest of the password length with random characters from all sets
    remaining_length = random.randint(minlen, maxlen) - len(password)
    all_characters = uppercase + lowercase + digits + special_characters
    password += [random.choice(all_characters) for _ in range(remaining_length)]
    
    # Shuffle the password list to avoid a predictable pattern
    random.shuffle(password)
    
    # Convert list to string
    return ''.join(password)

# Function to handle password generation
def handle_generate():
    try:
        # Get the values entered by the user
        minlen = int(entry_minlen.get())
        maxlen = int(entry_maxlen.get())
        minuchars = int(entry_minuchars.get())
        minlchars = int(entry_minlchars.get())
        minnumbers = int(entry_minnumbers.get())
        minschars = int(entry_minschars.get())

        if minlen < 6 or maxlen < minlen:
            messagebox.showerror("Input Error", "Ensure minimum length is 6 and max is greater than min.")
            return

        password = generate_password(minlen, maxlen, minuchars, minlchars, minnumbers, minschars)
        password_label.config(text=password)
        password_frame.pack(pady=10)  # Show the password frame

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid integers for all fields.")

# Function to copy the generated password to the clipboard
def copy_to_clipboard():
    pyperclip.copy(password_label.cget("text"))
    messagebox.showinfo("Clipboard", "Password copied to clipboard!")

# Function to exit the application
def exit_app():
    root.quit()

# Create the GUI
root = tk.Tk()
root.title("Random Password Generator")
root.geometry("400x300")  # Set window size

# Create a main frame for inputs
main_frame = tk.Frame(root, padx=10, pady=10)
main_frame.pack(fill=tk.BOTH, expand=True)

# Create a frame for password input fields
input_frame = ttk.LabelFrame(main_frame, text="Password Parameters", padding=(10, 10))
input_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

# Labels and Entries for inputs inside the frame
ttk.Label(input_frame, text="Min Length:").grid(row=0, column=0, sticky="w", pady=5)
entry_minlen = ttk.Entry(input_frame)
entry_minlen.grid(row=0, column=1, pady=5)

ttk.Label(input_frame, text="Max Length:").grid(row=1, column=0, sticky="w", pady=5)
entry_maxlen = ttk.Entry(input_frame)
entry_maxlen.grid(row=1, column=1, pady=5)

ttk.Label(input_frame, text="Min Uppercase:").grid(row=2, column=0, sticky="w", pady=5)
entry_minuchars = ttk.Entry(input_frame)
entry_minuchars.grid(row=2, column=1, pady=5)

ttk.Label(input_frame, text="Min Lowercase:").grid(row=3, column=0, sticky="w", pady=5)
entry_minlchars = ttk.Entry(input_frame)
entry_minlchars.grid(row=3, column=1, pady=5)

ttk.Label(input_frame, text="Min Numbers:").grid(row=4, column=0, sticky="w", pady=5)
entry_minnumbers = ttk.Entry(input_frame)
entry_minnumbers.grid(row=4, column=1, pady=5)

ttk.Label(input_frame, text="Min Special Chars:").grid(row=5, column=0, sticky="w", pady=5)
entry_minschars = ttk.Entry(input_frame)
entry_minschars.grid(row=5, column=1, pady=5)

# Generate button
ttk.Button(main_frame, text="Generate Password", command=handle_generate).pack(pady=10)

# Create a frame for the password output
password_frame = tk.Frame(main_frame, padx=10, pady=10)
password_label = ttk.Label(password_frame, text="", background="light yellow", font=("Helvetica", 12))
password_label.pack(side=tk.LEFT, padx=10)

# Copy button
ttk.Button(password_frame, text="Copy to Clipboard", command=copy_to_clipboard).pack(side=tk.LEFT, padx=10)

# Exit button
ttk.Button(main_frame, text="Exit", command=exit_app).pack(pady=10)

# Hide the password frame initially
password_frame.pack_forget()

# Start the GUI loop
root.mainloop()
