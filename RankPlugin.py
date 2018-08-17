import sys
import numpy



class RankPlugin:
   def input(self, filename):
      self.myfile = filename

   def run(self):
      filestuff = open(self.myfile, 'r')
      self.firstline = filestuff.readline()

      self.ADJ = []

      self.samples = []
      for line in filestuff:
         self.ADJ.append([])
         myline = line.strip()
         elements = line.split(',')
         self.samples.append(elements[0])
         elements.remove(elements[0])
         n = len(elements)
         mypairs = []
         for i in range(n):
            mypairs.append((float(elements[i]), i))
            self.ADJ[len(self.ADJ)-1].append(0)

         mypairs.sort()
         mypairs.reverse()

         ranking = 1
         for i in range(len(mypairs)):
            if (mypairs[i][0] != 0):
               self.ADJ[len(self.ADJ)-1][mypairs[i][1]] = ranking
            else:
               self.ADJ[len(self.ADJ)-1][mypairs[i][1]] = n
            if (i != len(mypairs)-1 and mypairs[i+1][0] != mypairs[i][0]):
               ranking += 1
 
      self.m = len(self.ADJ)
      self.n = len(self.ADJ[0])
           

   def output(self, filename):
      filestuff2 = open(filename, 'w')
      
      filestuff2.write(self.firstline)
            
      for i in range(self.m):
         #filestuff2.write(self.bacteria[i]+',')
         filestuff2.write(self.samples[i]+',')
         for j in range(self.n):
            filestuff2.write(str(self.ADJ[i][j]))
            if (j < self.n-1):
               filestuff2.write(",")
            else:
               filestuff2.write("\n")



