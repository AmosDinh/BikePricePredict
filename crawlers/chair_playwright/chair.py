import os
import urllib.request
import uuid
import time
from playwright.sync_api import Playwright, sync_playwright
import datetime

class XXXLutzSpider:
    def __init__(self):
        self.start_url = 'https://www.xxxlutz.de/stuehle-C12C1'
        self.image_directory = 'images'
        os.makedirs(self.image_directory, exist_ok=True)
        self.image_count = 0

    def download_image(self, image_url, filename):
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
            
    def get_save_csv_set(self, a=None):
        # if a is not None, save set a to csv file
        if a is not None:
            with open('xxxlutz.csv', 'w') as f:
                for item in a:
                    f.write("%s\n" % item)
        # read csv file and return set
        with open('xxxlutz.csv', 'r') as f:
            a = set()
            for line in f:
                a.add(line.strip())
        
        return a
    
    def download_images_of_parent(self, parent, filename_prefix):
        for i, image_url_element in enumerate(parent.query_selector_all('img[srcset]')):
            # image_url = image_url_element.get_attribute('srcset').strip()
            image_url = image_url_element.get_attribute('src').strip()
            filename = f'{filename_prefix}_{i+1}.jpg'
            if image_url not in self.a:
                self.a.add(image_url)
                self.get_save_csv_set(self.a)
                success = self.download_image(image_url, os.path.join(self.image_directory, filename))
                if success:
                    self.image_count += 1
                
                print(f'Download {image_url}')


    def run(self):
        with sync_playwright() as p:
            browser = p.firefox.launch(headless=True)
            context = browser.new_context()
            page = context.new_page()
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
            page.set_extra_http_headers(headers)
            page.goto(self.start_url)
            page.wait_for_selector('button[data-purpose="cookieBar.button.accept"]').click()
            self.a = self.get_save_csv_set()
            last_pos = 0
            while True:
                product_elements = page.query_selector_all('article')

                for i, product in enumerate(product_elements[last_pos:]):
                    last_pos+=1
                    price_parent = product.query_selector('div[data-testid="productCard.preview"]')
                    parent_more_options = product.query_selector('div > ul')
                    # parents.append(paren1)
                    
                    if price_parent:
                       
                        # image_url = image_urls[len(image_urls)//2].get_attribute('src').strip()
                        price_element = product.query_selector('div[data-purpose="product.price.current"]')
                        if price_element:
                            price = price_element.inner_text().replace('€', '').replace(',', '.').replace('\u202f', '').strip()
                            if not price:
                                price = product.query_selector('sup').inner_text()

                            unique_url = price_parent.query_selector_all('img[srcset]')[0].get_attribute('src').strip()
                            
                            # generate unique uuid from unique url
                            unique_uuid = uuid.uuid5(uuid.NAMESPACE_URL, unique_url)
                            filename_prefix = f'{unique_uuid}_{price}'
                            
                            self.download_images_of_parent(price_parent, filename_prefix)
                            if parent_more_options:
                                self.download_images_of_parent(parent_more_options, filename_prefix)
                                    

                # Click the "Load more" button to load the next page of products
              
                load_more_button = page.query_selector('button[data-purpose="listing.loadMore.next.button"]')
                if not load_more_button:
                    break
                load_more_button.click()
                time.sleep(3) # wait for 1 second before scraping the new data

            browser.close()

        print(f'Scraped {self.image_count} images.')

if __name__ == '__main__':
    spider = XXXLutzSpider()
    spider.run()