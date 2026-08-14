import heapq
import sys
from collections import defaultdict

def read_graph(file_path):
    """读取边文件，返回邻接表（带权重）"""
    graph = defaultdict(list)
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split(',')
            if len(parts) != 3:
                print(f"警告：跳过格式错误的行: {line}")
                continue
            u = parts[0].strip()
            v = parts[1].strip()
            try:
                w = float(parts[2].strip())
            except ValueError:
                print(f"警告：权重非数值，跳过: {line}")
                continue
            graph[u].append((v, w))
    return graph

def dijkstra_all_shortest_paths(graph, start, end):
    """
    Dijkstra 算法，计算从 start 到 end 的最短距离，
    并记录所有可能的前驱节点（用于回溯所有最短路径）。
    返回 (最短距离, 前驱字典, 距离字典)
    """
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    predecessors = {node: [] for node in graph}
    pq = [(0, start)]

    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in graph.get(u, []):
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                predecessors[v] = [u]
                heapq.heappush(pq, (nd, v))
            elif nd == dist[v]:
                predecessors[v].append(u)

    return dist, predecessors

def dfs_paths(predecessors, start, end, path, all_paths):
    """DFS 回溯所有最短路径（从 end 到 start）"""
    if end == start:
        all_paths.append(path[::-1])
        return
    for pred in predecessors.get(end, []):
        path.append(pred)
        dfs_paths(predecessors, start, pred, path, all_paths)
        path.pop()

def format_path_with_weights(path, dist):
    """
    将路径节点列表转换为带权重的字符串。
    格式：S -> A10 (1.0) -> A17 (1.0) ...
    每个边权重由 dist 差值计算得出。
    """
    if len(path) < 2:
        return str(path)
    parts = [path[0]]
    for i in range(len(path) - 1):
        w = dist[path[i+1]] - dist[path[i]]
        parts.append(f"-> {path[i+1]} ({w})")
    return " ".join(parts)

def main():
    file_path = "edge.txt"
    start = "S"
    end = "L1"

    try:
        graph = read_graph(file_path)
    except FileNotFoundError:
        print(f"错误：文件 {file_path} 不存在！")
        sys.exit(1)

    if start not in graph:
        print(f"错误：起点 {start} 不在图中！")
        sys.exit(1)
    if end not in graph and end != start:
        print(f"错误：终点 {end} 不在图中！")
        sys.exit(1)

    dist, predecessors = dijkstra_all_shortest_paths(graph, start, end)

    if dist[end] == float('inf'):
        print(f"从 {start} 到 {end} 不存在路径！")
        return

    all_paths = []
    dfs_paths(predecessors, start, end, [end], all_paths)

    if not all_paths:
        print("未找到任何最短路径，请检查前驱记录。")
        return

    print(f"从 {start} 到 {end} 的最短路径长度：{dist[end]}\n")
    print(f"共找到 {len(all_paths)} 条不循环的最短路径：\n")

    for idx, path in enumerate(all_paths, 1):
        path_str = format_path_with_weights(path, dist)
        node_count = len(path)
        print(f"路径 {idx}:")
        print(f"  路径（含每段权重）: {path_str}")
        print(f"  经过节点数量: {node_count}")
        print(f"  最短路径长度: {dist[end]}\n")

if __name__ == "__main__":
    main()
