import os

# cmd = @"REM 设置成UE4Editor-Cmd.exe的路径
UECMDPath = r"D:\Program Files\Epic Games\UE_4.19\Engine\Binaries\Win64\UE4Editor-Cmd.exe"

Pak_Path = r'D:\Program Files\Epic Games\UE_4.19\Engine\Binaries\Win64\UnrealPak.exe'

# REM 设置成项目的地址
ProjectPath = r"G:\Work\TangoAR\TangoAR.uproject"

# REM 设置成平台：IOS,WindowsNoEditor,Android_ETC2...
PlatForm = "IOS"

# %UECMDPath% %ProjectPath% -run=cook -targetplatform=%PlatForm% [-cookonthefly] [-iterate] [-Compressed]"
Cook_CMD = '"' + UECMDPath +'" ' + ProjectPath + ' -run=cook -targetplatform=' + PlatForm + ' [-cookonthefly] [-iterate] [-Compressed]'
# print(Cook_CMD)
# os.system( Cook_CMD )

Pak_CMD = '"' + Pak_Path + '"' + r' C:\Users\chenlei\Desktop\Temp\Paks\Common.pak ' + r'-Create=C:\Users\chenlei\Desktop\Temp\Paks\list.txt'
# print( Pak_CMD )
os.system( Pak_CMD )








