import part_2

def adj_matrix(adj_list, values):
	n = len(adj_list)
	matrix = []
	for i in range(n):
		matrix.append(part_2.dijkstra(adj_list, values, i, False))

	###############################################
	print("\nMacierz odleglosci:\n", end='   ')
	for i in range(n):
		print('{}'.format(i), end='  ')
	print()
	for i in range(n):
		print('{}: {}'.format(i, "  ".join(str(val) for val in matrix[i])))
	###############################################

	return matrix