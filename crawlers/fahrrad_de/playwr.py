
import csv
import uuid
import urllib.request
import os
from playwright.sync_api import sync_playwright

def download_image( image_url, filename):
    """
    Downloads the image from the given URL and saves it to the specified
    file. Returns True if the operation is successful, False otherwise.
    """
    try:
        urllib.request.urlretrieve(image_url, filename)
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
            return True

        # If none of the strategies work, log the error and return False
        print(f'Error downloading image: {e}')
        return False
        
def run() -> None:

    with sync_playwright() as playwright:
        seen = set()
        with open('images.csv', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
              
                if row:
                    seen.add(row[0])
        browser = playwright.firefox.launch(headless=True)
        page = browser.new_page()
        image_dir = 'images'

        if not os.path.exists(image_dir):
            os.makedirs(image_dir)
     
        with open('images.csv', 'a') as f:
            writer = csv.writer(f)

            for i in range(120, 145):
                print(f'Page {i}')
                page.goto(f'https://www.fahrrad.de/fahrraeder/?page={i}&sz=48')
                parent = page.query_selector('#search-result-items')
                div_children = parent.query_selector_all('div')
                for div_child in div_children:
                    price_element = div_child.query_selector('.product-price .price-sales')
                    if not price_element:
                        price_element = div_child.query_selector('.product-price .price-standard')
                    if price_element:
                        price = price_element.inner_text().replace('.', '').replace(',', '.').replace('€', '').strip()
                    else:
                        continue

                    swatches = div_child.query_selector('.product-swatches')
                    if swatches:
                        images = [x.get_attribute('data-productimage') for x in swatches.query_selector_all('img')]
                    else:
                        children = div_child.query_selector('.product-image img')
                        if children is None:
                            continue
                        try:
                            images = [x.get_attribute('src') for x in children]
                        except:
                            images = [children.get_attribute('src') ]
                            pass

                    image_id = uuid.uuid4()
                    for j, image in enumerate(images):
                        
                        
                        
                        image_url = image.split('?')[0]
                        if image_url in seen:
                            continue
                        seen.add(image_url)
                        writer.writerow([image_url])
                        print(j )
                        if '.gif' in image_url or 'N/A' in image_url:
                            continue
                        print({'image_url': image_url, 'image_name': f'{image_id}{str(j)}_{price}.jpg'})
                        
                        download_image(image_url, os.path.join(image_dir, f'{image_id}{str(j)}_{price}.jpg'))

        browser.close()


# if __name__ == '__main__':
#     run()