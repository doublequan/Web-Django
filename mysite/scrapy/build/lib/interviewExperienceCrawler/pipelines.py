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

        # print type(item['title'])
        # print item['link']
        # print type(item['time'])
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


# db_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# db = sqlite3.connect(db_path + "/db.sqlite3")
# cu = db.cursor()
#
# #""" Create Table
# cu.execute('create table IEItems ('
# #           'id integer,'
#            'title text, '
#            'link text UNIQUE PRIMARY KEY,'
#            'time text,'
#            'source text,'
#            'desc text'
#            ')'
#            )
#
#
# #cu.execute("insert into IEItems values("
#             "0, 'title', 'link1', '0', 'source', 'desc'"
#             ")")
# #db.commit()
