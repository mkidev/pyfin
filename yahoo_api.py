'''
Created on 23.12.2015

@author: marcelkisilowski
'''

import pandas as pd
from yql.api import YQL
from myql.contrib.finance.stockscraper import StockRetriever

class yahoo_api(object):
    
    '''
    classdocs
    '''

    @classmethod
    def __init__(self):
        '''
        Constructor
        '''
        self.path = "/Users/marcelkisilowski/Workspace/Proo/Finance"
        self.startDate = "2010-01-01"
        self.endDate = "2015-12-31"
           
    def load(self, fetchData=True):
        self.stocks = StockRetriever(format='json')
        self.symbols = self.loadSymbolList();
        if self.loadCacheData():
            pass
        elif fetchData:
            self.cache = pd.Panel({self.symbols[0]:self.fetchData(self.symbols[0],self.startDate,self.endDate)})
            self.loadPriceData()
        self.saveCache() 
           
    def loadSymbolList(self, symbolListPath="/Users/marcelkisilowski/Workspace/Proo/Finance"):
        """
        """
        data = pd.read_json(symbolListPath+"/dow.json");
        return data.Symbol
    
    def loadPriceData(self):
        """
        """
        result = dict()
        for symbol in self.symbols:
            if self.cache.get(symbol) is None:
                print("Fetching data for %s.", symbol)
                result[symbol] = self.fetchData(symbol, self.startDate, self.endDate)
                self.cache[symbol] = result[symbol]
                self.saveCache("_tmp.data")
            else:
                print("is in")
    def fetchData(self,symbol,startDate,endDate):
        #Bestehend aus date und adj_close->"price"
        print("Fetching %s..." % symbol)
        data = self.stocks.get_historical_info(symbol,items=['Open','Close','High','Low'] ,startDate=startDate,endDate=endDate)
        print("Loaded %d values." % len(data))
        pdata = pd.DataFrame(data, dtype=float)
        pdata = pdata.set_index("date")
        return pdata

    def saveCache(self,fileName="cache_large.data"):
        try:
            self.cache.to_pickle(self.path+"/"+fileName)
        except IOError:
            print("Cache not saved.")
    def loadCacheData(self,fileName="cache_large.data"):
        try:
            self.cache = pd.read_pickle(self.path+"/"+fileName)
            print("Loaded %d Symbols out of cache" % len(self.cache))
            return True
        except IOError as e:
            print("Cache not loaded.")
            print(e)
            return False

yapi = yahoo_api()
#yapi.checkMonthBetweenDates("22.01.2010", "22.07.2011")
#e = yapi.fetchData("AAPL", "2012-01-02", "2015-12-01")
#e.index.min()