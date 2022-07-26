import requests
from bs4 import BeautifulSoup
from bs4.element import Tag


class SparweltScraper:
    def __init__(self, url: str) -> None:
        self.url = url
        self.response = self.__make_request()
        self.soup = BeautifulSoup(self.response.text, "html.parser")
        self.product_list = self.__parse_soup()
        if not self.product_list:
            raise BaseException("self.product_list was empty!")

    def __make_request(self) -> requests.Response:
        response = requests.get(self.url)
        response.raise_for_status()
        return response

    def __parse_soup(self):
        section: Tag = self.soup.find("section", {"id": "section-content-stream"})
        return section.find_all("div", {"class": "teaser-content-full"})
