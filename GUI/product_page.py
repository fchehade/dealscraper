import webbrowser
import tkinter
from platform import system
from tkinter import ttk
from PIL import ImageTk


class ProductPage(tkinter.Toplevel):
    def __init__(self, controller, product):
        super().__init__(controller)
        platformD = system()
        if platformD == "Windows":
            self.iconbitmap(f"{controller.root_directory}/images/cashback.ico")
        elif platformD == "Darwin":
            self.iconbitmap(f"{controller.root_directory}/images/cashback.icns")
        container = ttk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        title = ttk.Label(
            container, text=f"{product.date} - {product.title}", font=("Verdana", 13)
        )
        title.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        img = ImageTk.PhotoImage(product.image)
        image_label = ttk.Label(container, image=img)
        image_label.img = img
        image_label.grid(row=1, column=0, columnspan=4, padx=5, pady=5)

        text = ttk.Label(
            container, text=product.text, wraplength=700, font=("Verdana", 10)
        )
        text.grid(row=3, column=0, padx=5, columnspan=4, pady=5)

        button = ttk.Button(
            container, text="Follow link", command=lambda: webbrowser.open(product.link)
        )
        button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)
        exit_button = ttk.Button(
            container, text="Close Subwindow", command=self.destroy
        )
        exit_button.grid(row=4, column=2, columnspan=2, padx=5, pady=5)
