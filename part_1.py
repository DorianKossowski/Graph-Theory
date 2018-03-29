import random as r

def gen_list(n, p):
	adj_list = [[] for _ in range(n)]
	for start in range(n):
		for end in range(n):
			if start == end:
				pass
			else:
				from_start = r.random()
				from_end = r.random()
				bigger, start_bigger = (from_start, True) if from_start >= from_end else (from_end, False)
				if bigger > p:
					if start_bigger and end not in adj_list[start]:
						adj_list[start].append(end)
					elif start not in adj_list[end]:
						adj_list[end].append(start)


	###############################################
	print("Lista sasiedztwa:")
	for i in range(n):
		print('{}: {}'.format(i, "  ".join(str(val) for val in adj_list[i])))
	###############################################

	return adj_list

def adj_matrix(adj_list):
	n = len(adj_list)
	matrix = [[0 for _ in range(n)]  for _ in range(n)]
	for start in range(n):
		for end in adj_list[start]:
			matrix[start][end] = 1	

	###############################################
	print("\nMacierz sasiedztwa:\n", end='   ')
	for i in range(n):
		print('{}'.format(i), end='  ')
	print()
	for i in range(n):
		print('{}: {}'.format(i, "  ".join(str(val) for val in matrix[i])))
	###############################################

def inc_matrix(adj_list):
	n = len(adj_list)
	m = sum(len(adj_list[i]) for i in range(n))
	matrix = [[0 for _ in range(m)] for _ in range(n)]
	present_m = 0
	for i in range(n):
		for el in adj_list[i]:
			matrix[i][present_m] = -1
			matrix[el][present_m] = 1
			present_m += 1

	###############################################
	print("\nMacierz incydencji:\n", end='  ')
	for i in range(m):
		print('{}'.format('L'+str(i)), end='\t')
	print()
	for i in range(n):
		print('{}: {}'.format(i, "\t".join(str(val) for val in matrix[i])))
	###############################################