from tkinter import ttk
from .product_page import ProductPage


class StartPage(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        label = ttk.Label(self, text="Start Page", font=("Verdana", 16))
        label.grid(row=0, column=0, columnspan=2)

        for index, product in enumerate(controller.product_list, start=1):
            button = ttk.Button(
                self,
                text=f"{product.date} - {product.title}",
                width=75,
                command=lambda specific_item=product: self.open_product_page(
                    specific_item, controller
                ),
            )
            if index % 2 == 0:
                button.grid(row=index - 1, column=0, padx=2, pady=2)
            else:
                button.grid(row=index, column=1, padx=2, pady=2)

    def open_product_page(self, product, controller):
        ProductPage(controller, product)
