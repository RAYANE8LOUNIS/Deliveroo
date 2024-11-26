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
def center_window(window, width=600, height=400):
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