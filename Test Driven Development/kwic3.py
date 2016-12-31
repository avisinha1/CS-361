def kwic(wordstr):
	wordstr = wordstr.splitlines()

	for i in range(0, len(wordstr)):
		wordstr[i] = wordstr[i].split(" ")

		for j in range(0, len(wordstr[i]) - 1):
			rotStr = list(wordstr[i])

			for k in range(0, j+1):
				temp = rotStr[0]

				for l in range( 0, len(rotStr) - 1):
					rotStr[l] = rotStr[l+1]

				rotStr[len(rotStr) -1] = temp
			Ntuple = ((rotStr), i + 1)
			wordstr.append(Ntuple)
		Ntuple = (wordstr[i], i+1)
		wordstr[i] = Ntuple

	print wordstr
	return wordstr

