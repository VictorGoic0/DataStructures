"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
  def __init__(self, value, prev=None, next=None):
    self.value = value
    self.prev = prev
    self.next = next

  """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""
  def insert_after(self, value):
    current_next = self.next
    self.next = ListNode(value, self, current_next)
    if current_next:
      current_next.prev = self.next

  """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""
  def insert_before(self, value):
    current_prev = self.prev
    self.prev = ListNode(value, current_prev, self)
    if current_prev:
      current_prev.next = self.prev

  """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""
  def delete(self):
    if self.prev:
      self.prev.next = self.next
    if self.next:
      self.next.prev = self.prev

"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
  def __init__(self, node=None):
    self.head = node
    self.tail = node
    self.length = 1 if node is not None else 0

  def __len__(self):
    return self.length

  def add_to_head(self, value):
    if self.head:
      current_head = self.head
      self.head.insert_before(value)
      self.head = ListNode(value, None, current_head)
      current_head.prev = self.head
    else:
      self.head = ListNode(value)
      self.tail = self.head
    self.length += 1

  def remove_from_head(self):
    current_head = self.head
    self.delete(self.head)
    self.head = current_head.next
    return current_head.value

  def add_to_tail(self, value):
    if self.tail:
      current_tail = self.tail
      self.tail.insert_after(value)
      self.tail = ListNode(value, current_tail)
      current_tail.next = self.tail
    else:
      self.tail = ListNode(value)
      self.head = self.tail
    self.length += 1

  def remove_from_tail(self):
    current_tail = self.tail
    self.delete(self.tail)
    self.tail = current_tail.prev
    return current_tail.value

  def move_to_front(self, node):
    tail = False
    if (node.next == None):
      tail = True
    if tail:
      self.tail = node.prev
    node.delete()
    current_head = self.head
    self.head = node
    self.head.next = current_head
    self.head.prev = None
    current_head.prev = self.head

  def move_to_end(self, node):
    head = False
    if (node.prev == None):
      head = True
    if head:
      self.head = node.next
    node.delete()
    current_tail = self.tail
    self.tail = node
    self.tail.prev = current_tail
    self.tail.next = None
    current_tail.next = self.tail

  def delete(self, node):
    if node.prev == None:
      self.head = node.next
    elif node.next == None:
      self.tail = node.prev
    node.delete()
    self.length -= 1
    if (self.length == 0):
      self.head = None
      self.tail = None
    
  def get_max(self):
    max_value = 0
    if self.length > 0:
      current_node = self.head
      while current_node:
        if current_node.value > max_value:
          max_value = current_node.value
        current_node = current_node.next
    return max_value
