import matplotlib.pyplot as plt
import networkx as nx

def p(s,n):
    ss = range(s)
    pp = []
    n = list(ss)
    while len(pp) < 64:
        node = n.pop(0)	
        cc = list(ss)
        p = pp.pop(0) if len(pp)>1 else []
        for i in range(len(cc)):
            p1 = list(p)
            p1.append(cc[i])
            pp.append(p1)
            n.append(cc[i])
    return pp

def Qx(q):
    return Q.index(q)

def inputs():
    l = []
    for i in [1,0]:
        for j in range(6):
            for k in range(6):
                l.append((i, 0, j, k))
    return l
def transition(q, i):
    l = []
    for j in range(len(q)):
        if i[1] == j or i[2] == j or i[3] == j:
            l.append(i[0])
        else:
            l.append(q[j])
    return l
valid = lambda q: not (sum([q[p[0]]==q[p[1]] and q[0]!=q[p[0]] for p in prohibited]) > 0)

def possible_transitions(q):
    l = []
    for e in E:
        if e[0]!=q[0] and e[0]!=q[e[2]] and e[0]!=q[e[3]]:
            l.append((e, Qx( transition(q,e))))
    return l
			
def valid_transitions(q):
    l = []
    for n in possible_transitions(q):
        if valid(Q[n[1]]):
            l.append(n)
    return l

def find():
    nlist = range(len(Q))
    p = []
    n = [0]
    r = []
    
    while nlist:
        nn = n.pop(0)
        cc = valid_transitions(Q[nn])
        pp = p.pop(0) if len(p) > 0 else []
        
        for i in range(len(cc)):
            c = cc[i][1]
            r.append(c)
            
            if c in nlist:
                nlist = [i for i in range(len(Q)) if i not in r]
                np = list(pp)
                e = cc[i][0]
                np.append(e)
                p.append(np)
                n.append(c)
                if (c == Qx(F)):
                    return np
    return p
	
def color(q):
    if q == F: return "#2ECC71"
    if q == Q[0]:   return "#FFFFFF"
    return "#446CB3" if valid(q) else "#F22613"
	
def main():
	global E
	E = inputs()
	solution = find()
	
	for q in Q:
			G.add_node(Qx(q))

	for q in Q:
		children = valid_transitions(q)
		for c in children:
			G.add_edge( Qx(q), c[1],valid_transitions=c[0])

	nx.draw(G,node_color=[color(q) for q in Q],with_labels=True)
	
Q = []
E = []
Q = p(2,6)
F = Q[-1]
G = nx.Graph()

entities = ["Scientist", "Boy", "Girl", "Lion", "Cow", "Grains"]
prohibited = [(1,3),(2,3),(1,4),(2,4),(3,4),(4,5)]

if __name__ == '__main__':
	main()	
	plt.show()