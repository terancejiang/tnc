# -*- coding: utf-8 -*-
import scrapy
import codecs
import sys
from urllib import urlencode
reload(sys)
sys.setdefaultencoding('utf8')
class TncspiderSpider(scrapy.Spider):
    name = 'tncspider'
    allowed_domains = ['tnc.com.cn']
    start_urls = ['https://ml.tnc.com.cn/search/company-c-90-k--p50.html?compModel=1']

    def parse(self, response):

        compynames =  response.css('div.cnt.cnt-company-list > p > a::text').extract()
        urls = response.css('div.cnt.cnt-company-list > p > a::attr(href)').extract()
        compynames = [x.rstrip() for x in compynames]
        urls = [ x for x in urls if "certificate" not in x ]
        k = filter(None, compynames)
        print k
        for count,url in enumerate( urls):


            print ("company is  %s url is %s count is %s" % (k[count], url,count))
            # if not ('www') in url:
            intro_url = url + 'introduce.html'
            certificate_url = url + 'certificate.html'
            print intro_url
            print certificate_url
            yield scrapy.Request(url = intro_url,callback=self.getDestails_certified_intro)
                # yield scrapy.Request(url=certificate_url, callback=self.getDestails_certified_intro)
            # else:
            #     yield scrapy.Request(url=url, callback=self.getDestails_uncertified)


        next_url = response.xpath('/html/body/div[4]/div[1]/div[4]/a/@href').extract()[-1]
        next_url = 'https://ml.tnc.com.cn/'+ next_url
        print next_url
        if next_url:
            yield scrapy.Request(url=next_url, callback=self.parse)

    def getDestails_certified_intro(selfself,response):
        print
        pass


    def getDestails_uncertified(selfself, response):
        pass

    # f = codecs.open('output.txt', 'a+')
    # # f.write()
    # # line = ",".join(productnames)
    # f.write(url + '  ssss  '+ compynames + '\n')
    # f.close()