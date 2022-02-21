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

# Sort in chunks to mimic the same behavior the thread and process functions go through
def insertion_sort_single(arr, num_workers):
  size = len(arr)
  
  for i in range(0, num_workers):
    start = i * (size//num_workers)
    end = (i+1) * (size//num_workers)
    if i == num_workers - 1:
      end = size

    chunk = arr[start:end]
    insertion_sort(chunk)

  return