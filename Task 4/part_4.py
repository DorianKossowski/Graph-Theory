# JOHNSON + DIJKSTRA
import part_3

def add_s(adj_list, val_list, new_adj_list, new_val_list):
	n = len(adj_list)
	for i in range(n):
		new_adj_list.append(adj_list[i])
		new_val_list.append(val_list[i])
	new_adj_list.append([i for i in range(n)])
	new_val_list.append([0 for i in range(n)])


def dijkstra(adj_list, val_list, v):
	n = len(adj_list)
	qs = [False for _ in range(n)]

	d = [part_3.sys.maxsize for _ in range(n)]
	p = [-1 for _ in range(n)]
	d[v] = 0

	for i in range(n):
		j = qs.index(False)		
		u = j
		j += 1
		while j<n:
			if not qs[j] and d[j] < d[u]:
				u = j
			j += 1
		qs[u] = True

		for y in range(len(adj_list[u])):
			if not qs[adj_list[u][y]] and d[adj_list[u][y]] > d[u] + val_list[u][y]:
				d[adj_list[u][y]] = d[u] + val_list[u][y]
				p[adj_list[u][y]] = u

	return d

def johnson(adj_list, val_list):
	new_adj_list = []
	new_val_list = []
	add_s(adj_list, val_list, new_adj_list, new_val_list)
	n = len(new_adj_list)

	###############################################
	print("Nowa lista sasiedztwa z dodanym wierzcholkiem 's':")
	for i in range(n):
		print('{}: {}'.format(i, "  ".join(str(el) for el in new_adj_list[i])))
	print("Nowa lista wag z dodanym 's':")
	for i in range(n):
		print('{}: {}'.format(i, "  ".join(str(el) for el in new_val_list[i])))
	###############################################

	h = part_3.bellman_ford(new_adj_list, new_val_list, n-1, True)

	if not h:
		print('Wykryto cykl ujemny z dodanym wierzcholkiem \'s\'')
	else:
		for u in range(n-1):
			for v in range(len(adj_list[u])):
				val_list[u][v] = val_list[u][v] + h[u] - h[adj_list[u][v]]

	n = len(adj_list)
	d_matrix = [[] for _ in range(n)]
	for u in range(n):
		d = dijkstra(adj_list, val_list, u)
		for v in range(n):
			d_matrix[u].append(d[v] - h[u] + h[v])

	for i in range(n):
		for j in range(n):
			print('d[{},{}] = {}'.format(i,j,d_matrix[i][j]))