from tkinter import ttk 
from tkinter.messagebox import showerror, showinfo, showwarning
import tkinter as tk

class AuthenticationModelUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Authentication Model")
        self.geometry("550x350")
        self.resizable(False, False)

        self.registered_users = {}

        #-----------------------------------------------------------------
        self.__build()
        self.__bind_events()
        self.mainloop()

    def __build(self):
        Frame = ttk.Frame
        Label = ttk.Label
        StringVar = tk.StringVar
        Button = ttk.Button
        Entry = ttk.Entry
        Notebook = ttk.Notebook

        label_grid_configurations = {
            "ipadx" : 10, "ipady" : 7.5, "padx" : 1.5, "sticky" : "ne",
        }
        entry_grid_configurations = {
           "ipadx" : 105, "ipady" : 7.5, "padx" : 1.5, "sticky" : "ne"
        }

        fonts = ("Helvetica", 14)
        
        self.fname = StringVar()
        self.lname = StringVar() 
        self.email = StringVar()
        self.username = StringVar()
        self.password = StringVar()

        self.username_log_in = StringVar()
        self.password_log_in = StringVar()


        #============================================================================
        #                        PARENT NOTEBOOK CONFIG
        #============================================================================
        self.notebook = Notebook(
            self, padding=(5, 5)
        )
        self.notebook.pack(
            fill="both", expand=True
        )

        #=============================================================================
        #                               REGISTER TAB
        #=============================================================================
        register_frame = Frame(
            self.notebook
        )
        register_frame.place(
            relwidth=1, relheight=1
        )

        register_frame.columnconfigure(index=0, weight=1)
        register_frame.columnconfigure(index=1, weight=1)
        register_frame.columnconfigure(index=2, weight=1)

        #----------------------------------------------------------------------------
        #                       REGISTER TAB COMPONENTS
        #----------------------------------------------------------------------------
        # FIRST NAME SECTION 
        fname_label = Label(
            register_frame, text="First name:", font=fonts, cursor="dot"
        )
        fname_label.grid(
            column=0, row=0, pady=1.5, **label_grid_configurations
        )
        fname_entry = Entry(
            register_frame, font=fonts, textvariable=self.fname
        ) 
        fname_entry.grid(
            column=1, row=0, columnspan=2, pady=1.5, **entry_grid_configurations
        )
        # LAST NAME SECTION
        lname_label = Label(
            register_frame, text="Last name:", font=fonts
        )
        lname_label.grid(
            column=0, row=1, pady=1.5, **label_grid_configurations
        )
        lname_entry = Entry(
            register_frame, font=fonts, textvariable=self.lname
        )
        lname_entry.grid(
            column=1, row=1, columnspan=2, **entry_grid_configurations
        )
        # EMAIL SECTION
        email_label = Label(
            register_frame, text="Email:", font=fonts
        )
        email_label.grid(
            column=0, row=2, pady=1.5, **label_grid_configurations
        )
        email_entry = Entry(
            register_frame, font=fonts, textvariable=self.email
        )
        email_entry.grid(
            column=1, row=2, columnspan=2, **entry_grid_configurations
        )
        # USER NAME SECTION
        username_label = Label(
            register_frame, text="Username:", font=fonts
        )
        username_label.grid(
            column=0, row=3, **label_grid_configurations
        )
        username_entry = Entry(
            register_frame, font=fonts, textvariable=self.username
        )
        username_entry.grid(
            column=1, row=3, columnspan=2, **entry_grid_configurations
        )
        # PASSWORD SECTION
        password_label = Label(
            register_frame, text="Password:", font=fonts
        )
        password_label.grid(
            column=0, row=4, pady=1.5, **label_grid_configurations
        )
        password_entry = Entry(
            register_frame, font=fonts, textvariable=self.password, show="*"
        )
        password_entry.grid(
            column=1, row=4, columnspan=2, **entry_grid_configurations
        )
        # SUBMIT BUTTON Section
        submit_button = Button(
            register_frame, text="register", command=lambda: self.__register()
        )
        submit_button.grid(
            column=2, row=5, sticky="ne", ipadx=15, ipady=10
        )

        #============================================================================
        #                            LOGIN TAB
        #============================================================================
        login_frame = Frame(
            self.notebook, 
        )
        login_frame.place(
            relwidth=1, relheight=1
        )

        login_frame.columnconfigure(index=0, weight=1)
        login_frame.columnconfigure(index=1, weight=1)
        login_frame.columnconfigure(index=2, weight=1)

        # USERNAME SECTION 
        username_login_label = Label(
            login_frame, text="Enter username:", font=fonts, cursor="dot"
        )
        username_login_label.grid(
            column=0, row=0, pady=1.5, **label_grid_configurations
        )

        username_login_entry = Entry(
            login_frame, font=fonts, textvariable=self.username_log_in
        ) 
        username_login_entry.grid(
            column=1, row=0, columnspan=2, pady=1.5, **entry_grid_configurations
        )
        # PASSWORD SECTION
        password_login_label = Label(
            login_frame, text="Enter password:", font=fonts
        )
        password_login_label.grid(
            column=0, row=1, pady=1.5, **label_grid_configurations
        )

        password_login_entry = Entry(
            login_frame, font=fonts, textvariable=self.password_log_in, show="*"
        )
        password_login_entry.grid(
            column=1, row=1, columnspan=2, **entry_grid_configurations
        )
        # SUBMIT BUTTON Section
        submit_button = Button(
            login_frame, text="login", command=lambda: self.__login()
        )
        submit_button.grid(
            column=2, row=2, sticky="ne", ipadx=15, ipady=10
        )

        #============================================================================
        #                   ADDING TABS TO NOTEBOOK
        #============================================================================

        self.notebook.add(
            register_frame, text="Register"
        )
        self.notebook.add(
            login_frame, text="login"
        )

    def __bind_events(self):
        self.bind(
            "<Control-w>", lambda event=None: self.destroy(), add="+"
        )
        self.bind(
            "<Control-W>", lambda event=None: self.destroy(), add="+"
        )

    def __register(self):

        fname = self.fname.get()
        lname = self.lname.get()
        email = self.email.get()
        username = self.username.get()
        password = self.password.get()

        register_details = [
            fname, lname, email, username, password
        ]
        if (not all(register_details)):
            showerror(
                title = "register",
                message ="Please fill in all input fields"
            )
        else:
            if (username not in self.registered_users.keys()):
                self.registered_users[username] = {
                    "fname" : fname,
                    "lname" : lname,
                    "email" : email,
                    "password" : password
                }
                showinfo(
                    title="register", 
                    message=f"Registration complete, welcome {username}"
                )
            else:
                showerror(
                    title="register",
                    message=f"An account already exists for username {username}, please choose a new username"
                )

    def __login(self):
        username = self.username_log_in.get()
        password = self.password_log_in.get()

        if (username and password):

            if ( not (username in self.registered_users.keys())):
                showwarning(
                    title="login",
                    message=f"{username} is not registered, please navigate to the register tab to register an account"
                )
            else:
                user_details = self.registered_users[username]
                if (password == user_details["password"]):
                    fname = user_details["fname"]
                    lname = user_details["lname"]
                    showinfo(
                        title="welcome",
                        message=f"Welcome {fname} {lname}"
                    )
                else:
                    showerror(
                        title="incorrect password",
                        message="incorrect password input"
                    )
        
        else:
            showerror(
                title="login",
                message="Please fill in all input fields"
            )



if __name__ == "__main__":
    AuthenticationModelUI()