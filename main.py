import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("minesweeper")
        self.geometry("470x620")

        self.center_window()
        self.focus_force()

        self.grid_rowconfigure((0, 1), weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.header = tk.Frame(self, width=450, height=250, background="red")
        self.header.grid(row=0, column=0, pady=(10, 5))
        self.header.grid_rowconfigure(0, weight=1)
        self.header.grid_columnconfigure((0, 1, 2), weight=1)

        self.game_area = tk.Frame(self, width=450, height=450)
        self.game_area.grid(row=1, column=0, padx=10, pady=(5, 10))

        self.buttons = []
        self.add_buttons()

    def center_window(self):
        self.update_idletasks()
        width, height = self.winfo_width(), self.winfo_height()
        scr_width, scr_height = self.winfo_screenwidth(), self.winfo_screenheight()
        x, y = (scr_width - width) // 2, (scr_height - height) // 2
        self.geometry(f"{width}x{height}+{x}+{y}")
    
    def add_buttons(self):
        for i in range(10):
            for j in range(10):
                btn = tk.Button(self.game_area, text="", relief="raised", width=20, height=3, borderwidth=5)
                btn.grid(row=i, column=j, sticky="nsew")
                self.buttons.append(btn)
        for i in range(10):
            self.game_area.grid_rowconfigure(i, weight=1)
            self.game_area.grid_columnconfigure(i, weight=1)


if __name__ == "__main__":
    app = App()
    app.mainloop()