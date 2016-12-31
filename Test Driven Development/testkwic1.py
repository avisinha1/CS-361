import kwic

document = "What a time\nto be\nAlive" 

expLen = 1 + len(filter(lambda c:c == "\n", document)) + len(filter(lambda c:c == " ", document))

totalCount = 0

for i in range (0,len(kwic.kwic(document))):
	totalCount += len((kwic.kwic(document))[i])
assert totalCount >= expLen 





