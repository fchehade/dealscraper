import os
from dealscraper import SparweltScraper, Manager
from GUI import Application

if __name__ == "__main__":
    root_directory = os.path.dirname(__file__)
    scraper = SparweltScraper("https://www.sparwelt.de/gratis/cashback")
    manager = Manager(scraper.product_list, root_directory)
    manager.extract_data()
    manager.get_product_list()

    app = Application(manager.get_product_list(), root_directory)
    app.mainloop()
