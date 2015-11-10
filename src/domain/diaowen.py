#coding:utf-8
'''
Created on 2015年11月9日

@author: liangxiaofei
'''

from collections import Counter
from common import pathconfig
from domain.product import Product

class Diaowen(Product):
    
    def __init__(self):
        Product.__init__(self, 
                         productDBFile=pathconfig.DATA_PATH + "db/diaowen.txt",
                         productDBFile2=pathconfig.DATA_PATH + "db/diaowen2.txt",
                         salingHtmlFile=pathconfig.DATA_PATH + "diaowen_saling.html",
                         toSaleFile=pathconfig.DATA_PATH + "diaowen_toSale.txt")
    
    def checkMissedDiaowen(self, salingDiaowen, allDiaowen):
        '''
        检查是否有新的雕文
        '''
        missedDiaowen = []
        for diaowen in salingDiaowen:
            if diaowen not in allDiaowen:
                missedDiaowen.append(diaowen)
        
        return missedDiaowen
    
    def checkRepeatedDiaowen(self, diaowenList):
        '''
        检查重复的雕文
        '''
        repeatedDiaowen = []
        c = Counter(diaowenList)
        for diaowen in c:
            if c[diaowen] > 1:
                repeatedDiaowen.append(diaowen)
                
        return repeatedDiaowen