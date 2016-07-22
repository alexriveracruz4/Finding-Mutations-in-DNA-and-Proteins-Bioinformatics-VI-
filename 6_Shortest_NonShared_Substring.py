'''

Shortest Non-Shared Substring Problem: Find the shortest substring of one string that does not appear in another string.
     Input: Strings Text1 and Text2.
     Output: The shortest substring of Text1 that does not appear in Text2.

CODE CHALLENGE: Solve the Shortest Non-Shared Substring Problem. (Multiple solutions may exist, in which case you may return any one.)

https://github.com/ngaude/sandbox/blob/f009d5a50260ce26a69cd7b354f6d37b48937ee5/bioinformatics-002/bioinformatics_chapter7.py
Sample Input:
     CCAAGCTGCTAGAGG
     CATGCTGGGCTGGCT

Sample Output:
     AA
	 
	 '''

"""
Shortest Non-Shared Substring Problem
Find the shortest substring of one string that does not appear in another string.
Given: Strings Text1 and Text2.
Return: The shortest substring of Text1 that does not appear in Text2.
"""

def naive_shortest_non_shared_substring(text1,text2):
    """    
    Shortest Non-Shared Substring Problem: Find the shortest substring of one string that does not appear in another string.
    Input: Strings Text1 and Text2.
    Output: The shortest substring of Text1 that does not appear in Text2.
    """
    shortests = [text1]
    for i in range(len(text1)):
        maxj = min(i+len(shortests[-1]),len(text1))
        for j in range(i,maxj):
            if text1[i:j] not in text2:
                shortests.append(text1[i:j])
                break
    return shortests[-1]
string = naive_shortest_non_shared_substring('AAAATAAACAAAGAATTAATCAATGAACTAACCAACGAAGTAAGCAAGGATATACATAGATTTATTCATTGATCTATCCATCGATGTATGCATGGACACAGACTTACTCACTGACCTACCCACCGACGTACGCACGGAGAGTTAGTCAGTGAGCTAGCCAGCGAGGTAGGCAGGGTTTTCTTTGTTCCTTCGTTGCTTGGTCTCTGTCCCTCCGTCGCTCGGTGTGCCTGCGTGGCTGGGCCCCGCCGGCGCGGGGAAAGATAATTATAGTGCGCCGAGGCATACGGAAACGTTCGATGCCAGGATGGGTATAAAACGATTATCGTGTACACCGGTATCCCAAGGGAGGGCACACAATTGTATCGTGGCTCTTCGTACTTAGGTAAATCTGAACCCATGTCTTTTAACTTAGCATCCACACGAGAGGCGTCGGTACGCGGGGCACGGATCACTACATTGTAAGACAACAAAGCTAGTTATCCTGAGGTTGCATCATCACGGTTACAGGGGTATTGAGAAGTTGCGACTGCTTAGCGCCGAAATAGCCCGTTCTGCCCTTTTGCTTTTCGGAGGATTAGTAGTCTATGACGAAGGGTAATGCTCCAGAAAATCTGGGGCTGGTAAGGGGCAGGGGTCGACTATAAGTAGTTCGAAGACGA','AAAATAAACAAAGAATTAATCAATGAACTAACCAACGAAGTAAGCAAGGATATACATAGATTTATTCATTGATCTATCCATCGATGTATGCATGGACACAGACTTACTCACTGACCTACCCACCGACGTACGCACGGAGAGTTAGTCAGTGAGCTAGCCAGCGAGGTAGGCAGGGTTTTCTTTGTTCCTTCGTTGCTTGGTCTCTGTCCCTCCGTCGCTCGGTGTGCCTGCGTGGCTGGGCCCCGCCGGCGCGGGGAAA')
print string
'''
with open('6_Shortest_NonShared_Substring.txt') as infile:
	text1a = infile.read().strip()
	text2a = infile.read().strip()
	text1a =str(text1a)
	text2a= str(text2a)

print text1a
print text2a
answer = naive_shortest_non_shared_substring(text1a,text2a)
print answer
'''
with open('6_Shortest_NonShared_Substring_Answer.txt','w') as outfile:
	outfile.write(string)
	 
	 