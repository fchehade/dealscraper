from dataclasses import dataclass
import datetime
from tkinter import Image


@dataclass
class Product:
    """Product dataclass representing one of the free products from the scraped
    website

    Args:
        id (int): unique number
        date (datetime.datetime): date when the product was published
        to the website
        title (str): title of the product
        text (str): paragraph of the product
        image_url (str): image url for downloading purposes
        link (str): link to the product page
        image (Image): Image object for displaying in the GUI application
    """

    id: int | None = None
    date: datetime.datetime | None = None
    title: str | None = None
    text: str | None = None
    image_url: str | None = None
    link: str | None = None
    image: Image | None = None
