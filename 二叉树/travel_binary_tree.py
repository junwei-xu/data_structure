#!/usr/bin/python3
# _*_coding=utf-8 _*_
# @author junwei
# @date 2021/5/30 16:48
# description 二叉树的遍历，深度优先（先序/中序/后序遍历），广度优先（层序遍历）
from 二叉树.create_binary_tree import BTNode, BinaryTree


class TravelDFS(object):
    def pre_order_travel(self, root: BTNode):
        """先序遍历"""
        if root is None:
            return
        print(root.data, end=' ')
        self.pre_order_travel(root.left)
        self.pre_order_travel(root.right)

    def in_order_travel(self, root: BTNode):
        """中序遍历"""
        if root is None:
            return
        self.in_order_travel(root.left)
        print(root.data, end=' ')
        self.in_order_travel(root.right)

    def post_order_travel(self, root: BTNode):
        """后序遍历"""
        if root is None:
            return
        self.post_order_travel(root.left)
        self.post_order_travel(root.right)
        print(root.data, end=' ')

    @staticmethod
    def layer_travel(root: BTNode):
        """层序遍历"""
        cur_nodes = [root]
        next_nodes = []
        while cur_nodes or next_nodes:
            for node in cur_nodes:
                print(node.data, end=' ')
                if node.left:
                    next_nodes.append(node.left)
                if node.right:
                    next_nodes.append(node.right)
            # 继续遍历下一层
            cur_nodes = next_nodes
            next_nodes = []

    def reverse(self, root: BTNode):
        """反转二叉树"""
        if root is not None:
            root.left, root.right = root.right, root.left
            self.reverse(root.left)
            self.reverse(root.right)


if __name__ == '__main__':
    # 构造二叉树
    tree = BinaryTree('A')
    B = tree.add(tree.root, 'B', True)
    C = tree.add(tree.root, 'C', False)
    D = tree.add(B, 'D', True)
    E = tree.add(B, 'E', False)
    F = tree.add(C, 'F', True)
    G = tree.add(C, 'G', False)
    H = tree.add(E, 'H', True)
    I = tree.add(G, 'I', True)
    J = tree.add(G, 'J', False)

    print('先序遍历:')
    TravelDFS().pre_order_travel(tree.root)
    print('\n中序遍历:')
    TravelDFS().in_order_travel(tree.root)
    print('\n后序遍历:')
    TravelDFS().post_order_travel(tree.root)

    print('\n层序遍历:')
    TravelDFS().layer_travel(tree.root)

    print('\n反转二叉树，先序遍历:')
    TravelDFS().reverse(tree.root)
    TravelDFS().pre_order_travel(tree.root)

