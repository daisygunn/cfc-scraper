# cfc-scraper

This programme has been designed to scrape data from the index webpage of _`cfcunderwriting.com`_, produce a JSON of all externally loaded resources, enumerates the page's hyperlinks and identifies the location of the "Privacy Policy"
page & use the privacy policy URL to scrape the pages content and produce a case-insensitive word frequency count for all of the visible text on the page.

**Inital setup & running the programme:**
- Using GitHub codespaces, open a new codespace
- Once codespace has been built, in the terminal run the following command: _`pip install -r requirements.txt`_
- Wait for all of the requirements to be installed
- To start the programme run the following command: _`python scrape.py`_
- In the terminal you will see the required outputs.
