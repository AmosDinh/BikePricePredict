import os
import urllib.request
import uuid
import time
from playwright.sync_api import Playwright, sync_playwright

class XXXLutzSpider:
    def __init__(self):
        self.start_url = 'https://www.xxxlutz.de/esszimmerstuehle-C12C1C6'
        self.image_directory = 'images'
        self.image_count = 0

    def download_image(self, image_url, filename):
        """
        Downloads the image from the given URL and saves it to the specified
        file. Returns True if the operation is successful, False otherwise.
        """
        srcset_urls = image_url.split(',')
        for url in srcset_urls:
            url = url.strip().split()[0]  # Use only the URL and ignore the size attribute
            if url.endswith('1200w'):
                try:
                    urllib.request.urlretrieve(url, filename)
                    return True
                except urllib.error.HTTPError as e:
                    print(f'Error downloading image from {url}: {e}')
            elif url.endswith('1000w'):
                try:
                    urllib.request.urlretrieve(url, filename)
                    return True
                except urllib.error.HTTPError as e:
                    print(f'Error downloading image from {url}: {e}')
            else:
                try:
                    urllib.request.urlretrieve(url, filename)
                    return True
                except urllib.error.HTTPError as e:
                    print(f'Error downloading image from {url}: {e}')

        # If none of the URLs in the srcset attribute work, log the error and return False
        print(f'Error downloading image: {image_url}')
        return False

    def run(self):
        with sync_playwright() as p:
            browser = p.firefox.launch(headless=True)
            context = browser.new_context()
            page = context.new_page()
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
            page.set_extra_http_headers(headers)
            page.goto(self.start_url)

            while True:
                product_elements = page.query_selector_all('article')

                for product in product_elements:
                    parent = product.query_selector('div[data-testid="productCard.preview"]')
                    if parent:
                        image_urls = parent.query_selector_all('img[srcset]')
                        price_element = product.query_selector('div[data-purpose="product.price.current"]')
                        if price_element:
                            price = price_element.inner_text().replace('€', '').replace(',', '.').replace('\u202f', '').strip()
                            if not price:
                                price = product.query_selector('sup').inner_text()
                            image_id = str(uuid.uuid4())
                            filename_prefix = f'{parent.get_attribute("data-product-id")}_{price}'
                            os.makedirs(self.image_directory, exist_ok=True)
                            for i, image_url_element in enumerate(image_urls):
                                image_url = image_url_element.get_attribute('srcset').strip()
                                filename = f'{filename_prefix}_{i+1}.jpg'
                                success = self.download_image(image_url, os.path.join(self.image_directory, filename))
                                if success:
                                    self.image_count += 1

                # Click the "Load more" button to load the next page of products
                load_more_button = page.query_selector('button[data-purpose="listing.loadMore.next.button"]')
                if not load_more_button:
                    break
                load_more_button.click()
                time.sleep(1) # wait for 1 second before scraping the new data

            browser.close()

        print(f'Scraped {self.image_count} images.')

if __name__ == '__main__':
    spider = XXXLutzSpider()
    spider.run()