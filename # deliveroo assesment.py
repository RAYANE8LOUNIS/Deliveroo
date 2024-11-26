import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime
import json
import os
# from Pillow import image, ImageTk
# File to store orders
ORDERS_FILE = "rayane.order"

def TAke_orders():
    """Load orders from a file, and creating it if it doesn't exist for more help."""
    try:
        if not os.path.exists(ORDERS_FILE):
            with open(ORDERS_FILE, 'w') as file:
                json.dump([], file)  #this should create an empty list if file doesn't exist for more efficasity 
        with open(ORDERS_FILE, 'r') as file:
            return json.load(file)
    except (json.JSONDecodeError, IOError):
        messagebox.showerror("Error", f"Failed to load or initialize {ORDERS_FILE}.")
        return []
    
# create a function to save orders to the file
def savee_orderss():
    try:
        with open(ORDERS_FILE, 'w') as file:
            json.dump(orders, file, indent=4)
    except IOError:
        messagebox.showerror("Error", "Failed to save orders.")
        
 # give a name to the orders list
orders = TAke_orders()        

# parameters to choose and configure the style of my app backround 
STYLE = {
    "bg": "#1e3a5f",
    "fg": "white",
    "font": ("Arial", 12)
}

# create a window wich will be display on the screen
def centerr_windoww(window, width=600, height=400):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")
    

# Bubble sort to sort orders by price as required always when we press the view order button the result will be sorted 
def bubble_sort_orders():
    n = len(orders)
    for i in range(n):
        for j in range(0, n - i - 1):
            if orders[j]['price'] < orders[j + 1]['price']:
                orders[j], orders[j + 1] = orders[j + 1], orders[j] 

# Calculate price if it is national or international or if it is in england the price will be dubble 
def calculate_price(region, is_fast, is_international):
    base_price = 25
    region_prices = {"England": 2, "Scotland": 1.5, "Wales": 1.15, "Northern Ireland": 1} # high taxes in england 
    price = base_price * region_prices.get(region, 1)
    if is_fast:
        price *= 2 
    if is_international:
        price += 50
    return price

 # a function to add an order to the list 
def add_order():
    name = name_entry.get().strip()
    address = address_entry.get().strip()
    item = item_entry.get().strip()
    delivery_person = delivery_person_combobox.get().strip()
    delivery_method = delivery_method_combobox.get().strip()
    region = region_combobox.get().strip()
    is_fast = fast_delivery_var.get()
    is_international = international_delivery_var.get()

    if not (name and address and item and delivery_person and delivery_method and region):
        messagebox.showerror("Error", "All fields are required! Please renter and put all information for batter service ")
        return

    final_price = calculate_price(region, is_fast, is_international)

  # option to open the payment window to valididat the order 
    open_payment_window(final_price, name, address, item, delivery_person, delivery_method, region, is_fast, is_international)

# I have create a function to show and view orders on the app 

def view_orders():
    # all the orders will be sorted and displayed because i had creat before a bubble sort for this perpus 
    bubble_sort_orders()

    orders_text.delete(1.0, tk.END)
    if not orders:
        orders_text.insert(tk.END, "No orders available.\n")
    else:
        for i, order in enumerate(orders):
            status = "Delivered" if order.get("delivered", False) else "Pending"
            orders_text.insert(
                tk.END,
                f"{i + 1}. {order['name']} - {order['address']} - {order['item']} - "
                f"{status} - Price: £{order['price']:.2f}\n"
            )        
   # function to clear input to restrat another order 
def clear_inputs():
    name_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)
    item_entry.delete(0, tk.END)
    delivery_person_combobox.set("")
    delivery_method_combobox.set("")
    region_combobox.set("")
    fast_delivery_var.set(False)
    international_delivery_var.set(False)

 # this is to creat the payment window function
def open_payment_window(price, name, address, item, delivery_person, delivery_method, region, is_fast, is_international):
    """Open a payment window where the user confirms the payment."""
    def confirm_payment(): # function to confirm the payment 
        """Handle the payment confirmation and add the order."""
        payment_method = payment_method_combobox.get().strip()
        card_number = card_number_entry.get().strip()
        card_expiry = card_expiry_entry.get().strip()
        card_cvc = card_cvc_entry.get().strip()   
    
        if not payment_method: # error handaling of payment methode 
            messagebox.showerror("Error", "Please select a payment method!")
            return
    
        
