import re

def parse_edges(file_path):
    edges = set()

    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            # 去掉注释
            line = line.split('%%')[0].strip()
            if not line or '<-->' not in line:
                continue

            # 匹配：源节点 <-->|权重| 目标节点1 & 目标节点2 & ...
            m = re.match(r'^(\w+)\s*<-->\s*\|(\d+)\|\s*(.+)$', line)
            if not m:
                continue

            src = m.group(1)
            weight = int(m.group(2))

            # 目标节点用 & 分隔
            targets = [t.strip() for t in re.split(r'\s*&\s*', m.group(3)) if t.strip()]

            for tgt in targets:
                # 双向边拆成两条有向边
                edges.add((src, tgt, weight))
                edges.add((tgt, src, weight))

    return edges


if __name__ == '__main__':
    # 请把文件名改成你的文件路径
    edges = parse_edges('flowchart.txt')

    # 输出 CSV：源,目的地,权重
    for src, tgt, weight in sorted(edges, key=lambda x: (x[0], x[1])):
        print(f'{src},{tgt},{weight}')
