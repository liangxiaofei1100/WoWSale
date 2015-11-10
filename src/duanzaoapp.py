#coding:utf-8
'''
Created on 2015年11月10日

@author: liangxiaofei
'''
from common import stringutil
from domain.duanzao import DuanZao

def main():
    duanzao = DuanZao()
    message('开始读取可以制作的锻造...')
    allDuanzaoList = duanzao.getAllProductList()
    message("读取完毕，共有锻造{count}个.".format(count=len(allDuanzaoList)))
    message('')
    
    message('开始读取正在拍卖中的锻造...')
    salingDuanzaoList = duanzao.getSalingProductList()
    message("读取完毕，共有在卖的锻造{count}个.".format(count=len(salingDuanzaoList)))
    message('')
    
    message('开始计算需要卖的锻造...')
    toSaleDuanzaoList = duanzao.calculateProductToSale2(salingDuanzaoList, allDuanzaoList)
    message('计算完毕，共有需要卖的锻造{count}个，详情请查看文件"{file}".'.format(count=len(toSaleDuanzaoList),file=duanzao.toSaleFile))
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