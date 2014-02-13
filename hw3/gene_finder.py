# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 11:24:42 2014

@author: Riley Chapman
"""

# you may find it useful to import these variables (although you are not required to use them)
from amino_acids import aa, codons

def collapse(L):
    """ Converts a list of strings to a string by concatenating all elements of the list """
    output = ""
    for s in L:
        output = output + s
    return output


def coding_strand_to_AA(dna):
    """ Computes the Protein encoded by a sequence of DNA.  This function
        does not check for start and stop codons (it assumes that the input
        DNA sequence represents an protein coding region).
        
        dna: a DNA sequence represented as a string
        returns: a string containing the sequence of amino acids encoded by the
                 the input DNA fragment
    """
    AA = '' #empty string for found amino acids
    i = 0;
    while i < len(dna):
        codon = dna[i:i+3] #grab a codon from the DNA seqence
        for a,refferenceCodon in enumerate(codons):
            for substring in refferenceCodon:
                #print 'checking', substring, ' against ', codon
                if codon == substring:
                    #print 'match!'
                    aminoAcid = aa[a]
                    AA += aminoAcid
                    #print 'matched ', codon, ' with ', aminoAcid
        i = i + 3
    return AA

def coding_strand_to_AA_unit_tests():
    """ Unit tests for the coding_strand_to_AA function """

    theinput = 'ATGCGA'
    output = coding_strand_to_AA(theinput) 
    expectedOutput = 'MR' 
    print 'input:', theinput, ' expected output: ', expectedOutput, ' output: ',output 

    theinput = 'ATGCCCGCTTT'
    output = coding_strand_to_AA(theinput) 
    expectedOutput = 'MPA' 
    print 'input:', theinput, ' expected output: ', expectedOutput, ' output: ',output 

def get_reverse_complement(dna):
    """ Computes the reverse complementary sequence of DNA for the specfied DNA
        sequence
    
        dna: a DNA sequence represented as a string
        returns: the reverse complementary DNA sequence represented as a string
    """
    compliment = '' #empty string to build the compliment in 
    for i,base in enumerate(dna): #match the base pairs
        if base == 'A':
            compliment += 'T'
        elif base == 'T':
            compliment += 'A'
        elif base == 'C':
            compliment += 'G'
        elif base == 'G':
            compliment += 'C'
    reverseCompliment = compliment[::-1] #reverse the compliment 
    return reverseCompliment


    
def get_reverse_complement_unit_tests():
    """ Unit tests for the get_complement function """
        
    theinput = 'ATGCCCGCTTT'
    output = get_reverse_complement(theinput) 
    expectedOutput = 'AAAGCGGGCAT' 
    print 'input:', theinput, ' expected output: ', expectedOutput, ' output: ',output  

    theinput = 'CCGCGTTCA'
    output = get_reverse_complement(theinput) 
    expectedOutput = 'TGAACGCGG' 
    print 'input:', theinput, ' expected output: ', expectedOutput, ' output: ',output 

def rest_of_ORF(dna):
    """ Takes a DNA sequence that is assumed to begin with a start codon and returns
        the sequence up to but not including the first in frame stop codon.  If there
        is no in frame stop codon, returns the whole string.
        
        dna: a DNA sequence
        returns: the open reading frame represented as a string
    """
    
    resultString = ''
    i = 0; 
    while i < len(dna):
        codon = dna[i:i+3]
        if codon == 'TAG' or codon == 'TAA' or codon == 'TGA': #check for stop sequence 
            break
        else:
            resultString += codon #otherwise, add the codon to the list and continue 
        i += 3
    return resultString

def rest_of_ORF_unit_tests():
    """ Unit tests for the rest_of_ORF function """
        
    theinput = 'ATGTGAA'
    output = rest_of_ORF(theinput)
    expectedOutput = 'ATG'
    print 'input: ', theinput, ' expected output: ', expectedOutput, ' output: ', output 

    theinput = 'ATGAGATAGG'
    output = rest_of_ORF(theinput)
    expectedOutput = 'ATGAGA'
    print 'input: ', theinput, ' expected output: ', expectedOutput, ' output: ', output 

    theinput = 'ATGCGAGATGTTCAATACTGCTAA'
    output = rest_of_ORF(theinput)
    expectedOutput = 'ATGCGAGATGTTCAATACTGC'
    print 'input: ', theinput, ' expected output: ', expectedOutput, ' output: ', output 

        
def find_all_ORFs_oneframe(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence and returns
        them as a list.  This function should only find ORFs that are in the default
        frame of the sequence (i.e. they start on indices that are multiples of 3).
        By non-nested we mean that if an ORF occurs entirely within
        another ORF, it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """
    resultList = [] 
    rf = ''
    i = 0;
    while i < len(dna):
        codon = dna[i:i+3]
        if codon == 'ATG':
            rf = rest_of_ORF(dna[i:])
            resultList.append(rf)
            i = i + len(rf) - 3 #skip to the end of the frame with compensation for the while loop increment
            rf = ''
        i += 3
    if rf != '':
         resultList.append(rf) #add the rest, even if a a stop codon is not found
    return resultList

        

     
def find_all_ORFs_oneframe_unit_tests():
    """ Unit tests for the find_all_ORFs_oneframe function """

    theinput = 'ATGCATGAATGTAGATAGATGTGCCC'
    output = find_all_ORFs_oneframe(theinput)
    expectedOutput = "['ATGCATGAATGTAGA', 'ATGTGCCC']"
    print 'input: ', theinput, ' expected output: ', expectedOutput, ' output: ', output 

    theinput = 'ATGTGCTGAGATATGCGATCGTAG'
    output = find_all_ORFs_oneframe(theinput)
    expectedOutput = "['ATGTGCTGA', 'ATGCGATCG']"
    print 'input: ', theinput, ' expected output: ', expectedOutput, ' output: ', output 


def find_all_ORFs(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence in all 3
        possible frames and returns them as a list.  By non-nested we mean that if an
        ORF occurs entirely within another ORF and they are both in the same frame,
        it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """
    resultList = [] 
    for i in range(0,3): #starting in the three possible positions 
        dnaFrame = dna[i:]
        strands = find_all_ORFs_oneframe(dnaFrame)
        for strand in strands:
            resultList.append(strand)
    return resultList


def find_all_ORFs_unit_tests():
    """ Unit tests for the find_all_ORFs function """
        
    theinput = 'ATGCATGAATGTAG'
    output = find_all_ORFs(theinput)
    expectedOutput = "['ATGCATGAATGTAG', 'ATGAATGTAG', 'ATG']"
    print 'input: ', theinput, ' expected output: ', expectedOutput, ' output: ', output 

def find_all_ORFs_both_strands(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence on both
        strands.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """
     
    resultList = []
    strands = find_all_ORFs(dna) #find all ORFs in strand
    for strand in strands:
        resultList.append(strand)
    reverseDna = get_reverse_complement(dna) #find all ORFs in compliment strand 
    strands = find_all_ORFs(reverseDna)
    for strand in strands:
        resultList.append(strand)
    return resultList

def find_all_ORFs_both_strands_unit_tests():
    """ Unit tests for the find_all_ORFs_both_strands function """

    theinput = 'ATGCGAATGTAGCATCAAA'
    output = find_all_ORFs_both_strands(theinput)
    expectedOutput = "['ATGCGAATG', 'ATGCTACATTCGCAT']"
    print 'input: ', theinput, ' expected output: ', expectedOutput, ' output: ', output 
    

def longest_ORF(dna):
    """ Finds the longest ORF on both strands of the specified DNA and returns it
        as a string"""

    readingFrames = find_all_ORFs_both_strands(dna)
    #print readingFrames
    currentLongest = ('')  #someting to compare the first item to 
    for frame in readingFrames:
        if len(frame) > len(currentLongest): #go through the list grabbing the longest one seen yet 
            currentLongest = frame
            #print "new longest! ", currentLongest
    return currentLongest

def longest_ORF_unit_tests():
    """ Unit tests for the longest_ORF function """

    theinput = 'ATGCGAATGTAGCATCAAA'
    output = longest_ORF(theinput)
    expectedOutput = "ATGCTACATTCGCAT"
    print 'input: ', theinput, ' expected output: ', expectedOutput, ' output: ', output 

def longest_ORF_noncoding(dna, num_trials):
    """ Computes the maximum length of the longest ORF over num_trials shuffles
        of the specfied DNA sequence
        
        dna: a DNA sequence
        num_trials: the number of random shuffles
        returns: the maximum length longest ORF """

    
    from random import shuffle 

    resultList = [] #setup list to append things to 

    dnaList = list(dna)
    for i in range(0, num_trials): #for each trial
        
        dnaListScramble = dnaList        # scramble the list
        shuffle(dnaListScramble)
        dnaStr = collapse(dnaListScramble)   #collapse back to a string and find all the frames 
        #print dnaStr 
        strings = find_all_ORFs_both_strands(dnaStr)
        #print strings 
        for string in strings:
            #print 'adding ', string   
            resultList.append(string)

    currentLongest = ''
    for result in resultList:
        if len(result) > len(currentLongest):
            currentLongest = result
    #print "the longest string is ", currentLongest 
    return len(currentLongest)


def gene_finder(dna, threshold):
    """ Returns the amino acid sequences coded by all genes that have an ORF
        larger than the specified threshold.
        
        dna: a DNA sequence
        threshold: the minimum length of the ORF for it to be considered a valid
                   gene.
        returns: a list of all amino acid sequences whose ORFs meet the minimum
                 length specified.
    """
    longEnoughStrands = [] #setup the list to be returned 
    resultAA = []

    allStrands = find_all_ORFs_both_strands(dna) 
    for strand in allStrands:
        if len(strand) > threshold: #sorts out the short strands
            longEnoughStrands.append(strand)
    for strand in longEnoughStrands:
        aminoAcids = coding_strand_to_AA(strand)
        resultAA.append(aminoAcids)
    return resultAA
