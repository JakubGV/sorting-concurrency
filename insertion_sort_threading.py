from threading import Thread
from insertion_sort import insertion_sort

def insertion_sort_threading(arr, num_threads):
  size = len(arr)
  threads = []
  
  for i in range(0, num_threads):
    start = i * (size//num_threads)
    end = (i+1) * (size//num_threads)
    if i == num_threads - 1:
      end = size

    threads.append(Thread(target=insertion_sort, args=(arr, start, end), daemon=True))

  for thread in threads:
    thread.start()

  for thread in threads:
    thread.join()
  
  return