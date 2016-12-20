import re

class Poem:
    def __init__(self):
        self.lines = []
        fobj = open("poem.txt", 'r')
        for line in fobj:
            self.lines.append(line.strip())
    
    def removePunctuation0(self):
        pat = "[^A-Z^a-z^0-9 ]"
        self.new_lines = []
    
        for index, line in enumerate(self.lines):
            str1 = re.sub(pat, "", line)
            self.lines[index] = str1

    def removePunctuation1(self):
        pat = "[^A-Z^a-z^0-9 ]"
        
        f = lambda line:re.sub(pat, "", line)
        #for line in self.lines:
        map(f,self.lines)

    def windex(self):
        wordIndex = {}
        for line in self.lines:
            words = line.split()
            for word in words:
                if word in wordIndex:
                    wordIndex[word] = wordIndex[word] + 1
                else:
                    wordIndex[word] = 1
        return wordIndex
                
    def getLines(self, word):
       result = [word] 
       for index, line in enumerate(self.lines):
           if word in line:
               result.append((index+1, line))
       return result
    
    def show(self):
        for line in self.lines:
            print(line)

if __name__ == "__main__":
    
    p1 = Poem()
  #  p1.show()
 #list(map(f,x1))
#    p1.removePunctuation1()
 #   p1.show()
  #  p1.windex(
  # print(p1.windex())
#    print(p1.getLines('the'))
