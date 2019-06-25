import sys, os, re, zipfile, time
import CopyDirectory

product_list = [
'630-109329'
,'610-109026'
,'620-109330'
,'610-109027'
,'660-109001'
,'630-109032'
,'610-109024'
,'610-109025'
,'620-109236'
,'620-109237'
,'620-109235'
,'620-109234'
,'660-109029'
,'610-109033'
,'660-109034'
,'660-109484'
,'660-109028'
,'660-109023'
,'629-109498'
,'610-109662'
,'610-109663'
,'610-109643'
,'620-109530'
,'630-109660'
,'630-109661'
,'649-109653'
,'649-109656'
,'649-109659'

]

for product_id in product_list:

    # srcFilename1 = r"\\192.168.10.18\Share\Web3D_AO_191221\Products" + "\\" + product_id
    srcFilename1  = r"\\192.168.10.16\VM_Projects\Apache24\htdocs\Web3DAO\Products" + "\\" + product_id
    desFilename = r'C:\Users\chenlei\Desktop\Temp\Web3DAO\Products'+ "\\" + product_id
    # print(srcFilename1)
    # print(srcFilename2)
    CopyDirectory.copyFromSharePath(srcFilename1, desFilename)