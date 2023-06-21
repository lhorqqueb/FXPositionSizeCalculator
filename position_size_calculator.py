import tkinter as tk
from tkinter import messagebox
import requests

def get_real_time_price(pair):
    API_KEY = 'HEIVEVFYZE00KBMX'
    BASE_URL = f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={pair[:3]}&to_currency={pair[4:]}&apikey={API_KEY}'

    response = requests.get(BASE_URL)
    data = response.json()

    exchange_rate = data["Realtime Currency Exchange Rate"]["5. Exchange Rate"]
    return float(exchange_rate)

def calculate_position_size():
    # Extract the input values
    try:
        balance = float(balance_entry.get())
        risk_percent = float(risk_entry.get()) / 100  # get as a decimal
        stop_loss_pips = float(stop_loss_entry.get())
        pair = pair_entry.get()
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers")
        return

    # Get the real time price data
    real_time_price = get_real_time_price(pair)

    # Calculate risk amount in money
    risk_amount = risk_percent * balance

    # Calculate pip value
    pip_value = (0.0001 / real_time_price)

    # Calculate position size
    position_size = risk_amount / (stop_loss_pips * pip_value)

    # Display the results
    risk_label.config(text=f"Amount at Risk: {risk_amount} USD")
    position_label.config(text=f"Position Size (units): {position_size}")
    standard_lots_label.config(text=f"Standard Lots: {position_size / 100000}")
    mini_lots_label.config(text=f"Mini Lots: {position_size / 10000}")
    micro_lots_label.config(text=f"Micro Lots: {position_size / 1000}")

# Create the main window
window = tk.Tk()
window.title("Position Size Calculator")

# Create the input fields
balance_entry = tk.Entry(window)
balance_entry.grid(row=0, column=1)
tk.Label(window, text="Account Balance:").grid(row=0)

risk_entry = tk.Entry(window)
risk_entry.grid(row=1, column=1)
tk.Label(window, text="Risk Percentage:").grid(row=1)

stop_loss_entry = tk.Entry(window)
stop_loss_entry.grid(row=2, column=1)
tk.Label(window, text="Stop Loss Pips:").grid(row=2)

pair_entry = tk.Entry(window)
pair_entry.grid(row=3, column=1)
tk.Label(window, text="Currency Pair:").grid(row=3)

# Create the calculate button
calculate_button = tk.Button(window, text="Calculate", command=calculate_position_size)
calculate_button.grid(row=4, column=0, columnspan=2)

# Create the result labels
risk_label = tk.Label(window, text="Amount at Risk: ")
risk_label.grid(row=5, column=0, columnspan=2)

position_label = tk.Label(window, text="Position Size (units): ")
position_label.grid(row=6, column=0, columnspan=2)

standard_lots_label = tk.Label(window, text="Standard Lots: ")
standard_lots_label.grid(row=7, column=0, columnspan=2)

mini_lots_label = tk.Label(window, text="Mini Lots: ")
mini_lots_label.grid(row=8, column=0, columnspan=2)

micro_lots_label = tk.Label(window, text="Micro Lots: ")
micro_lots_label.grid(row=9, column=0, columnspan=2)

# Run the GUI
window.mainloop()
