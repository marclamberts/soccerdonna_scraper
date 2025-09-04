Soccerdonna Scraper
===================

The ``soccerdonna_scraper`` package provides tools for extracting player and club
data from `Soccerdonna.de <https://www.soccerdonna.de>`_, one of the largest 
databases for women's football.

It can scrape all clubs in a given league, collect detailed player profiles, 
and export the data into an Excel file for analysis.

---

Installation
------------

.. _installation:

You can install the package directly from GitHub:

.. code-block:: bash

   pip install git+https://github.com/marclamberts/soccerdonna_scraper.git

The following dependencies are installed automatically:

- ``requests`` (HTTP requests)
- ``beautifulsoup4`` (HTML parsing)
- ``pandas`` (data handling)
- ``openpyxl`` (Excel export)

Python 3.8 or newer is required.

---

Usage
-----

You can use the scraper either from Python or via the command line interface (CLI).

### Using from Python

.. code-block:: python

   from soccerdonna_scraper import run_scraper

   # Scrape the Women's Super League (ENG1) and save results
   run_scraper("womens-super-league", "ENG1", output_file="WSL_ENG1_players.xlsx")

Parameters:

- ``league_code``: The league slug used in Soccerdonna URLs (e.g., ``womens-super-league``).
- ``comp_code``: The league competition code (e.g., ``ENG1``).
- ``output_file`` (optional): Name of the Excel file to save. Defaults to
  ``{league_code}_{comp_code}_players.xlsx``.

### Using from CLI

After installation, a command-line script ``wsl-scraper`` becomes available:

.. code-block:: bash

   wsl-scraper womens-super-league ENG1 -o WSL_ENG1.xlsx

Arguments:

- ``league_code``: The league slug (e.g., ``kvindeliga``, ``womens-super-league``).
- ``comp_code``: The competition code (e.g., ``3FL``, ``ENG1``).
- ``-o, --output``: Optional Excel file name.

---

Examples
--------

Scraping the **Kvindeliga 2024-25 season**:

.. code-block:: python

   from soccerdonna_scraper import run_scraper
   run_scraper("kvindeliga", "3FL", "Kvindeliga_2024_2025.xlsx")

Scraping the **Women's Super League**:

.. code-block:: bash

   wsl-scraper womens-super-league ENG1 -o WSL_ENG1.xlsx

The output Excel file contains one row per player with fields such as:

- Name
- Club
- Date of birth
- Nationality
- Position
- Height
- Shirt number
- Profile URL
- Additional attributes from the Soccerdonna player page

---

API Reference
-------------

.. autosummary::
   :toctree: generated
   :recursive:

   soccerdonna_scraper

---

Notes
-----

- **Politeness**: The scraper includes a short delay between requests (``time.sleep(0.5)``)
  to reduce server load. Do not remove this if running large scrapes.
- **Stability**: The scraper relies on Soccerdonna’s HTML structure. If the website changes,
  the scraper may need updating.
- **Ethics**: Use this package responsibly and respect the website’s terms of use.

---

Contributing
------------

Contributions are welcome! If you’d like to extend functionality (e.g., support more 
leagues, add data fields, or improve speed), please open a Pull Request on GitHub:

`https://github.com/marclamberts/soccerdonna_scraper <https://github.com/marclamberts/soccerdonna_scraper>`_

