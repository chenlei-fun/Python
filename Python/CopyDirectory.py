import sys, os, re, zipfile, time

def copyFileDir(srcFilename, desFilename):
    status = False
    try:
        fileList = os.listdir(srcFilename)
        for eachFile in fileList:
            sourceF = os.path.join(srcFilename, eachFile)
            targetF = os.path.join(desFilename, eachFile)

            if os.path.isdir(sourceF):
                if not os.path.exists(targetF):
                    os.makedirs(targetF)
                status = copyFileDir(sourceF, targetF)
            else:
                status = copyFile(sourceF, targetF)
    except Exception as e:
        print(e)
        status = False
    finally:
        print('copyFileDir function is quit!')
    return status


def copyFile(srcFilename, desFilename):
    status = False
    copyCommand = 'copy %s %s' % (srcFilename, desFilename)

    try:
        if (os.popen(copyCommand)):  # 不用op.system(copyCommand),因为这个会弹出命令行界面
            print('copy done!')
            status = True
        else:
            print('copy failed!')
            status = False
    except Exception as e:
        print(e)
        status = False
    finally:
        print('copyFile function is quit!')
    return status

def copyFromSharePath(srcFilename, desFilename):
    if not os.path.exists(srcFilename):
        print('no found ' + srcFilename)
        return False
    if not os.path.exists(desFilename):
        print('no found ' + desFilename)
        os.makedirs(str(desFilename))
        print('create ' + desFilename)

    copyStatus = False
    if os.path.isdir(srcFilename):
        copyStatus = copyFileDir(srcFilename, desFilename)
    else:
        copyStatus = copyFile(srcFilename, desFilename)
    return copyStatus

def zip_files( files, zip_name ):
    zip = zipfile.ZipFile( zip_name, 'w', zipfile.ZIP_DEFLATED )
    for file in files:
        print ('compressing', file)
        zip.write( file )
    zip.close()
    print ('compressing finished')

#
# # 打包成zip文件
# import zipfile
#
# f = zipfile.ZipFile('archive.zip', 'w', zipfile.ZIP_DEFLATED)
# f.write('file_to_add.py')
# f.close()
#
# # 从zip文件解包
# zfile = zipfile.ZipFile('archive.zip', 'r')
# for filename in zfile.namelist():
#     data = zfile.read(filename)
#     file = open(filename, 'w+b')
#     file.write(data)
#     file.close()

# 把整个文件夹内的文件打包
def zipFolder( startdir, desdir ):
    f = zipfile.ZipFile(desdir, 'w', zipfile.ZIP_DEFLATED)
    # startdir = "c:\\mydirectory"
    for dirpath, dirnames, filenames in os.walk(startdir):
        for filename in filenames:
            f.write(os.path.join(dirpath, filename))
            print( filename )
    f.close()

def main(argv=sys.argv):
    if not len(argv) == 3:
        print('input parameters\'s count should be 3,not %s' % (len(argv)))
        return
    print(u'脚本名字是：' + argv[0])
    srcFilename = argv[1]
    print(u'源目录：' + argv[1])
    desFilename = argv[2]
    print(u'目标目录：' + argv[2])

    if os.path.isdir(srcFilename):
        if os.path.isfile(desFilename):
            print('can not copy a folder to a file')
            return
    copyFromSharePath(srcFilename, desFilename)


if __name__ == '__main__':
    # hostIp = '192.168.10.16'
    # sharePath = '\\VM_Projects\MYI_Models\Wealin\220-107793'
    # filename = 'xxx'

    resultStr = []
    resultStr.append([])
    # srcFilename = r'\\192.168.10.16\VM_Projects\MYI_Models\Wealin\220-107793'

    # folder_to_zip = r"\\192.168.10.16\VM_Projects\Apache24\htdocs\Web3D"
    folder_to_zip = r"\\192.168.10.16\VM_Projects\Project\modelviewer\web"

    zipFilename = '%s%s%s' %(r'\\192.168.10.16\VM_Projects\Project\modelviewer\web',time.strftime("_%y%m%d",time.localtime()),'.zip')
    zipFolder( folder_to_zip, zipFilename )

    srcFilename = r"\\192.168.10.16\VM_Projects\Project\modelviewer\web" + time.strftime("_%y%m%d",time.localtime()) + '.zip'
    # desFilename = r'C:\Users\chenlei\Desktop\Temp'
    desFilename = r'D:\Temp'

    cmd = [
        r'G:\_Projects\Python\CopyDirectory.py',
        srcFilename,
        desFilename
    ]
    main(cmd)
    print ('ok' )