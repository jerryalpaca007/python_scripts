# ==========================================================
#   CAR DEALERSHIP / ACCIDENT REPORT SYSTEM (CSV VERSION)
# ==========================================================

import tkinter as tk
from tkinter import ttk, messagebox
import csv, os

# ==========================================================
#   FILE PATHS
# ==========================================================
CAR_DETAILS_FILE = "car_details.csv"
CAR_STATUS_FILE = "car_status.csv"
CAR_SPEC_FILE = "car_specifications.csv"
LOGIN_FILE = "login_data.csv"
CAR_OWNERS_FILE = "car_owners.csv"
CAR_LOCATION_FILE = "car_location.csv"

# ==========================================================
#   DEFAULT DATA
# ==========================================================
car_data = [
    [1, 'Civic', 'Honda', 2020, 'Petrol', 'Automatic', 'White'],
    [2, 'Model 3', 'Tesla', 2022, 'Electric', 'Automatic', 'Red'],
    [3, 'Corolla', 'Toyota', 2019, 'Diesel', 'Manual', 'Silver']
]

car_status_data = [
    [1, 'Available', 22000, 'Excellent'],
    [2, 'Sold', 10000, 'New'],
    [3, 'Available', 35000, 'Good']
]

car_specification_data = [
    [1, 1800, 140, 174, 5],
    [2, 0, 283, 350, 5],
    [3, 1600, 120, 150, 5]
]

car_owners_data = [
    [1, "John Doe", "9876543210", "New York", "2 years"],
    [1, "Jane Smith", "9123456789", "California", "1 year"],
    [2, "Michael Lee", "9998887777", "Texas", "3 years"]
]

car_location_data = [
    [1, "Lot A - Section 2", "New York Storage Facility"],
    [2, "Lot B - Section 1", "California Storage Facility"],
    [3, "Lot C - Section 4", "Houston Warehouse"]
]

# ==========================================================
#   CSV HELPERS
# ==========================================================
def create_csv_file(file_path, headers, data):
    if not os.path.exists(file_path):
        with open(file_path, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(headers)
            writer.writerows(data)

def read_csv_file(file_path):
    if not os.path.exists(file_path):
        return []
    with open(file_path, "r", newline="") as f:
        reader = csv.DictReader(f)
        return list(reader)

def append_to_csv(file_path, headers, row):
    file_exists = os.path.exists(file_path)
    with open(file_path, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        if not file_exists:
            writer.writeheader()
        writer.writerow(row)

# ==========================================================
#   INITIAL SETUP
# ==========================================================
def initialize_csvs():
    create_csv_file(CAR_DETAILS_FILE,
        ["Car ID", "Car Name", "Brand", "Model Year", "Fuel Type", "Transmission", "Color"],
        car_data)
    create_csv_file(CAR_STATUS_FILE,
        ["Car ID", "Availability", "Mileage", "Condition"],
        car_status_data)
    create_csv_file(CAR_SPEC_FILE,
        ["Car ID", "Engine CC", "Horsepower", "Torque", "Seating Capacity"],
        car_specification_data)
    create_csv_file(LOGIN_FILE,
        ["Username", "Password"],
        [["admin", "1234"]])
    create_csv_file(CAR_OWNERS_FILE,
        ["Car ID", "Owner Name", "Phone", "Address", "Ownership Duration"],
        car_owners_data)
    create_csv_file(CAR_LOCATION_FILE,
        ["Car ID", "Lot Number", "Storage Facility"],
        car_location_data)


def start_app():
    if not os.path.exists(CAR_DETAILS_FILE):
        if messagebox.askyesno("Add Default Data?", "Do you want to add default car details?"):
            initialize_csvs()
    show_login_screen()

# ==========================================================
#   MAIN WINDOW
# ==========================================================
root = tk.Tk()
root.geometry("700x650")

def clear_root():
    for widget in root.winfo_children():
        widget.destroy()

# ==========================================================
#   LOGIN SCREEN
# ==========================================================
def show_login_screen():
    clear_root()
    root.title("Login")

    tk.Label(root, text="Car Dealership Login", font=("Arial", 18, "bold")).pack(pady=20)
    username = tk.StringVar()
    password = tk.StringVar()

    tk.Label(root, text="Username").pack()
    tk.Entry(root, textvariable=username).pack(pady=5)
    tk.Label(root, text="Password").pack()
    tk.Entry(root, textvariable=password, show="*").pack(pady=5)

    def login():
        users = read_csv_file(LOGIN_FILE)
        for user in users:
            if user["Username"] == username.get() and user["Password"] == password.get():
                messagebox.showinfo("Login Successful", f"Welcome, {username.get()}!")
                show_menu_screen()
                return
        messagebox.showerror("Error", "Invalid username or password.")

    def open_register_screen():
        clear_root()
        root.title("Register")

        tk.Label(root, text="Register New User", font=("Arial", 18, "bold")).pack(pady=20)
        new_user = tk.StringVar()
        new_pass = tk.StringVar()

        tk.Label(root, text="New Username").pack()
        tk.Entry(root, textvariable=new_user).pack(pady=5)
        tk.Label(root, text="New Password").pack()
        tk.Entry(root, textvariable=new_pass, show="*").pack(pady=5)

        def register_user():
            if not new_user.get() or not new_pass.get():
                messagebox.showwarning("Warning", "Please fill all fields.")
                return
            users = read_csv_file(LOGIN_FILE)
            for u in users:
                if u["Username"] == new_user.get():
                    messagebox.showerror("Error", "Username already exists.")
                    return
            append_to_csv(LOGIN_FILE, ["Username", "Password"],
                          {"Username": new_user.get(), "Password": new_pass.get()})
            messagebox.showinfo("Success", "User registered successfully!")
            show_login_screen()

        tk.Button(root, text="Register", bg="green", fg="white", width=15, command=register_user).pack(pady=10)
        tk.Button(root, text="Back", command=show_login_screen).pack()

    tk.Button(root, text="Login", bg="green", fg="white", width=15, command=login).pack(pady=10)
    tk.Button(root, text="Register", bg="blue", fg="white", width=15, command=open_register_screen).pack(pady=5)

# ==========================================================
#   MENU SCREEN
# ========================================================== 
def show_menu_screen():
    clear_root()
    root.title("Main Menu")

    tk.Label(root, text="Car Dealership System", font=("Arial", 20, "bold")).pack(pady=20)
    tk.Button(root, text="Search Cars", bg="blue", fg="white", width=20, height=2,
          command=lambda: open_search_car_form(root)).pack(pady=10)
    tk.Button(root, text="Add New Car", bg="green", fg="white", width=20, height=2,
              command=open_add_car_screen).pack(pady=10)
    tk.Button(root, text="Logout", bg="red", fg="white", width=20, height=2,
              command=show_login_screen).pack(pady=10)

# ==========================================================
#   ADD CAR SCREEN (with sections)
# ==========================================================
def open_add_car_screen():
    clear_root()
    root.title("Add Car Details")

    canvas = tk.Canvas(root)
    scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scroll_frame = tk.Frame(canvas)

    scroll_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    entries = {}

    def section(title):
        lbl = tk.Label(scroll_frame, text=title, font=("Arial", 14, "bold"), bg="#e6f7ff")
        lbl.pack(fill="x", pady=10)

    def field(label):
        tk.Label(scroll_frame, text=label).pack()
        e = tk.Entry(scroll_frame, width=40)
        e.pack(pady=3)
        entries[label] = e

    # Section 1: Basic Car Info
    section("1️⃣  Basic Car Information")
    for f in ["Car ID", "Car Name", "Brand", "Model Year", "Fuel Type", "Transmission", "Color"]:
        field(f)

    # Section 2: Status & Technical
    section("2️⃣  Status & Technical Details")
    for f in ["Availability", "Mileage", "Condition", "Engine CC", "Horsepower", "Torque", "Seating Capacity"]:
        field(f)

    # Section 3: Previous Owner Details
    section("3️⃣  Previous Owner Details")
    for f in ["Owner Name", "Phone", "Address", "Ownership Duration"]:
        field(f)

    # Section 4: Location Details
    section("4️⃣  Car Storage / Location Information")
    for f in ["Lot Number", "Storage Facility"]:
        field(f)

    def save_car():
        try:
            car_id = int(entries["Car ID"].get())
        except ValueError:
            messagebox.showerror("Error", "Car ID must be numeric.")
            return

        all_cars = read_csv_file(CAR_DETAILS_FILE)
        for car in all_cars:
            if int(car["Car ID"]) == car_id:
                messagebox.showwarning("Warning", "Car ID already exists.")
                return

        append_to_csv(CAR_DETAILS_FILE,
            ["Car ID", "Car Name", "Brand", "Model Year", "Fuel Type", "Transmission", "Color"],
            {k: entries[k].get() for k in ["Car ID", "Car Name", "Brand", "Model Year", "Fuel Type", "Transmission", "Color"]})

        append_to_csv(CAR_STATUS_FILE,
            ["Car ID", "Availability", "Mileage", "Condition"],
            {k: entries[k].get() for k in ["Car ID", "Availability", "Mileage", "Condition"]})

        append_to_csv(CAR_SPEC_FILE,
            ["Car ID", "Engine CC", "Horsepower", "Torque", "Seating Capacity"],
            {k: entries[k].get() for k in ["Car ID", "Engine CC", "Horsepower", "Torque", "Seating Capacity"]})

        append_to_csv(CAR_OWNERS_FILE,
            ["Car ID", "Owner Name", "Phone", "Address", "Ownership Duration"],
            {k: entries[k].get() for k in ["Car ID", "Owner Name", "Phone", "Address", "Ownership Duration"]})

        append_to_csv(CAR_LOCATION_FILE,
            ["Car ID", "Lot Number", "Storage Facility"],
            {k: entries[k].get() for k in ["Car ID", "Lot Number", "Storage Facility"]})

        messagebox.showinfo("Success", "Car and owner details saved successfully!")
        show_menu_screen()

    tk.Button(scroll_frame, text="Save Car", bg="green", fg="white", width=15, command=save_car).pack(pady=15)
    tk.Button(scroll_frame, text="Back to Menu", command=show_menu_screen).pack(pady=5)

# ==========================================================
#   SEARCH + CAR DETAILS POPUP (with location)
# ==========================================================
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

    # --- Function to load all cars ---
    def load_all_cars():
        tree.delete(*tree.get_children())
        cars = read_csv_file(CAR_DETAILS_FILE)
        for car in cars:
            tree.insert("", tk.END, values=(
                car["Car ID"], car["Car Name"], car["Brand"], car["Model Year"],
                car["Fuel Type"], car["Transmission"], car["Color"]
            ))

    # --- Function to perform filtered search ---
    def perform_search(event=None):
        query_text = search_var.get().strip().lower()
        tree.delete(*tree.get_children())

        if len(query_text) >= 3:
            cars = read_csv_file(CAR_DETAILS_FILE)
            results = [
                car for car in cars
                if query_text in car["Car Name"].lower() or query_text in car["Brand"].lower()
            ]
            if results:
                for car in results:
                    tree.insert("", tk.END, values=(
                        car["Car ID"], car["Car Name"], car["Brand"], car["Model Year"],
                        car["Fuel Type"], car["Transmission"], car["Color"]
                    ))
            else:
                tree.insert("", tk.END, values=("No cars found", "", "", "", "", "", ""))
        elif query_text == "":
            load_all_cars()  # reload all when cleared

    search_entry.bind("<KeyRelease>", perform_search)

    def view_selected_car():
        selected = tree.selection()
        if not selected:
            messagebox.showwarning("No Selection", "Please select a car from the list.")
            return
        car_data = tree.item(selected[0], 'values')
        open_car_details_popup(car_data[0])

    tk.Button(root_window, text="View Selected Car", bg="orange", fg="white", command=view_selected_car).pack(pady=5)
    tk.Button(root_window, text="Back to Menu", command=show_menu_screen).pack(pady=5)

    # ✅ Automatically load all cars when screen opens
    load_all_cars()

# ==========================================================
#   CAR DETAILS POPUP
# ==========================================================
def open_car_details_popup(car_id):
    car_id = str(car_id)
    win = tk.Toplevel(root)
    win.title("Car Details")
    win.geometry("500x600")

    details = next((c for c in read_csv_file(CAR_DETAILS_FILE) if c["Car ID"] == car_id), None)
    status = next((s for s in read_csv_file(CAR_STATUS_FILE) if s["Car ID"] == car_id), None)
    spec = next((sp for sp in read_csv_file(CAR_SPEC_FILE) if sp["Car ID"] == car_id), None)
    owner = [o for o in read_csv_file(CAR_OWNERS_FILE) if o["Car ID"] == car_id]
    loc = next((l for l in read_csv_file(CAR_LOCATION_FILE) if l["Car ID"] == car_id), None)

    if not details:
        tk.Label(win, text="Car not found.").pack()
        return

    tk.Label(win, text=f"{details['Car Name']} ({details['Brand']})", font=("Arial", 16, "bold")).pack(pady=10)
    tk.Label(win, text=f"Year: {details['Model Year']}\nFuel: {details['Fuel Type']}\nTransmission: {details['Transmission']}\nColor: {details['Color']}", justify="left").pack(pady=5)

    if status:
        tk.Label(win, text=f"\nStatus:\nAvailability: {status['Availability']}\nMileage: {status['Mileage']} km\nCondition: {status['Condition']}", justify="left").pack(pady=5)

    if spec:
        tk.Label(win, text=f"\nSpecifications:\nEngine CC: {spec['Engine CC']}\nHorsepower: {spec['Horsepower']}\nTorque: {spec['Torque']}\nSeating: {spec['Seating Capacity']}", justify="left").pack(pady=5)

    def show_owner_details():
        owner_win = tk.Toplevel(win)
        owner_win.title("Previous Owners")
        owner_win.geometry("480x250")

        if not owner:
            tk.Label(owner_win, text="No previous owners found.", font=("Arial", 12)).pack(pady=20)
            return

        cols = ["Owner Name", "Phone", "Address", "Ownership Duration"]
        tree = ttk.Treeview(owner_win, columns=cols, show="headings", height=8)
        for col in cols:
            tree.heading(col, text=col)
            tree.column(col, width=110)
        for o in owner:
            tree.insert("", tk.END, values=[o[c] for c in cols])
        tree.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

    def show_location():
        loc_win = tk.Toplevel(win)
        loc_win.title("Car Location")
        loc_win.geometry("400x200")

        if not loc:
            tk.Label(loc_win, text="Location details not found.").pack(pady=20)
        else:
            tk.Label(loc_win, text=f"Lot: {loc['Lot Number']}\nStorage Facility: {loc['Storage Facility']}", font=("Arial", 12), justify="left").pack(pady=30)

    tk.Button(win, text="View Previous Owners", bg="blue", fg="white", command=show_owner_details).pack(pady=10)
    tk.Button(win, text="View Car Location", bg="purple", fg="white", command=show_location).pack(pady=5)

# ==========================================================
#   APP START
# ==========================================================

start_app()
root.mainloop()
