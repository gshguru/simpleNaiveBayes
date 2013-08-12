import sys
totalDocs = 0; Y = dict(); HashTable = dict()

def updateHashTable(currentDoc):  
	if Y.has_key(currentDoc[-1]): Y[currentDoc[-1]] += 1
	else: Y[currentDoc[-1]] = 1
	for j in range(0,len(currentDoc)-1):		
		if (HashTable.has_key(str(currentDoc[-1]+currentDoc[j]))): 
			HashTable[str(currentDoc[-1]+currentDoc[j])] += 1
		else:   HashTable[str(currentDoc[-1]+currentDoc[j])] = 1

def test(X):
	probabilities = list()	
	for key, value in Y.iteritems():
		Prob = Y[key]/totalDocs 	# initializing with prior
		for j in range( 0, len(X)-1 ): 	# features			
			try: Prob *= HashTable[ str(key + X[j]) ] / float(Y[key]) 
			except KeyError: Prob = 0; break # if combination is not found in the hash table
		probabilities.append( [key,Prob] )		
	for result in probabilities: print result[0],"-", result[1],";",

dataFile = open(sys.argv[1], "rb") # train
for line in dataFile: updateHashTable(line[:-2].split(",")); totalDocs += 1
dataFile = open(sys.argv[2], "rb") # test
for line in dataFile: test(line[:-2].split(",")); print ""
