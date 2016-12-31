
import eventspec

es = eventspec.EventSpec("kwic.fsm")

class kwic:
    def __init__(self,ignoreWords = [], periodsToBreaks = False):
		es.event("callConstructor")
		self.string = ""
		self.splitLines = []
		self.shiftedLines = []
		self.pairs = {}
		self.ignoreWords = ignoreWords
		self.periodsToBreaks = periodsToBreaks

    
    def addText(self, stringInput):
        es.event("callAddText")
        self.string += stringInput


    def shift(self, line):
        return [line[i:] + line[:i] for i in xrange(0,len(line))]

    def cleanWord(self, word):
        return filter (lambda c: c not in [".",",","?","!",":"], word.lower())

    def ignorable(self, word):
        return self.cleanWord(word) in map(lambda w: w.lower(), self.ignoreWords)

    def splitBreaks(self):
        if not self.periodsToBreaks:
            return self.string.split("\n")
        else:
            line = ""
            lines = []
            lastChar1 = None
            lastChar2 = None
            breakChars = map(chr, xrange(ord('a'),ord('z')+1))
            for c in self.string:
                if (c == " ") and (lastChar1 == ".") and (lastChar2 in breakChars):
                    lines.append(line)
                    line = ""
                line += c
                lastChar2 = lastChar1
                lastChar1 = c
            lines.append(line)
            return lines

    def getFlatLines(self):
        self.flattenedLines = [l for subList in self.shiftedLines for l in subList]

    def getShiftLines(self):
        self.shiftedLines = [map(lambda x:(x,i), self.shift(self.splitLines[i])) for i in xrange(0,len(self.splitLines))]

    def listPairs(self):
        es.event("callListPairs")
        self.getPairs()
        return self.pairs

    def getFilterLines(self):
        self.filteredLines = filter(lambda l: not self.ignorable(l[0][0]), self.flattenedLines)


    def getLines(self):
        self.lines = self.splitBreaks()

    def getSplitLines(self):
        self.splitLines = map(lambda l: l.split(), self.lines)

    def getPairs(self):
        self.pairs = {}
        for l in self.splitLines:
            seen = set([])
            for wu1 in l:
                wc1 = self.cleanWord(wu1)
                if len(wc1) == 0:
                    continue
                for wu2 in l:
                    wc2 = self.cleanWord(wu2)
                    if wc1 < wc2:
                        if (wc1,wc2) in seen:
                            continue
                        seen.add((wc1,wc2))
                        if (wc1, wc2) in self.pairs:
                            self.pairs[(wc1,wc2)] += 1
                        else:
                            self.pairs[(wc1,wc2)] = 1

    def index(self):
        es.event("callIndex")
        self.getLines()
        self.getSplitLines()
        self.getShiftLines()
        self.getFlatLines()
        self.getFilterLines()
        return sorted(self.filteredLines, key = lambda l: (map(self.cleanWord, l[0]),l[1]))

    def reset(self):
        es.event("callReset")
        self.string = ""
        self.index()
        self.listPairs()
