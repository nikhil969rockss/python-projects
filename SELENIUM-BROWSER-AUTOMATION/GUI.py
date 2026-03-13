# This file is for GUI for the website https://demoqa.com which has a login,
# username and password, and a form filling task,

import tkinter as tk
from tkinter import messagebox
from threading import Thread
from main import WebAutomation


class App:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Web Automation Tool")
        self.root.geometry("500x500")
        self.root.resizable(False, False)

        self.automate = WebAutomation(URL='https://demoqa.com')

        # Title
        tk.Label(root, text="Automation Panel",
                 font=("Helvetica", 20, "bold")).pack(pady=15)

        # Login Frame
        login_frame = tk.LabelFrame(root, text="Login Details", padx=10, pady=10)
        login_frame.pack(fill="x", padx=20, pady=10)

        tk.Label(login_frame, text="Username").grid(row=0, column=0, sticky="w")
        self.username_input = tk.Entry(login_frame, width=30)
        self.username_input.grid(row=0, column=1, pady=5)

        tk.Label(login_frame, text="Password").grid(row=1, column=0, sticky="w")
        self.password_input = tk.Entry(login_frame, show="*", width=30)
        self.password_input.grid(row=1, column=1, pady=5)

        # Form Frame
        form_frame = tk.LabelFrame(root, text="Form Details", padx=10, pady=10)
        form_frame.pack(fill="x", padx=20, pady=10)

        self.full_name_input = self.create_field(form_frame, "Full Name", 0)
        self.email_input = self.create_field(form_frame, "Email", 1)
        self.current_adrs = self.create_field(form_frame, "Current Address", 2)
        self.permanent_adrs = self.create_field(form_frame, "Permanent Address", 3)

        # Buttons
        button_frame = tk.Frame(root)
        button_frame.pack(pady=15)

        self.submit_btn = tk.Button(button_frame, text="Start Automation",
                                    width=18,
                                    command=self.start_thread)
        self.submit_btn.grid(row=0, column=0, padx=5)

        tk.Button(button_frame, text="Clear",
                  width=10, command=self.clear_form).grid(row=0, column=1, padx=5)

        tk.Button(button_frame, text="Close Browser",
                  width=12, command=self.close_browser).grid(row=0, column=2, padx=5)

        # Status Label
        self.status_label = tk.Label(root, text="Status: Idle",
                                     fg="blue", font=("Helvetica", 10))
        self.status_label.pack(pady=10)

    def create_field(self, parent, label_text, row):
        tk.Label(parent, text=label_text).grid(row=row, column=0, sticky="w")
        entry = tk.Entry(parent, width=30)
        entry.grid(row=row, column=1, pady=5)
        return entry

    #  Thread Starter
    def start_thread(self):
        thread = Thread(target=self.run_automation)
        thread.daemon = True
        thread.start()

    #  Actual Automation Logic
    def run_automation(self):
        self.submit_btn.config(state="disabled")
        self.status_label.config(text="Status: Running...", fg="orange")

        username = self.username_input.get()
        password = self.password_input.get()
        fullname = self.full_name_input.get()
        email = self.email_input.get()
        current = self.current_adrs.get()
        permanent = self.permanent_adrs.get()
        

        if not all([username, password, fullname, email, current, permanent]):
            messagebox.showerror("Error", "All fields are required")
            self.submit_btn.config(state="normal")
            self.status_label.config(text="Status: Idle", fg="blue")
            return

        try:
            self.automate.load_page()
            self.automate.login_form(username, password)
            self.automate.fill_form(fullname, email, current, permanent)

            self.status_label.config(text="Status: Completed ✅", fg="green")

        except Exception as e:
            messagebox.showerror("Error", str(e))
            self.status_label.config(text="Status: Failed ❌", fg="red")

        self.submit_btn.config(state="normal")

    def clear_form(self):
        for field in [self.username_input, self.password_input,
                      self.full_name_input, self.email_input,
                      self.current_adrs, self.permanent_adrs]:
            field.delete(0, tk.END)

        self.status_label.config(text="Status: Cleared", fg="blue")

    def close_browser(self):
        self.automate.exit()
        self.status_label.config(text="Status: Browser Closed", fg="black")


root = tk.Tk()
app = App(root)
root.mainloop()