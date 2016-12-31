def kwic(wordstr, ignoreWords = []):
	delete = []

	wordstr= wordstr.splitlines()

	for i in range(0,len(wordstr)):
		wordstr[i]= wordstr[i].split(" ")
		for k in range(0,len(wordstr[i]) - 1):
			newstr = list(wordstr[i])
			for h in range(0, k+1):
				temp = newstr[0]
				for j in range(0, len(newstr) - 1):
					newstr[j] = newstr[j+1]
				newstr[len(newstr) - 1] = temp
			contain = False
			for z in range(0, len(ignoreWords)):
				if ignoreWords[z] == newstr[0]:
					contain = True
			if contain == False: 
				Ntuple = (newstr, i+1)
				wordstr.append(Ntuple)
		test = False
		for z in range (0, len(ignoreWords)):
			if ignoreWords[z] == wordstr[i][0]:
				delete.append(i)
				test = True
		if test == False:
			Ntuple = (wordstr[i], i+1)
			wordstr[i] = Ntuple
	track = 0
	for c in range(0, len(delete)):
		wordstr.pop(delete[c] - track)
		track += 1

	wordstr.sort()
	print wordstr
	return wordstr


