file = open("district_data.txt")
while 1:
    line = file.readline()
    if not line:
        break
    print( line.split())
