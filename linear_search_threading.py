import threading
import numpy as np

def thread_search(arr, x, start, end, kill, results):
  for i in range(start, end):
    if kill: 
      return
    if arr[i] == x:
      kill = True
      results.append(i)
      return i
  
  results.append(-1)
  return -1

def linear_search_threading(arr, x, num_threads):
  kill = False
  results = []
  threads = []
  sections = np.array_split(arr, num_threads)

  start = 0
  end = 0
  for section in sections:
    length = len(section)
    end = start + length
    threads.append(threading.Thread(target=thread_search, args=(arr, x, start, end, kill, results), daemon=True))
    start = end

  for thread in threads:
    thread.start()

  for thread in threads:
    thread.join()
  
  return max(results)