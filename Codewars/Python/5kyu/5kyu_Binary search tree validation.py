class T:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def is_bst(node):
    arr = []

    def traverse(node):
        if node:
            traverse(node.left)
            arr.append(node.value)
            traverse(node.right)
    traverse(node)
    return arr == sorted(arr) or arr == sorted(arr, reverse=True)
