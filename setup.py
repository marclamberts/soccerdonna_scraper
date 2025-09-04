from setuptools import setup, find_packages

setup(
    name="soccerdonna_scraper",
    version="0.1.0",
    author="Marc Lamberts",
    description="Scraper for Soccerdonna leagues",
    packages=find_packages(),
    install_requires=[
        "requests",
        "beautifulsoup4",
        "pandas",
        "openpyxl"
    ],
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "wsl-scraper=soccerdonna_scraper.cli:main",
        ],
    },
)
