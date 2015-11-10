#coding:utf-8
'''
Created on 2015年11月9日

@author: liangxiaofei
'''
from common import stringutil

if __name__ == '__main__':
    diaowenfile = open("../data/diaowen.txt")
    diaowenList = diaowenfile.readlines()
    print(len(diaowenList))
    
    diaowenList2 = []
    for diaowen in diaowenList:
        diaowenList2.append(diaowen.strip() + '\n')
        pass
    
    print(len(diaowenList2))
#     print(stringutil.toString(diaowenList2))
    
    diaowenfile.close()
    
    file = open("../data/diaowen2.txt", 'w')
    for diaowen in diaowenList2:
        file.write(diaowen)
    
    file.close()
    pass