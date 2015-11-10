#coding:utf-8
'''
Created on 2015年11月10日

@author: liangxiaofei
'''
from bs4 import BeautifulSoup

class Product:
    '''
    商业技能制作的商品
    '''
    def __init__(self, productDBFile, productDBFile2=None, salingHtmlFile=None, toSaleFile=None):
        self.productDBFile = productDBFile
        self.productDBFile2 = productDBFile2
        self.salingHtmlFile = salingHtmlFile
        self.toSaleFile = toSaleFile
        pass
    
    def getAllProductList(self):
        '''
        获取所有可以制作的商品
        '''
        f = open(self.productDBFile)
        lines = f.readlines()
        f.close()
        allProductList = []
        for line in lines:
            allProductList.append(line.strip())
        
        return allProductList
    
    def getAllProduct2List(self):
        '''
        获取所有可以制作的商品中名字重复一次的雕文
        '''
        if not self.productDBFile2:
            return
        
        f = open(self.productDBFile2)
        lines = f.readlines()
        f.close()
        allProduct2List = []
        for line in lines:
            allProduct2List.append(line.strip())
        
        return allProduct2List
    
    def getSalingProductList(self):
        '''
        读取正在拍卖中的商品
        '''
        soup = BeautifulSoup(open(self.salingHtmlFile), "html.parser")
        salingTableBody = soup.find(id="auctions-active").div.table.tbody
        diaowens = salingTableBody.find_all('strong')
        salingProduct = []
        for diaowen in diaowens:
            salingProduct.append(unicode(diaowen.string).encode('utf-8'))
            
        return salingProduct
    
    def calculateProductToSale(self, salingProduct, allProduct, allProduct2=[], toSaleCount=1):
        '''
        计算出需要卖的商品，需要完全匹配
        '''
        f = open(self.toSaleFile, 'w')
        
        productToSale = []
        for product in allProduct:
            count = salingProduct.count(product)
            if count < toSaleCount:
                for n in range(toSaleCount - count):
                    productToSale.append(product)
                    f.write(product + '\n')
                
        for product in allProduct2:
            count = salingProduct.count(product)
            if count < 2 * toSaleCount:
                for n in range(2 * toSaleCount - count):
                    productToSale.append(product)
                    f.write(product + '\n')
                    
        f.close()
                
        return productToSale
    
    def calculateProductToSale2(self, salingProduct, allProduct):
        '''
        计算出需要卖的商品，只要在文字包含就算匹配
        '''
        f = open(self.toSaleFile, 'w')
        
        productToSale = []
        for product in allProduct:
            isSaling = False
            for product2 in salingProduct:
                #包含则认为在卖
                if product in product2:
                    isSaling = True
                    break
                
            if not isSaling:
                productToSale.append(product)
                f.write(product + '\n')
                    
        f.close()
                
        return productToSale