# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import sqlite3


class PreProcessingPipeline(object):
    def __init__(self):
        db_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        self.db = sqlite3.connect(db_path + "/db.sqlite3")

    def process_item(self, item, spider):
        # print "*****************process items****************"

        # print item['title']
        # print item['link']
        # print item['time']
        # print item['source']
        # print item['desc']
        cu = self.db.cursor()
        cu.execute("insert into IEItems values("
                   "'" + item['title'] + "', '" +
                   item['link'] + "', '" +
                   item['time'] + "', '" +
                   item['source'] + "', '" +
                   item['desc'] +
                   "')")
        self.db.commit()
        return item



