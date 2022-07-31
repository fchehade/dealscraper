import tkinter
from tkinter import ttk
from .product_page import ProductPage
from PIL import ImageTk


class StartPage(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        label = ttk.Label(self, text="Product Overview", font=("Verdana", 16))
        label.pack(side="top", pady=20)

        canvas = tkinter.Canvas(self)
        canvas.pack(side="left", expand=True, fill="both")

        scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        scrollbar.pack(side="right", fill="y")

        scrollable_frame = ttk.Frame(canvas)
        scrollable_frame.bind(
            "<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        for index, product in enumerate(controller.product_list, start=1):
            frame = ttk.Frame(scrollable_frame)
            img = ImageTk.PhotoImage(product.image)
            image_label = ttk.Label(frame, image=img)
            image_label.img = img
            image_label.pack()
            image_label.bind(
                "<Button-1>",
                lambda event, specific_item=product: self.open_product_page(
                    specific_item, controller
                ),
            )

            button = ttk.Button(
                frame,
                text=f"{product.date} - {product.title}",
                width=55,
                command=lambda specific_item=product: self.open_product_page(
                    specific_item, controller
                ),
            )
            button.pack()

            if index % 2 == 0:
                frame.grid(row=index - 1, column=1, padx=15, pady=15)
            else:
                frame.grid(row=index, column=0, padx=15, pady=15)

    def open_product_page(self, product, controller):
        ProductPage(controller, product)
