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