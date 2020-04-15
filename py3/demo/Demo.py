########################################
"""
测试
"""

# print('100+200 =  ', 100+200)

#输入
# name = input('Input your name: ')
# print('Name:', name)

from PIL import Image
import imagehash
imghash = imagehash.average_hash(Image.open('C:\PythonProject\IdenticalPic\wxz.jpg'))
print(imghash)


picset = set()
picset.add(imghash.__str__())
print(picset)

import os
# os.remove(r'C:\个人\py\图像处理\猫狗识别\测试集\1白猫.jpg')
# print('ok')

dic = {}
if dic:
    print('not null')
else:
    print('null')

import shutil, os
picpath = r'C:\个人\py\图像处理\猫狗识别\测试集\wxz - 副本 (6).jpg'
picnewpath = r'C:\个人\py\图像处理\猫狗识别\repeat'
if os.path.exists(picpath):
    # os.mkdir(r'C:\个人\py\图像处理\猫狗识别\repeat')
    shutil.move(picpath, picnewpath)
    print('move over')
else:
    print('pic not exists')

rootdir = r'C:\个人\py\图像处理\猫狗识别\测试集\aaa.jpg'
print(rootdir.rindex('\\'))
repeatdir = rootdir[:rootdir.rindex('\\')+1]
print(rootdir)
print(repeatdir)

