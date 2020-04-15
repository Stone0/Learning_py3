# -*- coding: utf-8 -*-
from PIL import Image
import imagehash
import os
import shutil
##################################################
"""
遍历文件夹下的所有图片并去重
"""

# 遍历文件筛选重复图片
def listDir(rootdir):
    print('##### 开始遍历:', rootdir, '#####')
    for filename in os.listdir(rootdir):
        if filename == 'repeat':
            continue
        pathname = os.path.join(rootdir, filename)
        if os.path.isfile(pathname):
            # 文件
            print('文件:', pathname)
            # 获取图片hash值
            # pichash = imagehash.average_hash(Image.open(pathname))
            # if pichash.__str__() in picset:
            #     print(' |-图片重复:', pichash)
            #     picdict[pathname] = filename
            # else:
            #     # print('新图片:', pichash)
            #     picset.add(pichash.__str__())

            if pathname.find('.txt') != -1:
                picdict[pathname] = filename

        else:
            # 文件夹
            print()
            print('===== 子目录:', pathname, '=====')
            listDir(pathname)
            print('===== 子目录遍历完成 =====')
            print()
    print('##### 遍历完成 #####')

# 移动重复图片至新路径
def mvrepeatpic(picdict):
    i = 1
    print('#################### 重复图片 ####################')
    # 判断图片字典是否为空
    if picdict:
        for k in picdict:
            print(k)
            # 删除重复图片
            # os.remove(k)
            # 移动到其他路径
            picnewpath = rootdir + '\\repeat\\'
            # if not os.path.exists(picnewpath):
            #     os.mkdir(picnewpath)
            # print(' |-Move To:', picnewpath)
            # shutil.move(k, picnewpath)
            newpath = rootdir + '\\repeat\\'
            if not os.path.exists(newpath):
                os.mkdir(newpath)
            if not os.path.exists(newpath + os.path.basename(k)):
                print(newpath)
                shutil.move(k, newpath)
            else:
                otherpath = newpath + i.__str__() + os.path.basename(k)
                print(otherpath)
                shutil.move(k, otherpath)
                i += 1

            #print(os.path.basename(k))
            #print(picnewpath + os.path.basename(k))
        print()
        print('移动完成')
    else:
        print('没有重复图片')

    print('#################################################')

# 所有图片set
picset = set()
# 重复图片dict
picdict = {}

rootdir = r'C:\个人\py\图像处理\猫狗识别'
listDir(rootdir)
mvrepeatpic(picdict)
