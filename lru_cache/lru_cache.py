from doubly_linked_list import DoublyLinkedList

class LRUCache:
  def __init__(self, limit=10):
    self.limit = limit
    self.items = 0
    self.storage = {}
    self.orderedKeys = DoublyLinkedList()

  def get(self, key):
    if key not in self.storage:
      return None
    current_node = self.orderedKeys.head
    while current_node:
      if current_node.value == key:
        self.orderedKeys.move_to_end(current_node)
        break
      current_node = current_node.next
    return self.storage[key]

  """
  Adds the given key-value pair to the cache. The newly-
  added pair should be considered the most-recently used
  entry in the cache. If the cache is already at max capacity
  before this entry is added, then the oldest entry in the
  cache needs to be removed to make room. Additionally, in the
  case that the key already exists in the cache, we simply 
  want to overwrite the old value associated with the key with
  the newly-specified value. 
  """
  def set(self, key, value):
    if key in self.storage:
      self.storage[key] = value
    else:
      self.storage[key] = value
      self.orderedKeys.add_to_tail(key)
      self.items += 1
      if self.items > self.limit:
        old_key = self.orderedKeys.remove_from_head()
        self.storage.pop(old_key)
        self.items -= 1
