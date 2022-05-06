# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pandas as pd

class BiliPipeline:
    def process_item(self, item, spider):
        UID = spider.UID
        tag_name = pd.DataFrame(dict(item), index=[0])
        tag_name.to_csv(f'UID-{UID}.csv', mode='a', header=False, index=False)

        return item