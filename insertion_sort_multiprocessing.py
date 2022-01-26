from multiprocessing import Process
from insertion_sort import insertion_sort

def insertion_sort_multiprocessing(arr, num_processes):
  size = len(arr)
  processes = []

  for i in range(0, num_processes):
    start = i * (size//num_processes)
    end = (i+1) * (size//num_processes)
    if i == num_processes - 1:
      end = size
    
    processes.append(Process(target=insertion_sort, args=(arr, start, end), daemon=True))

  for process in processes:
    process.start()

  for process in processes:
    process.join()
  
  return