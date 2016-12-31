def kwic(wordstr):
		wordstr = wordstr.splitlines()

		for i in range(0,len(wordstr)):
				wordstr[i] = wordstr[I].split(" ")

				for j in range(0, len(wordstr[i]) - 1):
					rotStr = list(wordstr[i])

					for k in range(0, j+1):
							temp = rotStr[0]

							for l in range( 0, len(rotStr) - 1):
								rotStr[l] = rotStr[l+1]
							rotStr[len(rotStr) -1] = temp

						wordstr.append(rotStr)

				for newLine in range( 0, len(wordstr) - 1):
					print wordstr[newLine], "\n"
				return wordstr
