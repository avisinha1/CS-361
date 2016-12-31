def shift(line): 
    return [line[i:] + line[:i] for i in xrange(0,len(line))] 

def cleanWord(word):
    return filter (lambda c: c not in [".",",","?","!",":"], word.lower())

def ignorable(word,ignoreWords):
    return cleanWord(word) in map(lambda w: w.lower(), ignoreWords)

def splitBreaks(string, periodsToBreaks): #every period have a line break, takes file and breaks it down
    if not periodsToBreaks:
        return string.split("\n")
    else:
        line = "" #input
        lines = []
        lastChar1 = None #null
        lastChar2 = None
        breakChars = map(chr, xrange(ord('a'),ord('z')+1)) #applying chr(integer to ascii), ord is opposite of chr, map them all to the function from a to z
        for c in string:
            if (c == " ") and (lastChar1 == ".") and (lastChar2 in breakChars): #keep track of last 2 characters and once we get to space, break the characters
                lines.append(line) #append b/c everytime we loop it stores in a new line
                line = "" 
            line += c #adding by character to character then appending the line
            lastChar2 = lastChar1
            lastChar1 = c 
        lines.append(line) 
        return lines 

def kwic(string,ignoreWords=[], listPairs=False, periodsToBreaks=False):
    lines = splitBreaks(string, periodsToBreaks) #lines is list of entire text broken by either the new line or period
    splitLines = map(lambda l: l.split(), lines) #another list, calling the function lambda l:, argument into the function,
    if listPairs:
        pairs = {} 
        for l in splitLines: #array of an array of words, for loop iterates over each array
            seen = set([])
            for wu1 in l: #iterates over each word
                wc1 = cleanWord(wu1) #lowercase word, and remove puncutation 
                if len(wc1) == 0: 
                    continue #go to next iteration
                for wu2 in l: #wu2 is a second word in l, goes through twice so u compare with another word
                    wc2 = cleanWord(wu2) #function has 2 possibilites, if it is then it is included in the ending list, if it isnt then it isn't
                    if wc1 < wc2: #forces tuples to sort, compare words, so lower alphabetized letter is first, and if they are the same, then moves on to the next letter in the words, also doesn't allow something to be added twice
                        if (wc1,wc2) in seen: 
                            continue
                        seen.add((wc1,wc2))
                        if (wc1, wc2) in pairs:
                            pairs[(wc1,wc2)] += 1 #defining an element in the dictionary to equal 1
                        else:
                            pairs[(wc1,wc2)] = 1
    shiftedLines = [map(lambda x:(x,i), shift(splitLines[i])) for i in xrange(0,len(splitLines))] #shifted lines produces all circular shifts
    flattenedLines = [l for subList in shiftedLines for l in subList] #flattens a list of a list to a list, instead of having 2 separate lists, it combines it into 1
    filteredLines = filter(lambda l: not ignorable(l[0][0], ignoreWords), flattenedLines) #if it can ignore the it will be true, if it can't then false
    if not listPairs:
        return sorted(filteredLines, key = lambda l: (map(cleanWord, l[0]),l[1])) #return the list and then cleaning
    else:
        return (sorted(filteredLines, key = lambda l: (map(lambda w:w.lower(), l[0]),l[1])),
                map(lambda wp: (wp, pairs[wp]), sorted(filter(lambda wp: pairs[wp] > 1, pairs.keys()))))
