#coding:utf-8
'''
Created on 2015年11月9日

@author: liangxiaofei
'''

from common import stringutil
from domain.diaowen import Diaowen

def main():
	diaowen = Diaowen()
	message('开始读取可以制作的雕文...')
	allDiaowenList = diaowen.getAllProductList()
	allDiaowen2List = diaowen.getAllProduct2List()
	message("读取完毕，共有雕文{count}个.".format(count=len(allDiaowenList)))
	message('')
	
	message('开始读取正在拍卖中的雕文...')
	salingDiaowenList = diaowen.getSalingProductList()
	message("读取完毕，共有在卖的雕文{count}个.".format(count=len(salingDiaowenList)))
	message('')
	
	message('开始检查是否有遗漏的雕文...')
	missedDiaowen = diaowen.checkMissedDiaowen(salingDiaowenList, allDiaowenList)
	message('遗漏的雕文：' + stringutil.toString(missedDiaowen))
	message('')
	
	message('开始计算需要卖的雕文...')
	toSaleDiaowenList = diaowen.calculateProductToSale(salingDiaowenList, allDiaowenList, allDiaowen2List)
	message('计算完毕，共有需要卖的雕文{count}个，详情请查看文件"{file}".'.format(count=len(toSaleDiaowenList),file=diaowen.toSaleFile))
	message('')
	
	#repeatedDiaowen(diaowen, salingDiaowenList, allDiaowenList)
	raw_input(stringutil.toSystemEncode("按Enter键退出: "))
	pass

def message(m):
	'''
	显示消息到终端，解决了乱码问题
	'''
	print(stringutil.toSystemEncode(m))

def repeatedDiaowen(diaowen, salingDiaowenList, allDiaowenList):
	'''
	重复雕文检查
	'''
	l = diaowen.checkRepeatedDiaowen(salingDiaowenList)
	message("在卖的重复雕文："+stringutil.toString(l))
	l = diaowen.checkRepeatedDiaowen(allDiaowenList)
	message("数据文件中的重复雕文："+stringutil.toString(l))

if __name__ == '__main__':
	main()