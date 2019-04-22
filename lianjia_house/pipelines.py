# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs,json
from datetime import datetime


class LianjiaHousePipeline(object):
    def __init__(self):
        self.time_now = datetime.now().strftime('%Y-%m-%d %H:%M')


    def open_spider(self,spider):
        filen = '/media/gumoha/资料/Scrapy/lianjia_house/house_json/{0}-({1}).json'.format('ChengDu_ershoufang',self.time_now)
        self.file = codecs.open(filen,'w')

    def close_spider(self,item,spider):
        self.file.close()

    def process_item(self, item, spider):
        line = '{0}\n'.format(json.dumps(dict(item),ensure_ascii=False))
        self.file.write(line)

        return item
