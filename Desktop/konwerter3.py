#!/usr/bin/python
# -*- coding: utf-8 -*-


import argparse

class konwerter1(): 
  

	def __init__(self):
                
		self.data = [] 
		self.chrom = []
		self.start = []
		self.end = []
        	self.values = [[] for x in range(1000)] #lista list wartosci dla poszczegolnych chromosomow
		self.info = []
		self.track = ""
                self.output = []
                self.filename = ""
                self.step = []
                self.span = []


	def open_file(self):
		
		file1 = open(self.filename, 'r')
		self.data = file1.readlines() 
		file1.close()

                for i in self.data:
			print i
                        if "fixedStep" in i:
                                return "fixedStep", self.filename
                        elif "variableStep" in i:
                                return "variableStep", self.filename
                        elif "bedGraph" in i:
                                return "bedGraph", self.filename
		
		
	def parser(self):
		
		parser = argparse.ArgumentParser() 
		parser.add_argument("-n", "--file_name", required = True, dest = "name", help = "Name of file")

       		args = parser.parse_args()
 
       	 	self.filename = args.name
       	

        def read_BG(self):
	

		a = 0 #iteracja po wartosciach self.chrom
		b = 0 #iteracja po listach w self.values
                for n in range(len(self.data)):
                        if self.data[n][:5] != "track": 
                                line = self.data[n].split()
                                self.chrom.append(line[0]) 
                                self.start.append(line[1]) 
                                self.end.append(line[2])	
                                if len(self.chrom) >= 2 and self.chrom[a-1] != self.chrom[a]: #wartosci zapisywane do nastepnej listy(nowy chromosom)
					b += 1						  	
				self.values[b].append(line[3])
				a += 1
                        elif self.data[n].startswith("track"):
                                self.track = self.data[n]
		
		self.values = filter(None, self.values)
		#print "chrom", self.chrom
		#print "start", self.start
		#print "end", self.end
		print "values", self.values
                        
                                
        def write_FS(self):
  
                self.track = self.track.replace("bedGraph", "wiggle_0")
                self.output.append(self.track)

                temp = ""
                a = 0 # iteracja po listach self.values
                b = 0 # iteracja po elementach list
                print self.values
                for i in range(len(self.chrom)):
			print len(self.chrom)
			if i == len(self.chrom)-1: 
			      temp = "fixedStep chrom=" + self.chrom[i] +  " start=" + self.start[i] + " step=" + str(1)+ " span=" + str(int(self.end[i]) - int(self.start[i])) + "\n"
			      self.output.append(temp) 
			      self.output.append((str(float(self.values[a][b])) + "\n")) 
			else:
			      temp = "fixedStep chrom=" + self.chrom[i] +  " start=" + self.start[i] + " step=" + str(int(self.start[i+1]) - int(self.start[i])) + " span=" + str(int(self.end[i]) - int(self.start[i])) + "\n"
			      self.output.append(temp)
			      self.output.append((str(float(self.values[a][b])) + "\n"))
			      b += 1
			      temp = ""
			      if self.chrom[i] != self.chrom[i+1]: #przejscie do nastepnego chromosomu, nastepna lista, element pierwszy
				      a += 1
				      b = 0
			    
                self.savefile(".wig")
                

        def read_FS(self):

		a = -1 #self.values od 0 listy
                for n in self.data:
                        if n.startswith("fix"):
                                line = n.split()
                                ab = line[1].split("=")
                                self.chrom.append(ab[1])
				sta = line[2].split("=")
                                self.start.append(sta[1])
                                st = line[3].split("=")
                                self.step.append(st[1])
                                sp = line[4].split("=")
                                self.span.append(sp[1])
                                a += 1
                        elif n.startswith("track"):
                                self.track = n                               
                        elif n[0].isdigit() is True or n.startswith("-"):
                                self.values[a].append(n.strip())
		
		self.values = filter(None, self.values)
		print "chrom", self.chrom
		print "start", self.start
		print "step", self.step
		print "span", self.span
		print "values", self.values

        def write_BG(self, formatname):
                
                self.track = self.track.replace("wiggle_0", "bedGraph")
                self.output.append(self.track)
		
		for i in range(len(self.start)): #numeracja BG
			self.start[i] = int(self.start[i]) - 1
		
		print self.start
		print self.step
		
		
		if formatname == "variableStep": #rozna liczba start i step
			a = 0
			for i in range(len(self.values)):
				for j in range(len(self.values[i])):
					self.end.append(int(self.start[a])+int(self.span[i]))
					a += 1
		else:
			for i in range(len(self.start)):
				self.start[i] = int(self.start[i])+int(self.step[i])
				self.end.append(int(self.start[i])+int(self.span[i]))

		#print len(self.step)
		#print len(self.start)
		#print len(self.end)
		#print self.end

		a = 0 #self.chrom
		b = 0 #n start != n end
		temp = ""
		print len(self.values)
		
		for chrom in self.values:
			print len(chrom)
			for number in chrom:
				temp = self.chrom[a] + " " + str(self.start[b]) + " " + str(self.end[b]) + " " + number + "\n"
				self.output.append(temp)
				temp = ""
				if formatname == "variableStep":
					b += 1
			if formatname == "fixedStep": 
				b += 1
			a += 1		      
			      
                self.savefile(".bedgraph")          
                        
                        
        def read_VS(self):
		
		a = 0 #index list self.values
		for n in self.data:
                        if n.startswith("var"):
                                line = n.split()
                                ab = line[1].split("=")
                                self.chrom.append(ab[1])
                                sp = line[2].split("=")
                                self.span.append(sp[1])
                                a += 1
                        elif n.startswith("track"):
                                self.track = n                               
                        elif n[0].isdigit() is True:
				line = n.split()
				self.start.append(line[0])
				self.values[a].append(line[1]) 
		
		self.values = filter(None, self.values)
		print "chrom", self.chrom
		print "start", self.start
		print "values", self.values
		print "span", self.span	
        

        def savefile(self, fileformat):

                file2 = open("output" + fileformat, "w")
                file2.writelines(self.output)
                file2.close()

                               
def main():
        
	konwerter2 = konwerter1() 
	konwerter2.parser()
	fileformat, name = konwerter2.open_file()
	print fileformat
	print name
        
        if "bedgraph" in name:
                konwerter2.read_BG()
                konwerter2.write_FS()
        elif "fixedStep" in fileformat:
                konwerter2.read_FS()
		konwerter2.write_BG("fixedStep")
        elif "variableStep" in fileformat:
		konwerter2.read_VS()
		konwerter2.write_BG("variableStep")

        
if __name__ == "__main__":
	main()

