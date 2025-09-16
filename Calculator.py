import tkinter as tk

# Function to add key presses to the entry field
def on_click(key):
    entry.insert(tk.END, key)

# Function to clear the entry field
def on_clear():
    entry.delete(0, tk.END)

# Function to evaluate the expression
def on_equal():
    try:
        # 'eval' function evaluates the string expression
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Main application window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400") # Set the size of the window
root.resizable(False, False) # Make the window non-resizable

# Entry widget to display the calculation
entry = tk.Entry(root, width=15, font=('Arial', 20), borderwidth=2, relief="solid", justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipady=10)

# Define the button layout
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

# Create and place buttons in the window
row_val = 1
col_val = 0
for button in buttons:
    # Special command for the '=' button
    if button == '=':
        btn = tk.Button(root, text=button, padx=20, pady=20, font=('Arial', 14), command=on_equal)
    # Command for all other buttons
    else:
        btn = tk.Button(root, text=button, padx=20, pady=20, font=('Arial', 14), command=lambda b=button: on_click(b))
    
    btn.grid(row=row_val, column=col_val, padx=5, pady=5)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Clear button
clear_btn = tk.Button(root, text='C', padx=20, pady=20, font=('Arial', 14), command=on_clear)
clear_btn.grid(row=row_val, column=0, columnspan=2, padx=5, pady=5, sticky='we')

# Start the application loop
root.mainloop()
