import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # Set window properties
        self.withdraw()
        self.title("My App")
        self.iconbitmap("assets/icon.ico")
        self.geometry("400x300")
        self.resizable(False, False)

        # center and up window
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 4) - (height // 2)
        self.geometry(f"{width}x{height}+{x}+{y}")
        self.deiconify()

        # Add widgets
        self.label = ttk.Label(self, text="Hello, World!")
        self.label.pack(pady=20)

        self.button = ttk.Button(self, text="Click me!", command=self.show_message)
        self.button.pack()

        self.menu_bar = tk.Menu(self)
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Exit", command=self.quit)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.config(menu=self.menu_bar)

    def show_message(self):
        messagebox.showinfo("Message", "You clicked the button!")


if __name__ == "__main__":
    app = App()
    app.mainloop()
