import tkinter as tk

class User:
    def _init_(self, email, password):
        self.email = email
        self.password = password

    def authenticate(self, email, password):
        return self.email == email and self.password == password

class LoginFrame(tk.Frame):
    def _init_(self, master=None):
        super()._init_(master)
        self.master = master
        self.master.title("Login")

        self.email_label = tk.Label(self, text="Email:")
        self.email_label.pack(side=tk.LEFT)

        self.email_entry = tk.Entry(self)
        self.email_entry.pack(side=tk.LEFT)

        self.password_label = tk.Label(self, text="Password:")
        self.password_label.pack(side=tk.LEFT)

        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack(side=tk.LEFT)

        self.submit_button = tk.Button(self, text="Submit", command=self.submit)
        self.submit_button.pack(side=tk.LEFT)

        self.pack()

    def submit(self):
        email = self.email_entry.get()
        password = self.password_entry.get()

        if email == "" or password == "":
            tk.messagebox.showerror("Error", "Email and password cannot be empty.")
            return

        user = User(email, password)

        if user.authenticate(email, password):
            tk.messagebox.showinfo("Success", "Welcome!")
        else:
            tk.messagebox.showerror("Error", "Incorrect email or password.")

root = tk.Tk()
login_frame = LoginFrame(root)
login_frame.mainloop()