import tkinter as tk
from tkinter import ttk, messagebox
from db_connection import connect  # ✅ fixed import

# -------- FUNCTIONS -------- #
def fetch_employees():
    con = connect()
    cur = con.cursor()
    cur.execute("SELECT * FROM employees")
    rows = cur.fetchall()
    for row in employee_table.get_children():
        employee_table.delete(row)
    for row in rows:
        employee_table.insert("", tk.END, values=row)
    con.close()


def add_employee():
    name = name_var.get()
    designation = designation_var.get()
    department = department_var.get()
    salary = salary_var.get()
    status = status_var.get()

    if name == "" or designation == "" or salary == "":
        messagebox.showerror("Error", "All fields are required!")
        return

    con = connect()
    cur = con.cursor()
    cur.execute(
        "INSERT INTO employees (name, designation, department, salary, status) VALUES (?,?,?,?,?)",
        (name, designation, department, salary, status)
    )
    con.commit()
    con.close()
    fetch_employees()
    messagebox.showinfo("Success", "Employee added successfully!")


def update_employee():
    selected = employee_table.focus()
    if not selected:
        messagebox.showwarning("Select Employee", "Please select a record to update.")
        return

    data = employee_table.item(selected, "values")

    con = connect()
    cur = con.cursor()
    cur.execute("""
        UPDATE employees
        SET name=?, designation=?, department=?, salary=?, status=?
        WHERE emp_id=?
    """, (name_var.get(), designation_var.get(), department_var.get(),
          salary_var.get(), status_var.get(), data[0]))
    con.commit()
    con.close()
    fetch_employees()
    messagebox.showinfo("Updated", "Employee details updated successfully!")


def delete_employee():
    selected = employee_table.focus()
    if not selected:
        messagebox.showwarning("Select Employee", "Please select a record to delete.")
        return

    data = employee_table.item(selected, "values")
    confirm = messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete employee ID {data[0]}?")
    if not confirm:
        return

    con = connect()
    cur = con.cursor()
    cur.execute("DELETE FROM employees WHERE emp_id=?", (data[0],))
    con.commit()
    con.close()
    fetch_employees()
    messagebox.showinfo("Deleted", "Employee deleted successfully!")


def clear_fields():
    name_var.set("")
    designation_var.set("")
    department_var.set("")
    salary_var.set("")
    status_var.set("Active")


# -------- GUI -------- #
root = tk.Tk()
root.title("Employee Payroll Management System")
root.geometry("950x600")
root.configure(bg="#f0f4f7")

tk.Label(root, text="Employee Payroll Management System", font=("Arial", 22, "bold"),
         bg="#f0f4f7", fg="#333").pack(pady=15)

frame = tk.Frame(root, bg="#f0f4f7")
frame.pack(pady=10)

name_var = tk.StringVar()
designation_var = tk.StringVar()
department_var = tk.StringVar()
salary_var = tk.StringVar()
status_var = tk.StringVar(value="Active")

labels = ["Name", "Designation", "Department", "Salary", "Status"]
variables = [name_var, designation_var, department_var, salary_var, status_var]

for i in range(5):
    tk.Label(frame, text=labels[i], bg="#f0f4f7", font=("Arial", 11)).grid(row=i, column=0, padx=10, pady=5, sticky="w")
    tk.Entry(frame, textvariable=variables[i], width=40, font=("Arial", 11)).grid(row=i, column=1, padx=10, pady=5)

# Buttons
button_frame = tk.Frame(root, bg="#f0f4f7")
button_frame.pack(pady=10)

tk.Button(button_frame, text="Add", width=10, command=add_employee, bg="#4CAF50", fg="white").grid(row=0, column=0, padx=10)
tk.Button(button_frame, text="Update", width=10, command=update_employee, bg="#2196F3", fg="white").grid(row=0, column=1, padx=10)
tk.Button(button_frame, text="Delete", width=10, command=delete_employee, bg="#f44336", fg="white").grid(row=0, column=2, padx=10)
tk.Button(button_frame, text="Clear", width=10, command=clear_fields, bg="#9E9E9E", fg="white").grid(row=0, column=3, padx=10)

# Table
columns = ("Emp ID", "Name", "Designation", "Department", "Salary", "Status")
employee_table = ttk.Treeview(root, columns=columns, show="headings", height=15)

for col in columns:
    employee_table.heading(col, text=col)
    employee_table.column(col, width=140)

employee_table.pack(fill="x", pady=10)

fetch_employees()
root.mainloop()
