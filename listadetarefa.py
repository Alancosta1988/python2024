import tkinter as tk
from tkinter import messagebox

#### cores ###############

co0 = "#f0f3f5"  # Preta
co1 = "#feffff"  # branca
co2 = "#3fb5a3"  # verde
co3 = "#6f9fbd"  # azul
co4 = "#ef5350"   # vermelha

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tarefas")
        
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=10)
        
        self.task_listbox = tk.Listbox(
            self.frame, 
            width=20,  
            height=10, 
            selectmode=tk.SINGLE
        )

        self.task_listbox = tk.Listbox(
            self.frame, 
            width=70,  
            height=10, 
            selectmode=tk.SINGLE
        )
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

        self.scrollbar = tk.Scrollbar(
            self.frame, 
            orient=tk.VERTICAL, 
            command=self.task_listbox.yview
        )
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.task_listbox.config(yscrollcommand=self.scrollbar.set)

        self.task_entry = tk.Entry(self.root, width=65)
        self.task_entry.pack(pady=10)

        self.add_button = tk.Button(
            self.root, 
            text="Adicionar Tarefa", 
            width=48, 
            bg=co2,
            command=self.add_task
        )
        self.add_button.pack(pady=5)

        self.remove_button = tk.Button(
            self.root, 
            text="Remover Tarefa Selecionada", 
            width=48, 
            bg=co4,
            command=self.remove_task
        )
        self.remove_button.pack(pady=5)

    def add_task(self):
        task = self.task_entry.get()
        if task != "":
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Aviso", "Você precisa digitar uma tarefa.")

    def remove_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected_task_index)
        except IndexError:
            messagebox.showwarning("Aviso", "Você precisa selecionar uma tarefa para remover.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()

