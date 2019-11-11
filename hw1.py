#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 16:18:29 2019

@author: stella
"""

def loadLexicon(fname):
    newLex=set()
    lex_conn=open(fname)
    #add every word in the file to the set
    for line in lex_conn:
        newLex.add(line.strip())# remember to strip to remove the lin-change character
    lex_conn.close()

    return newLex

#function that reads in a file with reviews and decides if each review is positive or negative
#The function returns a list of the input reviews and a list of the respective decisions
def run(path):
    
    fre={}
    
    negLex=loadLexicon('negative-words.txt')
    
    fin=open(path)
    for line in fin: 
        
        negList=[] 
        
        line=line.lower().strip()  
        
        words=line.split(' ') # slit on the space to get list of words
        

        
        for i in range(len(words)-1):
            
            if words[i+1]=='phone' and words[i] in negLex:
                
                negList.append(words[i])
                fre[words[i]]=fre.get(words[i],0)+1
    fin.close()
    return fre,negList
    

if __name__ == "__main__": 
    fre,negList=run('text')
    print(fre)
