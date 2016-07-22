"""
Suffix Array Construction Problem: Construct the suffix array of a string.
     Input: A string Text.
     Output: SuffixArray(Text).

CODE CHALLENGE: Solve the Suffix Array Construction Problem.

Sample Input:
     AACGATAGCGGTAGA$

Sample Output:
     15, 14, 0, 1, 12, 6, 4, 2, 8, 13, 3, 7, 9, 10, 11, 5
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
	
result = suffix_array ('TACTGGGCCTCCGGCGAATTGGACACGACTGGCACAGTGCGCCTGACTTTCGGCACAAAATATCTTCGTAATTCACTGTGGCGGGCCCTCGCCGATACGAACTGTGGGACAACCGTGCAACCAACGCCATCACCATCTTCCAGCTATCGTATGAGAACTAATGGTGGCAACAGTAAGAACATTGAGGCCGGGACGCCGGACACCTACTTCTACCTCGGCGAATAGATCGCTATCTCACTATAATGTATGTCCAGCACGAAAATCTTTTTAGCGGAGTAGTCGCTTATCGCGGGATGTAAACCCTTTCACGGCTATTATGGGGGGGAATTCCGTGTGGCTGACGTATATCCACAATAAACCTAATCGAACTTGCAGGCCAGGCGCCTTTTTCCACAGGTTTTCGCGAAGCGGACTATCTCACTGGCACAGGCCTCCAGCTGAGCTCTATCATCCGATTTGTTACCAAACAAACGCTTCGATAACTTAGACAACGCTACTTCACGTAAGCGTTTTAGGCCGTAGCAACCATCACAGATAGGTGTCAGGCAGATGTCTCTTTGCGAACGTATGTACATAGCGCATCGGGCGAGAAGGCGGTGTCGTCCGTAAGGACGGACAGGGTTAGATGCTATACGATCATGCAAGGGGTCTCTCAGCCGAGGACGCACGGCTGCGAATCTCCCTCTTCGAATCACTATACCTTGAGCCGTCTGTTCCGACTAACCCACTAGATCAAACTATCGGCAAATCTTATGAATAGGATGCCGAAGCTAACTCGTCAGATACCCCAAGAGCTCGTTACTGCTATATAGTCCTGTCAAATATAATAGTATAGAGACTAAGGAGATGTACGGCGCCTGGAAGGCGACCATGAATCGCTTGATGTACAACACGGTCTTGAGCGCTTCAAAGGGGTCTAGCATTAACCCGTCAGGTGGGTGGCGCTCCAGAAGCCAATTATTCCATTATCATTG$')
print result
result = str(result)
with open('9_Suffix_Array.txt', "w") as f:
	f.write(result)
	