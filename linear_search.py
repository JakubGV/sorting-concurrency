def linear_search(arr, x):
  for i, num in enumerate(arr):
    if num == x:
      return i
  
  return -1