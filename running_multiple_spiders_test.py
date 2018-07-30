import os
import sys
import argparse
import logging

from twisted.internet import reactor, defer
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
# from scrapy.utils.project import get_project_settings
from scrapy.settings import Settings

from sber.sber.spiders.dns import dnsEkbSpider
from sber.sber.spiders.avito import avitoEkbSpider

PATH = os.path.dirname(os.path.realpath(__file__))

logging.basicConfig(filename=PATH + '/crawl.log', filemode='a',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(lineno)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("inp", help="custom_input")
    args = parser.parse_args()

    argument = args.inp

    settings = Settings()
    sys.path.append(os.path.join(os.path.curdir, "spiders"))
    os.environ['SCRAPY_SETTINGS_MODULE'] = 'sber.sber.settings'
    settings_module_path = os.environ['SCRAPY_SETTINGS_MODULE']
    settings.setmodule(settings_module_path, priority='project')

    configure_logging()
    runner = CrawlerRunner(settings)

    @defer.inlineCallbacks
    def crawl():
        yield runner.crawl(dnsEkbSpider, argument)
        yield runner.crawl(avitoEkbSpider, argument)
        reactor.stop()

    crawl()
    reactor.run()  # the script will block here until the last crawl call is finished




