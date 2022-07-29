import os
import datetime
import requests
from PIL import Image
from .product import Product
from concurrent.futures import ThreadPoolExecutor, as_completed, wait


class Manager:
    def __init__(self, data_list, root_directory) -> None:
        self.soup = data_list
        self.root_directory = root_directory
        self.product_list: list[Product] = []

    def extract_data(self):
        with ThreadPoolExecutor(10) as executor:
            [
                executor.submit(self.__extract_data, index, item)
                for index, item in enumerate(self.soup, start=1)
            ]

    def __extract_data(self, index, item):
        product = Product(id=index)
        product.date = item.find("div", {"class": "date"}).text.strip()
        product.title = item.find("div", {"class": "title"}).text.strip()
        product.text = item.find("p").text.strip()
        product.image_url = item.find("img", {"class": "lazyload"})["data-src"]
        self.__download_image(product)
        product.image = self.__load_in_image(product)
        product.link = item.find("button", {"class": "btn"})["data-clickout-blank"]
        self.product_list.append(product)
        return product

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
        self.product_list = sorted(
            self.product_list,
            key=lambda product: datetime.datetime.strptime(product.date, "%d.%m.%Y"),
            reverse=True,
        )
        return self.product_list
