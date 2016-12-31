import kwic

document = "What a time\n to be\nAlive"

expLen = len(filter(lambda c:c == "\n", document)) + 1 + len(filter(lambda c:c == " ", document))

document = kwic.kwic(document)

assert(len(document) >= expLen)
