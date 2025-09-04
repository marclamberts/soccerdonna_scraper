from setuptools import setup, find_packages

setup(
    name="wsl_scraper",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="Scraper for Kvindeliga 2024-2025 player data from Soccerdonna",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/wsl_scraper",
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
            "wsl-scraper=wsl_scraper.scraper:run_scraper",
        ],
    },
)
