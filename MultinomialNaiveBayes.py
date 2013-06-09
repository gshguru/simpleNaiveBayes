import sys
totalDocs = 0; Y = dict(); featureValues = set(); nayaHashTable = dict()

def updateHashTable(currentDoc):  
	if Y.has_key(currentDoc[-1]):Y[currentDoc[-1]] += 1
	else: Y[currentDoc[-1]] = 1
	for j in range(0,len(currentDoc)-1):
		featureValues.add(currentDoc[j])
		if (nayaHashTable.has_key(str(currentDoc[-1]+currentDoc[j]))): nayaHashTable[str(currentDoc[-1]+currentDoc[j])] += 1
		else: nayaHashTable[str(currentDoc[-1]+currentDoc[j])] = 1

def test(X):
	probabilities = list()	
	for key, value in Y.iteritems():
		Prob = 1
		for j in range(0,len(X)-1): #features			
			try: Prob *= nayaHashTable[str(key +X[j])] / float(Y[key])		
			except KeyError: Prob = 0;
		probabilities.append([key,(Prob*Y[key]/totalDocs)])		
	for result in probabilities: print result[0],"-", result[1],";",

dataFile = open(sys.argv[1], "rb") #train
for line in dataFile: updateHashTable(line[:-2].split(",")); totalDocs += 1
dataFile = open(sys.argv[2], "rb") 
for line in dataFile: test(line[:-2].split(",")); print ""
