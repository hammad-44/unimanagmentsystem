from tkinter import *
from tkinter import ttk, messagebox
from PIL import ImageTk, Image
import sqlite3
import login 

conn = sqlite3.connect("university.db")
cursor = conn.cursor()

root = Tk()
root.iconbitmap("pics/icon.ico")
root.config(bg='#fff')
root.title("LIST")
root.geometry("830x800")
root.resizable(0,0)


cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        roll_number INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        department TEXT,
        age INTEGER,
        email TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS courses (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        department TEXT,
        credits INTEGER
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS faculty (
        Employeeid INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        department TEXT,
        position TEXT,
        email TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS departments (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        head TEXT
       
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS enrollments (
        id INTEGER PRIMARY KEY,
        student_id INTEGER NOT NULL,
        course_id INTEGER NOT NULL,
        FOREIGN KEY (student_id) REFERENCES students(id),
        FOREIGN KEY (course_id) REFERENCES courses(id)
    )
''')

def add_student():
    def submit():
        name = name_entry.get()
        roll = roll_entry.get()
        department = department_entry.get()
        age = age_entry.get()
        email = email_entry.get()
        if name_entry.get()=='' or roll_entry.get()=='' or department_entry.get()=='' or age_entry.get()=='' or email_entry.get()=='':
            messagebox.showerror('Error','All Feilds are required',parent=addStudent)
        else:
            cursor.execute("INSERT INTO students (name, roll_number, department, age, email) VALUES (?, ?, ?, ?, ?)",
                      (name, roll, department, age, email))
            conn.commit()
            messagebox.showinfo("Message","Added Succesfully")
            addStudent.destroy()
    addStudent= Toplevel(root)
    addStudent.title("Add New Students")
    addStudent.geometry("400x400")
    addStudent.iconbitmap("pics/icon.ico")

    name_label = ttk.Label(addStudent, text="Name:", foreground="green",font=("Helvetica", 20))
    name_label.grid(row=0, column=0, padx=10, pady=10,ipadx=10)
    name_entry = ttk.Entry(addStudent,style="Custom.TEntry")
    name_entry.grid(row=0, column=1, padx=10, pady=10)

    roll_label = ttk.Label(addStudent, text="Roll Number:", foreground="green",font=("Helvetica", 20))
    roll_label.grid(row=1, column=0, padx=10, pady=10,ipadx=10)
    roll_entry = ttk.Entry(addStudent,style="Custom.TEntry")
    roll_entry.grid(row=1, column=1, padx=10, pady=10)

    department_label = ttk.Label(addStudent, text="Department:", foreground="green",font=("Helvetica", 20))
    department_label.grid(row=2, column=0, padx=10, pady=10,ipadx=10)
    department_entry = ttk.Entry(addStudent,style="Custom.TEntry")
    department_entry.grid(row=2, column=1, padx=10, pady=10)

    email_label = ttk.Label(addStudent, text="Email:", foreground="green",font=("Helvetica", 20))
    email_label.grid(row=3, column=0, padx=10, pady=10,ipadx=10)
    email_entry = ttk.Entry(addStudent, style="Custom.TEntry")
    email_entry.grid(row=3, column=1, padx=10, pady=10)

    age_label = ttk.Label(addStudent, text="Age:", foreground="green",font=("Helvetica", 20))
    age_label.grid(row=4, column=0, padx=10, pady=10,ipadx=10)
    age_entry = ttk.Entry(addStudent,style="Custom.TEntry")
    age_entry.grid(row=4, column=1, padx=10, pady=10)

    submit_button = ttk.Button(addStudent, text="Submit",style="Custom.TButton" ,command=submit)
    submit_button.grid(row=5, columnspan=2, pady=20)

def remove_student():
   
    def Delete():
        roll = roll_entry.get()
        cursor.execute("SELECT * FROM students WHERE roll_number = ?", (roll,))
        result = cursor.fetchone()
        if result:
            cursor.execute("DELETE FROM students WHERE roll_number = ?", (roll,))
            conn.commit()
            messagebox.showinfo("Message","Deleted Succesfully")
            removeStudent.destroy()
        else:
            messagebox.showerror("Message","Student Does Not Exist")
           
            
    removeStudent= Toplevel(root)
    removeStudent.title("Remove Student")
    removeStudent.geometry("500x250")
    removeStudent.iconbitmap("pics/icon.ico")

    roll_label = ttk.Label(removeStudent, text="Enter The Roll Number", foreground="green",font=("Helvetica", 20))
    roll_label.grid(row=0, column=0, padx=10, pady=10,ipadx=10)
    roll_entry = ttk.Entry(removeStudent,style="Custom.TEntry")
    roll_entry.grid(row=0, column=1, padx=10, pady=10)
    
    
    submit_button = ttk.Button(removeStudent, text="Delete",style="Custom.TButton" ,command=Delete)
    submit_button.grid(row=5, columnspan=2, pady=20)


def update_student():

    def Update():
        roll_number = roll_number_entry.get()
        cursor.execute("SELECT name,roll_number,department, email, age FROM students WHERE roll_number = ?", (roll_number,))
        result = cursor.fetchone()

        def UpdateForm():
            new_name = name_entry.get()
            new_roll = roll_entry.get()
            new_department = department_entry.get()
            new_age = age_entry.get()
            new_email = email_entry.get()

            cursor.execute("UPDATE students SET name = ?,roll_number=?, email = ?, age = ?, department=?, email=? WHERE roll_number = ?",
                   (new_name, new_roll,new_email, new_age,new_department,new_email,roll_number,))
            conn.commit()
            messagebox.showinfo("Message","Updated Succesfully")
            updateStudentForm.destroy()
            updateStudent.destroy()

        if result:
            updateStudentForm= Toplevel(root)
            updateStudentForm.title("Update Student")
            updateStudentForm.geometry("400x400")
            updateStudentForm.iconbitmap("pics/icon.ico")
            updateStudentForm.resizable(0,0)


            name_label = ttk.Label(updateStudentForm, text="Name:", foreground="green",font=("Helvetica", 20))
            name_label.grid(row=0, column=0, padx=10, pady=10,ipadx=10)
            name_entry = ttk.Entry(updateStudentForm,style="Custom.TEntry")
            name_entry.grid(row=0, column=1, padx=10, pady=10)
            name_entry.insert(0,result[0])

            roll_label = ttk.Label(updateStudentForm, text="Roll Number:", foreground="green",font=("Helvetica", 20))
            roll_label.grid(row=1, column=0, padx=10, pady=10,ipadx=10)
            roll_entry = ttk.Entry(updateStudentForm,style="Custom.TEntry")
            roll_entry.grid(row=1, column=1, padx=10, pady=10)
            roll_entry.insert(0,result[1])

            department_label = ttk.Label(updateStudentForm, text="Department:", foreground="green",font=("Helvetica", 20))
            department_label.grid(row=2, column=0, padx=10, pady=10,ipadx=10)
            department_entry = ttk.Entry(updateStudentForm,style="Custom.TEntry")
            department_entry.grid(row=2, column=1, padx=10, pady=10)
            department_entry.insert(0,result[2])

            email_label = ttk.Label(updateStudentForm, text="Email:", foreground="green",font=("Helvetica", 20))
            email_label.grid(row=3, column=0, padx=10, pady=10,ipadx=10)
            email_entry = ttk.Entry(updateStudentForm, style="Custom.TEntry")
            email_entry.grid(row=3, column=1, padx=10, pady=10)
            email_entry.insert(0,result[3])
        
            age_label = ttk.Label(updateStudentForm, text="Age:", foreground="green",font=("Helvetica", 20))
            age_label.grid(row=4, column=0, padx=10, pady=10,ipadx=10)
            age_entry = ttk.Entry(updateStudentForm,style="Custom.TEntry")
            age_entry.grid(row=4, column=1, padx=10, pady=10)
            age_entry.insert(0,result[4])
        
            submit_button = ttk.Button(updateStudentForm, text="Update",style="Custom.TButton" ,command=UpdateForm)
            submit_button.grid(row=5, columnspan=2, pady=20)
        else: 
            messagebox.showerror("Message","Student Does Not Exist")


    updateStudent= Toplevel(root)
    updateStudent.title("Update Student")
    updateStudent.geometry("500x250")
    updateStudent.iconbitmap("pics/icon.ico")
    updateStudent.resizable(0,0)

    roll_number_label = ttk.Label(updateStudent, text="Enter The Roll Number", foreground="green",font=("Helvetica", 20))
    roll_number_label.grid(row=0, column=0, padx=10, pady=10,ipadx=10)
    roll_number_entry = ttk.Entry(updateStudent,style="Custom.TEntry")
    roll_number_entry.grid(row=0, column=1, padx=10, pady=10)

    submit_button = ttk.Button(updateStudent, text="Update",style="Custom.TButton" ,command=Update)
    submit_button.grid(row=5, columnspan=2, pady=20)
   

def display_students():
    StudentsInfo= Toplevel(root)
    StudentsInfo.title("Update Faculty")
    StudentsInfo.iconbitmap("pics/icon.ico")
    StudentsInfo.resizable(0,0)

    student_tree = ttk.Treeview(StudentsInfo, columns=("Roll Number", "Name" ,"Department", "Age", "Email"), show="headings")
    student_tree.heading("Roll Number", text="Roll Number", anchor='w')
    student_tree.heading("Name", text="Name", anchor='w')
    student_tree.heading("Department", text="Department", anchor='w')
    student_tree.heading("Age", text="Age", anchor='w')
    student_tree.heading("Email", text="Email", anchor='w')
    student_tree.grid() 


    for row in cursor.execute("SELECT * FROM students"):
        student_tree.insert("", "end", values=row)


def display_faculty():
    FacultyInfo= Toplevel(root)
    FacultyInfo.title("Update Faculty")
    FacultyInfo.iconbitmap("pics/icon.ico")
    FacultyInfo.resizable(0,0)

    Facultytree = ttk.Treeview(FacultyInfo, columns=("Employee ID", "Name" ,"Department", "Position", "Email"), show="headings")
    Facultytree.heading("Employee ID", text="Employee ID", anchor='w')
    Facultytree.heading("Name", text="Name", anchor='w')
    Facultytree.heading("Department", text="Department", anchor='w')
    Facultytree.heading("Position", text="Age", anchor='w')
    Facultytree.heading("Email", text="Email", anchor='w')
    Facultytree.grid() 


    for row in cursor.execute("SELECT * FROM faculty"):
        Facultytree.insert("", "end", values=row)

def add_faculty():
    def submit():
        EmployeeID = EmployeeID_entry.get()
        name = name_entry.get()
        department = department_entry.get()
        position = position_entry.get()
        email = email_entry.get()
        if name_entry.get()=='' or position_entry.get()=='' or department_entry.get()==''  or email_entry.get()=='':
            messagebox.showerror('Error','All Feilds are required',parent=addFaculty)
        else:
            cursor.execute("INSERT INTO faculty (Employeeid,name,  department, position, email) VALUES (?, ?, ?, ?, ?)",
                  (EmployeeID,name, department, position, email))
            conn.commit()
            messagebox.showinfo("Message","Added Succesfully")
            addFaculty.destroy()
    addFaculty= Toplevel(root)
    addFaculty.title("Add New Faculty")
    addFaculty.geometry("400x400")
    addFaculty.iconbitmap("pics/icon.ico")

    EmployeeID_label = ttk.Label(addFaculty, text="EmployeeID:", foreground="green",font=("Helvetica", 20))
    EmployeeID_label.grid(row=0, column=0, padx=10, pady=10,ipadx=10)
    EmployeeID_entry = ttk.Entry(addFaculty,style="Custom.TEntry")
    EmployeeID_entry.grid(row=0, column=1, padx=10, pady=10)

    name_label = ttk.Label(addFaculty, text="Name:", foreground="green",font=("Helvetica", 20))
    name_label.grid(row=1, column=0, padx=10, pady=10,ipadx=10)
    name_entry = ttk.Entry(addFaculty,style="Custom.TEntry")
    name_entry.grid(row=1, column=1, padx=10, pady=10)


    position_label = ttk.Label(addFaculty, text="Position:",foreground="green", font=("Helvetica", 20))
    position_label.grid(row=4, column=0, padx=10, pady=10,ipadx=10)
    position_entry = ttk.Entry(addFaculty,style="Custom.TEntry")
    position_entry.grid(row=4, column=1, padx=10, pady=10)

    department_label = ttk.Label(addFaculty, text="Department:", foreground="green",font=("Helvetica", 20))
    department_label.grid(row=2, column=0, padx=10, pady=10,ipadx=10)
    department_entry = ttk.Entry(addFaculty,style="Custom.TEntry")
    department_entry.grid(row=2, column=1, padx=10, pady=10)

    email_label = ttk.Label(addFaculty, text="Email:", foreground="green",font=("Helvetica", 20))
    email_label.grid(row=3, column=0, padx=10, pady=10,ipadx=10)
    email_entry = ttk.Entry(addFaculty, style="Custom.TEntry")
    email_entry.grid(row=3, column=1, padx=10, pady=10)


    submit_button = ttk.Button(addFaculty, text="Submit",style="Custom.TButton" ,command=submit)
    submit_button.grid(row=5, columnspan=2, pady=20)
 

def remove_faculty():

    def Delete():
        EmployeeID = str(EmployeeID_entry.get())
        cursor.execute("SELECT * FROM faculty WHERE Employeeid = ?", (EmployeeID,))
        result = cursor.fetchone()
        if result:
            cursor.execute("DELETE FROM faculty WHERE Employeeid = ?", (EmployeeID,))
            conn.commit()
            messagebox.showinfo("Message","Deleted Succesfully")
            removeFaculty.destroy()
        else: 
            messagebox.showerror("Message","Employee Does Not Exist")
           
            
    removeFaculty= Toplevel(root)
    removeFaculty.title("Remove Faculty")
    removeFaculty.geometry("500x250")
    removeFaculty.iconbitmap("pics/icon.ico")

    EmployeeID_label = ttk.Label(removeFaculty, text="Enter The Employee ID", foreground="green",font=("Helvetica", 20))
    EmployeeID_label.grid(row=0, column=0, padx=10, pady=10,ipadx=10)
    EmployeeID_entry = ttk.Entry(removeFaculty,style="Custom.TEntry")
    EmployeeID_entry.grid(row=0, column=1, padx=10, pady=10)

    submit_button = ttk.Button(removeFaculty, text="Delete",style="Custom.TButton" ,command=Delete)
    submit_button.grid(row=5, columnspan=2, pady=20)

def update_faculty():

    def Update():
        EmplyeeID = employeeID_entry.get()
        cursor.execute("SELECT name,Employeeid,department, email, position FROM faculty WHERE Employeeid = ?", (EmplyeeID,))
        result = cursor.fetchone()

        def UpdateForm():
            new_name = name_entry.get()
            new_Employeeid = Employeeid_entry.get()
            new_department = department_entry.get()
            new_position = position_entry.get()
            new_email = email_entry.get()

            cursor.execute("UPDATE faculty SET name = ?,Employeeid=?, email = ?, position = ?, department=?, email=? WHERE Employeeid = ?",
                   (new_name, new_Employeeid,new_email, new_position,new_department,new_email,EmplyeeID,))
            conn.commit()
            messagebox.showinfo("Message","Updated Succesfully")
            updateFacultyForm.destroy()
            updateFaculty.destroy()

        if result:
            updateFacultyForm= Toplevel(root)
            updateFacultyForm.title("Update Faculty")
            updateFacultyForm.geometry("400x400")
            updateFacultyForm.iconbitmap("pics/icon.ico")
            updateFacultyForm.resizable(0,0)


            name_label = ttk.Label(updateFacultyForm, text="Name:", foreground="green",font=("Helvetica", 20))
            name_label.grid(row=0, column=0, padx=10, pady=10,ipadx=10)
            name_entry = ttk.Entry(updateFacultyForm,style="Custom.TEntry")
            name_entry.grid(row=0, column=1, padx=10, pady=10)
            name_entry.insert(0,result[0])

            Employeeid_label = ttk.Label(updateFacultyForm, text="Employee ID:", foreground="green",font=("Helvetica", 20))
            Employeeid_label.grid(row=1, column=0, padx=10, pady=10,ipadx=10)
            Employeeid_entry = ttk.Entry(updateFacultyForm,style="Custom.TEntry")
            Employeeid_entry.grid(row=1, column=1, padx=10, pady=10)
            Employeeid_entry.insert(0,result[1])

            department_label = ttk.Label(updateFacultyForm, text="Department:", foreground="green",font=("Helvetica", 20))
            department_label.grid(row=2, column=0, padx=10, pady=10,ipadx=10)
            department_entry = ttk.Entry(updateFacultyForm,style="Custom.TEntry")
            department_entry.grid(row=2, column=1, padx=10, pady=10)
            department_entry.insert(0,result[2])

            email_label = ttk.Label(updateFacultyForm, text="Email:", foreground="green",font=("Helvetica", 20))
            email_label.grid(row=3, column=0, padx=10, pady=10,ipadx=10)
            email_entry = ttk.Entry(updateFacultyForm, style="Custom.TEntry")
            email_entry.grid(row=3, column=1, padx=10, pady=10)
            email_entry.insert(0,result[3])
        
            position_label = ttk.Label(updateFacultyForm, text="Position:", foreground="green",font=("Helvetica", 20))
            position_label.grid(row=4, column=0, padx=10, pady=10,ipadx=10)
            position_entry = ttk.Entry(updateFacultyForm,style="Custom.TEntry")
            position_entry.grid(row=4, column=1, padx=10, pady=10)
            position_entry.insert(0,result[4])
        
            submit_button = ttk.Button(updateFacultyForm, text="Update",style="Custom.TButton" ,command=UpdateForm)
            submit_button.grid(row=5, columnspan=2, pady=20)
        else: 
            messagebox.showerror("Message","Employee Does Not Exist")


    updateFaculty= Toplevel(root)
    updateFaculty.title("Update Faculty")
    updateFaculty.geometry("500x250")
    updateFaculty.iconbitmap("pics/icon.ico")
    updateFaculty.resizable(0,0)

    employeeID_label = ttk.Label(updateFaculty, text="Enter The Employee ID", foreground="green",font=("Helvetica", 20))
    employeeID_label.grid(row=0, column=0, padx=10, pady=10,ipadx=10)
    employeeID_entry = ttk.Entry(updateFaculty,style="Custom.TEntry")
    employeeID_entry.grid(row=0, column=1, padx=10, pady=10)

    submit_button = ttk.Button(updateFaculty, text="Update",style="Custom.TButton" ,command=Update)
    submit_button.grid(row=5, columnspan=2, pady=20)
   

style = ttk.Style()
style.configure("Custom.TButton", padding=10, relief="flat", background="#91e0b5", foreground="green", font=("Helvetica", 12))
style.configure("Custom.TLabel", background="#91e0b5", foreground="white", font=("Helvetica", 20))
style.configure("Custom.TEntry", padding=5, font=("Helvetica", 12), foreground="black", background="lightgray")



 


logo = ImageTk.PhotoImage(Image.open("pics/logo.jpg"))
logoLabel = ttk.Button(root,image=logo)
logoLabel.grid(row=0, column=0 ,padx=30,pady=60,columnspan=10)




label1 = ttk.Label(root, text="Manage Students", style="Custom.TLabel")
label1.grid(row=1, column=0,pady=40)

btn1 = ttk.Button(root, text="Get Students Info", style="Custom.TButton", command=display_students)
btn2 = ttk.Button(root, text="Add New Student", style="Custom.TButton", command=add_student)
btn3 = ttk.Button(root, text="Remove Student", style="Custom.TButton",command=remove_student)
btn4 = ttk.Button(root, text="Update Student Info", style="Custom.TButton", command=update_student)

btn1.grid(row=2,column=0 , padx=10, pady=10, ipadx=5, ipady=3)
btn2.grid(row=2,column=1 , padx=10, pady=10, ipadx=5, ipady=3)
btn3.grid(row=2,column=2 , padx=10, pady=10, ipadx=5, ipady=3)
btn4.grid(row=2,column=3 , padx=10, pady=10, ipadx=5, ipady=3)

label2 = ttk.Label(root, text="Manage Faculty", style="Custom.TLabel")
label2.grid(row=3, column=0,pady=40)

btn6 = ttk.Button(root, text="Get Teachers Info", style="Custom.TButton",command=display_faculty)
btn7 = ttk.Button(root, text="Add New Teacher", style="Custom.TButton", command=add_faculty)
btn8 = ttk.Button(root, text="Remove Teacher", style="Custom.TButton",command=remove_faculty)
btn9 = ttk.Button(root, text="Update Teacher Info", style="Custom.TButton",command=update_faculty)
btn6.grid(row=4,column=0 , padx=10, pady=10, ipadx=5, ipady=3)
btn7.grid(row=4,column=1 , padx=10, pady=10, ipadx=5, ipady=3)
btn8.grid(row=4,column=2 , padx=10, pady=10, ipadx=5, ipady=3)
btn9.grid(row=4,column=3 , padx=10, pady=10, ipadx=5, ipady=3)


btn5 = ttk.Button(root, text="Close", style="Custom.TButton",command=quit)
btn5.grid(row=5,column=0 , padx=10, pady=50, ipadx=5, ipady=3,columnspan=10)


root.mainloop()
