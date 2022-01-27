# Sort arr in-place using the insertion sort algorithm
def insertion_sort(arr):
  for i in range(1, len(arr)):
    key = arr[i]
    j = i
    
    while arr[j-1] > key and j > 0:
      arr[j] = arr[j-1]
      j -= 1
    arr[j] = key

  return