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

  def contains(self, target):
    pass

  def get_max(self):
    pass

  def for_each(self, cb):
    pass