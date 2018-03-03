transactionDatabase = [ [ 'a','c','e'],['b','c','e'],['a','b','c','e'],['b','e','d'] ]
#this holds the itemsets that frequently occur in the database
# a list of sets
frequencyList = []

#a candidate list - the cardinality of Fk with each element in the database
# a list of sets

candidateList = []

# 1 initialize the frequncy list

#find longest set in database
maxSetLength = 0
for currentSet in transactionDatabase :
    if (len(currentSet)> maxSetLength) :
        maxSetLenght = len(currentSet)
#creating [ set1, set2,... set-maxSetLength] where all these sets are empty

for index in range(maxSetLenght) :
    frequencyList.append(set())

# generate C(1)- candidate list and F(1)- frequency list
candidateMap = {}
for currentSet in transactionDatabase :
    for element in currentSet :
#        print (element)
        if element in candidateMap.keys() :
            candidateMap[element] = candidateMap[element] + 1
        else :
            candidateMap[element] = 1
removeList = [] 
f1 = { i:candidateMap[i] for i in candidateMap if candidateMap[i] != 1 }
print("F1 Map:", f1)
k_1Set = f1.keys()
 
for element in k_1Set :
    print("Common Transaction:", k_1Set)

#print(candidateMap)

#print(frequencyList)
k = 0
while len(frequencyList[k]) != 0  :1

F_0  =  { 'a', 'b', 'c', 'e', 'f' }


F_k  = [ { 'a','b','c' }, {'a','e','f'}, { 'b','c','e'}, {'a','f','c' } ]


# Here k represents the number of elements within Fk
def multiplySet(fk,f0,k) :
	# We want to union the cartesian products betwen the two sets.
	ckplus1 = []
	for f0Element in f0 :
		for ithSet in fk :
			# This option is for the full credit, not taking the hash
			result = ithSet.union(f0Element)
			if len(result) == k+1 :
				checkDuplicateSet(ckplus1,result)

	return ckplus1



# c is something like [ { ... }, { .... } ...  ]
# result is :  { .... }
def checkDuplicateSet(c,result) :
	duplicate = False
	for element in c :
		if element == result :
			duplicate = True
		
	if duplicate == False :
		c.append(result) 

c = multiplySet(F_k,F_0,3)
print(c)

