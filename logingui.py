import tkinter as tk
from tkinter import *
from tkinter import messagebox
from sql_program import save_sql #I am not using import * because i keep getting an error when doing so.
from sql_program import get_sql
from sql_program import first

# Create global variables to store user information
user_info = {'name': '', 'last_name': '', 'username': '', 'password': ''}


def window():
  global root  #create tkinter window with labels and buttons
  root = Tk()
  root.geometry("600x400")
  root.title("Window")
  label2 = Label(root, text="Login or create an account.")
  label2.pack()
  add_button = Button(root, text='Create an Account', command=create)
  add_button.pack()
  login_button = Button(root, text='Login', command=login)
  login_button.pack()
  button = Button(root, text='Save and Exit', command=root.destroy)
  button.pack()
  root.mainloop()


def create():
  global root  #make the create account window with labels and entry fields
  root = Tk()
  root.geometry("600x400")
  root.title("Create an Account")

  name = Label(root, text="Name: ")
  name.pack()
  name_entry = Entry(root)
  name_entry.pack()

  last = Label(root, text="Last Name: ")
  last.pack()
  last_entry = Entry(root)
  last_entry.pack()

  user = Label(root, text="User: ")
  user.pack()
  user_entry = Entry(root)
  user_entry.pack()

  passw = Label(root, text="Password: ")
  passw.pack()
  passw_entry = Entry(root, show='*')
  passw_entry.pack()

  def save_info():
    # Save user information to global variables, then run save_sql(), which has access to the dictionary.
    user_info['name'] = name_entry.get()
    user_info['last_name'] = last_entry.get()
    user_info['username'] = user_entry.get()
    user_info['password'] = passw_entry.get()
    save_sql()  #run save_sql
    root.destroy()  #close window

  save_button = Button(root, text='Save and Exit', command=save_info)
  save_button.pack()

  root.mainloop()


def login():  #make login window with entry fields and buttons
  global root
  root = Tk()
  root.geometry("600x400")
  root.title("Log In")

  user = Label(root, text="User: ")
  user.pack()
  user_entry = Entry(root)
  user_entry.pack()

  passw = Label(root, text="Password: ")
  passw.pack()
  passw_entry = Entry(root, show='*')
  passw_entry.pack()

  def check_login():  #check if the user name and passwords work.
    username = user_entry.get()
    password = passw_entry.get()
    key = get_sql(username, password)
    if key != []:
      pass
    else:
      messagebox.showerror('Error', "Incorrect Username or Password.")
      root.destroy()
    
    name = first(username,password)
    
     #key will be the key which corresponds to the user and password in db, and the user and password entered in the login.

    if key != []:  #if the key does exist, open menu
      root.destroy()
      loggedin(username, password, key, name)

    else:  #else preswnt error and destory window
      messagebox.showerror('Error', "Incorrect Username or Password.")
      root.destroy()

  login_button = Button(root, text='Log In', command=check_login)
  login_button.pack()


def loggedin(username, password,
             key,name):  #currently do not need password, but maybe in future

  def forward():
    log_message("Move Forward")

  def backward():
    log_message("Move Backward")

  def left():
    log_message("Turn Left")

  def right():
    log_message("Turn Right")

  def stop():
    log_message("Stop")

  def logout():
    log_message("Logged Out")
    root.destroy()
    window()

  def log_message(message):
    current_text = log_label.cget(
        "text"
    )  #cget just gets the current values of the widget, similar to +=1
    new_text = f"{message}\n{current_text}"
    log_label.config(text=new_text)

  # Create the main window
  root = tk.Tk()
  root.geometry("800x600")
  root.title("Logged In")

  # Create frames for each part of the grid
  top_left_frame = tk.Frame(root, bg="white", width=400, height=300)
  top_right_frame = tk.Frame(root, bg="black", width=400, height=300)
  bottom_left_frame = tk.Frame(root,
                               relief=tk.SUNKEN,
                               borderwidth=2,
                               width=400,
                               height=300)  #just makes empty frame look nice
  bottom_right_frame = tk.Frame(root, width=400, height=300)

  top_left_frame.grid(row=0, column=0, sticky="nsew")
  top_right_frame.grid(row=0, column=1, sticky="nsew")
  bottom_left_frame.grid(
      row=1, column=0,
      sticky="nsew")  #nsew just fills in all extra space within each frame
  bottom_right_frame.grid(row=1, column=1, sticky="nsew")

  # Place labels and buttons in the frames
  camera_label = tk.Label(top_left_frame, text="CAMERA")
  camera_label.pack()

  log_label = tk.Label(top_right_frame,
                       text=f"Welcome {name}",
                       fg="white",
                       bg="black",
                       anchor="nw")
  log_label.pack(fill="both", expand=True)

  button_frame = tk.Frame(top_right_frame, bg="black")
  button_frame.pack(side="bottom", fill="both", expand=True)

  forward_button = tk.Button(bottom_right_frame,
                             text="   ^   \nForward",
                             command=forward)
  backward_button = tk.Button(bottom_right_frame,
                              text="Backward\n   v   ",
                              command=backward)
  left_button = tk.Button(bottom_right_frame, text="<   Left", command=left)
  right_button = tk.Button(
      bottom_right_frame, text="Right   >",
      command=right)  #place move buttons, and call their functions
  stop_button = tk.Button(bottom_right_frame, text="   Stop   ", command=stop)
  logout_button = tk.Button(bottom_right_frame,
                            text="   Logout   ",
                            command=logout)

  forward_button.grid(row=0, column=1)
  backward_button.grid(row=2, column=1)
  left_button.grid(row=1, column=0)
  right_button.grid(row=1, column=2)
  stop_button.grid(row=1, column=1)
  logout_button.grid(row=2, column=2)

  root.grid_rowconfigure(0, weight=1)
  root.grid_rowconfigure(
      1, weight=1
  )  #this code makes it so everything has the same weight (power) so everything gets the same amount of space.
  root.grid_columnconfigure(0, weight=1)
  root.grid_columnconfigure(1, weight=1)

  # Make the log area fill the available space
  top_right_frame.pack_propagate(
      False
  )  #i googled this because the log frame was smaller than the camera frame?
  log_label.pack(fill="both", expand=True)

  root.mainloop()


def save():  #exit the windows and exit code
  global root
  root = Tk()
  root.geometry("600x400")
  root.title("Save and Exit")
  label3 = Label(root, text="")
  label3.pack()
  button = Button(root, text='Save and Exit', command=exit())
  button.pack()
  exit()
