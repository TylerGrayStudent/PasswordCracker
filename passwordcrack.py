import hashlib
import sys
from itertools import chain, product, combinations_with_replacement, combinations, permutations


def encrypt_string_sha256(hash_string):
    sha_sig = hashlib.sha256(hash_string.encode()).hexdigest()
    return sha_sig

def readDefaultFile():
    return open("hashes.txt", "r")

def getHash(line):
    return encrypt_string_sha256(line)

def rule1():
    #Rule 1: Tests a 7 char word with First letter in Caps and appends a 1 digit
    wordsToCheck = []
    file = open('7lenwordlist.txt','r')
    lines = file.readlines()
    for l in lines:
        l = l.rstrip()
        l = l.capitalize()
        wordsToCheck.append(l)
        for i in range(10):
            wordsToCheck.append(l  + str(i))
    return wordsToCheck

def rule2():
    symbols = [ '*', '~', '!', '#']
    symbolCombos = []
    #symbolCombos = [",".join(map(str, comb)) for comb in combinations(symbols, 1)]
    #symbolCombos += [",".join(map(str, comb)) for comb in combinations(symbols, 2)]
    #symbolCombos += [",".join(map(str, comb)) for comb in combinations(symbols, 3)]
    #symbolCombos += [",".join(map(str, comb)) for comb in combinations(symbols, 4)]
    for i in range(1,5):
        for p in permutations(symbols,i):
            symbolCombos.append(''.join(p))
    wordsToCheck = []
    for i in range(10000000000):
        wordsToCheck.append(str(i))
        for s in symbolCombos:
            wordsToCheck.append(s + str(i))7
    return wordsToCheck


def rule3():
    wordsToCheck = []
    file = open('5lenwordlist.txt','r')
    lines = file.readlines()
    lines = [s.replace('a','@') for s in lines]
    lines = [s.replace('l', '1') for s in lines]
    for l in lines:
        l = l.rstrip()
        wordsToCheck.append(l)
    return wordsToCheck

def rule4():
    digits='1234567890'
    generator=combinations_with_replacement(digits, 100)
    wordsToCheck = []
    for e in generator:
        wordsToCheck.append(''.join(e))

def rule5():
    try:
        return open('words','r').readlines()
    except:
        try:
            return open('/usr/share/dict/words','r').readlines()
        except:
            print("ERROR: MISSING WORDS FILE. EITHER PLACE YOUR OWN DICTIONARY NAMED \'word\' INTO THE DIREDCTORY THE SCRIPT IS RUNNIGG OR INTO \\usr\\share\\dict")
            return []







def gen7charwordlist():
    file = open('words','r')
    writefile = open('7lenwordlist.txt','w')
    lines = file.readlines()
    print(len(lines))
    sevenchars = filter(lambda x: len(x)==8,lines)
    for e in sevenchars:
        writefile.write(e)


def gen5charwordlist():
    file = open('words','r')
    writefile = open('5lenwordlist.txt','w')
    lines = file.readlines()
    print(len(lines))
    fivechars = filter(lambda x: len(x)==6,lines)
    for e in fivechars:
        writefile.write(e)



def main():
    try:
        if len(sys.argv) == 1:
            file = readDefaultFile()
        else:
            print('reading from arguemnts')
            file = open(sys.argv[1],'r')
    except:
        print("No file found. Either have your passwords stored in a file name hashes.txt or give the file name as an argument when you run the program")
        sys.exit(0);
    hashes = []
    for line in file:
        string =  line.strip().split(':')[1]
        hashes.append(string)
    try:
        open('7lenwordlist.txt','r')
    except:
        gen7charwordlist()
    try:
        open('5lenwordlist.txt', 'r')
    except:
        gen5charwordlist()

    #rule1list = rule1()
    wordsToTest = []
    wordsToTest += rule1()
    wordsToTest += rule3()
    wordsToTest += rule5()
    wordsToTest += rule2()
    wordsToTest = set(wordsToTest)
    #rule4list = rule4()

    for hash in hashes:
        print("Solving for " + hash)
        for test in wordsToTest:
            if getHash(test) == hash:
                print(hash + " solved to " + test)
                print("FOUND IT")
                break

        print("")
    print("TEST CONCLUDED")



main()
#rule2()







