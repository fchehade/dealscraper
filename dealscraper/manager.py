import os
import requests
from PIL import Image
from .product import Product


class Manager:
    def __init__(self, data_list, root_directory) -> None:
        self.soup = data_list
        self.root_directory = root_directory
        self.product_list: list[Product] = []

    def extract_data(self):
        for index, item in enumerate(self.soup, start=1):
            product = Product(id=index)
            product.date = item.find("div", {"class": "date"}).text.strip()
            product.title = item.find("div", {"class": "title"}).text.strip()
            product.text = item.find("p").text.strip()
            product.image_url = item.find("img", {"class": "lazyload"})["data-src"]
            self.__download_image(product)
            product.image = self.__load_in_image(product)
            product.link = item.find("button", {"class": "btn"})["data-clickout-blank"]
            self.product_list.append(product)

    def __download_image(self, product):
        path = os.path.join(self.root_directory, "dealscraper/images")
        response = requests.get(product.image_url)
        img = response.content
        with open(f"{path}/{product.id}.png", "wb") as file_handler:
            file_handler.write(img)

    def __load_in_image(self, product):
        path = os.path.join(self.root_directory, "dealscraper/images")
        img = Image.open(f"{path}/{product.id}.png")
        return img

    def get_product_list(self):
        return self.product_list
