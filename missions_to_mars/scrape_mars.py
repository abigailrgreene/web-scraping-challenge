from splinter import Browser
from bs4 import BeautifulSoup as bs
import time


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {'executable_path':r'C:\Users\abiga\chromedriver.exe'}
    return Browser("chrome", **executable_path, headless=False)


def scrape_info():
    browser = init_browser()

    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url)

    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    images_list = soup.find_all(class_='item')

    
    hemisphere_images_urls = []

    for image in images_list:
        link = "https://astrogeology.usgs.gov/" + image.a["href"]
        browser.visit(link)
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')
        pic = soup.find('img', class_="wide-image")["src"]
        pic_link = "https://astrogeology.usgs.gov/" + pic
        title_ = soup.find('h2', class_='title')
        hemisphere_images_urls.append(
        {
            'title': title_.text,
            'img_url': pic_link
        }
    )

    # Close the browser after scraping
    browser.quit()

    # Return results
    return hemisphere_images_urls
