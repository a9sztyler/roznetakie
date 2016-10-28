#import numpy as np

protein = "QIKDLLVSSSTDLDTTLVLVNAIYFKGMWKTAFNAEDTREMPFHVTKQESKPVQMMCMNNSFNVATLPAEKMKILELPFASGDLSMLVLLPDEVSDLERIEKTINFEKLTEWTNPNTMEKRRVKVYLPQMKIEEKYNLTS"

def get_words(input_string, a):
	res = [input_string[i:i+a] for i in range(len(input_string) - a+1)]
	#print len(res)
	return res
                
print get_words(protein, 3)

def check_seqs(db_seq, query, letters_quant):
        match_to_pos_map = {}
        query_triplets = get_words(query, letters_quant)
	for i in range(len(db_seq) - letters_quant + 1):
                if db_seq[i:i+letters_quant] in query_triplets:
                	
                        
