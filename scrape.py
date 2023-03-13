import requests
from bs4 import BeautifulSoup
import json


def scrape_html(html_page):
    """ Function to scrape desired html page """
    html_content = requests.get(html_page)

    # Using beautiful soup, pass in data from get request and use html parser to parse content
    content = BeautifulSoup(html_content.content, 'html.parser')
    # return soup variable to be used later on
    return content

def find_external_sources(html_content):
    """ Function to retrieve scripts in html page """
    
    scripts = html_content.findAll("script")
    images = html_content.findAll("img")
    svg = html_content.findAll("svg")
    links = html_content.findAll("link")
    # create data variable
    data = { 'scripts': str(scripts),
             'images': str(images),
             'svg': str(svg),
             'links': str(links)
            }

    external_sources = json.dumps(data, indent=4)
    print(external_sources)


def run_programme():
    # Set html link to be scraped and call GET request
    html_link = "https://www.cfcunderwriting.com"
    # pass link to scrape function
    html_scraped_content = scrape_html(html_link)
    # pass scraped content to retrieve external sources
    find_external_sources(html_scraped_content)


run_programme()