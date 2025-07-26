
import tkinter as tk
from tkinter import ttk, messagebox

class RestaurantOrderManagement:
    def __init__(self, root):
        self.root = root
        self.root.title("Restaurant Management App")
        
        # Menu items and prices
        self.menu_items = {
            "FRIES MEAL": 2,
            "LUNCH MEAL": 2,
            "BURGER MEAL": 3,
            "PIZZA MEAL": 4,
            "CHEESE BURGER": 2.5,
            "DRINKS": 1
        }

        self.exchange_rate = 82  # INR to USD conversion rate
        self.setup_background()

        # Frame setup
        frame = ttk.Frame(root)
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.entries = {}
        self.menu_labels = {}
        self.menu_quantities = {}
        row = 1
        for item, price in self.menu_items.items():
            # Create menu item labels
            label = ttk.Label(frame, text=f"{item} (${price}):", font=("Arial", 12))
            label.grid(row=row, column=0, padx=10, pady=5, sticky="w")
            self.menu_labels[item] = label

            # Create entry for quantities
            entry = ttk.Entry(frame, width=5)
            entry.insert(0, "0")
            entry.grid(row=row, column=1, padx=10, pady=5)
            self.menu_quantities[item] = entry
            row += 1

        # Currency selection dropdown
        self.currency_var = tk.StringVar()
        currency_label = ttk.Label(frame, text="Currency:", font=("Arial", 12))
        currency_label.grid(row=row, column=0, padx=10, pady=10, sticky="w")

        currency_dropdown = ttk.Combobox(frame, textvariable=self.currency_var, values=["USD", "INR"], state="readonly", width=10)
        currency_dropdown.grid(row=row, column=1, padx=10, pady=10)
        currency_dropdown.current(0)  # Set default to USD
        currency_dropdown.bind("<<ComboboxSelected>>", self.update_menu_prices)
        row += 1

        # Button to place the order
        order_button = ttk.Button(frame, text="Place Order", command=self.place_order)
        order_button.grid(row=row, column=0, columnspan=2, pady=10)

        # Total and background setup
        self.total_label = ttk.Label(frame, text="", font=("Arial", 12, "bold"))
        self.total_label.grid(row=row+1, column=0, columnspan=2, pady=10)

    def setup_background(self):
        # Set the background image
        canvas = tk.Canvas(self.root, width=800, height=600)
        canvas.pack()
        original_image = tk.PhotoImage(file="download.jpeg")
        background_image = original_image.subsample(2, 2)  # Resize the image
        canvas.create_image(0, 0, anchor=tk.NW, image=background_image)
        canvas.image = background_image  # Keep a reference to prevent garbage collection

    def update_menu_prices(self, event=None):
        currency = self.currency_var.get()
        rate = 1 if currency == "USD" else self.exchange_rate
        symbol = "$" if currency == "USD" else "₹"

        # Update menu item prices based on selected currency
        for item, price in self.menu_items.items():
            new_price = price * rate
            self.menu_labels[item].config(text=f"{item} ({symbol}{new_price:.2f}):")

    def place_order(self):
        total_cost = 0
        order_summary = "Order Summary:\n\n"

        currency = self.currency_var.get()
        symbol = "$" if currency == "USD" else "₹"
        rate = 1 if currency == "USD" else self.exchange_rate

        # Loop through menu items and calculate the total cost
        for item, price in self.menu_items.items():
            quantity_str = self.menu_quantities[item].get()

            if not quantity_str.isdigit():
                messagebox.showerror("Input Error", f"Please enter a valid quantity for {item}.")
                return

            quantity = int(quantity_str)
            if quantity > 0:
                item_total = quantity * price * rate
                order_summary += f"{item}: {quantity} x {symbol}{price * rate:.2f} = {symbol}{item_total:.2f}\n"
                total_cost += item_total

        # Display the order summary
        if total_cost > 0:
            order_summary += f"\nTotal: {symbol}{total_cost:.2f}"
            messagebox.showinfo("Order Placed", order_summary)
        else:
            messagebox.showerror("Order Error", "Please order at least one item.")

# Main code to run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = RestaurantOrderManagement(root)
    root.geometry("800x600")
    root.mainloop()