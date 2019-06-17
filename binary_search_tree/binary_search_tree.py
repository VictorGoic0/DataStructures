class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    while self:
      if value < self.value and self.left is None:
        self.left = BinarySearchTree(value)
        break
      elif value < self.value and self.left is not None:
        self = self.left
      elif value >= self.value and self.right is None:
        self.right = BinarySearchTree(value)
        break
      else:
        self = self.right
    # The recursive version below also works.
    # if value < self.value and self.left is None:
    #   self.left = BinarySearchTree(value)
    # elif value < self.value and self.left is not None:
    #   self.left.insert(value)
    # elif value >= self.value and self.right is None:
    #   self.right = BinarySearchTree(value)
    # else:
    #   self.right.insert(value)

  def contains(self, target):
    while True:
      if self.value == target:
        return True
      elif target < self.value and self.left is None:
        return False
      elif target < self.value and self.left is not None:
        self = self.left
      elif target >= self.value and self.right is None:
        return False
      else:
        self = self.right

  def get_max(self):
    while self:
      if self.right is None:
        return self.value
      else:
        self = self.right

  def for_each(self, cb):
    cb(self.value)
    if self.left and self.right:
      self.left.for_each(cb)
      self.right.for_each(cb)
    elif self.left:
      self.left.for_each(cb)
    elif self.right:
      self.right.for_each(cb)