# -*- coding: utf-8 -*-
import os
import sqlite3

db_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
db = sqlite3.connect(db_path + "/db.sqlite3")
cu = db.cursor()

#""" Create Table
# cu.execute('create table interviews_items ('
# #           'id integer,'
#            'title text NOT NULL ,'
#            'link text PRIMARY KEY NOT NULL ,'
#            'time text,'
#            'source text NOT NULL ,'
#            'desc text,'
#            'tag text'
#            ')'
#            )

# cu.execute('create table interviews_crawler_source ('
#            'source text NOT NULL ,'
#            'link text,'
#            'desc text'
#            ')'
#            )

cu.execute("insert into interviews_items values("
            "'title', 'link1', NULL , 'source', 'desc', NULL "
            ")")
db.commit()

# cu.execute("select * from IEItems WHERE title like '%FB%'")
# rst = cu.fetchall()
#
# print len(rst)
# for i, r in enumerate(rst):
#     print str(i), " ", r