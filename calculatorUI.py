import tkinter as tk

from tkinter import messagebox

# Function to update the expression in the text entry
def press(num):
    global expression
    expression += str(num)
    equation.set(expression)

# Function to evaluate the final expression
def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except:
        equation.set("Error")
        expression = ""

# Function to clear the text entry
def clear():
    global expression
    expression = ""
    equation.set("")

# Main function
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Simple Calculator")
    root.geometry("400x600")
    root.resizable(0, 0)
    
    expression = ""
    equation = tk.StringVar()
    
    input_frame = tk.Frame(root, width=400, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)
    input_frame.pack(side=tk.TOP)
    
    input_field = tk.Entry(input_frame, font=('arial', 18, 'bold'), textvariable=equation, width=50, bg="#eee", bd=0, justify=tk.RIGHT)
    input_field.grid(row=0, column=0)
    input_field.pack(ipady=10)
    
    btns_frame = tk.Frame(root, width=400, height=450, bg="grey")
    btns_frame.pack()
    
    # First row
    clear = tk.Button(btns_frame, text="C", fg="black", width=32, height=3, bd=0, bg="#eee", cursor="hand2", command=clear).grid(row=0, column=0, columnspan=3)
    divide = tk.Button(btns_frame, text="/", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: press("/")).grid(row=0, column=3)
    
    # Second row
    seven = tk.Button(btns_frame, text="7", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: press(7)).grid(row=1, column=0)
    eight = tk.Button(btns_frame, text="8", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: press(8)).grid(row=1, column=1)
    nine = tk.Button(btns_frame, text="9", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: press(9)).grid(row=1, column=2)
    multiply = tk.Button(btns_frame, text="*", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: press("*")).grid(row=1, column=3)
    
    # Third row
    four = tk.Button(btns_frame, text="4", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: press(4)).grid(row=2, column=0)
    five = tk.Button(btns_frame, text="5", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: press(5)).grid(row=2, column=1)
    six = tk.Button(btns_frame, text="6", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: press(6)).grid(row=2, column=2)
    subtract = tk.Button(btns_frame, text="-", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: press("-")).grid(row=2, column=3)
    
    # Fourth row
    one = tk.Button(btns_frame, text="1", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: press(1)).grid(row=3, column=0)
    two = tk.Button(btns_frame, text="2", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: press(2)).grid(row=3, column=1)
    three = tk.Button(btns_frame, text="3", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: press(3)).grid(row=3, column=2)
    add = tk.Button(btns_frame, text="+", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: press("+")).grid(row=3, column=3)
    
    # Fifth row
    zero = tk.Button(btns_frame, text="0", fg="black", width=21, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: press(0)).grid(row=4, column=0, columnspan=2)
    point = tk.Button(btns_frame, text=".", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: press(".")).grid(row=4, column=2)
    equals = tk.Button(btns_frame, text="=", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=equalpress).grid(row=4, column=3)
    
    root.mainloop()
