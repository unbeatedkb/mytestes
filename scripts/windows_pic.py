# coding: utf-8

import os
import getpass

# 获取当前用户的用户名
username = getpass.getuser()

PICPATH = 'C:/Users/'+username+'/AppData/Local/Packages/Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy/LocalState/Assets'
OUTPATH = 'C:/Users/'+username+'/Desktop/mypic'

# 判定图片文件是贴图还是壁纸的文件大小阈值，单位byte
MINSIZE = 1024*100

def diffname(picname, names):
    if picname not in names:
        return False
    else:
        return True
        # picname = picname + '_'
        # return diffname(picname, names)

def getname(names):
    newnames = []
    for name in names:
        newnames.append(name.split('.')[0])
    return newnames

if __name__ == '__main__':
    # 判断文件夹是否存在，不存在则创建
    if not os.access(OUTPATH, os.F_OK):
        os.mkdir(OUTPATH)
        print 1

    l1 = os.listdir(PICPATH)
    l2 = os.listdir(OUTPATH)

    names = getname(l2)

    for l in l1:
        with open(PICPATH + '/' + l, 'rb') as f:
            # 通过文件名前8位来判断重复，如果已经不存在则写入
            picname = l[:10]
            if not diffname(picname, names):
                # 通过文件大小判断是贴图图片还是壁纸图片，设定阈值为100kb
                # getsize返回以字节为单位的文件大小值
                size = os.path.getsize(PICPATH+'/'+l)
                print size
                if int(size) >= MINSIZE:
                    print '大小合适，存入'
                    with open(OUTPATH + '/' + picname + '.jpg', 'wb') as t:
                        t.write(f.read())

    temp = raw_input('已经获取完成，请任意键后退出！')






































