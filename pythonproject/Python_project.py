# ==========================================================
#   CAR ACCIDENT REPORT DATABASE + LOGIN / MENU SYSTEM
# ==========================================================

import mysql.connector
import tkinter as tk
from tkinter import messagebox, ttk
import os

# ---------- DATABASE CREATION ----------
sql = mysql.connector.connect(host='localhost', username='root', password='helloworld')
cur = sql.cursor()
try:
    cur.execute('create database car_inventory')
except:
    pass
try:
    cur.execute('create database customer_data')
except:
    pass

sql1 = mysql.connector.connect(host='localhost', username='root', password='helloworld', database='car_inventory')
sql2 = mysql.connector.connect(host='localhost', username='root', password='helloworld', database='customer_data')
cur1 = sql1.cursor()
cur2 = sql2.cursor()



'''# ------------------ DEFAULT DATA ------------------
car_data = [
    (1, 'Civic', 'Honda', 2020, 'Petrol', 'Automatic', 'White'),
    (2, 'Model 3', 'Tesla', 2022, 'Electric', 'Automatic', 'Red'),
    (3, 'Corolla', 'Toyota', 2019, 'Diesel', 'Manual', 'Silver'),
    (4, 'Mustang', 'Ford', 2021, 'Petrol', 'Automatic', 'Yellow'),
    (5, 'Creta', 'Hyundai', 2023, 'Diesel', 'Manual', 'Black'),
    (6, 'Swift', 'Suzuki', 2018, 'Petrol', 'Manual', 'Blue'),
    (7, 'Fortuner', 'Toyota', 2022, 'Diesel', 'Automatic', 'Grey'),
    (8, 'City', 'Honda', 2021, 'Petrol', 'CVT', 'Red'),
    (9, 'i20', 'Hyundai', 2020, 'Petrol', 'Manual', 'Blue'),
    (10, 'Compass', 'Jeep', 2021, 'Diesel', 'Automatic', 'Black'),
    (11, 'Seltos', 'Kia', 2022, 'Petrol', 'CVT', 'White'),
    (12, 'Altroz', 'Tata', 2023, 'Petrol', 'Manual', 'Grey'),
    (13, 'XUV700', 'Mahindra', 2022, 'Diesel', 'Automatic', 'Silver'),
    (14, 'Baleno', 'Suzuki', 2021, 'Petrol', 'Automatic', 'Blue'),
    (15, 'Venue', 'Hyundai', 2020, 'Petrol', 'Manual', 'Grey'),
    (16, 'Sonet', 'Kia', 2023, 'Diesel', 'Automatic', 'Red'),
    (17, 'Thar', 'Mahindra', 2021, 'Diesel', 'Manual', 'Black'),
    (18, 'A-Class', 'Mercedes', 2022, 'Petrol', 'Automatic', 'White'),
    (19, 'Q3', 'Audi', 2023, 'Petrol', 'Automatic', 'Blue'),
    (20, 'Kushaq', 'Skoda', 2023, 'Petrol', 'Manual', 'Orange')
]

query_car = """
INSERT INTO Car_details (car_id, car_name, brand, model_year, fuel_type, transmission, color)
VALUES (%s, %s, %s, %s, %s, %s, %s)
"""

car_status_data = [
    (1, 'Available', 22000, 'Excellent'),
    (2, 'Sold', 10000, 'New'),
    (3, 'Available', 35000, 'Good'),
    (4, 'Available', 15000, 'Excellent'),
    (5, 'Available', 5000, 'New'),
    (6, 'Sold', 45000, 'Fair'),
    (7, 'Available', 12000, 'Excellent'),
    (8, 'Available', 18000, 'Good'),
    (9, 'Sold', 30000, 'Fair'),
    (10, 'Available', 14000, 'Excellent'),
    (11, 'Available', 8000, 'Excellent'),
    (12, 'Available', 2000, 'New'),
    (13, 'Available', 9000, 'Excellent'),
    (14, 'Sold', 25000, 'Good'),
    (15, 'Available', 10000, 'Good'),
    (16, 'Available', 5000, 'New'),
    (17, 'Available', 11000, 'Excellent'),
    (18, 'Sold', 8000, 'Excellent'),
    (19, 'Available', 3000, 'New'),
    (20, 'Available', 7000, 'New')
]

query_status = """
INSERT INTO Car_status (car_id, availability, mileage, condition_status)
VALUES (%s, %s, %s, %s)
"""

car_specification_data = [
    (1, 1800, 140, 174, 5),
    (2, 0, 283, 350, 5),
    (3, 1600, 120, 150, 5),
    (4, 5000, 450, 530, 4),
    (5, 1493, 113, 250, 5),
    (6, 1200, 83, 113, 5),
    (7, 2755, 204, 420, 7),
    (8, 1498, 121, 145, 5),
    (9, 1197, 83, 115, 5),
    (10, 1956, 170, 350, 5),
    (11, 1497, 113, 144, 5),
    (12, 1199, 85, 113, 5),
    (13, 2198, 182, 420, 7),
    (14, 1197, 88, 113, 5),
    (15, 1493, 118, 250, 5),
    (16, 1493, 115, 250, 5),
    (17, 2184, 130, 300, 4),
    (18, 1332, 163, 250, 5),
    (19, 1984, 190, 320, 5),
    (20, 1498, 150, 250, 5)
]

query_spec = """
INSERT INTO Car_specification (car_id, engine_cc, horsepower, torque, seating_capacity)
VALUES (%s, %s, %s, %s, %s)
"""
'''

# ------------------ FUNCTION TO ADD DEFAULT DATA ------------------
def insert_default_data():
    try:
        cur1.executemany(query_car, car_data)
        cur1.executemany(query_status, car_status_data)
        cur1.executemany(query_spec, car_specification_data)
        sql1.commit()
        messagebox.showinfo("Success", "Default car details added successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to insert data:\n{e}")

# ---------- TABLE CREATION ----------
try:
    cur1.execute("""
    CREATE TABLE IF NOT EXISTS Car_details (
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
    CREATE TABLE IF NOT EXISTS Car_status (
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
    CREATE TABLE IF NOT EXISTS Car_specification (
        spec_id INT AUTO_INCREMENT PRIMARY KEY,
        car_id INT,
        engine_cc INT,
        horsepower INT,
        torque INT,
        seating_capacity INT,
        FOREIGN KEY (car_id) REFERENCES Car_details(car_id)
            ON DELETE CASCADE
            ON UPDATE CASCADE
    );
    """)
except Exception as e:
    print("Error creating Car_specification table:", e)

try:
    cur1.execute("""
    CREATE TABLE IF NOT EXISTS Car_price (
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
    CREATE TABLE IF NOT EXISTS Car_owner_history (
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
    CREATE TABLE IF NOT EXISTS Customers (
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
    CREATE TABLE IF NOT EXISTS Customer_login (
        login_id INT PRIMARY KEY AUTO_INCREMENT,
        username VARCHAR(50),
        password_hash VARCHAR(255)
    );
    """)
except Exception as e:
    print("Error creating Customer_login table:", e)

# ---------- DEFAULT LOGIN ----------
cur2.execute("SELECT * FROM Customer_login")
if not cur2.fetchall():
    cur2.execute("INSERT INTO Customer_login (username, password_hash) VALUES ('admin', '1234')")
    sql2.commit()


# ------------------ DEFAULT CAR DATA ------------------

car_data = [
    (1, 'Civic', 'Honda', 2020, 'Petrol', 'Automatic', 'White'),
    (2, 'Model 3', 'Tesla', 2022, 'Electric', 'Automatic', 'Red'),
    (3, 'Corolla', 'Toyota', 2019, 'Diesel', 'Manual', 'Silver'),
    (4, 'Mustang', 'Ford', 2021, 'Petrol', 'Automatic', 'Yellow'),
    (5, 'Creta', 'Hyundai', 2023, 'Diesel', 'Manual', 'Black'),
    (6, 'Swift', 'Suzuki', 2018, 'Petrol', 'Manual', 'Blue'),
    (7, 'Fortuner', 'Toyota', 2022, 'Diesel', 'Automatic', 'Grey'),
    (8, 'City', 'Honda', 2021, 'Petrol', 'CVT', 'Red'),
    (9, 'i20', 'Hyundai', 2020, 'Petrol', 'Manual', 'Blue'),
    (10, 'Compass', 'Jeep', 2021, 'Diesel', 'Automatic', 'Black'),
]

car_status_data = [
    (1, 'Available', 22000, 'Excellent'),
    (2, 'Sold', 10000, 'New'),
    (3, 'Available', 35000, 'Good'),
    (4, 'Available', 15000, 'Excellent'),
    (5, 'Available', 5000, 'New'),
    (6, 'Sold', 45000, 'Fair'),
    (7, 'Available', 12000, 'Excellent'),
    (8, 'Available', 18000, 'Good'),
    (9, 'Sold', 30000, 'Fair'),
    (10, 'Available', 14000, 'Excellent'),
]

car_specification_data = [
    (1, 1800, 140, 174, 5),
    (2, 0, 283, 350, 5),
    (3, 1600, 120, 150, 5),
    (4, 5000, 450, 530, 4),
    (5, 1493, 113, 250, 5),
    (6, 1200, 83, 113, 5),
    (7, 2755, 204, 420, 7),
    (8, 1498, 121, 145, 5),
    (9, 1197, 83, 115, 5),
    (10, 1956, 170, 350, 5),
]

# ------------------ INSERT DEFAULT DATA ------------------

def insert_default_data():
    try:
        cur1.executemany("""
            INSERT INTO Car_details (car_id, car_name, brand, model_year, fuel_type, transmission, color)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, car_data)

        cur1.executemany("""
            INSERT INTO Car_status (car_id, availability, mileage, condition_status)
            VALUES (%s, %s, %s, %s)
        """, car_status_data)

        cur1.executemany("""
            INSERT INTO Car_specification (car_id, engine_cc, horsepower, torque, seating_capacity)
            VALUES (%s, %s, %s, %s, %s)
        """, car_specification_data)

        sql1.commit()
        messagebox.showinfo("Success", "Default car details added successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to insert data:\n{e}")

# ==========================================================
#   GUI SECTION
# ==========================================================

root = tk.Tk()
root.geometry("600x500")

def clear_root():
    for widget in root.winfo_children():
        widget.destroy()

# --- LOGIN SCREEN ---

def show_login_screen():
    clear_root()
    root.title("Login")

    tk.Label(root, text="Car Dealership Login", font=("Arial", 18, "bold")).pack(pady=20)
    username_var = tk.StringVar()
    password_var = tk.StringVar()

    tk.Label(root, text="Username").pack()
    username_entry = tk.Entry(root, textvariable=username_var)
    username_entry.pack(pady=5)

    tk.Label(root, text="Password").pack()
    password_entry = tk.Entry(root, textvariable=password_var, show="*")
    password_entry.pack(pady=5)

    def login_action():
        cur2.execute("SELECT * FROM Customer_login WHERE username=%s AND password_hash=%s",
                     (username_var.get(), password_var.get()))
        if cur2.fetchone():
            messagebox.showinfo("Login Success", "Welcome!")
            show_menu_screen()
        else:
            messagebox.showerror("Error", "Invalid username or password.")

    def open_register_screen():
        clear_root()
        root.title("Register")
        tk.Label(root, text="Register New User", font=("Arial", 18, "bold")).pack(pady=20)

        new_user_var = tk.StringVar()
        new_pass_var = tk.StringVar()

        tk.Label(root, text="New Username").pack()
        tk.Entry(root, textvariable=new_user_var).pack(pady=5)
        tk.Label(root, text="New Password").pack()
        tk.Entry(root, textvariable=new_pass_var, show="*").pack(pady=5)

        def register_action():
            try:
                cur2.execute("INSERT INTO Customer_login (username, password_hash) VALUES (%s, %s)",
                             (new_user_var.get(), new_pass_var.get()))
                sql2.commit()
                messagebox.showinfo("Success", "Registration Successful! You can now log in.")
                show_login_screen()
            except Exception as e:
                messagebox.showerror("Error", f"Registration failed:\n{e}")

        tk.Button(root, text="Register", bg="green", fg="white", command=register_action).pack(pady=10)
        tk.Button(root, text="Back to Login", command=show_login_screen).pack()

    tk.Button(root, text="Login", bg="green", fg="white", width=15, command=login_action).pack(pady=15)
    tk.Button(root, text="Register New User", bg="blue", fg="white", width=15, command=open_register_screen).pack()

    # ✅ Ensure focus is set after everything loads
    root.after(100, lambda: username_entry.focus_set())

# --- MENU SCREEN ---

def show_menu_screen():
    clear_root()
    root.title("Main Menu")
    tk.Label(root, text="Car Dealership Menu", font=("Arial", 20, "bold")).pack(pady=30)

    tk.Button(root, text="Add Car Details", width=20, height=2, bg="green", fg="white",
              command=lambda: open_add_car_form(root)).pack(pady=10)
    tk.Button(root, text="Search Car", width=20, height=2, bg="blue", fg="white",
              command=lambda: open_search_car_form(root)).pack(pady=10)
    tk.Button(root, text="Logout", width=20, height=2, bg="red", fg="white",
              command=show_login_screen).pack(pady=30)

# --- ADD & SEARCH FUNCTIONS ---

def open_search_car_form(root_window):
    clear_root()
    root_window.title("Search Car Details")
    tk.Label(root_window, text="Search Car Details", font=("Arial", 16, "bold")).pack(pady=10)

    search_var = tk.StringVar()
    search_entry = tk.Entry(root_window, textvariable=search_var, width=40)
    search_entry.pack(pady=5)

    columns = ("Car ID", "Car Name", "Brand", "Model Year", "Fuel Type", "Transmission", "Color")
    tree = ttk.Treeview(root_window, columns=columns, show="headings", height=10)
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=85)
    tree.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

   
    def perform_search(event=None):
        query_text = search_var.get().strip()
        if len(query_text) >= 3:
            try:
                cur1.execute(
                    "SELECT * FROM Car_details WHERE car_name LIKE %s OR brand LIKE %s",
                    (f"%{query_text}%", f"%{query_text}%")
                )
                results = cur1.fetchall()
                tree.delete(*tree.get_children())
                for row in results:
                    tree.insert("", tk.END, values=row)
                if not results:
                    tree.insert("", tk.END, values=("No cars found", "", "", "", "", "", ""))
            except Exception as e:
                messagebox.showerror("Error", f"Error searching cars:\n{e}")
        else:
            tree.delete(*tree.get_children())
    search_entry.bind("<KeyRelease>", perform_search)
    
    def view_selected_car():
        selected = tree.selection()
        if not selected:
            messagebox.showwarning("No Selection", "Please select a car from the list.")
            return
        car_data = tree.item(selected[0], 'values')
        open_car_details_screen(car_data[0])

    tk.Button(root_window, text="View Selected Car", bg="orange", fg="white", command=view_selected_car).pack(pady=5)
    tk.Button(root_window, text="Back to Menu", command=show_menu_screen).pack(pady=5)

# --- CAR DETAILS SCREEN ---

def open_car_details_screen(car_id):
    details_window = tk.Toplevel(root)
    details_window.title("Car Full Details")
    details_window.geometry("550x450")
    details_window.config(bg="#f5f5f5")

    try:
        cur1.execute("SELECT * FROM Car_details WHERE car_id = %s", (car_id,))
        car = cur1.fetchone()
        if not car:
            messagebox.showerror("Error", "Car not found.")
            return

        tk.Label(details_window, text="Car Details", font=("Arial", 18, "bold"), bg="#f5f5f5").pack(pady=10)
        labels = ["Car ID", "Car Name", "Brand", "Model Year", "Fuel Type", "Transmission", "Color"]
        for i, label in enumerate(labels):
            tk.Label(details_window, text=f"{label}: {car[i]}", bg="#f5f5f5").pack(anchor="w", padx=20)

        def show_status():
            cur1.execute("SELECT availability, mileage, condition_status FROM Car_status WHERE car_id=%s", (car_id,))
            st = cur1.fetchone()
            if st:
                messagebox.showinfo("Car Status", f"Availability: {st[0]}\nMileage: {st[1]} km\nCondition: {st[2]}")
            else:
                messagebox.showwarning("No Status", "No status record found.")

        tk.Button(details_window, text="View Car Status", bg="#0078D7", fg="white", command=show_status).pack(pady=15)

    except Exception as e:
        messagebox.showerror("Error", f"Database error:\n{e}")

# --- STARTUP ---

def start_app():
    ans = messagebox.askyesno("Add Default Data", "Would you like to add the default car details?")
    if ans:
        insert_default_data()
    show_login_screen()

start_app()
root.mainloop()