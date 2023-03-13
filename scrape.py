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


def find_external_sources(html_content, element, search_item, contains):
    """ Function to retrieve sources in html page """
    # use element variable to retrieve all on the page
    all_resources = html_content.find_all(element)
    external_resource_list = []
    # iterate through all of the elements
    for x in all_resources:
        if search_item in x.attrs:
            # determine those with search item in their search item and add to list
            if contains in x[search_item]:
                external_resource_list.append(x)
    return external_resource_list


def get_external_sources(html_content):
    external_sources = []
    # find scripts
    scripts = find_external_sources(html_content, "script", "src", "https")
    external_sources.append(scripts)
    # find images
    images = find_external_sources(html_content, "img", "src", "https")
    external_sources.append(images)
    # find svgs
    svgs = find_external_sources(html_content, "svg", "src", "https")
    external_sources.append(svgs)
    # find links
    links = find_external_sources(html_content, "link", "href", "https")
    external_sources.append(links)

    # create data variable
    data = {'external sources count': len(external_sources),
            'external sources': str(external_sources)
            }

    # dump data in to json format
    external_sources_json = json.dumps(data, indent=4)
    print(external_sources_json)


def find_privacy_policy(html_content):
    """ Function to find Privacy policy """
    all_hyperlinks = html_content.find_all("a")
    i = 0
    while i <= len(all_hyperlinks):
        for y in all_hyperlinks:
            if "href" in y.attrs:
            # determine those with search item in their search item and add to list
                if "privacy" in y["href"]:
                    print(f"Link number: {i}, link: '{y['href']}'")
                    privacy_link = y['href'] 
            i+=1
    
    return privacy_link

def run_programme():
    """ Function to run whole programme """
    # Set html link to be scraped and call GET request
    html_link = "https://www.cfcunderwriting.com"

    # pass link to scrape function
    html_scraped_content = scrape_html(html_link)

    # get scripts/img/link/svgs
    get_external_sources(html_scraped_content)

    # get privacy policy link
    privacy_policy_path = find_privacy_policy(html_scraped_content)

    # combine the websites domain with privacy policy path
    privacy_policy_full = html_link + privacy_policy_path

    # get content from privacy policy
    privacy_policy_content = scrape_html(privacy_policy_full)

    print(privacy_policy_content)
    visible_text = (privacy_policy_content.text)
    #words = visible_text.replace(" ", "")
    #print(f"Word Count on Privacy Page: {word_count}")
    print(visible_text)

run_programme()
