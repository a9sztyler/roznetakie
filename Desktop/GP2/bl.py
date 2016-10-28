import numpy as np

protein = "QIKDLLVSSSTDLDTTLVLVNAIYFKGMWKTAFNAEDTREMPFHVTKQESKPVQMMCMNNSFNVATLPAEKMKILELPFASGDLSMLVLLPDEVSDLERIEKTINFEKLTEWTNPNTMEKRRVKVYLPQMKIEEKYNLTS"

#def get_words(input_string):
  #length = len(input_string)
  #return [input_string[i:j+1] for i in xrange(length) for j in xrange(i,length)]

#print get_words(protein)

def get_words(input_string):
	start = -1
	end = 2
	word = []
	dl = len(protein)
	#print "dl", dl

	while True:
		if end <= dl:
			start += 1
			#print "s", start
			end += 1
			#print "e", end
		else: 
			break

		substring = protein[start:end]
		print "len", len(substring)
		word.append(substring)

	return word


print get_words(protein)



