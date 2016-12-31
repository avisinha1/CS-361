import kwic

document = "What a time\nto be\nAlive"

numLines = kwic.kwic(document)

for i in range (0, len(numLines) - 1):
	assert (numLines[i][0][0][0].lower() <= numLines[i+1][0][0][0].lower())
	