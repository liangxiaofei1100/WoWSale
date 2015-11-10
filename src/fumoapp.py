#coding:utf-8
'''
Created on 2015年11月10日

@author: liangxiaofei
'''
from common import stringutil
from domain.fumo import FuMo

def main():
    fumo = FuMo()
    message('开始读取可以制作的附魔...')
    allFumoList = fumo.getAllProductList()
    message("读取完毕，共有附魔{count}个.".format(count=len(allFumoList)))
    message('')
    
    message('开始读取正在拍卖中的附魔...')
    salingFumoList = fumo.getSalingProductList()
    message("读取完毕，共有在卖的附魔{count}个.".format(count=len(salingFumoList)))
    message('')
    
    message('开始计算需要卖的附魔...')
    toSaleFumoList = fumo.calculateProductToSale(salingFumoList, allFumoList, toSaleCount=2)
    message('计算完毕，共有需要卖的雕文{count}个，详情请查看文件"{file}".'.format(count=len(toSaleFumoList),file=fumo.toSaleFile))
    message('')
    
    raw_input(stringutil.toSystemEncode("按Enter键退出: "))
    pass

def message(m):
    '''
    显示消息到终端，解决了乱码问题
    '''
    print(stringutil.toSystemEncode(m))

if __name__ == '__main__':
    main()
    pass