# DIJKSTRA
from sys import maxsize

def dijkstra(adj_list, val_list, v, printing):
	n = len(adj_list)
	qs = [False for _ in range(n)]

	d = [maxsize for _ in range(n)]
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

	if printing:
		print('Najkrotsze sciezki z wierzcholka {}'.format(v))
		for i in range(n):
			stack = []
			print('{}:'.format(i), end=' ')
			x = i
			while x != -1:
				stack.append(x)
				x = p[x]
			print('{} - {}'.format(stack[::-1], d[i]))
	return d