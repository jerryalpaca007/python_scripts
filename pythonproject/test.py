import tkinter as tk
from tkinter import ttk, messagebox
import csv
import os

# === CSV FILE PATHS ===
CAR_DETAILS_FILE = "car_details.csv"
CAR_STATUS_FILE = "car_status.csv"
CAR_SPEC_FILE = "car_specifications.csv"
CAR_OWNERS_FILE = "car_owners.csv"
CAR_LOCATION_FILE = "car_location.csv"

# === OS-BASED CSV UPDATE FUNCTION ===
def update_csv_row(file_path, key_field, key_value, new_data):
    temp_file = file_path + ".tmp"
    updated = False

    with open(file_path, "r", newline="") as f, open(temp_file, "w", newline="") as tmpf:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        writer = csv.DictWriter(tmpf, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            if row[key_field] == str(key_value):
                row.update(new_data)
                updated = True
            writer.writerow(row)

    if updated:
        os.replace(temp_file, file_path)
        return True
    else:
        os.remove(temp_file)
        return False

# === UPDATE CAR SCREEN ===
def open_update_car_screen(root, show_menu_callback):
    root.title("Update Car Details")
    root.geometry("700x650")
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Update Car Details", font=("Arial", 18, "bold"), bg="#4a90e2", fg="white").pack(fill="x")

    car_id_var = tk.StringVar()
    tk.Label(root, text="Enter Car ID to Load").pack(pady=5)
    tk.Entry(root, textvariable=car_id_var).pack(pady=5)
    tk.Button(root, text="Load Car", bg="green", fg="white",
              command=lambda: load_car(car_id_var.get())).pack(pady=5)

    # --- Scrollable Frame ---
    container = tk.Frame(root)
    container.pack(fill="both", expand=True)

    canvas = tk.Canvas(container)
    canvas.pack(side="left", fill="both", expand=True)

    scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")
    canvas.configure(yscrollcommand=scrollbar.set)

    scroll_frame = tk.Frame(canvas, bg="#f5f5f5")
    canvas.create_window((0, 0), window=scroll_frame, anchor="nw")

    def on_frame_configure(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    scroll_frame.bind("<Configure>", on_frame_configure)

    def _on_mousewheel(event):
        canvas.yview_scroll(-1 * int(event.delta / 120), "units")
    canvas.bind_all("<MouseWheel>", _on_mousewheel)

    # --- Fields ---
    entries = {}
    sections = {
        "Basic Info": ["Car Name", "Brand", "Model Year", "Fuel Type", "Transmission", "Color"],
        "Status & Technical": ["Availability", "Mileage", "Condition", "Engine CC", "Horsepower", "Torque", "Seating Capacity"],
        "Owner Info": ["Owner Name", "Phone", "Address", "Ownership Duration"],
        "Location Info": ["Lot Number", "Storage Facility"]
    }

    for section_name, fields in sections.items():
        tk.Label(scroll_frame, text=section_name, font=("Arial", 14, "bold"), bg="#e6f7ff").pack(fill="x", pady=10)
        for f in fields:
            tk.Label(scroll_frame, text=f, bg="#f5f5f5").pack()
            e = tk.Entry(scroll_frame, width=40)
            e.pack(pady=3)
            entries[f] = e

    # --- Load Car Data ---
    def load_car(car_id):
        car_id = car_id.strip()
        if not car_id:
            messagebox.showwarning("Warning", "Please enter a Car ID")
            return

        # Read all CSVs
        details = next((c for c in read_csv(CAR_DETAILS_FILE) if c["Car ID"] == car_id), None)
        status = next((c for c in read_csv(CAR_STATUS_FILE) if c["Car ID"] == car_id), None)
        spec = next((c for c in read_csv(CAR_SPEC_FILE) if c["Car ID"] == car_id), None)
        owner = next((c for c in read_csv(CAR_OWNERS_FILE) if c["Car ID"] == car_id), None)
        loc = next((c for c in read_csv(CAR_LOCATION_FILE) if c["Car ID"] == car_id), None)

        if not details:
            messagebox.showerror("Error", f"No car found with ID {car_id}")
            return

        # Fill entries
        for f in sections["Basic Info"]:
            entries[f].delete(0, tk.END)
            entries[f].insert(0, details.get(f, ""))

        for i, f in enumerate(["Availability", "Mileage", "Condition", "Engine CC", "Horsepower", "Torque", "Seating Capacity"]):
            val = status.get(f) if status and f in status else spec.get(f) if spec and f in spec else ""
            entries[f].delete(0, tk.END)
            entries[f].insert(0, val)

        for f in sections["Owner Info"]:
            entries[f].delete(0, tk.END)
            entries[f].insert(0, owner.get(f, "") if owner else "")

        for f in sections["Location Info"]:
            entries[f].delete(0, tk.END)
            entries[f].insert(0, loc.get(f, "") if loc else "")

    # --- Save Updates ---
    def save_updates():
        car_id = car_id_var.get().strip()
        if not car_id:
            messagebox.showwarning("Warning", "Please enter a Car ID")
            return

        # Prepare updated dictionaries
        updated_details = {f: entries[f].get() for f in sections["Basic Info"]}
        updated_status = {f: entries[f].get() for f in ["Availability", "Mileage", "Condition"]}
        updated_spec = {f: entries[f].get() for f in ["Engine CC", "Horsepower", "Torque", "Seating Capacity"]}
        updated_owner = {f: entries[f].get() for f in sections["Owner Info"]}
        updated_loc = {f: entries[f].get() for f in sections["Location Info"]}

        ok1 = update_csv_row(CAR_DETAILS_FILE, "Car ID", car_id, updated_details)
        ok2 = update_csv_row(CAR_STATUS_FILE, "Car ID", car_id, updated_status)
        ok3 = update_csv_row(CAR_SPEC_FILE, "Car ID", car_id, updated_spec)
        ok4 = update_csv_row(CAR_OWNERS_FILE, "Car ID", car_id, updated_owner)
        ok5 = update_csv_row(CAR_LOCATION_FILE, "Car ID", car_id, updated_loc)

        if all([ok1, ok2, ok3, ok4, ok5]):
            messagebox.showinfo("Success", f"Car ID {car_id} updated successfully!")
        else:
            messagebox.showwarning("Warning", f"Some updates may have failed. Check the CSV files.")

    tk.Button(scroll_frame, text="Save Updates", bg="green", fg="white", width=15, command=save_updates).pack(pady=15)
    tk.Button(scroll_frame, text="Back to Menu", command=show_menu_callback).pack(pady=5)
# --- Helper to read CSV ---
def read_csv(file_path):
    if not os.path.exists(file_path):
        return []
    with open(file_path, "r", newline="") as f:
        reader = csv.DictReader(f)
        return list(reader)

# Dummy menu screen for testing
def show_menu_screen(root):
    for widget in root.winfo_children():
        widget.destroy()
    tk.Label(root, text="Main Menu", font=("Arial", 18)).pack()
    tk.Button(root, text="Update Car", command=lambda: open_update_car_screen(root)).pack()

# --- Run App ---
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("700x650")
    show_menu_screen(root)
    root.mainloop()
