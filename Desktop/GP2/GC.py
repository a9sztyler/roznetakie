from collections import Counter
import matplotlib.pyplot as plt

with open ("Sta.fna", "r") as sekwencja:
	sekwencja = sekwencja.read().splitlines() 
	sekwencja2 = ''.join(sekwencja)


dl = len(sekwencja2)	
start = 0
end = 1000
content = []

while True:
	if end <= dl:
		start += 1000
		#print "start", start
		end += 1000 
		#print "end", end
	else: 
		break

	counter = Counter(sekwencja2[start:end])
	C = counter['C']
	G = counter['G']
	total = float(C+G)/1000
	print "total", total
	content.append(total)


#print "content", content
#print "total", total
print "dl", dl

plt.plot(content)
plt.show()









