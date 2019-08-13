# From https://github.com/TheAlgorithms/Python/blob/7cdda931fd6e272529f25a4cd2dbd7c6785d467c/graphs/basic_graphs.py#L146

if __name__ == "__main__":
    # Accept No. of Nodes and edges
    n, m = map(int, input().split(" "))
    
    # Initialising Dictionary of edges
    g = {}
    for i in range(n):
        g[i+1] = []

    """
    ----------------------------------------------------------------------------
        Accepting edges of Unweighted Directed Graphs
    ----------------------------------------------------------------------------
    """

    for _ in range(m):
        x, y = map(int, input().strip().strip(" "))
        g[x].append(y)

    """
    ----------------------------------------------------------------------------
        Accepting edges of Unweighted Undirected Graphs
    ----------------------------------------------------------------------------
    """

    for _ in range(m):
        x, y = map(int, input().strip.strip(" "))
        g[x].append(y)
        g[y].append(x)

    """
    ----------------------------------------------------------------------------
        Accepting edges of Weighted Undirected Graphs
    ----------------------------------------------------------------------------
    """

    for _ in range(m):
        x, y, r = map(int, input().strip.strip(" "))
        g[x].append([y, r])
        g[y].append([x, r])