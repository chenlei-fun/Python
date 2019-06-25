import json
import pickle

product_list = ['210-109061'
,'210-109062'
,'210-106002'
,'210-106098'
,'210-106124'
,'210-107706'
,'210-108202'
,'210-108796'
,'210-108876'
,'210-109129'
,'230-107791'
,'230-107795'
,'230-107816'
,'230-108211'
,'230-108758'
,'265-105485'
,'265-105486'
,'265-105488'
,'265-105522'
,'265-105523'
,'265-105524'
,'265-105525'
,'265-105526'
,'265-105527'
,'265-105537'
,'265-105538'
,'265-105998'
,'265-106015'
,'265-106016'
,'265-106017'
,'265-106021'
,'265-106023'
,'265-106024'
,'265-106044'
,'265-106423'
,'265-106903'
,'265-106904'
,'265-107277'
,'265-107475'
,'265-107487'
,'265-107488'
,'265-107490'
,'265-107562'
,'265-107563'
,'265-107710'
,'265-107711'
,'265-107860'
,'265-107906'
,'265-107907'
,'265-107972'
,'265-108643'
,'265-108723'
,'265-109120'
,'265-109130'
,'290-105990'
,'290-105991'
,'290-105992'
,'290-106134'
,'365-105989'
]
# for i in product_list:
#     print(i)
# print( product_list)

# path = "F:\\To-Delete\\{}.json"

def Get_Options( fullpath ):
    file = open(fullpath, 'r')
    load_dict = json.load( file )

    # print(load_dict)
    Mesh = load_dict["Meshs"]
    Option_String = []
    # print (Mesh)
    for i in Mesh:
        if( i.__contains__( "OptionType" ) and i["OptionType"]=="Fabric" ):
            for j in  i["Options"] :
                Option_String.append(j["base"]["textureName"])

    return Option_String

for product_id in product_list:
    path = "G:\Web3D_180918\Web3D - 180918\Products\{}\{}.json".format(product_id, product_id)
    # print( "{} - {}".format( product_id, Get_Options(path)).replace("[","").replace("]","").replace("'", ""))
    print("{}".format(Get_Options(path)).replace("[", "").replace("]", "").replace("'", ""))

