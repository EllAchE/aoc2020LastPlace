data = open("input.txt", "r")
datadict = {}
for line in data:
    line = int(line)
    if datadict.get(line, "None") == "None":
        datadict[2020 - line] = line;
    else:
        print(line*datadict.get(line))
        print("Numbers:", line, datadict.get(line))
