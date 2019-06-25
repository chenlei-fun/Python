import sys, os, re, zipfile, time
import CopyDirectory

product_list = ['260-109500'
,'260-109501'
,'660-109001'
,'660-109034'
,'660-109023'
,'610-109033'
,'660-109028'
]

for product_id in product_list:
    srcFilename1  = r"\\192.168.10.16\VM_Projects\MYI_Models\Wealin" + "\\" + product_id
    srcFilename2 =  r"\\192.168.10.16\VM_Projects\MYI_Models\YuLing" + "\\" + product_id
    desFilename = r'C:\Users\chenlei\Desktop\Temp\Puyee'+ "\\" + product_id
    # print(srcFilename1)
    # print(srcFilename2)
    CopyDirectory.copyFromSharePath(srcFilename2, desFilename)