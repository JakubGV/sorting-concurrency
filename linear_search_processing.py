from multiprocessing import Process, Queue, Event

def process_search(arr, x, start, end, kill, results):
  for i in range(start, end):
    if arr[i] == x:
      kill.set()
      results.put(i)
      return i
  
  results.put(-1)
  return -1

def linear_search_processing(arr, x, num_processes):
  size = len(arr)
  kill = Event()
  results = Queue()
  processes = []

  for i in range(0, num_processes):
    start = i * (size//num_processes)
    end = (i+1) * (size//num_processes)
    if i == num_processes - 1:
      end = size
    
    processes.append(Process(target=process_search, args=(arr, x, start, end, kill, results), daemon=True))

  for process in processes:
    process.start()

  for process in processes:
    process.join()
  
  while not results.empty():
    res = results.get()
    if res != -1:
      return res
  
  return -1