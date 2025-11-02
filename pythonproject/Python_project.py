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
#cur1.execute('ALTER TABLE Car_details ADD COLUMN image_path VARCHAR(255);')
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
        color VARCHAR(20),
        image_path VARCHAR(255)
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

#-------------Car values to be inserted-----------------
query = """
INSERT INTO Car_details (car_name, brand, model_year, fuel_type, transmission, color, image_path)
VALUES (%s, %s, %s, %s, %s, %s, %s)
"""
values = ('Civic', 'Honda', 2020, 'Petrol', 'Automatic', 'White', 'C:/Users/ajdks/Documents/python_scripts/pythonproject/Pictures/Civic.jpg')

cur1.execute(query, values)

# ---------- DEFAULT LOGIN ----------
cur2.execute("SELECT * FROM Customer_login")
if not cur2.fetchall():
    cur2.execute("INSERT INTO Customer_login (username, password_hash) VALUES ('admin', '1234')")
    sql2.commit()

# ==========================================================
#   VIEW CAR DETAILS SCREEN
# ==========================================================

def open_car_details_screen(car_id):
    details_window = tk.Toplevel(root)
    details_window.title("Car Full Details")
    details_window.geometry("650x700")
    details_window.config(bg="#f5f5f5")

    tk.Label(details_window, text="Car Details", font=("Arial", 18, "bold"), bg="#f5f5f5").pack(pady=10)

    try:
        # Fetch data from all related tables
        cur1.execute("SELECT * FROM Car_details WHERE car_id = %s", (car_id,))
        car_info = cur1.fetchone()

        cur1.execute("SELECT * FROM Car_status WHERE car_id = %s", (car_id,))
        status_info = cur1.fetchone()

        cur1.execute("SELECT * FROM Car_specification WHERE car_id = %s", (car_id,))
        spec_info = cur1.fetchone()

        cur1.execute("SELECT * FROM Car_price WHERE car_id = %s", (car_id,))
        price_info = cur1.fetchone()

        cur1.execute("SELECT * FROM Car_owner_history WHERE car_id = %s", (car_id,))
        owner_info = cur1.fetchone()

        # --- Display Image (if available) ---
        image_frame = tk.Frame(details_window, bg="#f5f5f5")
        image_frame.pack(pady=10)

        if car_info and len(car_info) > 7:
            image_path = car_info[7]
            if image_path and os.path.exists(image_path):
                try:
                    img = Image.open(image_path)
                    img = img.resize((350, 250))
                    photo = ImageTk.PhotoImage(img)
                    img_label = tk.Label(image_frame, image=photo, bg="#f5f5f5")
                    img_label.image = photo  # Prevent garbage collection
                    img_label.pack()
                except Exception as e:
                    tk.Label(image_frame, text=f"Image could not be loaded: {e}", fg="red", bg="#f5f5f5").pack()
            else:
                tk.Label(image_frame, text="Image not found", fg="red", bg="#f5f5f5").pack()

        # --- Allow user to upload or change the image ---
        def upload_image():
            file_path = filedialog.askopenfilename(
                title="Select Car Image",
                filetypes=[("Image Files", "*.jpg *.jpeg *.png")]
            )
            if file_path:
                file_path = file_path.replace("\\", "/")  # Normalize slashes
                try:
                    cur1.execute("UPDATE Car_details SET image_path=%s WHERE car_id=%s", (file_path, car_id))
                    sql1.commit()
                    messagebox.showinfo("Success", "Image updated successfully!")
                    details_window.destroy()
                    open_car_details_screen(car_id)  # Refresh window
                except Exception as e:
                    messagebox.showerror("Error", f"Failed to update image:\n{e}")

        tk.Button(details_window, text="Upload New Image", command=upload_image,
                  bg="green", fg="white").pack(pady=5)

        # --- Combine all text details ---
        text_box = tk.Text(details_window, wrap=tk.WORD, font=("Arial", 12),
                           bg="white", height=25, width=70)
        text_box.pack(padx=10, pady=10)

        display_text = ""

        if car_info:
            display_text += f"--- Car Information ---\n"
            display_text += f"Car ID: {car_info[0]}\nName: {car_info[1]}\nBrand: {car_info[2]}\n"
            display_text += f"Model Year: {car_info[3]}\nFuel Type: {car_info[4]}\n"
            display_text += f"Transmission: {car_info[5]}\nColor: {car_info[6]}\n\n"

        if status_info:
            display_text += f"--- Status ---\nAvailability: {status_info[2]}\n"
            display_text += f"Mileage: {status_info[3]} km\nCondition: {status_info[4]}\n\n"

        if spec_info:
            display_text += f"--- Specifications ---\nEngine: {spec_info[2]} cc\nHorsepower: {spec_info[3]} HP\n"
            display_text += f"Torque: {spec_info[4]} Nm\nSeating: {spec_info[5]}\nColor: {spec_info[6]}\n\n"

        if price_info:
            display_text += f"--- Price ---\nOn-road Price: {price_info[2]} {price_info[3]}\n"
            display_text += f"Listing Price: {price_info[4]} {price_info[3]}\n\n"

        if owner_info:
            display_text += f"--- Owner History ---\nPrevious Owners: {owner_info[2]}\n"
            display_text += f"Last Owner: {owner_info[3]}\nOwnership Type: {owner_info[4]}\n"
            display_text += f"Ownership Hand: {owner_info[5]}\n\n"

        if not any([car_info, status_info, spec_info, price_info, owner_info]):
            display_text = "No additional details found for this car."

        text_box.insert(tk.END, display_text)
        text_box.config(state="disabled")

        tk.Button(details_window, text="Close", command=details_window.destroy,
                  bg="red", fg="white").pack(pady=10)

    except Exception as e:
        messagebox.showerror("Error", f"Failed to fetch car details:\n{e}")

# ==========================================================
#   FUNCTIONS FOR ADD CAR AND SEARCH CAR
# ==========================================================

def open_add_car_form(root_window):
    """Opens the Add Car Details form"""
    for widget in root_window.winfo_children():
        widget.destroy()

    root_window.title("Add Car Details")
    tk.Label(root_window, text="Add Car Details", font=("Arial", 16, "bold")).pack(pady=10)

    # Tkinter Variables
    car_name_var = tk.StringVar()
    brand_var = tk.StringVar()
    model_year_var = tk.StringVar()
    fuel_type_var = tk.StringVar()
    transmission_var = tk.StringVar()
    color_var = tk.StringVar()

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

    entries = [
        ("Car Name", car_name_var),
        ("Brand", brand_var),
        ("Model Year", model_year_var),
        ("Fuel Type", fuel_type_var),
        ("Transmission", transmission_var),
        ("Color", color_var)
    ]

    for label, var in entries:
        tk.Label(root_window, text=label).pack()
        tk.Entry(root_window, textvariable=var).pack()

    tk.Button(root_window, text="Add Car Details", command=add_car_details,
              bg="green", fg="white").pack(pady=15)
    tk.Button(root_window, text="Back to Menu", command=lambda: show_menu_screen()).pack(pady=5)

# ----------------------------------------------------------

def open_search_car_form(root_window):
    """Opens the Search Car Details screen"""
    for widget in root_window.winfo_children():
        widget.destroy()

    root_window.title("Search Car Details")
    tk.Label(root_window, text="Search Car Details", font=("Arial", 16, "bold")).pack(pady=10)

    search_var = tk.StringVar()

    tk.Label(root_window, text="Search by Car Name or Brand:").pack()
    tk.Entry(root_window, textvariable=search_var, width=40).pack(pady=5)

    columns = ("Car ID", "Car Name", "Brand", "Model Year", "Fuel Type", "Transmission", "Color")
    tree = ttk.Treeview(root_window, columns=columns, show="headings")
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=100)
    tree.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

    tk.Button(root_window, text="View Selected Car Details", bg="purple", fg="white",
          command=lambda: view_selected_car()).pack(pady=5)

    def view_selected_car():
        selected = tree.selection()
        if not selected:
            messagebox.showwarning("No Selection", "Please select a car from the list.")
            return
        car_data = tree.item(selected[0], 'values')
        car_id = car_data[0]
        open_car_details_screen(car_id)

    def search_car():
        try:
            cur1.execute("SELECT * FROM Car_details WHERE car_name LIKE %s OR brand LIKE %s",
                         (f"%{search_var.get()}%", f"%{search_var.get()}%"))
            results = cur1.fetchall()

            for row in tree.get_children():
                tree.delete(row)
            for row in results:
                tree.insert("", tk.END, values=row)

            if not results:
                messagebox.showinfo("No Results", "No cars found matching your search.")
        except Exception as e:
            messagebox.showerror("Error", f"Error searching cars:\n{e}")

    tk.Button(root_window, text="Search", command=search_car, bg="blue", fg="white").pack(pady=5)
    tk.Button(root_window, text="Back to Menu", command=lambda: show_menu_screen()).pack(pady=5)



# ==========================================================
#   LOGIN / REGISTER / MENU SCREENS
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
    tk.Entry(root, textvariable=username_var).pack(pady=5)
    tk.Label(root, text="Password").pack()
    tk.Entry(root, textvariable=password_var, show="*").pack(pady=5)

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

# --- Start App ---
show_login_screen()
root.mainloop()

from tkinter import filedialog
from PIL import Image, ImageTk  # make sure Pillow is installed: pip install pillow

image_path_var = tk.StringVar()

def select_image():
    file_path = filedialog.askopenfilename(
        title="Select Car Image",
        filetypes=[("Image Files", "*.jpg *.jpeg *.png *.gif")]
    )
    if file_path:
        image_path_var.set(file_path)
        messagebox.showinfo("Image Selected", f"Image chosen:\n{file_path}")

# Add an image selector field
tk.Label(root, text="Car Image").pack()
tk.Button(root, text="Select Image", command=select_image).pack(pady=5)
