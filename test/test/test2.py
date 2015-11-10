#coding:utf-8
'''
Created on 2015年11月9日

@author: liangxiaofei
'''
from bs4 import BeautifulSoup
from common import stringutil

def main():
    soup = BeautifulSoup(open("../data/saling.html"), "html.parser")
#     print(soup.prettify())
    salingTableBody = soup.find(id="auctions-active").div.table.tbody
    diaowens = salingTableBody.find_all('strong')
    salingDiaowen = []
    for diaowen in diaowens:
        salingDiaowen.append(unicode(diaowen.string).encode('utf-8'))
    print(stringutil.toString(salingDiaowen))
    pass

if __name__ == '__main__':
    main()
    pass