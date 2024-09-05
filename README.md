# Web Scraping GitHub Profile Image

This Python script, `web_scrapping.py`, scrapes a GitHub user's profile to retrieve and display the URL of their profile image. The user inputs a GitHub username, and the script fetches the profile page, parses it, and extracts the link to the user's avatar image using BeautifulSoup.

## Key Features:
- Accepts input for a GitHub username.
- Fetches and parses the corresponding GitHub profile page.
- Extracts the URL of the user's profile image (avatar).
- Utilizes the `requests` library for HTTP requests and `BeautifulSoup` for HTML parsing.

## Technologies Used:
- Python
- `requests` library for making HTTP requests.
- `BeautifulSoup` (from the `bs4` library) for parsing HTML.

## Usage Instructions:
1. Install Python 3.x on your system.
2. Install the required libraries:
   ```bash
   pip install requests
   pip install beautifulsoup4
