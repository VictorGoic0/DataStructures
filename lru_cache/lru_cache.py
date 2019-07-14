# from doubly_linked_list import DoublyLinkedList
from collections import OrderedDict

# class LRUCache:
#   def __init__(self, limit=10):
#     self.limit = limit
#     self.items = 0
#     self.storage = {}
#     self.orderedKeys = DoublyLinkedList()

#   def get(self, key):
#     if key not in self.storage:
#       return None
#     current_node = self.orderedKeys.head
#     while current_node:
#       if current_node.value == key:
#         self.orderedKeys.move_to_end(current_node)
#         break
#       current_node = current_node.next
#     return self.storage[key]

#   def set(self, key, value):
#     if key in self.storage:
#       self.storage[key] = value
#     else:
#       self.storage[key] = value
#       self.orderedKeys.add_to_tail(key)
#       self.items += 1
#       if self.items > self.limit:
#         old_key = self.orderedKeys.remove_from_head()
#         self.storage.pop(old_key)
#         self.items -= 1
class LRUCache:
  def __init__(self, limit=10):
    self.limit = limit
    self.items = 0
    self.storage = OrderedDict()

  def get(self, key):
    if key not in self.storage:
      return None
    self.storage.move_to_end(key)
    return self.storage[key]

  def set(self, key, value):
    if key in self.storage:
      self.storage[key] = value
      self.storage.move_to_end(key)
    else:
      self.storage[key] = value
      self.items += 1
      if self.items > self.limit:
        self.storage.popitem(False)
        self.items -= 1