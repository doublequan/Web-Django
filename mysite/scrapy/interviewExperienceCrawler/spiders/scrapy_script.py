from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner, CrawlerProcess
from scrapy.utils.log import configure_logging

from oneP3acres_spider import OneP3acresSpider

# configure_logging({'LOG_FORMAT': '%(levelname)s: %(message)s'})
# runner = CrawlerRunner()
#
# d = runner.crawl(OneP3acresSpider)
# d.addBoth(lambda _: reactor.stop())
# reactor.run() # the script will block here until the crawling is finished

process = CrawlerProcess()
process.crawl(OneP3acresSpider)
# process.crawl(OneP3acresSpider)
process.start() # the script will block here until all crawling jobs are finished