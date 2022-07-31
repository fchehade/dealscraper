import os


def create_folder(root_directory) -> None:
    """Creates temporary folders where image data is stored for
    running the program properly.

    Args:
        root_directory (str): Root directory of the project as described
        in the main.py file
    """
    if not os.path.exists(os.path.join(root_directory, "dealscraper/images")):
        os.makedirs(os.path.join(root_directory, "dealscraper/images"))


def cleanup_folder(root_directory) -> None:
    """Removes temporary folders where image data was stored after
    closing the program.

    Args:
        root_directory (str): Root directory of the project as described
        in the main.py file
    """
    for file in os.listdir(os.path.join(root_directory, "dealscraper/images")):
        os.remove(os.path.join(root_directory, "dealscraper/images", file))
    os.removedirs(os.path.join(root_directory, "dealscraper/images"))
