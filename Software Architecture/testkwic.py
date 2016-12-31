import unittest 

def kwic(string,ignoreWords=[], listPairs=False, periodsToBreaks=False):
    lines = splitBreaks(string, periodsToBreaks)
    LineSplit = LineSplit(lines)
    if listPairs:
        pairs = createPairs(LineSplit)
    shiftedLines = LineShift(LineSplit)
    flattenedLines = flatLine(shiftedLines)
    filteredLines = filterLines(ignoreWords,flattenedLines)
    if not listPairs:
        return RandomSort1(filteredLines)
    else:
        return (filteredLines, pairs)

class TestKwic(unittest.TestCase):
	def test_splitbreaks(self):
		string = "A B C.\nD E?\nF G."
		stringB = "1 2 3. 4 5 6 7!"
		self.assertEqual(splitBreaks(string, False), ['A B C.', 'D E?' , 'F G.'])
		self.assertEqual(splitBreaks(stringB, False), ['1 2 3. 4 5 6 7!'])
	
	def test_splitbreaks_periods(self):
		string = "A B C. D E? F G."
		stringB = "1 2 3. 4 5 6 7!"
		self.assertEqual(splitBreaks(string, True), ['A B C. D E? F G.'])
		self.assertEqual(splitBreaks(stringB, True), ['1 2 3. 4 5 6 7!'])
	
	def test_split_lines(self):
		lines = ['A B C.', 'D E?' , 'F G.']
		linesB = ['1 2 3. 4 5 6 7!']
		self.assertEqual(LineSplit(lines), [['A','B','C.'], ['D','E?'],['F','G.']])
		self.assertEqual(LineSplit(linesB), [['1', '2', '3.','4', '5' ,'6', '7!']])
		
	def test_pairs(self):
		splitL = [['A','B','C.'],['D','E?'],['F','G.']]
		splitL2 =[['1','2','3.','4','5','6','7!']]
		self.assertEqual(createPairs(splitL),{('b', 'c'): 1, ('f', 'g'): 1, ('a', 'b'): 1, ('a', 'c'): 1, ('d', 'e'): 1}) 
		self.assertEqual(createPairs(splitL2),{('3', '6'): 1, ('2', '3'): 1, ('3', '7'): 1, ('5', '7'): 1, ('4', '7'): 1, ('5', '6'): 1, ('6', '7'): 1, ('4', '6'): 1, ('4', '5'): 1, ('1', '6'): 1, ('3', '5'): 1, ('1', '7'): 1, ('1', '4'): 1, ('3', '4'): 1, ('2', '7'): 1, ('1', '5'): 1, ('2', '6'): 1, ('1', '2'): 1, ('2', '5'): 1, ('1', '3'): 1, ('2', '4'): 1})
		
	def test_shifted_lines(self):
		shiftL = [['A','B','C.'],['D','E?'],['F','G.']]
		shiftL2 =[['1','2','3.','4','5','6','7!']]
		self.assertEqual(LineShift(shiftL),[[(['A', 'B', 'C.'], 0), (['B', 'C.', 'A'], 0), (['C.', 'A', 'B'], 0)],
		[(['D', 'E?'], 1), (['E?', 'D'], 1)], [(['F', 'G.'], 2), (['G.', 'F'], 2)]])
		self.assertEqual(LineShift(shiftL2),[[(['1', '2', '3.', '4', '5', '6', '7!'], 0),
		(['2', '3.', '4', '5', '6', '7!', '1'], 0),
		(['3.', '4', '5', '6', '7!', '1', '2'], 0), (['4', '5', '6', '7!', '1', '2', '3.'], 0),
		(['5', '6', '7!', '1', '2', '3.', '4'], 0), 
		(['6', '7!', '1', '2', '3.', '4', '5'], 0), (['7!', '1', '2', '3.', '4', '5', '6'], 0)]] )
	
	def test_flattened_lines(self):
		flatL = [[(['A', 'B', 'C.'], 0), (['B', 'C.', 'A'], 0), (['C.', 'A', 'B'], 0)],
		[(['D', 'E?'], 1), (['E?', 'D'], 1)], [(['F', 'G.'], 2), (['G.', 'F'], 2)]]
		
		flatL2 = [[(['1', '2', '3.', '4', '5', '6', '7!'], 0),
		(['2', '3.', '4', '5', '6', '7!', '1'], 0),
		(['3.', '4', '5', '6', '7!', '1', '2'], 0), (['4', '5', '6', '7!', '1', '2', '3.'], 0),
		(['5', '6', '7!', '1', '2', '3.', '4'], 0), 
		(['6', '7!', '1', '2', '3.', '4', '5'], 0), (['7!', '1', '2', '3.', '4', '5', '6'], 0)]] 
		
		self.assertEqual(flatLine(flatL),[(['A', 'B', 'C.'], 0), (['B', 'C.', 'A'], 0), 
		(['C.', 'A', 'B'], 0), (['D', 'E?'], 1), (['E?', 'D'], 1), (['F', 'G.'], 2), (['G.', 'F'], 2)])
		self.assertEqual(flatLine(flatL2),[(['1', '2', '3.', '4', '5', '6', '7!'], 0), (['2', '3.', '4', '5', '6', '7!', '1'], 0),
		(['3.', '4', '5', '6', '7!', '1', '2'], 0), (['4', '5', '6', '7!', '1', '2', '3.'], 0),
		(['5', '6', '7!', '1', '2', '3.', '4'], 0), (['6', '7!', '1', '2', '3.', '4', '5'], 0), 
		(['7!', '1', '2', '3.', '4', '5', '6'], 0)])
		
	def test_filtered_lines(self):
		filtL = [(['A', 'B', 'C.'], 0), (['B', 'C.', 'A'], 0), 
		(['C.', 'A', 'B'], 0), (['D', 'E?'], 1), (['E?', 'D'], 1), (['F', 'G.'], 2), (['G.', 'F'], 2)]
		
		filtL2 = [(['1', '2', '3.', '4', '5', '6', '7!'], 0), (['2', '3.', '4', '5', '6', '7!', '1'], 0),
		(['3.', '4', '5', '6', '7!', '1', '2'], 0), (['4', '5', '6', '7!', '1', '2', '3.'], 0),
		(['5', '6', '7!', '1', '2', '3.', '4'], 0), (['6', '7!', '1', '2', '3.', '4', '5'], 0), 
		(['7!', '1', '2', '3.', '4', '5', '6'], 0)]
		
		ignoreWords = ['B', '2'] 
		
		self.assertEqual(filterLines(ignoreWords, filtL),[(['A', 'B', 'C.'], 0), (['C.', 'A', 'B'], 0), (['D', 'E?'], 1),
		(['E?', 'D'], 1), (['F', 'G.'], 2), (['G.', 'F'], 2)])
		
		self.assertEqual(filterLines(ignoreWords, filtL2),[(['1', '2', '3.', '4', '5', '6', '7!'], 0),(['3.', '4', '5', '6', '7!', '1', '2'], 0),
		(['4', '5', '6', '7!', '1', '2', '3.'], 0),
		(['5', '6', '7!', '1', '2', '3.', '4'], 0), 
		(['6', '7!', '1', '2', '3.', '4', '5'], 0), 
		(['7!', '1', '2', '3.', '4', '5', '6'], 0)])

	def test_sort_r1(self):
		sortLr = [(['A', 'B', 'C.'], 0), (['C.', 'A', 'B'], 0), (['D', 'E?'], 1),
		(['E?', 'D'], 1), (['F', 'G.'], 2), (['G.', 'F'], 2)]
		
		sortLr2 = [(['1', '2', '3.', '4', '5', '6', '7!'], 0),(['3.', '4', '5', '6', '7!', '1', '2'], 0),
		(['4', '5', '6', '7!', '1', '2', '3.'], 0),
		(['5', '6', '7!', '1', '2', '3.', '4'], 0), 
		(['6', '7!', '1', '2', '3.', '4', '5'], 0), 
		(['7!', '1', '2', '3.', '4', '5', '6'], 0)]
		
		self.assertEqual(RandomSort1(sortLr), [(['A', 'B', 'C.'], 0), (['C.', 'A', 'B'], 0), (['D', 'E?'], 1), (['E?', 'D'], 1), (['F', 'G.'], 2), (['G.', 'F'], 2)])
		self.assertEqual(RandomSort1(sortLr2), [(['1', '2', '3.', '4', '5', '6', '7!'], 0), (['3.', '4', '5', '6', '7!', '1', '2'], 0), (['4', '5', '6', '7!', '1', '2', '3.'], 0), (['5', '6', '7!', '1', '2', '3.', '4'], 0), (['6', '7!', '1', '2', '3.', '4', '5'], 0), (['7!', '1', '2', '3.', '4', '5', '6'], 0)] )
		
	def test_sort_r2(self):
		pairs = {('cool', 'with'): 1, ('and', 'words'): 1, ('and', 'with'): 1, ('pairs', 'with'): 1, ('cool', 'many'): 1, ('many', 'pairs'): 1, 
		('and', 'cool'): 1, ('many', 'words'): 1, ('with', 'words'): 1, ('many', 'with'): 1, ('and', 'pairs'): 1, ('cool', 'words'): 1,
		('pairs', 'words'): 1, ('cool', 'make'): 1, ('cool', 'pairs'): 1, 
		('and', 'make'): 1, ('and', 'many'): 1, ('make', 'words'): 1, ('make', 'with'): 1, ('make', 'many'): 1, ('make', 'pairs'): 1}
		
		
		sortLt = [(['make', 'many', 'cool', 'pairs', 'with', 'many', 'words', 'and', 'cool', 'words'], 0),
		(['many', 'cool', 'pairs', 'with', 'many', 'words', 'and', 'cool', 'words', 'make'], 0),
		(['cool', 'pairs', 'with', 'many', 'words', 'and', 'cool', 'words', 'make', 'many'], 0),
		(['pairs', 'with', 'many', 'words', 'and', 'cool', 'words', 'make', 'many', 'cool'], 0), 
		(['many', 'words', 'and', 'cool', 'words', 'make', 'many', 'cool', 'pairs', 'with'], 0), 
		(['words', 'and', 'cool', 'words', 'make', 'many', 'cool', 'pairs', 'with', 'many'], 0),
		(['cool', 'words', 'make', 'many', 'cool', 'pairs', 'with', 'many', 'words', 'and'], 0),
		(['words', 'make', 'many', 'cool', 'pairs', 'with', 'many', 'words', 'and', 'cool'], 0)]
		
		self.assertEqual(RandomSort2(sortLt, pairs), ([(['cool', 'pairs', 'with', 'many', 'words', 'and', 'cool', 'words', 'make', 'many'], 0), 
		(['cool', 'words', 'make', 'many', 'cool', 'pairs', 'with', 'many', 'words', 'and'], 0), 
		(['make', 'many', 'cool', 'pairs', 'with', 'many', 'words', 'and', 'cool', 'words'], 0),
		(['many', 'cool', 'pairs', 'with', 'many', 'words', 'and', 'cool', 'words', 'make'], 0), 
		(['many', 'words', 'and', 'cool', 'words', 'make', 'many', 'cool', 'pairs', 'with'], 0),
		(['pairs', 'with', 'many', 'words', 'and', 'cool', 'words', 'make', 'many', 'cool'], 0),
		(['words', 'and', 'cool', 'words', 'make', 'many', 'cool', 'pairs', 'with', 'many'], 0), 
		(['words', 'make', 'many', 'cool', 'pairs', 'with', 'many', 'words', 'and', 'cool'], 0)], []))
		
		

def thetest():
	testMain = unittest.TestSuite()
	testMain.addTest(TestKwic('test_splitbreaks'))
	testMain.addTest(TestKwic('test_splitbreaks_periods'))
	testMain.addTest(TestKwic('test_split_lines'))
	testMain.addTest(TestKwic('test_pairs'))
	testMain.addTest(TestKwic('test_shifted_lines'))
	testMain.addTest(TestKwic('test_flattened_lines'))
	testMain.addTest(TestKwic('test_filtered_lines'))
	testMain.addTest(TestKwic('test_sort_r1'))
	testMain.addTest(TestKwic('test_sort_r2'))
	return testMain
		

def shift(line):
    return [line[i:] + line[:i] for i in xrange(0,len(line))]

def cleanWord(word):
    return filter (lambda c: c not in [".",",","?","!",":"], word.lower())

def ignorable(word,ignoreWords):
    return cleanWord(word) in map(lambda w: w.lower(), ignoreWords)

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

def LineSplit(lines):
	return map(lambda l: l.split(), lines)
	
def createPairs(splitL):
	pairs = {}
        for l in splitL:
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

def LineShift(shiftL):
	return [map(lambda x:(x,i), shift(shiftL[i])) for i in xrange(0,len(shiftL))]
	
def flatLine(flatL):
	return [l for subList in flatL for l in subList]
	
def filterLines(ignoreWords,filtL):
	return filter(lambda l: not ignorable(l[0][0], ignoreWords), filtL)
	
def RandomSort1(sortLr):
	return sorted(sortLr, key = lambda l: (map(cleanWord, l[0]),l[1]))
	
def RandomSort2(sortLt, pairs):
	 return (sorted(sortLt, key = lambda l: (map(lambda w:w.lower(), l[0]),l[1])),
                map(lambda wp: (wp, pairs[wp]), sorted(filter(lambda wp: pairs[wp] > 1, pairs.keys()))))

