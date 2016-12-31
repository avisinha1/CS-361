import kwic

document = "What a time\nto be\nAlive"
expectedLen = len(filter(lambda c:c == "\n", document)) + 1
assert len(kwic.kwic(document)) >= expectedLen




