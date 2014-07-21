import xml.etree.ElementTree as ET
import codecs
import MSSQL
import logging
import ConfigParser
import os

def UpdateBOMDrillInfo( CustomerPO, ProductName, fileNameList ):

    cf = ConfigParser.ConfigParser()
    cf.read("app.ini")
    db_host = cf.get("db", "db_host")
    db_name = cf.get("db", "db_name")
    db_user = cf.get("db", "db_user")
    db_pwd = cf.get("db", "db_pwd")

    # print CustomerPO, ProductName, fileNameList
    for fileName in fileNameList:

        myfile = codecs.open( fileName,"r","gb2312")

        str = myfile.read()

        str = str.replace("gb2312", "utf-8")
        str = str.encode("utf-8")

        root = ET.fromstring(str)

        A = False
        B = False

        for FaceA in root.iter("FaceA"):
            if len(FaceA) > 0:
                A = True

        for FaceB in root.iter("FaceB"):
            if len(FaceB) > 0:
                B = True

        HoleFlag = ""
        if A and not B:
            logging.info(" %s = %s" %(fileName, "A"))
            HoleFlag = "A"
        elif B and not A:
            logging.info(" %s = %s" %(fileName, "B"))
            HoleFlag = "B"
        elif A and B:
            logging.info(" %s = %s" %( fileName, "C"))
            HoleFlag = "C"
        else:
            HoleFlag = ""
            logging.info( " %s = %s" %( fileName, " "))


        ms = MSSQL.MSSQL(host=db_host, user=db_user, pwd=db_pwd, db=db_name)

        sql = """
        Update ERP_ComponentBase set ERP_ComponentBase.HolesOtherSurface = '{{HoleFlag}}'
        from PurchaseOrders
        inner join POLineItems on PurchaseOrders.POID = POLineItems.POID
        inner join ProductNames on POLineItems.ProductID = ProductNames.ProductID and ProductNames.CurrentFlag = 'Y'
        inner join ProductNameMC on ProductNames.ProductNameID = ProductNameMC.ProductNameID and CultureID = 2
        inner join ERP_BOM on ProductNames.ProductID = ERP_BOM.ProductID
        inner join ERP_BOMComponent on ERP_BOMComponent.BOMID = ERP_BOM.BOMID
        inner join ERP_ComponentBase on ERP_BOMComponent.ComponentID = ERP_ComponentBase.ComponentID
        where CustomerPO = '{{CustomerPO}}'
        and ProductNameMC.ProductName like '{{ProductName}}%'
        and HolesOneSurface = '{{HoleOneSerface}}'

        Update ERP_BOMHistory set ERP_BOMHistory.HolesOtherSurface = '{{HoleFlag}}'
        from PurchaseOrders
        inner join POLineItems on PurchaseOrders.POID = POLineItems.POID
        inner join ProductNames on POLineItems.ProductID = ProductNames.ProductID and ProductNames.CurrentFlag = 'Y'
        inner join ProductNameMC on ProductNames.ProductNameID = ProductNameMC.ProductNameID and CultureID = 2
        inner join ERP_BOM on ProductNames.ProductID = ERP_BOM.ProductID
        inner join ERP_BOMComponent on ERP_BOMComponent.BOMID = ERP_BOM.BOMID
        inner join ERP_BOMHistory on ERP_BOMComponent.ComponentID = ERP_BOMHistory.ComponentID
        where CustomerPO = '{{CustomerPO}}'
        and ProductNameMC.ProductName like '{{ProductName}}%'
        and HolesOneSurface = '{{HoleOneSerface}}'  """

        sql = sql.replace("{{HoleFlag}}", HoleFlag)
        sql = sql.replace("{{CustomerPO}}", CustomerPO)
        sql = sql.replace("{{ProductName}}", ProductName)

        fileNameWithoutPath = os.path.basename(fileName)

        sql = sql.replace("{{HoleOneSerface}}", fileNameWithoutPath.replace(".bd",""))

        # logging.info(sql)

        ms.ExecNonQuery(sql)



