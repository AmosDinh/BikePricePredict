
import csv
import uuid
import urllib.request
import os
from playwright.sync_api import sync_playwright
import time
from PIL import Image
from threading import Lock
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
def url_generator():
    def generate(term, minp, maxp):
        minmax = f'https://www.google.com/search?biw=1920&bih=933&tbm=shop&q={term}&tbs=mr%3A1%2Cprice%3A1%2Cppr_min%3A{minp}%2Cppr_max%3A{maxp}'
        return minmax
    urls = []
    # colors
    # generate a list of tuples with min max steps in 100 steps
    steps = []
    # steps.append((100,200))
    stepslower = np.arange(200,1500,50)
    stepsupper = stepslower+50
    steps.extend(list(zip(stepslower,stepsupper)))
    stepslower = np.arange(1500,3000,500)
    stepsupper = stepslower+500
    steps.extend(list(zip(stepslower,stepsupper)))
    stepslower = np.arange(3000,6001,3000)
    stepsupper = stepslower+3000
    steps.extend(list(zip(stepslower,stepsupper)))
    
    

    
    colors=['blue','brown','yellow','orange','turkis','purple','white', 'grey', 'green','red','silver']
    typen = ['e-bike','childrens bike','mountainbike','trekkingbike','citybike',] # 
    # typen = [
    #     'Road Bike',
    #     'Mountain Bike',
    #     'Hybrid Bike',
    #     'Cyclocross Bike',
    #     'Gravel Bike',
    #     'Touring Bike',
    #     'Adventure Bike',
    #     'Electric Bike (e-bike)',
    #     'Folding Bike',
    #     'Fat Bike',
    #     'Single-Speed Bike',
    #     'Fixed-Gear Bike (Fixie)',
    #     'Time Trial Bike',
    #     'Triathlon Bike',
    #     'Track Bike (Velodrome)',
    #     'Downhill Mountain Bike',
    #     'Enduro Mountain Bike',
    #     'Cross-Country Mountain Bike',
    #     'Dirt Jump Bike',
    #     'Recumbent Bike',
    #     'Tandem Bike',
    #     'Cargo Bike',
    #     'City Bike',
    #     'Comfort Bike',
    #     'Beach Cruiser',
    #     'BMX Bike',
    #     "Kids' Bike",
    #     'Balance Bike',
    #     'Dutch Bike',
    #     'Vintage Bike'
    # ]
    materials = ['alu','carbon','stahl']
    # fahrrad%20rot
    trigger = True 
    for typ in typen:
        for (lower,upper) in steps:
            for color in colors:
            
                # for material in materials:
                
                    # if typ == 'trekkingrad'  and lower == 550 and upper == 600 and material=='alu': # and color == 'grün'
                    #     trigger = True 
                    #     continue
                if trigger:
                    urls.append(generate(f'{typ}%20{color}',lower,upper))
                
 
    return urls
def get_seen_images():
    seen = set()
    with open('images.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            
            if row:
                seen.add(row[0])

    return seen
    
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
        pageulrs =[
                'https://www.google.com/search?tbm=shop&sxsrf=APwXEdcZn39do5-mmaLJaiiaWH9ZgpmbQw:1683746846973&q=bike&tbs=mr:1,merchagg:m3290712,pdtr0:714013%7C714015,pdtr1:711457%7C714003&sa=X&ved=0ahUKEwjD4tHlvev-AhWHq6QKHaa_C2gQwQkIkgcoAA&biw=876&bih=862&dpr=2.19',
                'https://www.google.com/search?tbm=shop&sxsrf=APwXEdfOHj07yPl-uAPcnYjjUTHAY8tA6A:1683746533463&q=bike&tbs=mr:1,pdtr0:4560076%7C4560078&sa=X&ved=0ahUKEwi01ZLQvOv-AhXNO-wKHZjTD7wQwQkI_AkoAA&biw=876&bih=862&dpr=2.19',
                'https://www.google.com/search?tbm=shop&sxsrf=APwXEddLYEpiGgiXw5nVbIL1Ct52Fzga-g:1683746944218&q=bike&tbs=mr:1,pdtr0:4560076%7C4560078,pdtr1:878464%7C878468&sa=X&ved=0ahUKEwjU8YCUvuv-AhVNxAIHHUyTAysQwQkIhQooAA&biw=876&bih=862&dpr=2.19',
                'https://www.google.com/search?tbm=shop&sxsrf=APwXEddiKZglFqTH8c1F_ZNuMCc25ilgAA:1683746955391&q=bike&tbs=mr:1,pdtr0:4560076%7C4560078,pdtr1:878464%7C878468,pdtr2:711457%7C890342&sa=X&ved=0ahUKEwicgKuZvuv-AhWW7KQKHZNyBvYQ1yoI1QkoAQ&biw=876&bih=862&dpr=2.19',
                'https://www.google.com/search?tbm=shop&sxsrf=APwXEddiKZglFqTH8c1F_ZNuMCc25ilgAA:1683746955391&q=bike&tbs=mr:1,pdtr0:4560076%7C4560078,pdtr1:878464%7C878468,pdtr2:711457%7C913151&sa=X&ved=0ahUKEwicgKuZvuv-AhWW7KQKHZNyBvYQwQkI1wkoAA&biw=876&bih=862&dpr=2.19',
                'https://www.google.com/search?tbm=shop&sxsrf=APwXEddiKZglFqTH8c1F_ZNuMCc25ilgAA:1683746955391&q=bike&tbs=mr:1,pdtr0:4560076%7C4560078,pdtr1:878464%7C878468,pdtr2:711457%7C711480&sa=X&ved=0ahUKEwicgKuZvuv-AhWW7KQKHZNyBvYQwQkI2gkoAA&biw=876&bih=862&dpr=2.19',
                'https://www.google.com/search?tbm=shop&sxsrf=APwXEddLYEpiGgiXw5nVbIL1Ct52Fzga-g:1683746944218&q=bike&tbs=mr:1,pdtr0:4560076%7C4560078,pdtr1:714013%7C714014&sa=X&ved=0ahUKEwjU8YCUvuv-AhVNxAIHHUyTAysQwQkI-wkoAA&biw=876&bih=862&dpr=2.19',
                'https://www.google.com/search?tbm=shop&sxsrf=APwXEddLYEpiGgiXw5nVbIL1Ct52Fzga-g:1683746944218&q=bike&tbs=mr:1,pdtr0:4560076%7C4560078,pdtr1:714013%7C714016&sa=X&ved=0ahUKEwjU8YCUvuv-AhVNxAIHHUyTAysQwQkI-AkoAA&biw=876&bih=862&dpr=2.19',
                'https://www.google.com/search?tbm=shop&sxsrf=APwXEddLYEpiGgiXw5nVbIL1Ct52Fzga-g:1683746944218&q=bike&tbs=mr:1,pdtr0:4560076%7C4560078,pdtr1:711457%7C890342&sa=X&ved=0ahUKEwjU8YCUvuv-AhVNxAIHHUyTAysQwQkIjgooAA&biw=876&bih=862&dpr=2.19',
                'https://www.google.com/search?tbm=shop&sxsrf=APwXEddLYEpiGgiXw5nVbIL1Ct52Fzga-g:1683746944218&q=bike&tbs=mr:1,pdtr0:4560076%7C4560078,pdtr1:712025%7C712026&sa=X&ved=0ahUKEwjU8YCUvuv-AhVNxAIHHUyTAysQwQkIggooAA&biw=876&bih=862&dpr=2.19',
                'https://www.google.com/search?tbm=shop&sxsrf=APwXEddLYEpiGgiXw5nVbIL1Ct52Fzga-g:1683746944218&q=bike&tbs=mr:1,pdtr0:4560076%7C4560078,pdtr1:878464%7C878466&sa=X&ved=0ahUKEwjU8YCUvuv-AhVNxAIHHUyTAysQwQkInQooAA&biw=1129&bih=862&dpr=2.19',
                'https://www.google.com/search?tbm=shop&sxsrf=APwXEddLYEpiGgiXw5nVbIL1Ct52Fzga-g:1683746944218&q=bike&tbs=mr:1,pdtr0:4560076%7C4560078,pdtr1:712025%7C712027&sa=X&ved=0ahUKEwjU8YCUvuv-AhVNxAIHHUyTAysQwQkIkQooAA&biw=1129&bih=862&dpr=2.19',
                'https://www.google.com/search?tbm=shop&sxsrf=APwXEddLYEpiGgiXw5nVbIL1Ct52Fzga-g:1683746944218&q=bike&tbs=mr:1,root_cat:536464&sa=X&ved=0ahUKEwjU8YCUvuv-AhVNxAIHHUyTAysQyY4HCPkEKAE&biw=1129&bih=862&dpr=2.19',
                'https://www.google.com/search?tbm=shop&sxsrf=APwXEddLYEpiGgiXw5nVbIL1Ct52Fzga-g:1683746944218&q=bike&tbs=mr:1,root_cat:536469&sa=X&ved=0ahUKEwjU8YCUvuv-AhVNxAIHHUyTAysQyY4HCPsEKAM&biw=1129&bih=862&dpr=2.19',
                'https://www.google.com/search?tbm=shop&sxsrf=APwXEddLYEpiGgiXw5nVbIL1Ct52Fzga-g:1683746944218&q=bike&tbs=mr:1,root_cat:536466&sa=X&ved=0ahUKEwjU8YCUvuv-AhVNxAIHHUyTAysQyY4HCPgEKAA&biw=1129&bih=862&dpr=2.19',
                'https://www.google.com/search?q=fahrrad&sa=X&biw=1129&bih=862&tbm=shop&sxsrf=APwXEdfOHj07yPl-uAPcnYjjUTHAY8tA6A%3A1683746533463&ei=5e5bZPTOG833sAeYp7_gCw&ved=0ahUKEwi01ZLQvOv-AhXNO-wKHZjTD7wQ4dUDCAg&uact=5&oq=fahrrad&gs_lcp=Cgtwcm9kdWN0cy1jYxADMgQIIxAnMgQIIxAnMgsIABCABBCxAxCDATILCAAQgAQQsQMQgwEyCwgAEIAEELEDEIMBMgsIABCABBCxAxCDATILCAAQgAQQsQMQgwEyCwgAEIAEELEDEIMBMgsIABCABBCxAxCDATILCAAQgAQQsQMQgwE6BwgAEIoFEEM6CQgAEIoFEAoQQzoFCAAQgARQAFjLBmC5B2gAcAB4AIABRogB9AKSAQE3mAEAoAEBwAEB&sclient=products-cc',
                'https://www.google.com/search?sa=X&tbm=shop&sxsrf=APwXEdf_yfzxahlxFYEKe0NuONTYYc3eQw:1683747182342&q=fahrrad+kinder&ved=0ahUKEwiH-MaFv-v-AhWBD-wKHXPQBocQ2wsIhws&biw=1129&bih=862&dpr=2.19',
                'https://www.google.com/search?sa=X&tbm=shop&sxsrf=APwXEdf_yfzxahlxFYEKe0NuONTYYc3eQw:1683747182342&q=fahrrad+g%C3%BCnstig&ved=0ahUKEwiH-MaFv-v-AhWBD-wKHXPQBocQ2wsIiws&biw=1129&bih=862&dpr=2.19',
                'https://www.google.com/search?sa=X&tbm=shop&sxsrf=APwXEdf_yfzxahlxFYEKe0NuONTYYc3eQw:1683747182342&q=fahrrad+mountainbike&ved=0ahUKEwiH-MaFv-v-AhWBD-wKHXPQBocQ2wsIgQs&biw=1129&bih=862&dpr=2.19',
                'https://www.google.com/search?sa=X&tbm=shop&sxsrf=APwXEddqqWi9iRj1HkLVumYBA61MnmJH8A:1683747241153&q=fahrrad+mountainbike+28+zoll&ved=0ahUKEwiQt8yhv-v-AhWH7aQKHcX6DDgQ2wsIjws&biw=1129&bih=862&dpr=2.19',
                'https://www.google.com/search?sa=X&tbm=shop&sxsrf=APwXEddqqWi9iRj1HkLVumYBA61MnmJH8A:1683747241153&q=fahrrad+mountainbike+29+zoll&ved=0ahUKEwiQt8yhv-v-AhWH7aQKHcX6DDgQ2wsIkws&biw=1129&bih=862&dpr=2.19',
                'https://www.google.com/search?sa=X&tbm=shop&sxsrf=APwXEddqqWi9iRj1HkLVumYBA61MnmJH8A:1683747241153&q=fahrrad+mountainbike+26+zoll&ved=0ahUKEwiQt8yhv-v-AhWH7aQKHcX6DDgQ2wsIjQs&biw=1129&bih=862&dpr=2.19',





        ]       
        pageulrs = url_generator()
        sleepcount = 0
        context = browser.new_context(locale=countrysymbols)
        page = context.new_page()
        needaccept = True
        for pageurl in pageulrs:
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


        browser.close()


if __name__ == '__main__':
    run('de-DE', 'germany',Lock(), Lock())