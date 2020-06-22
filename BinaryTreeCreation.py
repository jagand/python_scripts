from collections import deque

class Node:

    def __init__(self, val = 0):
        self.val = val
        self.left = None
        self.right = None

class BinaryTree:

    def __init__(self):
        self.root = None
        self.all_paths = []

    def create_binary_tree(self, elems = []):

        if len(elems) < 1:
            return 
        else:
            mid_index = len(elems) // 2

        self.root = Node(elems[mid_index])
        for counter, elem in enumerate(elems):
            if counter != mid_index:
                self.add_elem(elem)

    def add_elem(self, val):

        if self.root is None:
            self.root = Node(val)
        elif (val < self.root.val):
            self.root.left = self._add_elems(val, self.root.left)
        elif (val > self.root.val):
            self.root.right = self._add_elems(val, self.root.right)

    def _add_elems(self, val, node):

        if node is None:
            return Node(val)
        elif (val < node.val):
            node.left = self._add_elems(val, node.left)
            return node
        elif (val > node.val):
            node.right = self._add_elems(val, node.right)
            return node

    def __repr__(self):
        nodes = []
        que = deque()
        que.append(self.root)
        while que:
            len_of_curr_level = len(que)
            elems_in_level = []
            for _ in range(len_of_curr_level):
                current_node = que.popleft()
                elems_in_level.append(current_node.val)

                if current_node.left:
                    que.append(current_node.left)
                if current_node.right:
                    que.append(current_node.right)

            nodes.append(elems_in_level)
        return '\n'.join([' | '.join([str(elem) for elem in node]) for node in nodes])

    def get_all_paths(self, node = None, path = None):

        if node is None and self.root is not None:
            node = self.root
        
        if path is None:
            path = []
        
        path.append(node.val)

        if node.left is None and node.right is None:
            self.all_paths.append(list(path))
        else:
            if node.left is not None:
                self.get_all_paths(node.left, path)
            if node.right is not None:
                self.get_all_paths(node.right, path)

        del path[-1]

    def get_tree_depth(self):

        depth = 0
        que = deque()
        que.append(self.root)
        while que:
            depth += 1

            length_of_curr_level = len(que)
            for _ in range(length_of_curr_level):
                curent_node = que.popleft()
                if curent_node.left:
                    que.append(curent_node.left)
                if curent_node.right:
                    que.append(curent_node.right)  

        return depth


tree = BinaryTree()
tree.create_binary_tree([10,20,30,40,50,60])
print ('-'*20)
print (tree)
print (f"Tree depth: {tree.get_tree_depth()}")  
print (tree.get_all_paths())
print (tree.all_paths)
print ('-'*20)
tree.add_elem(12)
tree.add_elem(22)
tree.add_elem(32)
tree.add_elem(42)
tree.add_elem(52)
tree.add_elem(62)
tree.add_elem(72)
tree.add_elem(2)
print (tree)
print (f"Tree depth: {tree.get_tree_depth()}")  
tree.all_paths = []
print (tree.get_all_paths())
print (tree.all_paths)
print ('-'*20)
