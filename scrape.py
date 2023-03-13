import requests
from bs4 import BeautifulSoup

# Set html link to be scraped and call GET request
html_link = "https://www.cfcunderwriting.com"

def scrape_html(html_page):
    """ Function to scrape desired html page """
    html_content = requests.get(html_page)

    # Using beautiful soup, pass in data from get request and use html parser to parse content
    soup = BeautifulSoup(html_content.content, 'html.parser')
    print(soup)
    # return soup variable to be used later on
    return soup

