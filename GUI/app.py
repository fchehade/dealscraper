import tkinter
from platform import system
from tkinter import ttk
from .start_page import StartPage


class Application(tkinter.Tk):
    def __init__(self, product_list, root_directory):
        super().__init__()
        self.configure(background="white")
        self.geometry("1100x1000")
        self.product_list = product_list
        self.root_directory = root_directory

        self.title("Cashback - GUI")
        platformD = system()
        if platformD == "Windows":
            self.iconbitmap(f"{self.root_directory}/images/cashback.ico")
        elif platformD == "Darwin":
            self.iconbitmap(f"{self.root_directory}/images/cashback.icns")

        container = ttk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        frame = StartPage(container, self)
        frame.grid(row=0, column=0, sticky="nsew")
        self.frames[StartPage] = frame

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
