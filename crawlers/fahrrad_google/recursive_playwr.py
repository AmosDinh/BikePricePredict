# clicks randomly on links to find more bicycles


import csv
import uuid
import urllib.request
import os
from playwright.sync_api import sync_playwright
import time
from PIL import Image
from threading import Lock
from urllib.parse import urljoin

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

import numpy as np

def get_seen_images():
    seen = set()
    with open('images.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            
            if row:
                seen.add(row[0])

    return seen

def get_urls_of_morerecommendations(page):
    urls = []
    divs = page.query_selector_all('div.sh-vrd__container') # .sh-sr__shop-result-group
    for div in divs:
        spans = div.query_selector_all('span.sh-vrd__option[role="listitem"]')
        for span in spans:
            link = span.query_selector('a') # get first link
            if link:
                href = link.get_attribute('href')
                if href:
                    url = urljoin(page.url, href)
                    urls.append(url)
    
    return urls

def run(countrysymbols, countryname, lock1, lock2) -> None:
    with sync_playwright() as playwright:
        
        seen_googlepages = set()
        
        seen = get_seen_images()

        with open('seengoogle.csv', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
              
                if row:
                    seen_googlepages.add(row[0])

        browser = playwright.firefox.launch(headless=False)
        # page = browser.new_page()
        image_dir = 'images'

        if not os.path.exists(image_dir):
            os.makedirs(image_dir)
        #page.goto(f'https://www.google.com/search?hl=de&tbm=shop&sxsrf=APwXEdf1CR4jZOOYQLWV20Ke7h1ixTUa5Q:1683468593273&q=fahrrad+neu+kaufen&tbs=mr:1,merchagg:g120407133%7Cg123903187%7Cg126139323%7Cg537545771%7Cg138017413%7Cg124693729%7Cg118425033%7Cg9066730%7Cg130828198%7Cg122675645%7Cm134781051%7Cm131090620%7Cm127746289%7Cm113400242%7Cm111419755%7Cm737027241%7Cm7727347%7Cm441680280%7Cm105724296%7Cm118874979%7Cm117226497%7Cm8209683%7Cm6023587%7Cm481307201%7Cm502235107%7Cm138041772%7Cm9587419%7Cm437192%7Cm455517306%7Cm8846952%7Cm9820503%7Cm311370497%7Cm118453782%7Cm9068210%7Cm554576381%7Cm193215840%7Cm275908879%7Cm199627821%7Cm134841060%7Cm7754443&sa=X&ved=0ahUKEwigl_ebseP-AhWatqQKHX2IDOAQsysI7gQoKA&biw=1462&bih=923&dpr=2')
        # page.goto('https://www.google.com/search?q=fahrrad+neu+kaufen&hl=de&tbs=mr:1,merchagg:g120407133%7Cg123903187%7Cg126139323%7Cg537545771%7Cg138017413%7Cg124693729%7Cg118425033%7Cg9066730%7Cg130828198%7Cg122675645%7Cm134781051%7Cm131090620%7Cm127746289%7Cm113400242%7Cm111419755%7Cm737027241%7Cm7727347%7Cm441680280%7Cm105724296%7Cm118874979%7Cm117226497%7Cm8209683%7Cm6023587%7Cm481307201%7Cm502235107%7Cm138041772%7Cm9587419%7Cm437192%7Cm455517306%7Cm8846952%7Cm9820503%7Cm311370497%7Cm118453782%7Cm9068210%7Cm554576381%7Cm193215840%7Cm275908879%7Cm199627821%7Cm134841060%7Cm7754443,vw:d&tbm=shop&ei=G7xXZNXXKrbl7_UPr4qwoAE&start=300&sa=N&ved=0ahUKEwiV0bbQu-P-AhW28rsIHS8FDBQ48AEQ8NMDCNAS&biw=1280&bih=720&dpr=2')
    
       
        sleepcount = 0
        context = browser.new_context(locale=countrysymbols)
        page = context.new_page()
        needaccept = True

        recurse_urls = {}
      
            

        recurse_level = 0
        inside_level_index = 0
        recurse_urls[0] = ['https://www.google.com/search?q=rennrad&tbm=shop&sxsrf=APwXEdcmE8_OriEMg7LmAXPwGmbsP7yupQ:1684085143657&source=lnms&sa=X&ved=2ahUKEwjEiomGqvX-AhUoMewKHRvPCasQ_AUoAXoECAEQAw&biw=1756&bih=870&dpr=2.19']
        
        while True:
            
           
            print(f'Level {recurse_level} Index {inside_level_index}')   
            if len(recurse_urls[recurse_level]) == inside_level_index:
                recurse_level += 1
                inside_level_index = 0
                continue

            pageurl = recurse_urls[recurse_level][inside_level_index]
            inside_level_index +=1
      
            if pageurl in seen:
                continue
            else:
                seen_googlepages.add(pageurl)
                with lock1:
                    with open('seengoogle.csv', 'a') as f:
                        writer = csv.writer(f)
                        writer.writerow([pageurl])
            page.goto(pageurl)
            if needaccept:
                page.click('button[aria-label="Alle akzeptieren"]')
                needaccept = False

            time.sleep(3)
            page_urls = get_urls_of_morerecommendations(page)
            print(page_urls)
            if recurse_level+1 not in recurse_urls:
                recurse_urls[recurse_level+1] = []
            recurse_urls[recurse_level+1] += page_urls
            
            while True:
                print(f'Page {page.url}')
                
                parent = page.query_selector('.sh-pr__product-results-grid.sh-pr__product-results')
                if parent is None:
                    if sleepcount ==2:
                         sleepcount=0
                         break
            
                    time.sleep(3)
                    sleepcount+=1
                    continue
                else:
                    sleepcount=0

                div_children = parent.query_selector_all('>div')
                for div_child in div_children:
                    price_element = div_child.query_selector('span.OFFNJ') # first element
                
                    if price_element:
                        price = price_element.inner_text().replace('.', '').replace(',', '.').replace('€', '').strip()
                    else:
                        continue

                    picture_parent = div_child.query_selector('.sh-dgr__content')
                    if picture_parent:
                        images = [picture_parent.query_selector('img[role="presentation"]').get_attribute('src') ]
                    else:
                        continue

                    image_id = uuid.uuid4()
                    
                    for j, image_url in enumerate(images):
                        
                        
                        
                        with lock2:
                            seen = get_seen_images()
                            if image_url in seen:
                                continue
                            seen.add(image_url)
                        
                            with open('images.csv', 'a') as f:
                                writer = csv.writer(f)
                                writer.writerow([image_url])
                            

                        if '.gif' in image_url or 'N/A' in image_url:
                            continue
                        # print({'image_url': image_url, 'image_name': f'{image_id}{str(j)}_{price}.jpg'})
                        print(f'download')
                        download_image(image_url, os.path.join(image_dir, f'{countryname}_{image_id}{str(j)}_{price}.jpg'))
                
                time.sleep(1)
                page.set_default_timeout(7000)
                try:
                    next_button = page.locator('text="Weiter"')
                    if not next_button:
                        break
                    
                    next_button.click()
                except:
                    break


        


if __name__ == '__main__':

    # recursively iterate over pages sstarting from google search "bike"
    # do breath first iteration:
    # add links from "other recommendations" to the list of pages to iterate over at level 0
    # for subpages add the "other recommendations" to the list but at level 1 
    # ...
    run('de-DE', 'germany',Lock(), Lock())