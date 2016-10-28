import numpy as np

protein = "QIKDLLVSSSTDLDTTLVLVNAIYFKGMWKTAFNAEDTREMPFHVTKQESKPVQMMCMNNSFNVATLPAEKMKILELPFASGDLSMLVLLPDEVSDLERIEKTINFEKLTEWTNPNTMEKRRVKVYLPQMKIEEKYNLTS"

#def get_words(input_string):
  #length = len(input_string)
  #return [input_string[i:j+1] for i in xrange(length) for j in xrange(i,length)]

#print get_words(protein)

def get_words(input_string, word_lenght):
	res = [input_string[i:i + a] for i in range(len(input_string) - a + 1)]
	#print len(res)
	return res
                
print get_words(protein, 11)

def check_seqs(db_seq, res, word_lenght):
	wycinek = db_seq[i:i + b] for i in range(len(db_seq) - b + 1)
	for element in res:
		if wycinek == element:
			cos

	return cos

