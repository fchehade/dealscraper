import os


def create_folder(root_directory):
    if not os.path.exists(os.path.join(root_directory, "dealscraper/images")):
        os.makedirs(os.path.join(root_directory, "dealscraper/images"))


def cleanup_folder(root_directory):
    for file in os.listdir(os.path.join(root_directory, "dealscraper/images")):
        os.remove(os.path.join(root_directory, "dealscraper/images", file))
    os.removedirs(os.path.join(root_directory, "dealscraper/images"))
