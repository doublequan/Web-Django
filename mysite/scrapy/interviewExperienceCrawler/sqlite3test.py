# -*- coding: utf-8 -*-
import os
import sqlite3

db_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
db = sqlite3.connect(db_path + "/db.sqlite3")
cu = db.cursor()

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

# #cu.execute("insert into IEItems values("
#             "0, 'title', 'link1', '0', 'source', 'desc'"
#             ")")
# #db.commit()

cu.execute("select * from IEItems WHERE title like '%FB%'")
rst = cu.fetchall()

print len(rst)
for i, r in enumerate(rst):
    print str(i), " ", r