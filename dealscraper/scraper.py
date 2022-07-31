from typing import Any
import requests
from bs4 import BeautifulSoup, ResultSet
from bs4.element import Tag


class SparweltScraper:
    """SparweltScraper scrapes the www.sparwelt.de/gratis/cashback"""

    def __init__(self, url: str) -> None:
        self.url = url
        self.response = self.__make_request()
        self.soup = BeautifulSoup(self.response.text, "html.parser")
        self.product_list = self.__parse_soup()
        if not self.product_list:
            raise BaseException("self.product_list was empty!")

    def __make_request(self) -> requests.Response:
        """Makes a request to www.sparwelt.de/gratis/cashback and returns
        the Response object.

        Returns:
            requests.Response: Contains data from the requested URL
        """
        response = requests.get(self.url)
        response.raise_for_status()
        return response

    def __parse_soup(self) -> ResultSet[Any]:
        """Parses the relevant section on the page and returns all relevant
        sections as a ResultSet

        Returns:
            ResultSet[Any]: All relevant sections of free products
        """
        section: Tag = self.soup.find("section", {"id": "section-content-stream"})
        return section.find_all("div", {"class": "teaser-content-full"})
