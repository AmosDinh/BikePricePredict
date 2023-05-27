
import scrapy
import uuid
import csv

class FahrradSpider(scrapy.Spider):
    name = 'fahrrad'
    start_urls = [f'https://www.fahrrad.de/fahrraeder/?page={i}&sz=48' for i in range(1, 145)]
    seen = set()

    def parse(self, response):
        parent = response.css('#search-result-items')
        div_children = parent.xpath('./div')
        for div_child in div_children:
            price_element = div_child.css('.product-price .price-sales')
            if not price_element:
                price_element = div_child.css('.product-price .price-standard')

            if not price_element:
                continue
            price = price_element.css('::text').get().replace('.', '').replace(',', '.').replace('€', '').strip()
            
            swatches = div_child.css('.tns-inner')
            if swatches:
                images = swatches.css('img::attr(src)').extract()
            # else:
            #     images = div_child.css('.product-image img::attr(src)').extract()
            image_id = uuid.uuid4()
            for i, image in enumerate(images):
                if image in self.seen:
                    continue
                self.seen.add(image)
                image_url = image.split('?')[0]
                with open('images.csv', 'a') as f:
                    writer = csv.writer(f)
                    writer.writerow([image_url])
                yield {'image_url': image_url, 'image_name': f'{image_id}{str(i)}_{price}.jpg'}