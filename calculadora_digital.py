import tkinter as tk

# cores
co1 = "#feffff"  # white/branca
co2 = "#38576b"  
co3 ="#ECEFF1"
co4='#FFAB40' # Orange/laranja

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora Digital")

        self.expression = ""

        self.display = tk.Entry(root, font=('Helvetica', 30), bd=60, insertwidth=6, width=14, borderwidth=30)
        self.display.grid(row=0, column=0, columnspan=10)

        self.create_buttons()

    def create_buttons(self):
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
            ('C', 5, 0)
        ]

        for (text, row, col) in buttons:
            self.create_button(text, row, col)

    def create_button(self, text, row, col):
        button = tk.Button(self.root, text=text, padx=20, pady=20, font=('Helvetica', 20), command=lambda: self.on_button_click(text))
        button.grid(row=row, column=col, sticky='nsew')

    def on_button_click(self, char):
        if char == 'C':
            self.expression = ""
        elif char == '=':
            try:
                self.expression = str(eval(self.expression))
            except Exception as e:
                self.expression = "Erro"
        else:
            self.expression += str(char)
        self.update_display()

    def update_display(self):
        self.display.delete(0, tk.END)
        self.display.insert(0, self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)

    for i in range(6):
        root.grid_rowconfigure(i, weight=1)
        root.grid_columnconfigure(i, weight=1)

    root.mainloop()
