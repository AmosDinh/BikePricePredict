

# import scrapy
# import uuid
# import os
# import urllib.request

# class FahrradSpider(scrapy.Spider):
#     name = 'fahrrad'
#     start_urls = [f'https://www.fahrrad-xxl.de/fahrraeder/seite/{i}/?o=docscore' for i in range(1, 122)]

#     def parse(self, response):
#         for product in response.css('div[data-product-id]'):
#             parent = product.css('.fxxl-element-artikel__variant-main-slider')
#             if parent:
#                 image_url = parent.css('img::attr(data-srcset)').get()
#                 if image_url:
#                     image_url = image_url.split(',')[-1].split()[0]
#                 else:
#                     continue
#                 price_elements = product.css('.fxxl-element-artikel__price:not(.fxxl-price-with-strike-price)')
#                 price = None
#                 for price_element in price_elements:
#                     if '€' in price_element.get():
#                         price = price_element.css('::text').get()
#                         break
#                 if price:
#                     image_id = str(uuid.uuid4())
#                     price = price.replace(',', '.').replace(' €', '').strip('')
#                     filename = f'{image_id}_{price}.jpg'
#                     os.makedirs('fahrrad_images', exist_ok=True)
#                     urllib.request.urlretrieve(response.urljoin(image_url), f'fahrrad_images/{filename}')