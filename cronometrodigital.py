import tkinter as tk

#### cores ###############

co1 = "#3fb5a3"  # verde
co2 = "#6f9fbd"  # azul
co3 = "#ef5350"   # vermelha


class Stopwatch:
    def __init__(self, root):
        self.root = root
        self.root.title("Cronômetro Digital")

        self.running = False
        self.time = 0

        self.label = tk.Label(root, text=self.format_time(self.time), font=('Helvetica', 70))
        self.label.pack(pady=80)

        self.start_button = tk.Button(root, text="Iniciar", command=self.start, bg = co1)
        self.start_button.pack(side=tk.LEFT, padx=10)

        self.stop_button = tk.Button(root, text="Parar", command=self.stop, bg = co2)
        self.stop_button.pack(side=tk.LEFT, padx=10)

        self.reset_button = tk.Button(root, text="Resetar", command=self.reset, bg = co3)
        self.reset_button.pack(side=tk.LEFT, padx=10)

    def format_time(self, time):
        minutes = time // 600
        seconds = (time // 10) % 60
        tenths = time % 10
        return f"{minutes:02}:{seconds:02}.{tenths}"

    def update_time(self):
        if self.running:
            self.time += 1
            self.label.config(text=self.format_time(self.time))
            self.root.after(100, self.update_time)

    def start(self):
        if not self.running:
            self.running = True
            self.update_time()

    def stop(self):
        if self.running:
            self.running = False

    def reset(self):
        self.running = False
        self.time = 0
        self.label.config(text=self.format_time(self.time))

if __name__ == "__main__":
    root = tk.Tk()
    stopwatch = Stopwatch(root)
    root.mainloop()
