import os
from dealscraper import SparweltScraper, Manager, create_folder, cleanup_folder
from GUI import Application

if __name__ == "__main__":
    root_directory = os.path.dirname(__file__)
    create_folder(root_directory)
    scraper = SparweltScraper("https://www.sparwelt.de/gratis/cashback")
    manager = Manager(scraper.product_list, root_directory)
    manager.extract_data()
    product_list = manager.get_product_list()
    app = Application(manager.get_product_list(), root_directory)
    app.mainloop()
    cleanup_folder(root_directory)
