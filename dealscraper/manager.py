import os
import datetime
import requests
from PIL import Image
from .product import Product
from concurrent.futures import ThreadPoolExecutor


class Manager:
    """Manager class for handling the data further and scrape the
    essential data out
    """

    def __init__(self, data_list, root_directory) -> None:
        self.soup = data_list
        self.root_directory = root_directory
        self.product_list: list[Product] = []

    def extract_data(self):
        """Threaded approach for faster scraping of image data mainly"""
        with ThreadPoolExecutor(10) as executor:
            [
                executor.submit(self._extract_data, index, item)
                for index, item in enumerate(self.soup, start=1)
            ]

    def _extract_data(self, index, item) -> None:
        """Extracts relevant data and assigns it to self.product_list

        Args:
            index (int): index from the enumerate call for assigning unique IDs to the products
            item (Product): A Product item from the ResultSet.
        """
        product = Product(id=index)
        product.date = item.find("div", {"class": "date"}).text.strip()
        product.title = item.find("div", {"class": "title"}).text.strip()
        product.text = item.find("p").text.strip()
        product.image_url = item.find("img", {"class": "lazyload"})["data-src"]
        self._download_image(product)
        product.image = self._load_in_image(product)
        product.link = item.find("button", {"class": "btn"})["data-clickout-blank"]
        self.product_list.append(product)

    def _download_image(self, product) -> None:
        """Downloads image data and saves it in temporary folder under it's unique ID.

        Args:
            product (Product): A Product item from the ResultSet
        """
        path = os.path.join(self.root_directory, "dealscraper/images")
        response = requests.get(product.image_url)
        img = response.content
        with open(f"{path}/{product.id}.png", "wb") as file_handler:
            file_handler.write(img)

    def _load_in_image(self, product) -> Image:
        """Loads in the stored images as Image objects

        Args:
            product (Product): A Product item from the ResultSet

        Returns:
            Image: Image object
        """
        path = os.path.join(self.root_directory, "dealscraper/images")
        img = Image.open(f"{path}/{product.id}.png")
        return img

    def get_product_list(self) -> list[Product]:
        """Returns the completed product list and sorts it by date (new - old)

        Returns:
            list[Product]: Sorted list of Products by date
        """
        self.product_list = sorted(
            self.product_list,
            key=lambda product: datetime.datetime.strptime(product.date, "%d.%m.%Y"),
            reverse=True,
        )
        return self.product_list
