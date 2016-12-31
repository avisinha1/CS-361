import kwic

document = "What a time\nto be\nAlive"

ignoreWords = ["words"]
output = kwic.kwic(document, ignoreWords)

for i in range (0, len(output)):
	for j in range (0,len(ignoreWords)):
			assert(output[i][0] != ignoreWords[j])