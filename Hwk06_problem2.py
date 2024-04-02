#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 11:36:34 2024

@author: gabriellemurray
"""

def GetComplement(base):
    if base == 'A':
        compbase = 'T'
    elif base == 'C':
        compbase = 'G'
    elif base == 'G':
        compbase = 'C'
    else:
        compbase = 'A'
    return compbase

def main():
    
    dnabases = ['A', 'C', 'G', 'T']
    dnaString = "ACAAGATGCCATTGTCCCCCGGCCTCCTGCTGCTGCTGCTCTCCGGGGCCACGGCCACCGCTGCCCTGCCCCTGGAGGGT"
    #2.1
    print(len(dnaString))
    #2.2
    for base in dnabases:
        count = dnaString.count(base)
        print(base, ":", count)    
    #2.3
    basepairlist = []
    for b1 in dnabases:
        for b2 in dnabases:
            basepair = b1+b2 
            basepairlist.append(basepair)   #store the pair in a list
            countpair = dnaString.count(basepair)
            print(basepair, ":", countpair)
    #2.4
    compSequence = []
    for b in dnaString:
        compbase = GetComplement(b)
        compSequence.append(compbase)
    CompSeq = str(''.join(compSequence))
    print(CompSeq)
    #2.5
    ReverseCompSeq = ''.join(CompSeq[::-1])
    print(ReverseCompSeq)
    
    
main()
            
    
