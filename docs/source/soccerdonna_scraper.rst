Soccerdonna Scraper
===================

The ``soccerdonna_scraper`` package scrapes player and club data from 
[Soccerdonna.de](https://www.soccerdonna.de).

Installation
------------

.. _installation:

You can install the package directly from GitHub:

.. code-block:: bash

   pip install git+https://github.com/marclamberts/soccerdonna_scraper.git

Usage
-----

Using from Python:

.. code-block:: python

   from soccerdonna_scraper import run_scraper
   run_scraper("womens-super-league", "ENG1")

Using from CLI:

.. code-block:: bash

   wsl-scraper womens-super-league ENG1 -o WSL_ENG1.xlsx

API Reference
-------------

.. autosummary::
   :toctree: generated
   :recursive:

   soccerdonna_scraper

