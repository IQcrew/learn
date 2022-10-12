lec_graph = [ [2, 4, 5, 6, 7],
    [2, 3, 5, 6 ,7],
    [0, 1, 6, 7],
    [1, 4, 7],
    [0, 3, 6],
    [0, 1],
    [0, 1, 2, 4, 7],
    [0, 1, 2, 4, 7] ]

def is_indset(grapf_list, a):
    for graph in grapf_list:
        if "".join([str(i) for i in a]) in "".join([str(i) for i in graph]) or "".join([str(i) for i in a[::-1]]) in "".join([str(i) for i in graph]): return True
    return False

print(is_indset(lec_graph, []))

print(is_indset(lec_graph, [5]))

print(is_indset(lec_graph, [0, 2]))

print(is_indset(lec_graph, [6, 5, 3]))
