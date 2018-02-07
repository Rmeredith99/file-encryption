#from math import sqrt, exp, tan, pi, log, sin, e
import string
import random
from random import randint

###
# Enter file names here
read_file = "data2.txt"
write_file = "data2.txt"
###



numberOfRotors = 40

chars = string.printable[:98]
charsList = []
for s in chars:
	charsList.append(s)
wheelList = []

numbersList = [1]

def getRandom(item):
	"""function to sort the characters randomly"""
	return randint(0,200)

random.seed(1863472) #so that the random wheel starting positions are the same every time

for i in range(numberOfRotors):
	tempChars = list(chars)
	tempChars.sort(key=getRandom)
	wheelList.append(tempChars)
	numbersList.append(randint(2,100))

def Init(L,s):
    """Initializes a rotor, L, to the starting location, s."""
    while L[0]!=s:
        a=L[0]
        del L[0]
        L.append(a)
        
def Turn(L):
    """Takes a list and turns it one letter."""
    a=L[0]
    del L[0]
    L.append(a)
    
def locate(L,s):
    """Finds the location of a character, s, in a list, L"""
    n=0
    for i in L:
        if i==s:
            a=n
        n+=1
    return a

def change(L,s):
    """Takes in a character and a gear and changes the character accordingly
    L:list
    s:string
    """
    a=locate(charsList,s)
    b=L[a]
    return b

def reversechange(L,s):
    """The opposite of change, for the part after the reflector.
    L:list
    s:string
    """
    b=locate(L,s)
    a=charsList[b]
    return a

def reflector(s):
    a=['o', '6', '?', '7', 'P', '!', ' ', '%', '.', 's', 'i', 'I', 'N', '*', '-', 'p', ']', '<', 'l', 'x', 'U', 'Y', 'y', '#', 'v', 'Z', 'd', '>', '9', '8', '@', 'w', '`', ')', 'c', '+', 'Q', '\t','b', '4', 'E', 'H', 'D', 'O', 'F', '^', '&', 'G', 'C']
    b=['u', 'g', 'h', 'S', 'm', '{', 'R', 'A', '_', 'q', 'T', 'z', 'J', 'j', 'r', '0', 'X', '[', '"', 'V', 'n', '$', 'B', '\n', 'L', 'k', 'K', '}', '\\', 'a', ';', 'f', '\r', 'e', '2', ',', '5', 'W', 't', "'", '(', 'M', '|', '1', '=', '~', ':', '3', '/']
    if s in a:
        return b[a.index(s)]
    elif s in b:
        return a[b.index(s)]

def Encrypt(s,InitS=""):
    """s is the string to be encrypted.
    InitS is the initialization string. It must be 'numberOfRotors' characters long."""
    s=str(s)
    n=0
    if (InitS!=""):
        for i in InitS:
            Init(wheelList[n],i)
            n+=1
    result = ''
    count=0
    for i in s:
        a=i
        for j in wheelList:
            a=change(j,a)
        a=reflector(a)
        for j in range(numberOfRotors):
            l=wheelList[numberOfRotors-1-j]
            a=reversechange(l,a)
        result+=a
    
        for j in range(numberOfRotors):
            if count%numbersList[j]==0:
                Turn(wheelList[j])
        count+=1
    return result


password = raw_input("Enter your password here: ")


with open(read_file, 'r') as myfile:
    data=myfile.read()

newData = Encrypt(data,password[:numberOfRotors])

with open(write_file, 'w') as myfile:
	myfile.write(newData)
