# KOSARAJU

def dfs_stack(v, visited, stack, adj_list):
	visited[v] = True
	for el in adj_list[v]:
		if visited[el] == False:
			dfs_stack(el, visited, stack, adj_list)
	stack.append(v)

def dfs_end(v, visited, adj_list, present_scc):
	visited[v] = True
	present_scc.append(v)
	for el in adj_list[v]:
		if visited[el] == False:
			dfs_end(el, visited, adj_list, present_scc)

def transposition(adj_list):
	n = len(adj_list)
	trans_list = [[] for _ in range(n)]
	for i in range(n):
		for el in adj_list[i]:
			trans_list[el].append(i)

	return trans_list


def kosaraju(adj_list):
	n = len(adj_list)
	visited = [False for _ in range(n)]
	stack = []

	for v in range(n):
		if visited[v] == False:
			dfs_stack(v, visited, stack, adj_list)

	print('\nStos: {}\n'.format(stack))

	trans_list = transposition(adj_list)

	visited = [False for _ in range(n)]
	component_nr = 1
	scc = []
	present_scc = []
	while len(stack):
		v = stack.pop()
		if visited[v] == False:
			print('Silnie spojna skladowa nr {}:'.format(component_nr))
			component_nr += 1
			dfs_end(v, visited, trans_list, present_scc)
			scc.append(present_scc)
			print(present_scc)
			present_scc = []
	

	longest_scc = max(scc, key=len)
	longest_scc.sort()
	print('\nNajdluzsza silnie spojna skladowa, ktora bedzie wykorzystywana w dalszej czesci programu: {}'.format(longest_scc))
	result = [adj_list[el] for el in longest_scc]
	
	for i in range(len(result)):
		j=0
		while j < len(result[i]):
			if result[i][j] not in longest_scc:
				result[i].remove(result[i][j])
			else:
				result[i][j] = longest_scc.index(result[i][j])
				j += 1

	###############################################
	print("Nowa lista sasiedztwa:")
	for i in range(len(result)):
		print('{}: {}'.format(i, "  ".join(str(val) for val in result[i])))
	###############################################

	return result