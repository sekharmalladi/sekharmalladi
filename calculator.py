import tkinter as tk

# Function to update the display
def update_display(value):
    current_text = display_var.get()
    if current_text == "0":
        display_var.set(value)
    else:
        display_var.set(current_text + value)

# Function to clear the display
def clear_display():
    display_var.set("0")

# Function to evaluate the expression and display the result
def calculate_result():
    try:
        result = eval(display_var.get())
        display_var.set(result)
    except Exception as e:
        display_var.set("Error")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Variable to hold the display text
display_var = tk.StringVar(value="0")

# Create the display
display = tk.Entry(root, textvariable=display_var, font=("Arial", 24), bd=10, insertwidth=2, width=14, borderwidth=4)
display.grid(row=0, column=0, columnspan=4)


# Create buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    if button == 'C':
        action = clear_display
    elif button == '=':
        action = calculate_result
    else:
        action = lambda x=button: update_display(x)

    tk.Button(root, text=button, padx=20, pady=20, font=("Arial", 18), command=action).grid(row=row_val, column=col_val)
    
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Run the application
root.mainloop()
