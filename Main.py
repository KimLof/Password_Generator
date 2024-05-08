import tkinter as tk
from tkinter import ttk
import string
import secrets

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("400x350")

        # Variables
        self.password_var = tk.StringVar()
        self.length_var = tk.IntVar(value=12)
        self.use_upper_var = tk.BooleanVar(value=True)
        self.use_lower_var = tk.BooleanVar(value=True)
        self.use_digits_var = tk.BooleanVar(value=True)
        self.use_special_var = tk.BooleanVar(value=True)
        self.special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?`~"

        # GUI Elements
        style = ttk.Style()
        style.configure('TLabel', font=('Arial', 12))
        style.configure('TButton', font=('Arial', 12))
        style.configure('TCheckbutton', font=('Arial', 12))

        length_label = ttk.Label(root, text="Password Length:")
        length_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.length_entry = ttk.Entry(root, textvariable=self.length_var, width=5)
        self.length_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        use_upper_check = ttk.Checkbutton(root, text="Uppercase Letters", variable=self.use_upper_var)
        use_upper_check.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        use_lower_check = ttk.Checkbutton(root, text="Lowercase Letters", variable=self.use_lower_var)
        use_lower_check.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        use_digits_check = ttk.Checkbutton(root, text="Digits", variable=self.use_digits_var)
        use_digits_check.grid(row=3, column=0, padx=10, pady=10, sticky="w")

        self.special_check = ttk.Checkbutton(root, text="Special Characters", variable=self.use_special_var)
        self.special_check.grid(row=4, column=0, padx=10, pady=10, sticky="w")

        self.min_length_label = ttk.Label(root, text="", font=('Arial', 10))
        self.min_length_label.grid(row=5, column=0, columnspan=2, padx=10, pady=5, sticky="w")

        generate_button = ttk.Button(root, text="Generate Password", command=self.generate_password)
        generate_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

        self.password_label = ttk.Label(root, textvariable=self.password_var, wraplength=380, font=('Arial', 14))
        self.password_label.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

        self.update_min_length_label()

    def update_min_length_label(self):
        min_length = self.calculate_min_length()
        self.min_length_label.config(text=f"Minimum password length: {min_length}")

    def calculate_min_length(self):
        min_length = 0
        if self.use_upper_var.get():
            min_length += 1
        if self.use_lower_var.get():
            min_length += 1
        if self.use_digits_var.get():
            min_length += 1
        if self.use_special_var.get():
            min_length += 1
        return max(4 if min_length == 4 else 3, min_length)

    def generate_password(self):
        min_length = self.calculate_min_length()
        length = self.length_var.get()
        if length < min_length:
            self.password_var.set(f"Minimum password length is {min_length}")
            return

        use_upper = self.use_upper_var.get()
        use_lower = self.use_lower_var.get()
        use_digits = self.use_digits_var.get()
        use_special = self.use_special_var.get()

        chars = ""
        if use_upper:
            chars += string.ascii_uppercase
        if use_lower:
            chars += string.ascii_lowercase
        if use_digits:
            chars += string.digits
        if use_special:
            chars += self.special_chars

        if not chars:
            self.password_var.set("Please select at least one character type.")
            return

        password = ''.join(secrets.choice(chars) for _ in range(length))
        self.password_var.set(password)

        # Check that password meets all requirements. IF dont  then generate new password
        if use_upper and not any(c.isupper() for c in password):
            self.generate_password()
        elif use_lower and not any(c.islower() for c in password):
            self.generate_password()
        elif use_digits and not any(c.isdigit() for c in password):
            self.generate_password()
        elif use_special and not any(c in self.special_chars for c in password):
            self.generate_password()
        
        


def main():
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
