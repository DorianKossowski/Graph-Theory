from random import randint

def gen_list(n,v):
	adj_list = [[] for _ in range(n)]
	for i in range(1,n):
		u = randint(0,i-1)
		adj_list[u].append(i)
		adj_list[i].append(u)

	counter = n-1
	while counter < v:
		u = randint(0, n-1)
		w = randint(0, n-1)
		if w not in adj_list[u] and u != w:
			adj_list[u].append(w)
			adj_list[w].append(u)
			counter += 1

	###############################################
	print("Lista sasiedztwa:")
	for i in range(n):
		adj_list[i].sort()
		print('{}: {}'.format(i, "  ".join(str(val) for val in adj_list[i])))
	###############################################
	return adj_list

def adj_matrix(adj_list):
	n = len(adj_list)
	matrix = [[0 for _ in range(n)]  for _ in range(n)]
	for start in range(n):
		for end in adj_list[start]:
			matrix[start][end] = 1
			matrix[end][start] = 1	

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
	temp = [[el for el in adj_list[i]] for i in range(n)]
	m = sum(len(adj_list[i]) for i in range(n)) // 2
	matrix = [[0 for _ in range(m)] for _ in range(n)]
	present_m = 0
	for i in range(n):
		for el in temp[i]:
			matrix[i][present_m] = 1
			matrix[el][present_m] = 1
			present_m += 1
			temp[el].remove(i)


	###############################################
	print("\nMacierz incydencji:\n", end='  ')
	for i in range(m):
		print('{}'.format('L'+str(i)), end='\t')
	print()
	for i in range(n):
		print('{}: {}'.format(i, "\t".join(str(val) for val in matrix[i])))
	###############################################

def assign_values(adj_list):
	n = len(adj_list)
	val = [[0 for _ in range(len(adj_list[i]))] for i in range(n)]
	for i in range(n):
		for j, ele in enumerate (adj_list[i]):
			if val[i][j] == 0:
				number = randint(1,10)
				val[i][j] = number
				val[ele][adj_list[ele].index(i)] = number

	###############################################
	print("Lista wag:")
	for i in range(len(val)):
		print('{}: {}'.format(i, "  ".join(str(el) for el in val[i])))
	###############################################

	return val