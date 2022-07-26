![dealscraper logo](images/logo.png)

![Badges](https://img.shields.io/github/languages/code-size/fchehade/dealscraper) ![Badges](https://img.shields.io/github/license/fchehade/dealscraper)

`dealscraper` is a quick alternative to searching https://www.sparwelt.de/gratis/cashback manually. dealscraper will download all free product offers and displays them sorted by date in a tkinter application.

From here you can select offer that interest you to get more information in a new window. If you like to read more about the product, you can click the `follow link`-Button to open a new browser tab directly to the product.

As this is a site I check regularly for offers and those kind of websites tend to swarm you with information I scraped this website to extract necessary information.

All of this project is a work-in-progress and subject to change.

Constructive criticism and contributions are well appreciated.

**Table of Contents**
---
+ [Key Features](#key-features)
+ [Usage](#usage)
+ [Quick Example Images](#quick-example-images)
+ [Installation Options](#installation-options)
+ [How to contribute](#how-to-contribute)
+ [License](#license)
+ [Donations](#donations)

**Key Features**
---
+ check current free products on https://www.sparwelt.de/gratis/cashback in a single application
+ `dealscraper` helps to unclog all the clutter that you normally receive on a free products page

**Usage**
---

```
After initial loading, simply click on any of the offer that catch your interest.
A new popup-window will open up with further details.
Afterwards, you can choose to follow the product link or close the window to look for other deals.
```

**Quick Example Images**
---
![example start screen](images/example1.png)
![example offer screen](images/example2.png)

Currently only tested on Windows 10.

**Installation Options**
---

1. Clone this repository.
    + `cd ~/your/project/path`
    + `git clone https://github.com/fchehade/dealscraper.git`

2. Change directory `cd` to the dealscraper root directory.
3. Create a virtual environment and install requirements.txt
    + `python3 -m venv .env`
    + `source .env/bin/activate`
    + `pip install requirements.txt`
4. Afterwards, just run `python3 main.py` <i>The run process will take a while to complete due to downloading image data.</i>

**How to Contribute**
---

1. Clone repo and create a new branch: `$ git checkout https://github.com/fchehade/dealscraper -b name_for_new_branch`.
2. Make changes and test
3. Submit Pull Request with comprehensive description of changes

**License**
---
This project is licensed under [MIT](LICENSE)

**Donations**
---

This is free, open-source software. If you'd like to support the development of future projects, or say thanks for this one, feel free to donate.

<a href="https://www.paypal.me/decalift"><img src="https://www.paypalobjects.com/webstatic/de_DE/i/de-pp-logo-200px.png" alt="PayPal Logo"></a>&nbsp; &nbsp; <a href="https://www.buymeacoffee.com/decalift" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/guidelines/download-assets-sm-2.svg" alt="Buy Me A Coffee"/></a>