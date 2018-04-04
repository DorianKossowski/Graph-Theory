def graph_center(adj_matrix):
	n = len(adj_matrix)
	values = [[i, sum(adj_matrix[i])] for i in range(n)]	# zlicza sume wartosci krawedzi
	print('Centrum grafu jest wierzcholek nr {}.'.format(min(values, key= lambda x: x[1])[0]))	# wypisuje index min z values

def graph_minimax(adj_matrix):
	n = len(adj_matrix)
	values = [[i, max(adj_matrix[i])] for i in range(n)]	# wyznacza odl do najdalszego wierzcholka	
	print('Centrum minimax grafu jest wierzcholek nr {}.'.format(min(values, key= lambda x: x[1])[0]))	# wypisuje index min z values