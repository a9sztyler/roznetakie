from Bio import SeqIO
import math

def is_different(t=10.0):
	return math.log(float(0.25+(0.75*math.exp(-t))))

def is_equal(t=10.0):
	return math.log(float(0.25+(0.25*math.exp(-t))))


def get_jukes_cantor_prob(seq1, seq2, t):
	seq_len = len(str(seq1))
	p_s = 0
	for i in range(seq_len):
		if seq1[i] != seq2[i]:
			p = is_different(t)
		else:
			p = is_equal(t)
		
		p_s += p
	
	return p_s

def get_jukes_cantor_dist(seq1, seq2):
	seq_len = len(str(rec1.seq))
	cnt = 0
	for i in range(seq_len):
		if rec1.seq[i] != rec2.seq[i]:
			cnt+=1
	dist = calc_dist(cnt, seq_len)
	return dist

def calc_dist(diffs, seq_len):
	dist = -0.75 * math.log(1 - (4.0 / 3.0) * 
                                  (float(diffs) / float(seq_len)), math.e)
	return dist
				
if __name__ == "__main__":
	infile = "sequences.fas"
	matr = []
	for rec1 in SeqIO.parse(open(infile, "rU"), "fasta"):
		mati = []
		for rec2 in SeqIO.parse(open("sequences.fas", "rU"), "fasta"):
			prob = get_jukes_cantor_prob(rec1.seq, rec2.seq, 10.0)
			dist = get_jukes_cantor_dist(rec1.seq, rec2.seq)
			mati.append(str(dist))
		matr.append(mati)

	for line in matr:
		print " ".join(line)
			


		
