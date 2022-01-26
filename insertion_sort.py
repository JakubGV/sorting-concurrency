# Sort arr in-place using the insertion sort algorithm from [start, end)
def insertion_sort(arr, start, end):
  for i in range(start+1, end):
    key = arr[i]
    j = i
    
    while arr[j-1] > key and j > 0:
      arr[j] = arr[j-1]
      j -= 1
    arr[j] = key

  return