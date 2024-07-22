import tkinter as tk

calculation = ""

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

def evaluate_calculation():
    global calculation
    try:
        result = str(eval(calculation))
        clear_field()
        text_result.insert(1.0, result)
    except:
        clear_field()
        text_result.insert(1.0, "Error")

def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")

# Create main window
root = tk.Tk()
root.geometry("350x550")
root.configure(bg='black')  # Set background color to black

text_result = tk.Text(root, height=2, width=16, font=("Arial", 24), bg='black', fg='white', bd=0)
text_result.grid(columnspan=4, padx=10, pady=10)

# Button styles
btn_num_style = {'width': 5, 'height': 2, 'font': ("Arial", 18), 'bg': '#333333', 'fg': 'white', 'bd': 0}
btn_op_style = {'width': 5, 'height': 2, 'font': ("Arial", 18), 'bg': 'orange', 'fg': 'white', 'bd': 0}
btn_clear_style = {'width': 5, 'height': 2, 'font': ("Arial", 18), 'bg': '#A5A5A5', 'fg': 'black', 'bd': 0}
btn_op1_style = {'width': 5, 'height': 2, 'font': ("Arial", 18), 'bg': '#A5A5A5', 'fg': 'black', 'bd': 0}

# Number buttons
numbers = [
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2),
    ('0', 5, 1)
]

for (text, row, col) in numbers:
    btn = tk.Button(root, text=text, command=lambda t=text: add_to_calculation(t), **btn_num_style)
    btn.grid(row=row, column=col, padx=5, pady=5)

# Operator buttons
operators = [
    ('C', clear_field, 1, 0, btn_clear_style), ('±', lambda: add_to_calculation('(-'), 1, 1, btn_op1_style), ('%', lambda: add_to_calculation('%'), 1, 2, btn_op1_style), ('÷', lambda: add_to_calculation('/'), 1, 3, btn_op_style),
    ('×', lambda: add_to_calculation('*'), 2, 3, btn_op_style), ('−', lambda: add_to_calculation('-'), 3, 3, btn_op_style), ('+', lambda: add_to_calculation('+'), 4, 3, btn_op_style),
    ('=', evaluate_calculation, 5, 3, btn_op_style), ('.', lambda: add_to_calculation('.'), 5, 2, btn_num_style)
]

for (text, command, row, col, style) in operators:
    btn = tk.Button(root, text=text, command=command, **style)
    btn.grid(row=row, column=col, padx=5, pady=5)

# Special buttons for 0
btn_0 = tk.Button(root, text="0", command=lambda: add_to_calculation('0'), **btn_num_style)
btn_0.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky="we")

root.mainloop()
