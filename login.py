from tkinter import *
from tkinter import messagebox, ttk
from PIL import ImageTk, Image

def login():
    if usernameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror('Error','Fields cannot be empty')
    elif usernameEntry.get()=='Hammad' and passwordEntry.get()=='2233':
        messagebox.showinfo('Success','Welcome')
        root.destroy()
        
    else:
        messagebox.showerror('Error','Please enter correct credentials')



root = Tk()
root.iconbitmap("pics/icon.ico")
root.config(bg='#fff')
root.title("LIST")
root.geometry("620x500")
root.resizable(0,0)

style = ttk.Style()
style.configure("Custom.TEntry", padding=5, foreground="black", background="lightgray")
style.configure("Custom.TButton", padding=10, relief="flat", background="#91e0b5", foreground="green", font=("Helvetica", 12))
style.configure("Custom.TLabel", foreground="#91e0b5", font=("Helvetica", 20))
font_s = ("Helvetica", 18)

logo = ImageTk.PhotoImage(Image.open("pics/logo.jpg"))
logoLabel = ttk.Button(root,image=logo)
logoLabel.grid(row=0, column=0 ,padx=30,pady=60,columnspan=10)

usernameImage=PhotoImage(file='pics/user.png')
usernameLabel=ttk.Label(root,image=usernameImage,text='Username',compound=LEFT, style="Custom.TLabel" )
usernameLabel.grid(row=1,column=0,pady=10,padx=20, sticky="nsew")

usernameEntry=ttk.Entry(root, style="Custom.TEntry", font=font_s)
usernameEntry.grid(row=1,column=1,pady=10,padx=20,ipadx=20,ipady=7,sticky="nsew")

passwordImage=PhotoImage(file='pics/password.png')
passwordLabel=ttk.Label(root,image=passwordImage,text='Password',compound=LEFT, style="Custom.TLabel")
passwordLabel.grid(row=2,column=0,pady=10,padx=20,sticky="nsew")

passwordEntry=ttk.Entry(root, style="Custom.TEntry", font=font_s)
passwordEntry.grid(row=2,column=1,pady=10,padx=20, ipadx=20,ipady=7,sticky="nsew")

loginButton=ttk.Button(root,text='Login',width=15
                   ,cursor='hand2',command=login, style="Custom.TButton")
loginButton.grid(row=3,column=1,pady=10,sticky="nsew", columnspan=3)



root.mainloop()