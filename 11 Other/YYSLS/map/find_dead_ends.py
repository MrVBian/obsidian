def find_dead_ends(filename="edge.txt", start="S", target="L1"):
    # 构建无向图：每个节点用 set 存储其邻居（自动去重）
    neighbors = {}
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split(',')
            if len(parts) < 3:
                continue
            u, v = parts[0].strip(), parts[1].strip()
            # 添加双向连接（因为是双向图）
            if u not in neighbors:
                neighbors[u] = set()
            if v not in neighbors:
                neighbors[v] = set()
            neighbors[u].add(v)
            neighbors[v].add(u)

    # 筛选度为 1 且不是起点或终点的节点
    dead_ends = [node for node, nbrs in neighbors.items()
                 if len(nbrs) == 1 and node not in (start, target)]

    # 按字母顺序排序输出
    dead_ends.sort()
    print(f"死胡同节点数: {len(dead_ends)}")
    print("节点列表:")
    for node in dead_ends:
        print(node)

if __name__ == "__main__":
    find_dead_ends()
