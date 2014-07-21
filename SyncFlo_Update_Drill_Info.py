__author__ = 'Administrator'

import os
import DrillInfoProcess
import logging
import time
import ConfigParser
import re

from datetime import datetime, timedelta

try:

    logging.basicConfig(filename='app.log',level=logging.DEBUG, format='%(asctime)s %(levelname)-8s %(message)s')

    # s = os.getcwd()
    cf = ConfigParser.ConfigParser()
    cf.read("app.ini")
    directory = cf.get("init", "default_dir")
    day_to_update = cf.getint("init", "day_to_update")
    dir_format = cf.get("init", "dir_format")

    logging.info(" --------------------------------------------------------------")
    logging.info(" Start!")

    PODirList = []
    listDir = os.listdir(directory)

    # logging.info(directory)
    # logging.info(listDir)
    pattern = re.compile(dir_format)

    for item in listDir:
        absPath = os.path.join( directory ,item )
        if os.path.isdir( absPath ) and pattern.match(item):
            fileCreateDate = os.path.getctime(absPath)
            tillTime = datetime.today() - timedelta( days = day_to_update )
            todaystr = "%s-%s-%s" %( tillTime.year, tillTime.month, tillTime.day )
            today = time.mktime( time.strptime( todaystr,'%Y-%m-%d'))
            # logging.info( item )
            if( fileCreateDate > today ):
                PODirList.append(item)
                logging.info(" Find Directory:  %s", item)
        else:
            logging.info("*Wrong Directory:  %s", item)

    if not os.path.exists("Dir_List.txt"):
        f = open("Dir_List.txt", "w")
        f.close()

    fp = open("Dir_List.txt", "r")
    ProcessedDirString = fp.read()
    fp.close()

    fp = open("Dir_List.txt", "a")

    # print ProcessedDirString
    for PODir in PODirList:

        if PODir in ProcessedDirString:
            continue

        fileNameList = []
        absPODir = os.path.join(directory, PODir)
        fileList = os.listdir( absPODir)
        for file in fileList:
            # print file
            filePath = os.path.join( absPODir, file)
            if os.path.isfile( filePath ):
                fileNameList.append(filePath)
        DrillInfoProcess.UpdateBOMDrillInfo(PODir.split("_")[0], PODir.split("_")[1], fileNameList)
        fp.write( str(datetime.today()))
        fp.write( "    " + PODir + "\n")
        logging.info(" Success!")
    fp.close()

except Exception as e:
    logging.error(e)









