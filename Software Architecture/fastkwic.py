
####Improves Kwic by 30 percent based on 8 tests of both the original kwic and fast kwic when running on my qualities.txt which was around 56 kb.

from multiprocessing import Process 

def shift(line):
    return [line[i:] + line[:i] for i in xrange(0,len(line))]

def cleanWord(word):
    return filter (lambda c: c not in [".",",","?","!",":"], word.lower())

def ignorable(word,AvoidWords):
    return cleanWord(word) in map(lambda w: w.lower(), AvoidWords)

def splitBreaks(string, periodsToBreaks):
    if not periodsToBreaks:
        return string.split("\n")
    else:
        line = ""
        lines = []
        lastChar1 = None
        lastChar2 = None
        breakChars = map(chr, xrange(ord('a'),ord('z')+1))
        for c in string:
            if (c == " ") and (lastChar1 == ".") and (lastChar2 in breakChars):
                lines.append(line)
                line = ""
            line += c
            lastChar2 = lastChar1
            lastChar1 = c
        lines.append(line)
        return lines

def splitLines(lines):
    return map(lambda l: l.split(), lines)
    
def createPairs(splitLine, pairs = {}):
    for l in splitLine:
        seen = set([])
        for wu1 in l:
            wc1 = cleanWord(wu1)
            if len(wc1) == 0:
                continue
            for wu2 in l:
                wc2 = cleanWord(wu2)
                if wc1 < wc2:
                    if (wc1,wc2) in seen:
                        continue
                    seen.add((wc1,wc2))
                    if (wc1, wc2) in pairs:
                        pairs[(wc1,wc2)] += 1
                    else:
                        pairs[(wc1,wc2)] = 1
    return pairs


def LinesShift(shiftL):
    return [map(lambda x:(x,i), shift(shiftL[i])) for i in xrange(0,len(shiftL))]
    
def flatLines(flatL):
    return [l for subList in flatL for l in subList]
    
def filtLines(AvoidWords,filtL):
    return filter(lambda l: not ignorable(l[0][0], AvoidWords), filtL)
    
def RandomSort1(sortLr):
    return sorted(sortLr, key = lambda l: (map(cleanWord, l[0]),l[1]))
    
def RandomSort2(sortLt, pairs, p = None):
    i = (sorted(sortLt, key = lambda l: (map(lambda w:w.lower(), l[0]),l[1])))
    if (p != None):
        p.join()
    return (i,map(lambda wp: (wp, pairs[wp]), sorted(filter(lambda wp: pairs[wp] > 1, pairs.keys()))))


def kwic(string,AvoidWords=[], listPairs=False, periodsToBreaks=False):
    lines = splitBreaks(string, periodsToBreaks)
    splitLine = splitLines(lines)
    pairs = {}
    p = Process(target=createPairs, args=(splitLine, pairs))
    if listPairs:
        p.start()
    shiftedLines = LinesShift(splitLine)
    flattenedLines = flatLines(shiftedLines)
    filteredLines = filtLines(AvoidWords,flattenedLines)
    
    if not listPairs:
        return RandomSort1(filteredLines)
    else:
        return RandomSort2(filteredLines, pairs, p)
