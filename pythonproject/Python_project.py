#Car accident report database

import mysql.connector
import tkinter as tk
import csv
import pickle
from tkinter import messagebox

sql=mysql.connector.connect(host='localhost',username='root',password='helloworld')
cur=sql.cursor()
try:
    cur.execute('create database car_inventory')
except:
     pass
try:
    cur.execute('create database customer_data')
except:
     pass
sql1=mysql.connector.connect(host='localhost',username='root',password='helloworld',database='car_inventory')
sql2=mysql.connector.connect(host='localhost',username='root',password='helloworld',database='customer_data')
cur1=sql1.cursor()
cur2=sql2.cursor()
try:
    cur1.execute("""
    CREATE TABLE Car_details (
        car_id INT AUTO_INCREMENT PRIMARY KEY,
        car_name VARCHAR(50),
        brand VARCHAR(50),
        model_year INT,
        fuel_type VARCHAR(20),
        transmission VARCHAR(20),
        color VARCHAR(20)
    );
    """)
except Exception as e:
    print("Error creating Car_details table:", e)

try:
    cur1.execute("""
    CREATE TABLE Car_status (
        status_id INT AUTO_INCREMENT PRIMARY KEY,
        car_id INT,
        availability VARCHAR(20),
        mileage INT,
        condition_status VARCHAR(20),
        FOREIGN KEY (car_id) REFERENCES Car_details(car_id)
            ON DELETE CASCADE
            ON UPDATE CASCADE
    );
    """)
except Exception as e:
    print("Error creating Car_status table:", e)


try:
    cur1.execute("""
    CREATE TABLE Car_specification (
        spec_id INT AUTO_INCREMENT PRIMARY KEY,
        car_id INT,
        engine_cc INT,
        horsepower INT,
        torque INT,
        seating_capacity INT,
        color VARCHAR(20),
        FOREIGN KEY (car_id) REFERENCES Car_details(car_id)
            ON DELETE CASCADE
            ON UPDATE CASCADE
    );
    """)
except Exception as e:
    print("Error creating Car_specification table:", e)

try:
    cur1.execute("""
    CREATE TABLE Car_price (
        price_id INT AUTO_INCREMENT PRIMARY KEY,
        car_id INT,
        onroad_price INT,
        currency VARCHAR(10),
        listing_price INT,
        FOREIGN KEY (car_id) REFERENCES Car_details(car_id)
            ON DELETE CASCADE
            ON UPDATE CASCADE
    );
    """)
except Exception as e:
    print("Error creating Car_price table:", e)

try:
    cur1.execute("""
    CREATE TABLE Car_owner_history (
        owner_id INT AUTO_INCREMENT PRIMARY KEY,
        car_id INT,
        previous_owners INT,
        last_owner_name VARCHAR(100),
        ownership_type VARCHAR(20),
        ownership_hand VARCHAR(30),
        FOREIGN KEY (car_id) REFERENCES Car_details(car_id)
            ON DELETE CASCADE
            ON UPDATE CASCADE
    );
    """)
except Exception as e:
    print("Error creating Car_owner_history table:", e)

try:
    cur2.execute("""
    CREATE TABLE Customers (
        customer_id INT PRIMARY KEY AUTO_INCREMENT,
        first_name VARCHAR(50),
        last_name VARCHAR(50),
        email VARCHAR(100),
        phone VARCHAR(15),
        city VARCHAR(50),
        country VARCHAR(50)
    );
    """)
except Exception as e:
    print("Error creating Customers table:", e)

try:
    cur2.execute("""
    CREATE TABLE Customer_login (
        login_id INT PRIMARY KEY AUTO_INCREMENT,
        customer_id INT,
        username VARCHAR(50),
        password_hash VARCHAR(255),
        last_login DATETIME,
        FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
    );
    """)
except Exception as e:
    print("Error creating Customer_login table:", e)

try:
    cur2.execute("""
    CREATE TABLE Customer_purchase_history (
        purchase_id INT PRIMARY KEY AUTO_INCREMENT,
        customer_id INT,
        car_id INT,
        purchase_date DATE,
        purchase_type VARCHAR(20),
        price_paid DECIMAL(10,2),
        FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
    );
    """)
except Exception as e:
    print("Error creating Customer_purchase_history table:", e)


root = tk.Tk()
root.title("Car Dealership Data Entry")
root.geometry("600x500")

# --- Car Details Entry Form ---
def add_car_details():
    try:
        cur1.execute(
            "INSERT INTO Car_details (car_name, brand, model_year, fuel_type, transmission, color) "
            "VALUES (%s, %s, %s, %s, %s, %s)",
            (car_name_var.get(), brand_var.get(), int(model_year_var.get()), fuel_type_var.get(),
             transmission_var.get(), color_var.get())
        )
        sql1.commit()
        messagebox.showinfo("Success", "Car details added successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Error adding car details:\n{e}")

# --- Tkinter Variables ---
car_name_var = tk.StringVar()
brand_var = tk.StringVar()
model_year_var = tk.StringVar()
fuel_type_var = tk.StringVar()
transmission_var = tk.StringVar()
color_var = tk.StringVar()

# --- Car Details Form ---
tk.Label(root, text="Car Details Entry", font=("Arial", 16)).pack(pady=10)

tk.Label(root, text="Car Name").pack()
tk.Entry(root, textvariable=car_name_var).pack()

tk.Label(root, text="Brand").pack()
tk.Entry(root, textvariable=brand_var).pack()

tk.Label(root, text="Model Year").pack()
tk.Entry(root, textvariable=model_year_var).pack()

tk.Label(root, text="Fuel Type").pack()
tk.Entry(root, textvariable=fuel_type_var).pack()

tk.Label(root, text="Transmission").pack()
tk.Entry(root, textvariable=transmission_var).pack()

tk.Label(root, text="Color").pack()
tk.Entry(root, textvariable=color_var).pack()

tk.Button(root, text="Add Car Details", command=add_car_details, bg="green", fg="white").pack(pady=20)

root.mainloop()

root = tk.Tk()
root.title("Search Car Details")
root.geometry("800x500")

# --- Search Function ---
def search_car():
    search_term = search_var.get()
    query = "SELECT * FROM Car_details WHERE car_name LIKE %s OR brand LIKE %s"
    try:
        cur1.execute(query, (f"%{search_term}%", f"%{search_term}%"))
        results = cur1.fetchall()
        
        # Clear previous treeview results
        for row in tree.get_children():
            tree.delete(row)
        
        # Insert new results
        for row in results:
            tree.insert("", tk.END, values=row)
        
        if not results:
            messagebox.showinfo("No Results", "No cars found matching your search.")
    except Exception as e:
        messagebox.showerror("Error", f"Error searching cars:\n{e}")

# --- Search Entry ---
tk.Label(root, text="Search by Car Name or Brand:", font=("Arial", 14)).pack(pady=10)
search_var = tk.StringVar()
tk.Entry(root, textvariable=search_var, width=50).pack()
tk.Button(root, text="Search", command=search_car, bg="blue", fg="white").pack(pady=10)

# --- Treeview to display results ---
columns = ("Car ID", "Car Name", "Brand", "Model Year", "Fuel Type", "Transmission", "Color")
tree = ttk.Treeview(root, columns=columns, show="headings")
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=100)
tree.pack(expand=True, fill=tk.BOTH)

root.mainloop()