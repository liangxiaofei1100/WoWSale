#coding:utf-8
'''
Created on 2015年11月10日

@author: liangxiaofei
'''
from domain.product import Product
from common import pathconfig

class ZhiPi(Product):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        Product.__init__(self, productDBFile=pathconfig.DATA_PATH+"db/zhipi.txt", 
                         productDBFile2=None, 
                         salingHtmlFile=pathconfig.DATA_PATH+"zhipi_saling.html", 
                         toSaleFile=pathconfig.DATA_PATH+"zhipi_toSale.txt")
        