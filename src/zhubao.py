#coding:utf-8
'''
Created on 2015年11月10日

@author: liangxiaofei
'''
from common import stringutil
from domain.zhubao import ZhuBao

def main():
    zhubao = ZhuBao()
    message('开始读取可以制作的珠宝...')
    allZhubaoList = zhubao.getAllProductList()
    message("读取完毕，共有珠宝{count}个.".format(count=len(allZhubaoList)))
    message('')
    
    message('开始读取正在拍卖中的珠宝...')
    salingZhubaoList = zhubao.getSalingProductList()
    message("读取完毕，共有在卖的珠宝{count}个.".format(count=len(salingZhubaoList)))
    message('')
    
    message('开始计算需要卖的珠宝...')
    toSaleZhubaoList = zhubao.calculateProductToSale2(salingZhubaoList, allZhubaoList)
    message('计算完毕，共有需要卖的珠宝{count}个，详情请查看文件"{file}".'.format(count=len(toSaleZhubaoList),file=zhubao.toSaleFile))
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