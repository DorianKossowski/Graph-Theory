# BELLMAN-FORD
import random as r
import sys

def assign_values(adj_list):
	n = len(adj_list)
	val = [[] for _ in range(n)]
	for i in range(n):
		for j in range(len(adj_list[i])):
			val[i].append(r.randrange(-5,11))

	###############################################
	print("Lista wag:")
	for i in range(len(val)):
		print('{}: {}'.format(i, "  ".join(str(el) for el in val[i])))
	###############################################

	return val

def bellman_ford(adj_list, val_list, v, s=False):
	n = len(adj_list)
	d = [sys.maxsize for _ in range(n)]
	p = [-1 for _ in range(n)]
	d[v] = 0

	for i in range(n-1):
		for x in range(n):
			for y in range(len(adj_list[x])):
				if d[adj_list[x][y]] > d[x] + val_list[x][y]:
					d[adj_list[x][y]] = d[x] + val_list[x][y]
					p[adj_list[x][y]] = x

	for x in range(n-1):
		for y in range(len(adj_list[x])):
			if d[adj_list[x][y]] > d[x] + val_list[x][y]:
				return None


	print('Najkrotsze sciezki z wierzcholka {}'.format('\'s\'' if s else v))
	for i in range(n):
		stack = []
		print('{}:'.format(i), end=' ')
		x = i
		while x != -1:
			stack.append(x)
			x = p[x]
		print('{} - {}'.format(stack[::-1], d[i]))

	return d