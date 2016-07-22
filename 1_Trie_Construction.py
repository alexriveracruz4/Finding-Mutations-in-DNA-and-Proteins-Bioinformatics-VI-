'''  
  TRIECONSTRUCTION(Patterns)
        Trie is a graph consisting of a single node root
        for each string Pattern in Patterns
            currentNode  to root
            for i equals 1 to pattern length
                if there is an outgoing edge from currentNode with label currentSymbol
                    currentNode to ending node of this edge
                else
                    add a new node newNode to Trie
                    add a new edge from currentNode to newNode with label currentSymbol
                    currentNode go to  newNode
        return Trie
		
	CODE CHALLENGE: Solve the Trie Construction Problem.
     Input: A collection of strings Patterns.
     Output: The adjacency list corresponding to Trie(Patterns), in the following format. If
     Trie(Patterns) has n nodes, first label the root with 0 and then label the remaining nodes with
     the integers 1 through n minus 1 in any order you like. Each edge of the adjacency list of
    Trie(Patterns) will be encoded by a triple: the first two members of the triple must be the
    integers labeling the initial and terminal nodes of the edge, respectively; the third member
     of the triple must be the symbol labeling the edge.
	 '''
	 
def PrintTrie(trie):
    for i in range(len(trie)):
        for eachc in trie[i]:
			#string = '->'.join(map(str,trie[i][eachc]))
			print i,'->',trie[i][eachc],':',eachc
			#string = str(string)
			#print string
			with open('1_Trie_Construction_Answer.txt', 'a') as outputData:
				outputData.write(str(i))
				outputData.write('->')
				outputData.write(str(trie[i][eachc]))
				outputData.write(':')
				outputData.write(str(eachc))
				outputData.write('\n')

def BuildTrie(patterns):
    trie = [{}, {}] # a list of dictionary contain the trie structure
    id_inc = 1
    for eachp in patterns:
        startnode = 0
        for eachc in eachp:
            if eachc in trie[startnode]:
                startnode = trie[startnode][eachc]
            else:
                trie[startnode][eachc] = id_inc
                trie.append({})
                startnode = id_inc
                id_inc += 1
    return trie

if __name__ == "__main__":
    content = "GGTA\nCG\nGGC"
    patterns = content.split()
    #content = "GGCA"
    infile   = "1_Trie_Construction.txt"
    patterns = [ x.strip() for x in open(infile).readlines()]
    #patterns.sort()
    #print patterns
    trie = BuildTrie(patterns)
    PrintTrie(trie)
