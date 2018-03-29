import part_1, part_2, part_3, part_4

if __name__ == "__main__":
	
	n = int(input('Podaj ilosc wierzcholkow: '))

	while True:
		adj_list = part_1.gen_list(n, 0.5)
		part_1.adj_matrix(adj_list)
		part_1.inc_matrix(adj_list)

		adj_list = part_2.kosaraju(adj_list)

		values = part_3.assign_values(adj_list)

		b_f = part_3.bellman_ford(adj_list, values, 0)
		
		if b_f:
			part_4.johnson(adj_list, values)
		else:
			print('Ujemny cykl')

		if input('Powtorz (t - tak, n - nie): ') != 't':
			break

