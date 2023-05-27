from playwright.sync_api import Playwright, sync_playwright
import urllib
from PIL import Image
import uuid 
import os

def download_image( image_url, filename):
    """
    Downloads the image from the given URL and saves it to the specified
    file. Returns True if the operation is successful, False otherwise.
    """
    

    def convert_to_jpg(filename):
        # check if file is jpg with PIL
        with Image.open(filename) as img:
            if img.format != 'JPEG':
                img.save(filename, 'JPEG')

    try:
        urllib.request.urlretrieve(image_url, filename)
        convert_to_jpg(filename)
        return True
    except urllib.error.HTTPError as e:
        # If the server returns a 403 Forbidden error, try to bypass it using
        # one of several strategies
        if e.code == 403:
            # Option 1: Set a custom User-Agent header
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
            opener = urllib.request.build_opener()
            opener.addheaders = headers.items()
            urllib.request.install_opener(opener)
            urllib.request.urlretrieve(image_url, filename)
            convert_to_jpg(filename)
            return True

        # If none of the strategies work, log the error and return False
        print(f'Error downloading image: {e}')
        return False
    
def run(playwright: Playwright, download_folder) -> None:
    browser = playwright.chromium.launch(headless=True)
    os.mkdir(download_folder, exist_ok=True)
    page = browser.new_page()
    urls = ["<URL1>", "<URL2>", "<URL3>"]


    for url in urls:
        page.goto(url)
        div = page.locator("#srchrslt-content")
        articles = div.locators(".aditem")
        for article in articles:
            img_src = article.locator("img").get_attribute("src")
            price_text = article.locator(".aditem-main--middle--price-shipping--price").inner_text()
            price = price_text.replace('VB','').replace('€','').replace('.','').strip().replace(',','.')
           
            image_id = uuid.uuid4()
            download_image(img_src, os.path.join(download_folder, f'{image_id}_{price}.jpg'))
    browser.close()

with sync_playwright() as playwright:
    run(playwright, download_folder='images')
