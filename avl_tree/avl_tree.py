class Stack():
  def __init__(self):
    self.stack = []
    self.length = 0
  def push(self, value):
    self.length += 1
    self.stack.append(value)
  def pop(self):
    if self.size() > 0:
      self.length -= 1
      return self.stack.pop()
    else:
      return None
  def size(self):
    return self.length
  def clear(self):
    self.stack = []

"""
Node class to keep track of
the data internal to individual nodes
"""
class Node:
  def __init__(self, key):
    self.key = key
    self.left = None
    self.right = None

"""
A tree class to keep track of things like the
balance factor and the rebalancing logic
"""
class AVLTree:
  def __init__(self, node=None):
    self.node = node
    # init height to -1 because of 0-indexing
    self.height = -1
    self.balance = 0

  """
  Display the whole tree. Uses recursive def.
  """
  def display(self, level=0, pref=''):
    self.update_height()  # Update height before balancing
    self.update_balance()
    
    if self.node != None: 
      print ('-' * level * 2, pref, self.node.key,
        f'[{self.height}:{self.balance}]',
        'L' if self.height == 0 else ' ')
      if self.node.left != None:
        self.node.left.display(level + 1, '<')
      if self.node.right != None:
        self.node.right.display(level + 1, '>')

  """
  Computes the maximum number of levels there are
  in the tree
  """
  def update_height(self):
    ## Come back and optimize later, should know which side to search for deepest node based on the balance of the tree
    if self.node is None:
      return
    s = Stack()
    visited = set()
    max_height = -1
    starting_vertex = self.node
    s.push([starting_vertex])
    while s.size() > 0:
      path = s.pop()
      node = path[-1]
      if node not in visited:
        visited.add(node)
        if node.left and node.right:
          left_path = path[:]
          left_path.append(node.left.node)
          s.push(left_path)
          right_path = path[:]
          right_path.append(node.right.node)
          s.push(right_path)
        elif node.left:
          left_path = path[:]
          left_path.append(node.left.node)
          s.push(left_path)
        elif node.right:
          right_path = path[:]
          right_path.append(node.right.node)
          s.push(right_path)
        else:
          length = len(path) - 1
          if length > max_height:
            max_height = length
      self.height = max_height
    
    
  """
  Updates the balance factor on the AVLTree class
  """
  def update_balance(self):
    if self.node.left and self.node.right:
      self.node.left.update_height()
      left_height = self.node.left.height
      self.node.right.update_height()
      right_height = self.node.right.height
      self.balance = left_height - right_height
    elif self.node.left:
      self.node.left.update_height()
      self.balance = self.node.left.height + 1
    elif self.node.right:
      self.node.right.update_height()
      self.balance = -1 - self.node.right.height
    else:
      self.balance = 0


  """
  Perform a left rotation, making the right child of this
  node the parent and making the old parent the left child
  of the new parent. 
  """
  def left_rotate(self):
    if self.node.right:
      right_child = self.node.right.node
      self.node.right = None
      previous_node = self.node
      self.node = right_child
      if self.node.left:
        previous_left = self.node.left.node
        self.node.left.node = previous_node
        self.node.left.node.right = AVLTree(previous_left)
      else:
        self.node.left = AVLTree(previous_node)

  """
  Perform a right rotation, making the left child of this
  node the parent and making the old parent the right child
  of the new parent. 
  """
  def right_rotate(self):
    if self.node.left:
      left_child = self.node.left.node
      self.node.left = None
      previous_node = self.node
      self.node = left_child
      if self.node.right:
        previous_right = self.node.right.node
        self.node.right.node = previous_node
        self.node.right.node.left = AVLTree(previous_right)
      else:
        self.node.right = AVLTree(previous_node) 
  """
  Sets in motion the rebalancing logic to ensure the
  tree is balanced such that the balance factor is
  1 or -1
  """
  def rebalance(self):
    balances = set([-1, 1])
    self.update_balance()
    if self.balance > 1 or self.balance < -1:
      s = Stack()
      if self.balance > 1:
        self.node.left.update_balance()
        s.push([self, self.node.left])
      elif self.balance < -1:
        self.node.right.update_balance()
        s.push([self, self.node.right])
      while s.size() > 0:
        # Keep performing rotations until balance is <= 1
        path = s.pop()
        tree = path[-1]
        if tree.balance in balances:
          if tree.balance == -1 or tree.balance == 1:
            parent = path[-2]
            # print('fired')
            def getKey(tree):
              return tree.node.key
            result = map(getKey, path)
            # print(list(result), '<----path')
            # print(tree.node.key)
            # print(parent.node.key)
            if self.balance > 1:
              tree.left_rotate()
              parent.right_rotate()
            elif self.balance < -1 :
              tree.right_rotate()
              parent.left_rotate()
            # print(parent.node.key, '<--- parent')
            break
          else:
            parent = path[-2]
            tree.right_rotate()
            parent.left_rotate()
            break
        else:
          if tree.node.left:
            tree.node.left.update_balance()
            new_path = path[:]
            new_path.append(tree.node.left)
            s.push(new_path)
          if tree.node.right:
            tree.node.right.update_balance()
            new_path = path[:]
            new_path.append(tree.node.right)
            s.push(new_path)

    
  """
  Uses the same insertion logic as a binary search tree
  after the value is inserted, we need to check to see
  if we need to rebalance
  """
  def insert(self, key):
    # Regular BST insertion
    if self.node:
      s = Stack()
      s.push([self])
      final_path = None
      while s.size() > 0:
        path = s.pop()
        tree = path[-1]
        if key < tree.node.key and tree.node.left is None:
          tree.node.left = AVLTree(Node(key))
          final_path = path[:]
          s.clear()
          break
        elif key < tree.node.key and tree.node.left is not None:
          new_path = path[:]
          new_path.append(tree.node.left)
          s.push(new_path)
        elif key >= tree.node.key and tree.node.right is None:
          tree.node.right = AVLTree(Node(key))
          final_path = path[:]
          s.clear()
          break
        else:
          new_path = path[:]
          new_path.append(tree.node.right)
          s.push(new_path)
      while len(final_path) > 0:
        parent = final_path.pop()
        parent.update_balance()
        if parent.balance > 1 or parent.balance < -1:
          parent.rebalance()
    else:
      self.node = Node(key)