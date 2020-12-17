
data = open("input.txt", "r")
# copy the data to a list
lst = [d for d in data]

def process(value):
	result = 2020 - value
	datadict = {}
	for line in lst:
	    line = int(line)
	    if line != value:
		    if datadict.get(line, "None") == "None":
		    	datadict[result - line] = line
		    else:
		        print(line*datadict.get(line)*value)
		        print("Numbers:", line, datadict.get(line), value) 

for line in lst:
	process(int(line))

print 'test'