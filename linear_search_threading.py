from threading import Thread

def thread_search(arr, x, start, end, kill, results):
  for i in range(start, end):
    if kill: 
      return
    if arr[i] == x:
      kill.append(True)
      results.append(i)
      return i
  
  results.append(-1)
  return -1

def linear_search_threading(arr, x, num_threads):
  size = len(arr)
  kill = []
  results = []
  threads = []
  
  for i in range(0, num_threads):
    start = i * (size//num_threads)
    end = (i+1) * (size//num_threads)
    if i == num_threads - 1:
      end = size

    threads.append(Thread(target=thread_search, args=(arr, x, start, end, kill, results), daemon=True))

  for thread in threads:
    thread.start()

  for thread in threads:
    thread.join()
  
  return max(results)