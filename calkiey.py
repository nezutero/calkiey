from tkinter import *
import math
import numpy as np

def create_button(root, params, text, command, row, column, sticky="nsew"):
    button = Button(root, params, text=text, command=command)
    button.grid(row=row, column=column, sticky=sticky)
    return button

def button_click(char):
    calc_operator.set(calc_operator.get() + str(char))

def button_clear_all():
    calc_operator.set("")
    result_var.set("")

def button_delete():
    calc_operator.set(calc_operator.get()[:-1])

def factorial(n):
    return 1 if n == 0 or n == 1 else n * factorial(n - 1)

def fact_func():
    result = str(factorial(int(calc_operator.get())))
    calc_operator.set(result)
    result_var.set(result)

def perform_operation(operation):
    try:
        temp = str(eval(calc_operator.get()))
        calc_operator.set(temp)
        result_var.set(temp)
    except Exception:
        calc_operator.set("ERROR")
        result_var.set("ERROR")

def square_root():
    if int(calc_operator.get()) >= 0:
        temp = str(eval(calc_operator.get() + '**(1/2)'))
        calc_operator.set(temp)
    else:
        temp = "ERROR"
    result_var.set(temp)

def percent():
    temp = str(eval(calc_operator.get() + '/100'))
    calc_operator.set(temp)
    result_var.set(temp)

def log_base(log_func):
    try:
        temp = str(log_func(int(calc_operator.get())))
        calc_operator.set(temp)
    except ValueError:
        temp = "ERROR"
    result_var.set(temp)

def button_equal():
    perform_operation(eval)

tk_calc = Tk()
tk_calc.configure(bg="#000000", bd=1)
tk_calc.title("CALKIEY")

calc_operator = StringVar()
text_input = Entry(
    tk_calc,
    font=('sans-serif', 20, 'bold'),
    textvariable=calc_operator,
    bd=1,
    fg='#fff',
    insertwidth=10,
    bg='#E26EE5',
    justify='right'
)
text_input.grid(columnspan=4, row=0)

result_var = StringVar()
result_display = Entry(
    tk_calc,
    font=('sans-serif', 20, 'bold'),
    textvariable=result_var,
    bd=1,
    fg='#fff',
    insertwidth=10,
    bg='#E26EE5',
    justify='right'
)
result_display.grid(columnspan=4, row=1)

button_params = {
    'bd': 1,
    'fg': '#fff',
    'bg': '#F7418F',
    'font': ('sans-serif', 20, 'bold')
}

button_params_main = {
    'bd': 1,
    'fg': '#fff',
    'bg': '#FF9BD2',
    'font': ('sans-serif', 20, 'bold')
}

#--1st row--
modulo = create_button(tk_calc, button_params, 'mod', lambda: button_click('%'), 1, 0, "nsew")
int_div = create_button(tk_calc, button_params, 'div', lambda: button_click('//'), 1, 1, "nsew")
factorial_button = create_button(tk_calc, button_params, 'x!', fact_func, 1, 2, "nsew")
second_power = create_button(tk_calc, button_params, 'x\u00B2', lambda: button_click('**2'), 1, 3, "nsew")

#--2nd row--
third_power = create_button(tk_calc, button_params, 'x\u00B3', lambda: button_click('**3'), 2, 0, "nsew")
nth_power = create_button(tk_calc, button_params, 'x^n', lambda: button_click('**'), 2, 1, "nsew")
inv_power = create_button(tk_calc, button_params, 'x\u207b\xb9', lambda: button_click('**(-1)'), 2, 2, "nsew")
tens_powers = create_button(tk_calc, button_params, '10^x', lambda: button_click('10**'), 2, 3, "nsew")

#--3rd row--
square_root_button = create_button(tk_calc, button_params, '\u00B2\u221A', square_root, 3, 0, "nsew")
nth_root_button = create_button(tk_calc, button_params, '\u221A', lambda: button_click('**(1/'), 3, 1, "nsew")
log_base10_button = create_button(tk_calc, button_params, 'log\u2081\u2080', lambda: button_click('log('), 3, 2, "nsew")
log_basee_button = create_button(tk_calc, button_params, 'ln', lambda: button_click('ln('), 3, 3, "nsew")

#--4th row--
left_par_button = create_button(tk_calc, button_params, '(', lambda: button_click('('), 4, 0, "nsew")
right_par_button = create_button(tk_calc, button_params, ')', lambda: button_click(')'), 4, 1, "nsew")
percentage_button = create_button(tk_calc, button_params, '%', percent, 4, 2, "nsew")
delete_all_button = create_button(tk_calc, button_params, 'AC', button_clear_all, 4, 3, "nsew")

#--5th row--
button_7 = create_button(tk_calc, button_params_main, '7', lambda: button_click('7'), 5, 0, "nsew")
button_8 = create_button(tk_calc, button_params_main, '8', lambda: button_click('8'), 5, 1, "nsew")
button_9 = create_button(tk_calc, button_params_main, '9', lambda: button_click('9'), 5, 2, "nsew")
delete_one_button = create_button(tk_calc, button_params_main, 'DEL', button_delete, 5, 3, "nsew")

#--6th row--
button_4 = create_button(tk_calc, button_params_main, '4', lambda: button_click('4'), 6, 0, "nsew")
button_5 = create_button(tk_calc, button_params_main, '5', lambda: button_click('5'), 6, 1, "nsew")
button_6 = create_button(tk_calc, button_params_main, '6', lambda: button_click('6'), 6, 2, "nsew")
mul_button = create_button(tk_calc, button_params_main, '*', lambda: button_click('*'), 6, 3, "nsew")

#--7th row--
button_1 = create_button(tk_calc, button_params_main, '1', lambda: button_click('1'), 7, 0, "nsew")
button_2 = create_button(tk_calc, button_params_main, '2', lambda: button_click('2'), 7, 1, "nsew")
button_3 = create_button(tk_calc, button_params_main, '3', lambda: button_click('3'), 7, 2, "nsew")
add_button = create_button(tk_calc, button_params_main, '+', lambda: button_click('+'), 7, 3, "nsew")

#--8th row--
button_0 = create_button(tk_calc, button_params_main, '0', lambda: button_click('0'), 8, 0, "nsew")
point_button = create_button(tk_calc, button_params_main, '.', lambda: button_click('.'), 8, 1, "nsew")
equal_button = create_button(tk_calc, button_params_main, '=', button_equal, 8, 2, "nsew")
sub_button = create_button(tk_calc, button_params_main, '-', lambda: button_click('-'), 8, 3, "nsew")

tk_calc.mainloop()
