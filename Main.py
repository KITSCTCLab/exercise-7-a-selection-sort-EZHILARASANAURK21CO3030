class Node:
  def _from typing import List

def selectionSort(array, size) -> List[int]:
    for y in range(len(array)):
        mid = y
        for j in range(y+1,len(array)):
            if array[mid] > array[j]:
                mid = j
        array[y], array[mid] = array[mid] , array[y]
    return array

input_data = input()
data = []
for item in input_data.split(', '):
  if item.isnumeric():
    data.append(int(item))
  elif item.lstrip("-").isnumeric():
    data.append(int(item))
print(selectionSort(data, len(data)))
_init__(self, data):
    self.data = data
    self.next = None


class Queue:
  def __init__(self):
    self.head = None
    self.last = None

  def enqueue(self, data) -> None:
    # Write your code here
    if self.last is None:
      self.head = Node(data)
      self.last = self.head
    else:
      self.last.next = Node(data)
      self.last = self.last.next

  def dequeue(self) -> None:
    # Write your code here
    if self.head is None:
      return None
    else:
      val_returned = self.head.data
      self.head = self.head.next

  def status(self) -> None:
    # Write your code here
    current = self.head
    status_of_queue = []
    while (current):
      status_of_queue.append(current.data)
      current = current.next
    for element in status_of_queue:
      print(element, end="=>")
    print(None)


# Do not change the following code
queue = Queue()
operations = []
for specific_operation in input().split(','):
    operations.append(specific_operation.strip())
input_data = input()
data = input_data.split(',')
for i in range(len(operations)):
  if operations[i] == "enqueue":
    queue.enqueue(int(data[i]))
  elif operations[i] == "dequeue":
    queue.dequeue()
queue.status()

