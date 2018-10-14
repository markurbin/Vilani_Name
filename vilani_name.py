# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 22:13:18 2016

@author: Mark Urbin
# "The Traveller game in all forms is owned by Far Future Enterprises. 
# Copyright 1977 - 2018 Far Future Enterprises."

This program translates Terran names to Vilani.
This for the science fiction role playing game Traveller.
Names of length of 2 or 3 names can be entered as a command line option
examples: "Joe Generic" or "John Quincy Citizen"
In the case of no middle name, a common name will be used
If no command line input, a default name of "Walter Piracy Smith" will be used.
It is up to the user to break the resulting name in to first and last names.
For guidance see 
http://www.freelancetraveller.com/features/culture/customs/vilnames.html
This is based on a 'Your name in Vilani' web page that I'm pretty sure does
not exist anymore.
"""

#Standard libraries
import random
import sys

def replace1(nWip):
    
    list1 = ('ag', 'ir', 'uk', 'aag', 'iir')
    list2 = ('shir','sir')
    list3 = ('uu','u')

    nWip = nWip.replace('ch','sh')
    nWip = nWip.replace('c','k')
    nWip = nWip.replace('f','b')
    nWip = nWip.replace('j','ii')
    nWip = nWip.replace('o','aa')
    nWip = nWip.replace('p','m')
    nWip = nWip.replace('q','k')
    nWip = nWip.replace('t','r')
    nWip = nWip.replace('x','kash')
    nWip = nWip.replace('y','ii')
    nWip = nWip.replace('l',random.choice(list1))
    nWip = nWip.replace('s',random.choice(list2))
    nWip = nWip.replace('u',random.choice(list3))
    nWip = nWip.replace('v',random.choice(list3))
    nWip = nWip.replace('w',random.choice(list3))
    
    c = 0
    tWip = ''
    for x in nWip:
        if x == 'h':
            if c > 0:
                if (nWip[c-1] != 's') and (nWip[c-1] != 'g'):
                    tWip += 'kh'
                else:
                    tWip += x
            else:
                tWip += x
        else:
            tWip += x
        c+=1
    return tWip
    
def doubleCon(nWip):

    vowels = 'aeiou'
    list1 = ('ii','i','aa','a')    
    c = 0
    tWip = ''
    for x in nWip:
        if x not in vowels:
            if c > 0:
                if x == nWip[c-1]:
                    tWip += random.choice(list1)
                    tWip += x
                else:
                    tWip += x
            else:
                tWip += x
        else:
            tWip += x
        c+=1
    return tWip
    
def addvowel(x):
    tWip = ''
    list1 = ('a','e','i','ii','uu','aa')
    tWip += random.choice(list1)
    tWip += x
    return tWip
    
def sepCon(nWip):
    vowels = 'aeiou'
    c = 0
    tWip = ''
    temp = ''
    for x in nWip:
        if x not in vowels:
            if c > 0:
                if nWip[c-1] not in vowels:
                    temp = nWip[c-1] + x
                    if (temp == 'kh') or (temp == 'sh') or (temp == 'rk'):
                        tWip += x
                    else:
                        tWip += addvowel(x)
                else:
                    tWip += x
            else:
                tWip += x
        else:
            tWip += x
        c+=1
    return tWip
    
def dipReplace(nWip):
    
    dipList = ('ow','ou','oi','oy','ou','ea')
    list1 = ('a','e','i','ii','uu','aa')
    tWip = ''
    c = 0
    temp = ' ' 
    
    for x in nWip:
        if c > 0:
            temp = nWip[c-1] + x
            if temp in dipList:
                tWip += random.choice(list1)
            else:
                tWip += x
        else:
            tWip += x
        c += 1
    return tWip

def dipthong(nWip):
    nWip = nWip.replace('ae','e')
    nWip = nWip.replace('ai','ii')
    nWip = nWip.replace('ao','uu')
    nWip = nWip.replace('au','aa')
    nWip = nWip.replace('ay','e')
    nWip = nWip.replace('ea','i')
    nWip = nWip.replace('ee','ii')
    nWip = nWip.replace('ei','e')
    nWip = nWip.replace('eo','i')
    nWip = nWip.replace('eu','u')
    nWip = nWip.replace('ey','ii')
    nWip = nWip.replace('ia','a')
    nWip = nWip.replace('ie','e')
    nWip = nWip.replace('io','o')
    nWip = nWip.replace('iu','u')
    nWip = nWip.replace('oa','ua')
    nWip = nWip.replace('oe','e')
    nWip = nWip.replace('oi','i')
    nWip = nWip.replace('oo','uu')
    nWip = nWip.replace('ou','uu')
    nWip = nWip.replace('oy','i')
    nWip = nWip.replace('ue','u')
    nWip = nWip.replace('ui','ii')
    nWip = nWip.replace('uo','ua')
    nWip = nWip.replace('uy','ii')
    
    return nWip
    
def vilaniName(nWip):
    nWip = dipthong(nWip)
    #print '1: ',nWip
    nWip = replace1(nWip)
    #print '2: ',nWip
    nWip = doubleCon(nWip)
    #print '3: ',nWip
    nWip = sepCon(nWip)
    #print '4: ',nWip
    nWip = dipReplace(nWip)
    #print '5: ',nWip
    return nWip

def insertName():
    'Insert a common middle name'
    
    commonMale = ['john','james','michael','robert','mark','kevin','noah',
                  'mason','lucas','adam','carter','henry','alexander','jack',
                  'gabriel','muhammad','asher','clark','bruce','donald',
                  'scott','christopher', 'jerry','roger','alan','ian',
                  'mohammand', 'yue', 'yang', 'raj', 'edgar','steve',
                  'marc','jean','chad', 'gary', 'larry','neil','glenn',
                  'ace','christian','gabriel','raphael','azrael','chamuel',
                  'lincoln','samuel','hunter','fitzgerald','otto','gunther',
                  'karl','rudolf','benjamin','ernest','oscar','ralph',
                  'elmer','frederick','herbert','lee','spock','lawerance',
                  'ronald','william','billy']
    commonFemale =['susan','mary','carolyn','judy', 'kim', 'lori','kathy',
                   'carol', 'laura', 'kimberly','olivia','sophia','charlotte',
                   'harper', 'evelyn', 'scarlett', 'emily', 'madison', 
                   'elizabeth', 'victoria', 'grace', 'aubrey', 'aurora',
                   'skylar', 'hazel', 'nova', 'brooklyn', 'kaitlyn','sally',
                   'patty','patricia', 'linda','amy','yelena','joan',
                   'stephanie','ursula', 'taylor', 'jophiel','ariel','priya',
                   'li','jamie','josephine','carrie','sarah', 'helen',
                   'gracie','ann','alice','ada','sadie','doris','virginia',
                   'dakota','marilyn','catherine','ruby','beverly','reagan']
    
    # For now, randomly select either a male or femalename
    if 1 == random.randint(1,2):
        nName = random.choice(commonMale)
    else:
        nName = random.choice(commonFemale)
    return nName
    

#Start of main executable code

# If no Middle Name use a common name
if len(sys.argv) < 4:
    if len(sys.argv) == 3:
        name = sys.argv[1]
        name += ' '
        name += insertName()
        name += ' '
        name += sys.argv[2]
else:
    name = sys.argv[1]
    name += ' '
    name += sys.argv[2]
    name += ' '
    name += sys.argv[3]

if len(sys.argv) < 3:
    name = 'Walter Piracy Smith'
print 'Original Name: ', name
sName = name.split(' ')

# Reverse the middle name
vNameWip = sName[0] + sName[2][::-1] + sName[1]
# Make everything lower Case
nWip = vNameWip.lower()

#nWip = villaniName(nWip)
#Printing 5 names to get multiple values due to random selection
for y in range(0,5):
    print vilaniName(nWip)

