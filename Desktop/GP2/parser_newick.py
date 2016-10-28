drzewo_newick = "(((A, B), C), (D, E))"

def znajdz_litery(sekwencja):
	lista_liter = []
	for element in sekwencja:
		if element.isalpha() == True:
			lista_liter.append(element)

	return lista_liter

def zrob_wycinek(sekwencja):
	for i in range(len(sekwencja)):
		if sekwencja[i] == "A":
			pocz = i
		if sekwencja[i] == "C":
			koniec = i+1

	wycinek = sekwencja[pocz:koniec]
	return wycinek

def licz_nawias(wycinek):
	nawiasy = 0
	for element in wycinek:
		if element in "()":
			nawiasy =+1 

	return nawiasy

print znajdz_litery(drzewo_newick)
print zrob_wycinek(drzewo_newick)
print licz_nawias(zrob_wycinek(drzewo_newick))

