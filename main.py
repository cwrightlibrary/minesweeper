import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("minesweeper")
        self.geometry("450x450")
        self.center_window()
        self.focus_force()

        self.buttons = []

        self.create_grid()

    def center_window(self):
        self.update_idletasks()
        width, height = self.winfo_width(), self.winfo_height()
        scr_width, scr_height = self.winfo_screenwidth(), self.winfo_screenheight()
        x, y = (scr_width - width) // 2, (scr_height - height) // 2
        self.geometry(f"{width}x{height}+{x}+{y}")

    def create_grid(self):
        for x in range(0, 450, 50):
            for y in range(0, 450 ,50):
                btn = tk.Frame(self, relief="raised", borderwidth=5, width=50, height=50)
                btn.place(x=x, y=y)
                self.buttons.append(btn)


if __name__ == "__main__":
    app = App()
    app.mainloop()