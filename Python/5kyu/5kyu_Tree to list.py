from collections import deque


class Node:
    def __init__(self, data, child_nodes=None):
        self.data = data
        self.child_nodes = child_nodes


def tree_to_list(tree_root):
    data = [tree_root.data]
    leaves = deque(tree_root.child_nodes)
    while leaves:
        node = leaves.popleft()
        data.append(node.data)
        if node.child_nodes:
            leaves.extend(node.child_nodes)
    return data


