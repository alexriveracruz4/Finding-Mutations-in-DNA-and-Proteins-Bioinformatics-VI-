"""
Created on Wed Apr 01 21:41:45 2015
@author: ngaude
"""

def suffix_array(s):
    """
    Suffix Array Construction Problem: Construct the suffix array of a string.
    Input: A string Text.
    Output: SuffixArray(Text).
    """
    # elegant by uses too much memory 
    # return sorted(range(len(s)), key=lambda i: s[i:])
    
    # no memory issue, but still not time loglinear because of string copy
    # return sorted(range(len(s)), cmp=lambda i,j: cmp(s[i:],s[j:]))
    
    # no memory issue, no string copy issue, but python bytecode is still slow
    l = len(s)
    def compare(i,j):        
        while i<l and j<l:
            if s[i]>s[j]:
                return 1
            elif s[i]<s[j]:
                return -1
            i +=1
            j +=1
        return 0
    return sorted(range(len(s)), cmp=compare)
    
assert suffix_array('AACGATAGCGGTAGA$') == [15, 14, 0, 1, 12, 6, 4, 2, 8, 13, 3, 7, 9, 10, 11, 5]

def bwt(s):
    """
    Burrows-Wheeler Transform Construction Problem: 
    Construct the Burrows-Wheeler transform of a string.
    Input: A string Text.
    Output: BWT(Text).
    """
    return ''.join([s[(i-1) % len(s)] for i in suffix_array(s)])

result = bwt('ACTTGCCAGCCGCCAGGGGACAAGCGCTTACTTAGTCTGTATGATATATAAGGTTTTAAAGCGCCAGCTAGTTCTCATCTGCCACACCCGCTGAATCGCCCCGTCCTTAATTCGGCTATTTAAAGAGGTCAGTCACTAGACCCGATCCCCGCATGTGTTCGATGCCTGCTCCCTTGGTGCGCTTCCGGCACGGTCTAGGCGTTGGTACGCAACCGTTCCTCCTTTCTGGTCTGAGCGTCAGTGTATGGGACCCGCCGGACACTACTTATGGTCGCCTGGAGACCTTGAAGTTAGGCGCGATTGCAACGGGGGACTTTCCATTTCAGAAGGGTTCAGGGCTTTATGCGGAGATATATCGAATTCTAGAGTTATCGTCACAAACTACTCATCACTTCCCTCCCGGGACCGACCTGAATTACGGAATCGCTAATGCGCTATTAGGTCTTTCACTGCGTCTCGAGTGCACGCGCCTATGAAGCCTAATAGGTATGCCCACGACGCGTTAAACGTGGTGCTCAGAGGCCCCTTAATAACACCCTAGGATCATAAATGGATATGCGATGAGAAGATCGGACTGTTGCTGCTGTTCCTGTGTGTCGACCACTTGAAAACTTAAAGCAGGTCACAAACTCCCAGCGAAAGTTATTTCTGGATCTGCACGAGAGGTGACTAGCGCCACAGGTGTCACGAGCAAGCAACATTCGGCGGCCTGCCCGCGGATGATTGCTGCTCTCATGCCGGCCGATAATACTATTAACCAAAGCGTGAGTACTGGCTCGGTACGGTACGGCTTAACGAGAACCAGTGCAAGCTGCTCCGTTCATGTCTGTTATCCT$')
print result
result = str(result)
with open('10_Burrows_Wheeler_Answer.txt', "w") as f:
	f.write(result)