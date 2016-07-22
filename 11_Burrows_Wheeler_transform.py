"""
Inverse Burrows-Wheeler Transform Problem: Reconstruct a string from its Burrows-Wheeler transform.
     Input: A string Transform (with a single "$" symbol).
     Output: The string Text such that BWT(Text) = Transform.

CODE CHALLENGE: Solve the Inverse Burrows-Wheeler Transform Problem.

Sample Input:

TTCCTAACG$A

Sample Output:

TACATCACGT$
https://github.com/ngaude/sandbox/blob/f009d5a50260ce26a69cd7b354f6d37b48937ee5/bioinformatics-002/bioinformatics_chapter8.py
"""

def ibwt(s):
    """
    Inverse Burrows-Wheeler Transform Problem: 
    Reconstruct a string from its Burrows-Wheeler transform.
    Input: A string Transform (with a single "$" symbol).
    Output: The string Text such that BWT(Text) = Transform.
    """
    l = len(s)
    
    def char_rank(i):
        d[s[i]] = d.get(s[i],0) + 1
        return d[s[i]]
    d = {}
    # produce a list tuple (char,rank) for the last column
    last_char_rank = [(s[i],char_rank(i),i) for i in range(l)]
    d = {}
    # produce the list tuple (char,rank) for the first column
    first_char_rank = sorted(last_char_rank)
        
#    for i in range(l):
#        r = str(first_char_rank[i])+('*'*(l-2))+str(last_char_rank[i])
#        print r
    
    i = 0
    decoded = ''
    for j in range(l):
        i = first_char_rank[i][2]
        decoded += first_char_rank[i][0]
    return decoded
    

with open('11_Burrows_Wheeler_transform.txt') as infile:
    text = infile.read().strip()
	
result = ibwt(text)
print result
result = str(result)
with open('11_Burrows_Wheeler_transform_Answer.txt', "w") as f:
	f.write(result)