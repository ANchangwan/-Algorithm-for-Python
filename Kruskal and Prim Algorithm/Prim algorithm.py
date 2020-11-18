from queue import priorityQueue

def prim(adj, start):
    covered = set()

    res_edges = []

    queue = PriorityQueue()
    queue.put(0, start, None) # cost, node, source

    while not queue.empty():
        u_cost, u, u_src = queue.get()
        if u in covered: continue

        covered.add(u)

        if u_src is not None:
            res_edges.append((u_cost, u, u_src))

        for v_cost, v in adj[u]:
            if v not in covered:
                queue.put((v_cost, v, u))

    return res_edges
