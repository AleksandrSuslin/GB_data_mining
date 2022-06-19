BOT_NAME = 'castoramaparser'

IMAGES_STORE = 'photos'

SPIDER_MODULES = ['castoramaparser.spiders']
NEWSPIDER_MODULE = 'castoramaparser.spiders'



USER_AGENT = "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64)"
                        " AppleWebKit/537.36 (KHTML, like Gecko)"
                        " Chrome/101.0.4951.54 Safari/537.36"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False


CONCURRENT_REQUESTS = 16

LOG_ENABLED = True
LOG_LEVEL = "DEBUG"

s
DOWNLOAD_DELAY = 1.5
)
COOKIES_ENABLED = True

ITEM_PIPELINES = {
   'castoramaparser.pipelines.CastoramaparserPipeline': 300,
   'castoramaparser.pipelines.CastoramaPhotosPipeline': 200
}
