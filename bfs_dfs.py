import queue
import time
import networkx as nx
import matplotlib.pyplot as plt  

# bfs: as broad as possible, and then going deeper
def order_bfs(graph, start_node):
    visited = set() 
    q = queue.Queue()
    q.put(start_node)
    order = []

    while not q.empty():
        vertex = q.get()
        if vertex not in visited:
            order.append(vertex)
            visited.add(vertex) 
            for node in graph[vertex]:  # go through neighbor nodes
                if node not in visited:
                    q.put(node)
    return order

# dfs: as deep as possible, and then going broad -> recursive!
def order_dfs(graph, start_node, visited=None):
    if visited is None:
        visited = set()
    order = []
    if start_node not in visited:
        order.append(start_node)
        visited.add(start_node)
        for node in graph[start_node]:
            if node not in visited:
                order.extend(order_dfs(graph, node, visited))
    return order

# visualize the algorithms!
def visualize_search(order, title, G, pos):
    plt.figure()
    plt.title(title)
    for i, node in enumerate(order, start=1):
        plt.clf()
        plt.title(title)
        nx.draw(G, pos, with_labels=True, node_color=['r' if n == node else 'g' for n in G.nodes])
        plt.draw()
        plt.pause(2)
    plt.show()
    time.sleep(0.5)

# creating a graph to test
G = nx.Graph()  
G.add_edges_from([('A', 'B'), ('A', 'C'), ('B', 'D'), ('B', 'E'), ('C', 'F'), ('C', 'G')])
pos = nx.spring_layout(G)

# visualize the bfs search order
visualize_search(order_bfs(G, start_node='A'), title='BFS Visualization', G=G, pos=pos)
# visualize the dfs search order
visualize_search(order_dfs(G, start_node='A'), title='DFS Visualization', G=G, pos=pos)