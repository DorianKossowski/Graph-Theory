import part_1, part_2, part_3, part_4, part_5

if __name__ == "__main__":
	
	n = int(input('Podaj ilosc wierzcholkow: '))
	v = 0
	while v < n-1 or v > sum(range(n)):
		v = int(input('Podaj ilosc krawedzi (min. {}, max. {}): '.format(n-1, sum(range(n)))))
	
	adj_list = part_1.gen_list(n,v)
	part_1.adj_matrix(adj_list)
	part_1.inc_matrix(adj_list)
	values = part_1.assign_values(adj_list)

	part_2.dijkstra(adj_list,values,0, True)

	matrix = part_3.adj_matrix(adj_list,values)

	part_4.graph_center(matrix)
	part_4.graph_minimax(matrix)

	part_5.prim(adj_list, values)