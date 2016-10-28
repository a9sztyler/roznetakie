#dystans w modelu J-C, macierz odleglosci pomiedzy tymi sekwencjami, moga byc przerwy

def hd(str1, str2):
	diffs = 0
	for ch1, ch2 in zip(str1, str2):
		if ch1 != ch2:
			diffs += 1
        return diffs












def differences(str1, str2,str3,str4):
	diffs1.2 = 0
	diffs1.3 = 0
	diffs1.4 = 0
	diffs2.3 = 0
	diffs2.4 = 0
	diffs3.4 = 0
	for ch1, ch2, ch3, ch4 in zip(str1, str2, str3, str4):
		if ch1 != ch2:
			diffs1.2 += 1
		elif ch1 != ch3:
			diffs1.2 += 1
		elif ch1 != ch4:
			diffs1.4 += 1
		elif ch2 != ch3:
			diffs1

        return diffs