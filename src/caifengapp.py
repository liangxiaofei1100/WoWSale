#coding:utf-8
'''
Created on 2015年11月10日

@author: liangxiaofei
'''
from common import stringutil
from domain.caifeng import CaiFeng

def main():
    caifeng = CaiFeng()
    message('开始读取可以制作的裁缝...')
    allCaifengList = caifeng.getAllProductList()
    message("读取完毕，共有裁缝{count}个.".format(count=len(allCaifengList)))
    message('')
    
    message('开始读取正在拍卖中的裁缝...')
    salingCaifengList = caifeng.getSalingProductList()
    message("读取完毕，共有在卖的裁缝{count}个.".format(count=len(salingCaifengList)))
    message('')
    
    message('开始计算需要卖的裁缝...')
    toSaleCaifengList = caifeng.calculateProductToSale2(salingCaifengList, allCaifengList)
    message('计算完毕，共有需要卖的裁缝{count}个，详情请查看文件"{file}".'.format(count=len(toSaleCaifengList),file=caifeng.toSaleFile))
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