import os


def create_folder(root_directory):
    if not os.path.exists(os.path.join(root_directory, "dealscraper/images")):
        os.makedirs(os.path.join(root_directory, "dealscraper/images"))
