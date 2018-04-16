import numpy as np
import random

def lowerChar(char):
    return char.lower()
def crypto(x,n,enc): #x=list, n=value between 0 to 2,000,000,000 and enc=true or false
    random.seed(n)
    a=random.randint(0,25)
    print(a)
    y=[]
    
    for c in x:
        counter=0
        tempWord=""
        for counter in range(len(c)):
            char = c[counter]
            if (char.isalpha()):
                tempChar=lowerChar(char)
                num=ord(tempChar)
                num2=num+a
                #print(num2,num)
                if (num2<=122):
                    pass
                else:
                    num2=96+num2-122
                newChar=chr(num2)
                if(char.islower()):
                    pass
                else:
                    newChar=newChar.upper()
                char=newChar
            tempWord=tempWord+char
        y.append(tempWord)
    print(y)



                        #65 to 90 (caps), 97 - 122 (small)
x=["This", "is", "gonnabeencrypted"]
crypto(x,20,0)
