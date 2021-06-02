#!/usr/bin/python3
# _*_coding=utf-8 _*_
# @author junwei
# @date 2021/5/30 15:03
# description 构建一个二叉树
class BTNode(object):
    """定义二叉树结点"""

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BinaryTree(object):
    def __init__(self, root_item):
        self.root = BTNode(root_item)

    def add(self, parent: BTNode, item, is_left=True):
        """添加结点"""
        new_node = BTNode(item)
        if parent is None:
            raise Exception('no such node')
        else:
            if is_left:
                parent.left = new_node
            else:
                parent.right = new_node
        return new_node


if __name__ == '__main__':
    tree = BinaryTree('A')
    B = tree.add(tree.root, 'B', True)
    C = tree.add(tree.root, 'C', False)
    D = tree.add(B, 'D', True)
    E = tree.add(B, 'E', False)
    F = tree.add(C, 'F', True)
    G = tree.add(F, 'G', True)
    print(tree.root.left.data)
    print(B.right.data)
    print(F.left.data)
