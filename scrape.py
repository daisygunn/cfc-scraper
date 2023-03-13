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


def find_external_sources(html_content, element, search_item):
    """ Function to retrieve sources in html page """
    all_resources = html_content.find_all(element)
    external_resource_list = []
    for x in all_resources:
        if search_item in x.attrs:
            if 'https' in x[search_item]:
                external_resource_list.append(x)
    return external_resource_list


def run_programme():
    # Set html link to be scraped and call GET request
    html_link = "https://www.cfcunderwriting.com"

    external_sources = []
    # pass link to scrape function
    html_scraped_content = scrape_html(html_link)
    # pass scraped content to retrieve external sources
    scripts = find_external_sources(html_scraped_content, "script", "src")
    external_sources.append(scripts)
    images = find_external_sources(html_scraped_content, "img", "src")
    external_sources.append(images)
    svgs = find_external_sources(html_scraped_content, "svg", "src")
    external_sources.append(svgs)
    links = find_external_sources(html_scraped_content, "link", "href")
    external_sources.append(links)
    # create data variable
    data = {'external sources count': len(external_sources),
            'external sources': str(external_sources)
            }

    external_sources_json = json.dumps(data, indent=4)
    print(external_sources_json)


run_programme()
