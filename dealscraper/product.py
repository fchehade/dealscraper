from dataclasses import dataclass
import datetime
from tkinter import Image


@dataclass
class Product:
    id: int | None = None
    date: datetime.datetime | None = None
    title: str | None = None
    text: str | None = None
    image_url: str | None = None
    link: str | None = None
    image: Image | None = None
