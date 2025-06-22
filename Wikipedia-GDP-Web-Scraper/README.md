# Wikipedia GDP Web Scraper

This project is a Python script that scrapes the latest nominal GDP data by country from Wikipedia, cleans and processes the data, and exports it to a CSV file for easy analysis.

## Features

- Fetches the "List of countries by GDP (nominal)" table from Wikipedia
- Cleans country names and GDP values
- Exports the data to `Wikipedia_GDeP.csv`

## Requirements

- Python 3.x
- `requests`
- `pandas`
- `beautifulsoup4`
- `lxml`

Install dependencies with:
```
pip install requests pandas beautifulsoup4 lxml
```

## Usage

Run the script:
```
python Wikipedia-GDP-Web-Scraper.py
```

The output CSV file `Wikipedia_GDeP.csv` will be created in the project directory.

