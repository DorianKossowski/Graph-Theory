# PRIM

def prim(adj_list, values):
	n = len(adj_list)

	visited = [False for _ in range(n)]
	v = 0
	visited[v] = True

	result = [[] for _ in range(n)]

	help_list = []
	for i in range(len(adj_list[v])):
		help_list.append([v,adj_list[v][i],values[v][i]])
	help_list.sort(key = lambda x: x[2])

	flag = True
	for _ in range(1,n):
		while flag:
			if not visited[help_list[0][1]]:
				visited[help_list[0][1]] = True
				result[help_list[0][0]].append(help_list[0][1])
				result[help_list[0][1]].append(help_list[0][0])
				for i in range(len(adj_list[help_list[0][1]])):
					help_list.append([help_list[0][1],adj_list[help_list[0][1]][i],values[help_list[0][1]][i]])
				del help_list[0]
				help_list.sort(key = lambda x: x[2])
				flag = False
			else:
				del help_list[0]
		flag = True
			


	###############################################
	print("Minimalne drzewo rozpinające:")
	for i in range(n):
		result[i].sort()
		print('{}: {}'.format(i, "  ".join(str(val) for val in result[i])))
	###############################################