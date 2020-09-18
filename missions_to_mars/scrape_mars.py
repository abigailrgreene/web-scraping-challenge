from splinter import Browser
from bs4 import BeautifulSoup as bs
import time


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {'executable_path':r'C:\Users\abiga\chromedriver.exe'}
    return Browser("chrome", **executable_path, headless=False)


def scrape_info():
    browser = init_browser()

    url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url)

    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, 'html.parser')

    background = soup.find('footer')
    image = background.find('a')['data-fancybox-href']
    featured_image_url = 'https://www.jpl.nasa.gov' + image

    mars_data = {
        "feat_img": featured_image_url
    }

    # Close the browser after scraping
    browser.quit()

    # Return results
    return mars_data

