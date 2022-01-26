import random
import time
import argparse

from linear_search import linear_search
from linear_search_threading import linear_search_threading
from linear_search_processing import linear_search_processing

def time_search(arr, search_for, **kwargs):
  num_threads = kwargs.get('num_threads', None)
  num_processes = kwargs.get('num_processes', None)

  res = None
  start = time.time()
  if num_threads:
    res = linear_search_threading(arr, search_for, num_threads)
  elif num_processes:
    res = linear_search_processing(arr, search_for, num_processes)
  else:
    res = linear_search(arr, search_for)
  end = time.time()
  
  return {'result': res, 'time': round(end-start, 3)}

if __name__ == "__main__":
  start = time.time()
  
  parser = argparse.ArgumentParser(description='Compare searching time without threads, with multithreading, and with multiprocessing')
  parser.add_argument('n', type=int, help='Size of array to search')
  parser.add_argument('num_threads', type=int, help='Number of threads to search with')
  parser.add_argument('num_processes', type=int, help='Number of processes to search with')

  args = parser.parse_args()
  n = args.n
  num_threads = args.num_threads
  num_processes = args.num_processes

  test = []
  random.seed(16)

  
  for i in range(n):
    test.append(i)
  search_for = random.randint(0, n-1)

  no_thread = time_search(test, search_for)
  print('{:<15}'.format('No threads'), no_thread)
  
  with_threads = time_search(test, search_for, num_threads=num_threads)
  print('{:<15}'.format(f'{num_threads} threads'), with_threads)
  
  with_processes = time_search(test, search_for, num_processes=num_processes)
  print('{:<15}'.format(f'{num_processes} processes'), with_processes)

  end = time.time()
  print(f'Execution took: {end-start:.3f}s')