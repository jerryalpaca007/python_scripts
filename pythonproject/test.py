import tkinter as tk
from tkinter import ttk, messagebox
import csv, os

# ============================================================
#   THEME + BASIC HELPERS (copied here to avoid circular import)
# ============================================================
THEME = {
    "bg_main": "#f5f5f5",
    "banner_bg": "#007acc",
    "fg_text": "#222222",
    "field_bg": "#ffffff",
    "field_fg": "#000000",
    "btn_primary_bg": "#007acc",
    "btn_primary_fg": "white",
    "btn_success_bg": "green",
    "btn_success_fg": "white",
    "btn_neutral_bg": "gray",
    "btn_neutral_fg": "white",
}

def create_banner(parent, text, bg_color=None, fg_color="white", font=("Arial", 16, "bold")):
    """Creates a nice banner section header."""
    bg_color = bg_color or THEME["banner_bg"]
    frame = tk.Frame(parent, bg=bg_color)
    frame.pack(fill="x", pady=(10, 5))
    tk.Label(frame, text=text, bg=bg_color, fg=fg_color, font=font, pady=5).pack(fill="x")
    return frame

def field(parent, label_text, widget_type="entry", options=None, entries=None):
    """Creates a labeled field and stores the widget in entries dict."""
    if entries is None:
        entries = {}  # ✅ ensure it's always a dictionary

    tk.Label(parent, text=label_text, bg=THEME["bg_main"], fg=THEME["fg_text"]).pack(pady=(5, 0))
    if widget_type == "entry":
        entry = tk.Entry(parent, bg=THEME["field_bg"], fg=THEME["field_fg"], width=35)
        entry.pack(pady=3)
        entries[label_text] = entry
    elif widget_type == "dropdown":
        var = tk.StringVar()
        combo = ttk.Combobox(parent, textvariable=var, values=options or [], width=32)
        combo.pack(pady=3)
        entries[label_text] = var
    elif widget_type == "text":
        text_box = tk.Text(parent, width=45, height=4, bg=THEME["field_bg"], fg=THEME["field_fg"])
        text_box.pack(pady=3)
        entries[label_text] = text_box


# ============================================================
#   CSV HELPERS (self-contained)
# ============================================================
def read_csv_file(file_path):
    """Reads a CSV file and returns a list of dict rows."""
    if not os.path.exists(file_path):
        return []
    with open(file_path, "r", newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def update_csv_row(file_path, key_field, key_value, new_data):
    """Updates a row in a CSV file based on key_field."""
    if not os.path.exists(file_path):
        return False
    tmp_path = file_path + ".tmp"
    updated = False
    with open(file_path, "r", newline="", encoding="utf-8") as rf, open(tmp_path, "w", newline="", encoding="utf-8") as wf:
        reader = csv.DictReader(rf)
        fieldnames = reader.fieldnames
        writer = csv.DictWriter(wf, fieldnames=fieldnames)
        writer.writeheader()
        for row in reader:
            if row.get(key_field) == str(key_value):
                row.update(new_data)
                updated = True
            writer.writerow(row)
    if updated:
        os.replace(tmp_path, file_path)
    else:
        os.remove(tmp_path)
    return updated

def append_to_csv(file_path, fieldnames, data):
    """Appends a new row to a CSV file."""
    exists = os.path.exists(file_path)
    with open(file_path, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        if not exists:
            writer.writeheader()
        writer.writerow(data)


# ============================================================
#   CSV FILE LOCATIONS
# ============================================================
CAR_DETAILS_FILE = "car_details.csv"
CAR_STATUS_FILE = "car_status.csv"
CAR_SPEC_FILE = "car_specifications.csv"
CAR_OWNERS_FILE = "car_owners.csv"
CAR_LOCATION_FILE = "car_location.csv"
CAR_CRASH_FILE = "car_crash_info.csv"


# ============================================================
#   MAIN FUNCTION (exported)
# ============================================================
def open_update_car_screen(root, show_menu_callback=None):
    """Standalone update car screen UI."""
    for widget in root.winfo_children():
        widget.destroy()

    root.title("Update Car Details")
    root.geometry("700x650")
    root.configure(bg=THEME["bg_main"])

    create_banner(root, "Update Car Details")

    car_id_var = tk.StringVar()
    tk.Label(root, text="Enter Car ID to Load", bg=THEME["bg_main"], fg=THEME["fg_text"]).pack(pady=5)
    tk.Entry(root, textvariable=car_id_var, width=30, bg=THEME["field_bg"], fg=THEME["field_fg"]).pack(pady=5)
    tk.Button(root, text="Load Car", bg=THEME["btn_primary_bg"], fg=THEME["btn_primary_fg"],
              command=lambda: load_car(car_id_var.get())).pack(pady=5)

    # scrollable frame
    container = tk.Frame(root, bg=THEME["bg_main"])
    container.pack(fill="both", expand=True)
    canvas = tk.Canvas(container, bg=THEME["bg_main"])
    scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
    scroll_frame = tk.Frame(canvas, bg=THEME["bg_main"])
    canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")
    scroll_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    entries = {}

    sections = {
        "Basic Info": ["Car Name", "Brand", "Model Year", "Fuel Type", "Transmission", "Color"],
        "Status & Technical": ["Availability", "Mileage", "Condition", "Engine CC", "Horsepower", "Torque", "Seating Capacity"],
        "Owner Info": ["Owner Name", "Phone", "Address", "Ownership Duration"],
        "Location Info": ["Lot Number", "Storage Facility"],
    }

    for section_name, fields_list in sections.items():
        create_banner(scroll_frame, section_name)
        for field_label in fields_list:
            if field_label == "Fuel Type":
                field(scroll_frame, field_label, "dropdown", ["Petrol", "Diesel", "Electric", "Hybrid"], entries)
            elif field_label == "Transmission":
                field(scroll_frame, field_label, "dropdown", ["Manual", "Automatic"], entries)
            elif field_label == "Condition":
                field(scroll_frame, field_label, "dropdown", ["Excellent", "Good", "Fair", "Poor", "Crashed"], entries)
            else:
                field(scroll_frame, field_label, "entry", entries)

    create_banner(scroll_frame, "Crash Details (if any)")
    field(scroll_frame, "Crash Description", "text", entries)

    def load_car(car_id):
        car_id = car_id.strip()
        if not car_id:
            messagebox.showwarning("Warning", "Please enter a Car ID")
            return

        details = next((c for c in read_csv_file(CAR_DETAILS_FILE) if c["Car ID"] == car_id), None)
        if not details:
            messagebox.showerror("Error", f"No car found with ID {car_id}")
            return

        for f in details:
            if f in entries:
                w = entries[f]
                if isinstance(w, tk.Entry):
                    w.delete(0, tk.END)
                    w.insert(0, details[f])
                elif isinstance(w, tk.StringVar):
                    w.set(details[f])
                elif isinstance(w, tk.Text):
                    w.delete("1.0", tk.END)
                    w.insert(tk.END, details[f])

        messagebox.showinfo("Loaded", f"Car ID {car_id} details loaded successfully.")

    def save_updates():
        car_id = car_id_var.get().strip()
        if not car_id:
            messagebox.showwarning("Warning", "Please enter a Car ID")
            return

        def read_val(w):
            if isinstance(w, tk.Entry): return w.get()
            elif isinstance(w, tk.Text): return w.get("1.0", "end").strip()
            elif isinstance(w, tk.StringVar): return w.get()
            else: return ""

        new_data = {k: read_val(v) for k, v in entries.items()}
        ok = update_csv_row(CAR_DETAILS_FILE, "Car ID", car_id, new_data)
        if ok:
            messagebox.showinfo("Success", f"Car ID {car_id} updated successfully!")
            if show_menu_callback: show_menu_callback()
        else:
            messagebox.showerror("Error", "Failed to update car details.")

    tk.Button(scroll_frame, text="Save Updates", bg=THEME["btn_success_bg"], fg=THEME["btn_success_fg"],
              command=save_updates).pack(pady=10)
    tk.Button(scroll_frame, text="Back to Menu", bg=THEME["btn_neutral_bg"], fg=THEME["btn_neutral_fg"],
              command=show_menu_callback).pack(pady=5)


# ============================================================
#   TEST STANDALONE
# ============================================================
if __name__ == "__main__":
    root = tk.Tk()
    open_update_car_screen(root)
    root.mainloop()
