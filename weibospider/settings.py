# -*- coding: utf-8 -*-

BOT_NAME = 'spider'

SPIDER_MODULES = ['spiders']
NEWSPIDER_MODULE = 'spiders'

ROBOTSTXT_OBEY = False

# change cookie to yours
DEFAULT_REQUEST_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:61.0) Gecko/20100101 Firefox/61.0',
    'Cookie': '_T_WM=60649516893; SCF=Ar-U3Gy_2HdV9J2klVQk6_TMokK04zFINdOnntZIr5rB7cFa2AMpOOOeuWHKfX7qm_eVWK3718DnCb0DJEfXfB4.; SUB=_2A25NMi6FDeRhGeRG61UQ9SrMwj6IHXVu3LLNrDV6PUJbktANLVXdkW1NUl1d0xG2osDwrakC0XbNfjL8pK7k4Gaz; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWIFT5I9LQueBmgA-bgOQr45NHD95QE1h5NeK-Xeh.EWs4DqcjJi--fiKysi-i2i--fiKysi-i2i--fiK.Ei-8si--fiK.Ei-8seo2t; SSOLoginState=1614175957'}

CONCURRENT_REQUESTS = 16

DOWNLOAD_DELAY = 2

DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.cookies.CookiesMiddleware': None,
    'scrapy.downloadermiddlewares.redirect.RedirectMiddleware': None,
    'middlewares.IPProxyMiddleware': 100,
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 101,
}

ITEM_PIPELINES = {
    'pipelines.MongoDBPipeline': 300,
}

MONGO_HOST = '127.0.0.1:27017'
MONGO_USER_NAME = ""
MONGO_USER_PWD = ""
