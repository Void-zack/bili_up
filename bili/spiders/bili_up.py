import scrapy
import json
from scrapy import Request
from bili.items import BiliItem

class BiliUpSpider(scrapy.Spider):
    name = 'bili_up'
    UID = '1339327684'
    allowed_domains = ['bilibili.com']
    start_urls = ['http://api.bilibili.com/x/space/arc/search?mid='+UID]

    def parse(self, response):
        vlurls = [response.url+'&pn=1']
        page = json.loads(response.body)["data"]["page"]
        pn = int(page["pn"])
        while pn*int(page["ps"]) < int(page["count"]):
            vlurls.append(response.url+'&pn='+str(pn+1))
            pn += 1
        for vlurl in vlurls:
            yield Request(url=vlurl, callback=self.vlist_parse)

    def vlist_parse(self, response):
        vlist = json.loads(response.body)["data"]["list"]["vlist"]
        for vinfo in vlist:
            yield Request('http://api.bilibili.com/x/tag/archive/tags?bvid='+vinfo["bvid"], callback=self.vtag_parse)

    def vtag_parse(self, response):
        datas = json.loads(response.body)["data"]
        for data in datas:
            item = BiliItem(tag_name=data["tag_name"])
            yield item
