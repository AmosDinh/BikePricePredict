# Define your item pipelines here
import scrapy
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem

class MyImagesPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        return [scrapy.Request(item['image_url'], meta={'image_name': item['image_name']})]

    def file_path(self, request, response=None, info=None):
        return request.meta['image_name']

    def item_completed(self, results, item, info):
        if not any(x[0] for x in results):
            raise DropItem(f"Item contains no images: {item}")
        return item
