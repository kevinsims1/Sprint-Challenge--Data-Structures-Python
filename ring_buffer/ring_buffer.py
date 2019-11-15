class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    if self.storage[self.current] == None:
      self.storage[self.current] = item
      self.current += 1
    else:
      self.storage.append(item)

  def get(self):
    res = []
    for i in self.storage:
      if i != None:
        res.append(i)
    return res
    #list comprehension/same as above:
    #res = [i for i in self.storage if i]