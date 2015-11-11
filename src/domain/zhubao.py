#coding:utf-8
'''
Created on 2015年11月10日

@author: liangxiaofei
'''
from domain.product import Product
from common import pathconfig

class ZhuBao(Product):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        Product.__init__(self, productDBFile=pathconfig.DATA_PATH+"db/zhubao.txt", 
                         productDBFile2=pathconfig.DATA_PATH+"db/zhubao2.txt", 
                         salingHtmlFile=pathconfig.DATA_PATH+"zhubao_saling.html", 
                         toSaleFile=pathconfig.DATA_PATH+"zhubao_toSale.txt")
        