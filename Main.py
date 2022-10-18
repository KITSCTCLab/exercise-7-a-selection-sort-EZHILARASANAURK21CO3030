from typing import List

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
