# !/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf8') #解决python2.x的str默认是ascii编码和unicode编码冲突冲突问题
from Tkinter import *
import tkFileDialog
import tkMessageBox
import os
import re
import json
import random
import fileinput

# 检查 UITableViewCell、UICollectionViewCell 子视图是否添加到 contentview 上，如果没有添加，输出当前类名以及所在行
def matchATSMethod(dir_path, rematch):
    suf_set = ('.swift') # 只需要遍历 .swift 文件，就可以确定，是否是 UITableViewCell、UICollectionViewCell 类
    interface_symbol_containing = ': ' + rematch
    print('\n 继承自 ' + rematch + ' 的类 ' + '\n')
    for (root, dirs, files) in os.walk(dir_path):
        
        for file_name in files:
            if file_name.endswith(suf_set):
                with open(os.path.join(root, file_name), 'r+') as f:
                    line = f.readline()
                    while line:
                        if interface_symbol_containing in line: # 命中
                            checkATSMethod(root, file_name, rematch)
                            break
                        line = f.readline()
                    f.close()


# 将 .h 文件路径转为 .m 文件路径
def getOCFileName(s):
    return s[::-1].replace("h", "m", 1)[::-1]  

# 打开 .swift 文件，遍历每一行，是否符合 addSubview( 格式，符合输出当前类名、以及所在行
def checkATSMethod(root, file_name, match):
    ats_symbol_containing = 'addSubview('
    #file_name = getOCFileName(file_name)
    with open(os.path.join(root, file_name), 'r+') as f:
        line = f.readline()    
        idx = 0 
        while line:
            idx += 1
            if ats_symbol_containing in line: # 命中 
                print(file_name + ' 第 ' + str(idx) + ' 行, 路径为' + root + '\n' )  
                idx = 0
                break
            line = f.readline()
        f.close()

# 直接指定源码根路径就可以
matchATSMethod('/Users/sx/SxWork/PlayBar/PlayBar/Pods', 'UICollectionViewCell') 
matchATSMethod('/Users/sx/SxWork/PlayBar/PlayBar/Pods', 'UITableViewCell')                      
