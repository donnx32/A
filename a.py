import matplotlib.pyplot as plt
import networkx as nx

Q = []
G = nx.Graph()

entities = ["Scientist", "Human1", "Human2", "Lion", "Cow", "Grains"]
prohibited = [(1,3),(2,3),(1,4),(2,4),(3,4),(4,5)]



def permute(s,n):
    seq = range(s)
    permutations = []
    nodes = list(seq)
    while len(permutations) < s**n:
        node = nodes.pop(0)
        children = list(seq)
        permutation = permutations.pop(0) if len(permutations)>1 else []
        for i in range(len(children)):
            perm = list(permutation)
            perm.append(children[i])
            permutations.append(perm)
            nodes.append(children[i])
    return permutations

def solve(q):
	not_visited = range(len(Q))
	paths = []
	nodes = [Qx(q)]
	r = []
	while not_visited:
		node = nodes.pop(0)
		children = valid_transitions(Q[node])
		path = paths.pop(0) if len(paths)>0 else []
		for i in range(len(children)):
			child = children[i][1]
			r.append(child)
			if child in not_visited:
				not_visited = [i for i in range(len(Q)) if i not in r]
				newpath = list(path)
				e = children[i][0]
				newpath.append(e)
				paths.append(newpath)
				nodes.append(child)
				if (child == Qx(F)):
					return newpath
	return paths
	
def color(q):
    if q == F: return "#2ECC71"
    if q == Q[0]:   return "#FFFFFF"
    return "#446CB3" if valid(q) else "#F22613"

def t():
	temp = []
	for i in [1,0]:
		for j in range(6):
			for k in range(6):
				temp.append((i, 0, j, k))
	
	return temp

def main():
	solution = solve(Q[0])
	
	q = Q[0]
	print(q)
	for e in solution:
		q = T(q,e)
		print(q)
		
	for q in Q:
		G.add_node(Qx(q))

	for q in Q:
		children = transition(q)
		for c in children:
			G.add_edge( Qx(q), c[1],transition=c[0])
	
	path = nx.shortest_path(G,source=0,target=63)
	path1 = nx.all_shortest_paths(G,source=0,target=63)
	nx.draw(G,node_color=[color(q) for q in Q],with_labels=True)
	print(path1)
	plt.show()

Q = permute(2,6)
F = Q[-1]
Qx = lambda q: Q.index(q)
E = [ (i, 0, j, k) for i in [1,0] for j in range(6) for k in range(6) ]
T = lambda q, i: [ i[0] if i[1] == j or i[2] == j or i[3] == j else q[j] for j in range(len(q))]
valid = lambda q: not (sum([q[p[0]]==q[p[1]] and q[0]!=q[p[0]] for p in prohibited]) > 0)
transition = lambda q: [ (e, Qx( T(q,e) )) for e in E if e[0]!=q[0] and e[0]!=q[e[2]] ]
valid_transitions = lambda q: [ n for n in transition(q) if valid(Q[n[1]]) ]

if __name__ == '__main__':
	print(Qx([0,0,0,0,0,1]))
	print("x")
	main()	
	