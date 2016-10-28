seq1 = "ATGCAT"
seq2 = "ATGAGA"

rows = len(seq1) + 1
cols = len(seq2) + 1

match = 2
mismatch = -1
gap = -1


def build_matrix(rows, cols):

	scoring_matrix = [[0 for col in range(cols)] for row in range(rows)]

	return scoring_matrix


print build_matrix(rows, cols)