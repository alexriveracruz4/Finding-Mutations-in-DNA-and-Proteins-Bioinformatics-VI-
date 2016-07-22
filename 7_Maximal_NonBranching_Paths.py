'''

https://github.com/ngaude/sandbox/blob/f009d5a50260ce26a69cd7b354f6d37b48937ee5/bioinformatics-002/bioinformatics_chapter4.py
Next lesson
CODE CHALLENGE: Implement MaximalNonBranchingPaths.
     Input: The adjacency list of a graph whose nodes are integers.
     Output: The collection of all maximal nonbranching paths in this graph.

Extra Dataset

View the code-graded challenge

Sample Input:
1 -> 2
2 -> 3
3 -> 4,5
6 -> 7
7 -> 6
Sample Output:
1 -> 2 -> 3
3 -> 4
3 -> 5
7 -> 6 -> 7

'''

def in_and_out_degree(adjacency_list):
    '''
    return the in and out degree lists for a given graph's adjacency list
    '''
    ind = {}
    outd = {}
    for (k, v) in adjacency_list:
        outd[k] = len(v)
        for kk in v:
            ind[kk] = ind.get(kk,0)+1
    return (ind,outd)
	
def maximal_non_branching_paths(adjacency_list):
    ''' 
    Implement MaximalNonBranchingPaths.
    Input: The adjacency list of a graph whose nodes are integers.
    Output: The collection of all maximal nonbranching paths in this graph.    
    '''
    dadj = {}
    for (k, v) in adjacency_list:
        dadj[k] = dadj.get(k,[]) + v[:]
    degree = in_and_out_degree(adjacency_list)
    paths = []
    def is_one_in_one_out(vertex):
        deg_in = degree[0].get(vertex,0)
        deg_out = degree[1].get(vertex,0)
        return (deg_in == 1) and (deg_out == 1)
    def visited(vertex):
        # linear time visited-vertex implementation
        # fixme : use dict to get constant time
        for path in paths:
            if vertex in path:
                return True
        return False
    def isolated_cycle(vertex):
        '''
        return isolated cycle including vertex v if any
        '''
        cycle = [vertex]
        while is_one_in_one_out(cycle[-1]):
            cycle.append(dadj[cycle[-1]][0])
            if cycle[0]==cycle[-1]:
                return cycle
        return None
    def non_branching_path(edge):
        '''
        return the non-branching path starting with edge edge
        '''
        branch = edge[:]
        while is_one_in_one_out(branch[-1]):     
            branch.append(dadj[branch[-1]][0])
        return branch
    for (v,e) in dadj.iteritems():
#        # cut-off optimization, skip v node if already in path list
#        if visited(v) : 
#            continue
        deg_in = degree[0].get(v,0)
        deg_out = degree[1].get(v,0)
        if (deg_in == 1 and deg_out == 1):
            # vertex v is 1-in-1-out node
            # could be part of a new isolated cycle, check this...
            if not visited(v):
                cycle = isolated_cycle(v)
                if cycle:
                    paths.append(cycle)
        elif (deg_out>0):
            # explore vertex v outgoing branches
            for w in e:
                paths.append(non_branching_path([v,w]))
    return paths
	
	
#fname = 'C:/Users/ngaude/Downloads/MaximalNonBranchingPaths.txt'
fname = '7_Maximal_NonBranching_Paths.txt'
ladj = [ ( int(l.split(' -> ')[0]), map(int,l.split(' -> ')[1].split(',')) ) for l in open(fname) ]
mnbp = maximal_non_branching_paths(ladj)
with open('7_Maximal_NonBranching_Paths_Answer.txt', "w") as f:
    for p in mnbp:
        f.write(' -> '.join(map(str,p))+'\n')
	