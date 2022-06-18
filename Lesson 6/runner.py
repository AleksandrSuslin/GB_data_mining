

BOT_NAME = 'booksparser'

SPIDER_MODULES = ['booksparser.spiders']
NEWSPIDER_MODULE = 'booksparser.spiders'


USER_AGENT = "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64)"
                        " AppleWebKit/537.36 (KHTML, like Gecko)"
                        " Chrome/101.0.4951.54 Safari/537.36"
# Obey robots.txt rules
ROBOTSTXT_OBEY = False

LOG_ENABLED = True
LOG_LEVEL = "DEBUG"


CONCURRENT_REQUESTS = 8

DOWNLOAD_DELAY = 1.5

COOKIES_ENABLED = True


ITEM_PIPELINES = {
   'booksparser.pipelines.BooksparserPipeline': 300,
}


