import  nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
#word_tokenize accepts a string as an input, not a file.
stop_words = set(stopwords.words('english'))
file1 = open("/Users\zulfa\PycharmProjects\projectalgorithm/testinput1.txt")
line = file1.read()# Use this to read file content as a stream:
words = line.split()
for r in words:
    if not r in stop_words:
        appendFile = open('/Users\zulfa\PycharmProjects\projectalgorithm/filteredtext.txt','a')
        appendFile.write(" "+r)
        appendFile.close()

class q5:
    def calcfreq(self):
        fname = input('Enter File: ')

        if len(fname) < 1 : fname = '/Users\zulfa\PycharmProjects\projectalgorithm/filteredtext.txt'
        hand = open(fname)

        di = dict()
        for lin in hand:
            lin = lin.rstrip().lower()           #rstrip() = remove right emptyspace    #.lower() = convert all text to lowercase
            wds = lin.split()                    #split the sentence into individual word
            for w in wds:
                di[w] = di.get(w,0)+1           #calculate frequency with looping

        for k,v in di.items():                   #items() = display list
         print(k, "-",v)

        largest = 0
        theword = None
        for k,v in di.items():                  #comparison to calculate the highest frequency
            if v > largest :
                largest = v
                theword = k

        print("Words with highest count:",theword,"-",largest)

q5 = q5()
q5.calcfreq()