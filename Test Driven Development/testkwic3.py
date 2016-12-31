import kwic

document ="What a time\nto be\nAlive"

numLines = kwic.kwic(document)

for i in range( 0, len(numLines)):
	assert(type(numLines[i]) == tuple)
	