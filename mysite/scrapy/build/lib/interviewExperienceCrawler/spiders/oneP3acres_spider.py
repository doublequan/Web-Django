# -*- coding: utf-8 -*-
__author__ = 'Administrator'

import scrapy
import sys
import os
import re
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parentdir)
from items import IEItem

class OneP3acresSpider(scrapy.Spider):
    name = "1p3"
    allowed_domains = ["1point3acres.com"]
    start_urls = [
        "http://www.1point3acres.com/bbs/forum-28-1.html",
    ]

    def parse(self, response):
        '''
        parse the list page of 1p3.com, yield separate pages for late parse
        :param response:
        :return:
        '''
        self.logger.info("***Parsing List Page***")
        table = response.xpath("//table[@id = 'threadlisttableid']")
        #tbody_list = response.xpath("//table[@id = 'threadlisttableid']//tbody")
        a_list = response.xpath("//table[@id = 'threadlisttableid']//a[@class = 's xst']/@href").extract()
        # print len(a_list)

        for a in a_list:
            a_href = a.encode("utf-8")
            if self.is_new(a_href):
                # print "Yielding New Request :" + a_href
                yield scrapy.Request(a_href, callback=self.parse_page)

    def parse_page(self, response):
        self.logger.info("***Parsing Post Page***")

        postlist = response.xpath('//div[@id = \'postlist\']')
        title = postlist.xpath('//span[@id = \'thread_subject\']/text()').extract()[0].encode('utf-8')
        link = response.url

        first_floor = postlist.xpath('div[1]/table/tr/td[@class = \'plc\']')

        time_list = first_floor.xpath('//div[@class = \'authi\']/em/span/@title').extract()
        if len(time_list) != 0:
            time = time_list[0].encode('utf-8')
        else:
            time = first_floor.xpath("//div[@class = 'authi']/em/text()").extract()[0].encode('utf-8')
            time = re.search(r"[0-9]{4}-[0-9]{1,2}-[0-9]{1,2} [0-9]{1,2}:[0-9]{1,2}:[0-9]{1,2}", time).group(0)

        desc_unprocess = first_floor.xpath("//td[@class='t_f']").extract()[0].encode('utf-8')
        desc = re.sub(r"(<.*?>)|(\n)", "", desc_unprocess)

        item = IEItem()
        item['title'] = title
        item['link'] = link
        item['time'] = time
        item['source'] = "1point3acres"
        item['desc'] = desc
        yield item


    def is_new(self, url):
        return True

#print(sys.path)
