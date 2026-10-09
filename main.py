import tkinter as tk
from tkinter import messagebox

# Function to validate and save PIN
def set_pin():
    pin = entry_pin.get()
    confirm_pin = entry_confirm.get()

    # Validation: Check if PIN is numeric and exactly 4 digits
    if not pin.isdigit() or len(pin) != 4:
        messagebox.showerror("Invalid PIN", "PIN must be exactly 4 digits and numeric.")
        return

    # Check if confirmation matches
    if pin != confirm_pin:
        messagebox.showerror("Mismatch", "PIN and Confirm PIN do not match.")
        return

    # Save PIN securely (for demo, just print — in real apps, encrypt & store securely)
    messagebox.showinfo("Success", "Your ATM PIN has been set successfully!")
    print(f"PIN set to: {pin}")  # For debugging/demo only
    root.destroy()  # Close window after setting PIN

# Create main window
root = tk.Tk()
root.title("ATM PIN Setup")
root.geometry("300x200")
root.resizable(False, False)

# Labels and Entry fields
label_title = tk.Label(root, text="Set Your ATM PIN", font=("Arial", 14, "bold"))
label_title.pack(pady=10)

label_pin = tk.Label(root, text="Enter New PIN:")
label_pin.pack()
entry_pin = tk.Entry(root, show="*", font=("Arial", 12), justify="center")
entry_pin.pack(pady=5)

label_confirm = tk.Label(root, text="Confirm PIN:")
label_confirm.pack()
entry_confirm = tk.Entry(root, show="*", font=("Arial", 12), justify="center")
entry_confirm.pack(pady=5)

# Submit button
btn_set = tk.Button(root, text="Set PIN", command=set_pin, bg="green", fg="white", font=("Arial", 12))
btn_set.pack(pady=15)

# Run the Tkinter event loop
root.mainloop()