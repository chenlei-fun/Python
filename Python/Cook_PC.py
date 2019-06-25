import os

# cmd = @"REM 设置成UE4Editor-Cmd.exe的路径
UECMDPath = r"E:\UE_4.19\Engine\Binaries\Win64\UE4Editor-Cmd.exe"

Pak_Path = r'E:\UE_4.19\Engine\Binaries\Win64\UnrealPak.exe'

# REM 设置成项目的地址
ProjectPath = r"F:\UE_Projects\Simple_1\Simple_1.uproject"

# REM 设置成平台：IOS,WindowsNoEditor,Android_ETC2...
PlatForm = "WindowsNoEditor"

# %UECMDPath% %ProjectPath% -run=cook -targetplatform=%PlatForm% [-cookonthefly] [-iterate] [-Compressed]"
Cook_CMD = '"' + UECMDPath +'" ' + ProjectPath + ' -run=cook -targetplatform=' + PlatForm + ' [-cookonthefly] [-iterate] [-Compressed]'
print(Cook_CMD)
os.system( Cook_CMD )

Pak_CMD = '"' + Pak_Path + '"' + r' C:\Users\user\Desktop\Temp\Paks\Simple_1.pak ' + r'-Create=C:\Users\user\Desktop\Temp\Paks\Simple_1.txt'
print(Pak_CMD)
os.system(Pak_CMD)








