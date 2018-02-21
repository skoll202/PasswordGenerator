#!/usr/bin/python3
'''
Created on Feb 16, 2018

@author: skoll202
'''
import sys
import getopt

rule = {
    'a':['@','4'],'b':[],'c':[],'d':[],'e':['3'],'f':[],'g':[],'h':[],'i':['1','!'],
    'j':[],'k':[],'l':['1','!'],'m':[],'n':[],'o':['0'],'p':[],'q':[],'r':[],
    's':['$'],'t':['7'],'u':[],'v':[],'w':[],'x':[],'y':[],'z':[],'1':['!'],
    '2':[],'3':[],'4':[],'5':[],'6':[],'7':[],'8':[],'9':[],'0':[], ' ':[]}



def mangle(word):
    list = []
    if len(word)==1:
        list.append(word.upper())
        list.append(word.lower())
        for r in rule[word]:
            list.append(r)
    else:
        #print(word)
        firstLetters = mangle(word[0])
        for l in firstLetters:
            restOfWord = mangle(word[1:])
            for w in restOfWord:
                list.append(l+w)
    return list

def addNumbers(word, maxNum):
    #print(word)
    #print(maxNum)
    list = []
    for n in range(0,maxNum+1):
        list.append("%s%d"%(word,n))
    return list
        
def addDates(word,dates):
    list = []
    for d in dates:
        list.append("%s%s"%(word,d))
    return list    

def printHelp():
    print()
    print("Options:")
    print()
    print("-w WORDS,--words=WORDS    List of words separated by comma, or file with list of words")
    print("-d DATES,--dates=DATES    List of relevant dates or numbers separated by comma, or file with list of dates")
    print("-o OUTPUT,--output=OUTPUT File to write password list to, or ignore for stdout")
    print()
def main(*args):
    try:
        OUTPUT = ''
        WORDS=''
        DATES=''
        options, remainder = getopt.getopt(sys.argv[1:], 'o:w:d:h', 
                                           ['output=','words=','dates=','help'])
    
        for opt, arg in options:
            if opt in ('-o', '--output'):
                OUTPUT = arg
            elif opt in ('-w', '--words'):
                WORDS=arg
            elif opt in ('-d', '--dates'):
                DATES = arg
            else:
                printHelp()
        kindofFinalList = []
        finalList = []
        try:
            with open(WORDS) as f:
                content = f.readlines()
        # you may also want to remove whitespace characters like `\n` at the end of each line
            words = [x.strip() for x in content] 
        except:
            words = WORDS.split(",")
        try:
            with open(DATES) as f:
                content = f.readlines()
        # you may also want to remove whitespace characters like `\n` at the end of each line
            dates = [x.strip() for x in content] 
        except:
            dates = DATES.split(",")
        #words = args[0][1:]
        for word in words:
            if len(word)>0:
                newWords = mangle(word.lower())
                kindofFinalList+=newWords
        for word in kindofFinalList:
            finalList.append(word)
        for word in kindofFinalList:
            finalList+=addDates(word,dates)
        if OUTPUT!='':
            try:
                outFile = open(OUTPUT, 'w')
                for word in finalList:
                    outFile.write("%s\n" % word)
            except:
                for word in finalList:
                    print(word)
        return finalList
    except:
        printHelp()

main(sys.argv)
