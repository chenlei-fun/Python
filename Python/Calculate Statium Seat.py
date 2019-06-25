# LT Corner = ( 367, 78 )
# RD Corner = ( 535, 144 )
# LT Row = 23
# LT Col = 1
# RD Row = 20
# RD Col = 13

# Area = "A"
# LT_Corner = (367, 78)
# RD_Corner = (535, 144)
# LT_Row = 23
# LT_Col = 1
# RD_Row = 20
# RD_Col = 13



def Calculate_Seat(area, row, row1, col, x,y,x1,y1, file_output):
    Area = area
    # LT_Corner = (367, 166)
    # RD_Corner = (563, 562)
    LT_Corner = (x, y)
    RD_Corner = (x1, y1)
    LT_Row = row
    RD_Row = row1

    LT_Col = 1
    RD_Col = 1
    str_col = str(col)
    print(str_col)
    if( str_col.find("-")>= 0 ):
       LT_Col = int(str_col.split("-")[0])
       RD_Col = int(str_col.split("-")[1])
    else:
        LT_Col = int(str_col)

    Row_Count = abs(LT_Row - RD_Row) + 1
    Col_Count = abs(RD_Col - LT_Col) + 1

    print("Left Top Corner:{},{}".format(LT_Corner[0], LT_Corner[1]))
    print("Right Down Corner:{},{}".format(RD_Corner[0], RD_Corner[1]))
    print("Row_Count:" + str(Row_Count))
    print("Col_Count:" + str(Col_Count))

    for row_space in range(0,Row_Count):
        for col_space in range(0, Col_Count):
            x_value = LT_Corner[0] + col_space*( RD_Corner[0] - LT_Corner[0])/(Col_Count-1)
            if Row_Count == 1:
                y_value = LT_Corner[1]
            else:
                y_value = LT_Corner[1] + row_space * (RD_Corner[1] - LT_Corner[1]) / (Row_Count - 1)
            # print("Area:{}, Row:{}, Col:{} x:{}, y:{}".format(Area, LT_Row+row_space, LT_Col+col_space, x_value, y_value))
            # print("{},{},{},{},{}".format(Area, LT_Row+row_space, LT_Col - col_space, round(x_value,1), round(y_value,1)))
            print("{},{},{},{},{}".format(Area, LT_Row+row_space, LT_Col - col_space, round(x_value,1), round(y_value,1)), file=file_output)




file_name = "update"
file = open(file_name + ".txt")
file_output = open(file_name + "_output.txt", "w")
print("area,row,col,x,y", file=file_output)
while 1:
    line = file.readline()
    if not line:
        break
    list1 = line.split()
    print (list1)
    Calculate_Seat(list1[0],int(list1[1]),int(list1[2]),str(list1[3]),float(list1[4]),float(list1[5]),float(list1[6]),float(list1[7]), file_output)

file_output.close()




