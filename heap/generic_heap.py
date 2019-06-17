class Heap:
  def __init__(self, comparator = lambda x, y: x >= y ):
    self.storage = []
    self.comparator = comparator

  def insert(self, value):
    index = len(self.storage)
    self.storage.append(value)
    self._bubble_up(index)

  def delete(self):
    deleted = self.storage[0]
    self.storage[0] = self.storage[-1]
    self.storage.pop()
    self._sift_down(0)
    return deleted

  def get_priority(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    while index > 0:
      parent = (index - 1) // 2
      if self.comparator(self.storage[index], self.storage[parent]):
        self.storage[index], self.storage[parent] = self.storage[parent], self.storage[index]
        index = parent
      else:
        break

  def _sift_down(self, index):
    length = len(self.storage)
    while True:
      child1 = (2 * index) + 1
      child2 = (2 * index) + 2
      if child1 >= length and child2 >= length:
        break
      elif child1 < length and child2 < length:
        if self.comparator(self.storage[child1], self.storage[child2]):
          if self.comparator(self.storage[child1], self.storage[index]):
            self.storage[child1], self.storage[index] = self.storage[index], self.storage[child1]
            index = child1
          else:
            break
        elif self.comparator(self.storage[child2], self.storage[child1]):
          if self.comparator(self.storage[child2], self.storage[index]):
            self.storage[child2], self.storage[index] = self.storage[index], self.storage[child2]
            index = child2
          else:
            break
      elif child1 < length:
        if self.comparator(self.storage[child1], self.storage[index]):
          self.storage[child1], self.storage[index] = self.storage[index], self.storage[child1]
          index = child1
        else:
          break
      elif child2 < length:
        if self.comparator(self.storage[child2], self.storage[index]):
          self.storage[child2], self.storage[index] = self.storage[index], self.storage[child2]
          index = child2
        else:
          break
