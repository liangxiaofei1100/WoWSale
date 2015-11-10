#coding:utf-8
'''
Created on 2015年11月2日

@author: liangxiaofei
'''
import types
import sys

def objListToString(objList):
    result = "["
    listSize = len(objList)
    for index in range(listSize):
        if index == listSize - 1:
            result += str(objList[index])
        else:
            result += str(objList[index]) + ","
    result += "]"
    return result

def unicodeToString(unicodeObj):
    return unicodeObj.encode('utf-8')

def intToString(intObj):
    return str(intObj)

# 字典，定义各种type的toString方法
__toString = {types.IntType:intToString, 
              types.UnicodeType:unicodeToString, 
              types.ListType:objListToString}

def toString(obj):
    '''
    将obj转换为string，支持的类型有：types.IntType，types.UnicodeType，types.ListType
    '''
    re = __toString.get(type(obj))
    if re:
        return re(obj)
    else:
        print(type(obj))
        print("StringUtil.py, unkonw sysencoding")
        return str(obj)

def toSystemEncode(s):
    '''
    将string重新用当前系统编码编码，解决print乱码问题
    '''
    sysencoding = sys.getfilesystemencoding()
    return s.decode('utf-8').encode(sysencoding)