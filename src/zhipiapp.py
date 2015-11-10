#coding:utf-8
'''
Created on 2015年11月10日

@author: liangxiaofei
'''
from common import stringutil
from domain.zhipi import ZhiPi

def main():
    zhipi = ZhiPi()
    message('开始读取可以制作的制皮...')
    allZhipiList = zhipi.getAllProductList()
    message("读取完毕，共有制皮{count}个.".format(count=len(allZhipiList)))
    message('')
    
    message('开始读取正在拍卖中的制皮...')
    salingZhipiList = zhipi.getSalingProductList()
    message("读取完毕，共有在卖的制皮{count}个.".format(count=len(salingZhipiList)))
    message('')
    
    message('开始计算需要卖的制皮...')
    toSaleZhipiList = zhipi.calculateProductToSale2(salingZhipiList, allZhipiList)
    message('计算完毕，共有需要卖的制皮{count}个，详情请查看文件"{file}".'.format(count=len(toSaleZhipiList),file=zhipi.toSaleFile))
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