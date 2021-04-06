# -*- coding: utf-8 -*-
"""
Created on Thu May  7 15:23:36 2020

@author: fabio.tamburus
"""


import scrapy
from urllib.parse import urlparse
from scrapy.spidermiddlewares.httperror import HttpError
from twisted.internet.error import DNSLookupError
from twisted.internet.error import TimeoutError, TCPTimedOutError
import csv
import pandas as pd
from authx.spiders.manageLoginElo import manageLoginElo


class DemoSpider(scrapy.Spider): 
   name = 'auth_s'
   step = 'initial'
   stepDetail = 'initial'
   start_urls = ['https://www.elo7.com.br/login.do']  
   productGeneralList = []
   productDetailList = []
   errorList = []
   entrouDetalhePagina = []
   temporaryList = []
   whichLogin = 2 #escolher qual login faremos o scraping (1-principal;2-secundário)
   loginElo  = manageLoginElo(whichLogin) 
   cookies_X = loginElo.cookies
   headers_X = loginElo.headers
   data_X = loginElo.data

   def start_requests(self):
       yield scrapy.Request(url='https://www.elo7.com.br/login.do', callback=self.parse, headers=self.headers_X, cookies=self.cookies_X)
       
   def parse(self, response):
            
    return scrapy.FormRequest.from_response( 
       response, 
       formdata = self.data_X, 
       headers = self.headers_X,
       cookies = self.cookies_X,
       callback = self.after_login 
      )  
   

   def after_login(self, response): 
       #scrcode = response.css('img').xpath('@src').extract()
       searchstring = response.xpath('//a[contains(@href, "allMyProducts")]/@href').getall()
       for link in searchstring:
           return scrapy.Request("https://www.elo7.com.br/store/products.do?command=allMyProducts", 
      callback = self.ProductLoadPage, dont_filter=True) 
       pass

       
   def ProductLoadPage(self, response):

       btnnext = response.css("a[title='próximo']::attr('href')").extract_first()
       #Obtem o titulo de todos os elementos <a> da classe nav.pagination
       #btnnext = response.css('nav.pagination a::attr(title)').getall()
       page = response.xpath('//span[contains(@class, "selected")]/text()').get()
       if (self.step == 'initial'):
           productDetail = [
                   'itemDetailLink',
                   'itemSKUCode',
                   'itemTitle',
                   'itemImageLink',
                   'itemAvailability',
                   'itemPrice',
                   'itemFreight',
                   'itemAd',
                   'page',
                   'detaillink1',
                   'detaillink2',
                   'detaillink3',
                   'detaillink4',
                   'detaillink5',
                   'detaillink6'
                   ]
           self.addProductList(productDetail)
       domain = self.get_domain(response)
       #self.log('inicioooooooooooooooooooooooooooooo')
       #self.log(domain)
       #self.log(btnnext)
       #self.log('fimmmoooooooooooooooooooooooooooooo')

       for row in response.xpath('//*[@class="striped-table "]//tbody/tr'):
           #self.log(row.xpath('td[1]//a/@href').extract_first())
           itemDetailLink = domain + row.xpath('td[1]//a/@href').extract_first()
           #self.log(itemDetailLink)
           
           #itemDetailLink = 'https://www.elo7.com.br/copo-termico-enfermagem/dp/127EB36'
           
           itemSKUCode = str(itemDetailLink[itemDetailLink.rfind('/'):len(itemDetailLink)])
           #self.log(itemSKUCode)
           
           requestItemDetail = scrapy.Request(url=itemDetailLink, callback=self.ProductDetailLoadPage, errback=self.errback_httpbin, dont_filter=True, priority=1)
           requestItemDetail.meta['itemDetailLink'] = itemDetailLink
           requestItemDetail.meta['SKU'] = itemSKUCode
           yield requestItemDetail
           
           #self.log(row.xpath('td[1]//a/@title').extract_first())
           itemTitle = row.xpath('td[1]//a/@title').extract_first()
           #self.log(itemTitle)
               
           #self.log(row.xpath('td[1]//a/img/@src').extract_first())
           itemImageLink = 'https:' + row.xpath('td[1]//a/img/@src').extract_first()
           #self.log(itemImageLink)
           
           
           #self.log(row.xpath('td[2]//text()').extract_first())
           itemAvailability = row.xpath('td[2]//text()').extract_first()
           itemAvailability = itemAvailability.rstrip()
           itemAvailability = itemAvailability.lstrip()
           #self.log(itemAvailability)
           
           #self.log(row.xpath('td[3]//span').extract_first())
           itemPrice = row.xpath('td[3]//span/text()').extract_first()
           itemPrice = float(itemPrice[3:].replace(',','.'))
           #self.log(itemPrice)
           
           #self.log(row.xpath('td[4]//text()').extract_first())
           itemFreight = row.xpath('td[4]//text()').extract_first()
           itemFreight = itemFreight.rstrip()
           itemFreight = itemFreight.lstrip()
           #self.log(itemFreight)
           
           #self.log(row.xpath('td[5]//text()').extract_first())
           itemAd = row.xpath('td[5]//text()').extract_first()
           itemAd = itemAd.rstrip()
           itemAd = itemAd.lstrip()
           #self.log(itemAd)
           productDetail = [
               itemDetailLink,
               itemSKUCode,
               itemTitle,
               itemImageLink,
               itemAvailability,
               itemPrice,
               itemFreight,
               itemAd,
               page,
               '',
               '',
               '',
               '',
               '',
               ''
               ]
           
           self.addProductList(productDetail)
           #self.findSpecificValueInList(productDetail[1])
       #self.log('sai do loop')
       if not isinstance(btnnext,str):
           self.findSpecificValueInList(self.productGeneralList, self.productDetailList)
           #self.exportCSV(self.productGeneralList, 'mainItens.csv')
           #self.exportCSV(self.productDetailList, 'detailedItens.csv')
           #self.exportCSV(self.errorList, 'errorList.csv')
           #self.exportCSV(self.entrouDetalhePagina, 'entrouDetalhe.csv')
           
           self.log('fim export')
       else:
           next_page = domain + btnnext
           self.step = 'end'
           yield scrapy.Request(url=next_page, callback=self.ProductLoadPage, errback=self.errback_httpbin, dont_filter=True, priority=0)
       pass

       
   def get_domain(self, response):
       parsed_uri = urlparse(response.url)
       domain = '{uri.scheme}://{uri.netloc}'.format(uri=parsed_uri)
       return domain
   
 
    
   def addProductList (self, productDetail):
       self.productGeneralList.append(productDetail)
       return self.productGeneralList
   
   def ProductDetailLoadPage(self, response):
       #response.css("a[title='próximo']::attr('href')").extract_first()
       #self.log(response.xpath('//*[@class="gallery"]//ul/li').extract_first())
       productDescriptionDetail = ''
       productDescriptionDetailConcat = ''
       productDescription = response.xpath('//*[@class="content details"]//p/text()').extract()
       productPolicies = response.xpath('//*[@class="content policies"]//p/text()').extract()
       #response.xpath('//*[@class="detailed-info"]//ul/li'):
       
       #self.entrouDetalhePagina.append(response.meta['SKU'])
       #self.log(response.meta['SKU'])
       for li in response.xpath('//*[@class="content details"]//ul/li'):
           productDescriptionDetail = li.xpath('text()').extract_first()
           if isinstance(productDescriptionDetail,str):
               productDescriptionDetail = productDescriptionDetail.rstrip()
               productDescriptionDetail = productDescriptionDetail.lstrip()
               productDescriptionDetailConcat += '<br>' + productDescriptionDetail
           #self.log(productDescriptionDetail)
           
           #productDescriptionDetail = Selector(text=li.extract()).xpath('./li/text()').extract()  
       domain = self.get_domain(response)

       productVariationLink1 = ''
       productVariationTitle = ''
       productVariationLink2 = ''
       productVariationLink3 = ''
       productVariationLink4 = ''
       if (self.stepDetail == 'initial'):
           productDetail = [
            'productOriginalLink',
            'productOriginalSKU',
            'productVariationLink1',
            'productVariationTitle',
            'productVariationLink2',
            'productVariationLink3',
            'productVariationLink4',
            'productDescription',
            'productDescriptionDetail',
            'productPolicies'
            ]
           self.addProductDetailsList(productDetail)

       for row in response.xpath('//*[@class="gallery"]//ul/li'):
           #self.log(row.css("li::attr('class')").extract_first() + 'li+class____________')
           productOriginalLink = response.meta['itemDetailLink']
           productOriginalSKU = response.meta['SKU']
           productVariationTitle = row.css("a::attr('title')").extract_first()
           if(productVariationTitle == 'Zoom'):
               productVariationLink1 = 'https:' + row.css("a::attr('href')").extract_first()
           else:
               productVariationLink1 = domain + row.css("a::attr('href')").extract_first()

           if(row.css("li::attr('class')").extract_first() == 'thumb'):
               productVariationLink2 = 'https:' + row.css("a::attr('data-main')").extract_first()
               productVariationLink3 = 'https:' + row.css("a::attr('data-zoom')").extract_first()
               productVariationLink4 = 'https:' + row.css("img::attr('src')").extract_first()

 
           productDetail = [
                       productOriginalLink,
                       productOriginalSKU,
                       productVariationLink1,
                       productVariationTitle,
                       productVariationLink2,
                       productVariationLink3,
                       productVariationLink4,
                       productDescription,
                       productDescriptionDetailConcat,
                       productPolicies
               ]
           #self.findSpecificValueInList(productDetail[1])
           self.addProductDetailsList(productDetail)
       
       self.stepDetail = 'end'
       
   

   def errback_httpbin(self, failure):
        # log all failures
        self.errorList.append(repr(failure))

        # in case you want to do something special for some errors,
        # you may need the failure's type:

        if failure.check(HttpError):
            # these exceptions come from HttpError spider middleware
            # you can get the non-200 response
            response = failure.value.response
            self.errorList.append('HttpError on %s', response.url)

        elif failure.check(DNSLookupError):
            # this is the original request
            request = failure.request
            self.errorList.append('DNSLookupError on %s', request.url)

        elif failure.check(TimeoutError, TCPTimedOutError):
            request = failure.request
            self.errorList.append('TimeoutError on %s', request.url)
   
   def exportCSV (self, dataToExport, csvName):
       with open (csvName, "w", newline ="") as f:
           writer = csv.writer(f)
           writer.writerows(dataToExport)
           pass
   
   def exportToExcel (self, dataToExport, fileName):
       writer = pd.ExcelWriter(fileName)
       dataToExport.to_excel(writer)
       writer.save()
       pass
   
   def addProductDetailsList (self, productDetailsItem):
       self.productDetailList.append(productDetailsItem)
       return self.productDetailList
   
   def findSpecificValueInList(self, productGeneralList, productDetailList):
       
       pdlDataFrame = pd.DataFrame(productDetailList[1:], columns=productDetailList[0]) 
       pdgDataFrame = pd.DataFrame(productGeneralList[1:], columns=productGeneralList[0])
       i = 0

       for item in pdgDataFrame.index:
           i = 0          
           for ind in pdlDataFrame[pdlDataFrame['productOriginalSKU'] == pdgDataFrame['itemSKUCode'][item]].index:
               i += 1
               if (i == 1):
                   pdgDataFrame.at[item, "detaillink1"] = pdlDataFrame['productVariationLink3'][ind]
               elif (i == 2):
                   pdgDataFrame.at[item, "detaillink2"] = pdlDataFrame['productVariationLink3'][ind]
               elif (i == 3):
                   pdgDataFrame.at[item, "detaillink3"] = pdlDataFrame['productVariationLink3'][ind]                     
               elif (i == 4):
                   pdgDataFrame.at[item, "detaillink4"] = pdlDataFrame['productVariationLink3'][ind]                     
               elif (i == 5):
                   pdgDataFrame.at[item, "detaillink5"] = pdlDataFrame['productVariationLink3'][ind]                     
               elif (i == 6):
                   pdgDataFrame.at[item, "detaillink6"] = pdlDataFrame['productVariationLink3'][ind]
               else:
                   print('erroooooo - atualizacao dataframe')
                                            
               #print(pdlDataFrame['productOriginalSKU'][ind], pdlDataFrame['productOriginalLink'][ind])
           print (str(i) + ' Contador____')
       self.exportToExcel(pdgDataFrame, str(self.whichLogin) + "-mainItems.xlsx")
       self.exportToExcel(pdlDataFrame, str(self.whichLogin) + "-detailedItems.xlsx")
       
       pass
      
       