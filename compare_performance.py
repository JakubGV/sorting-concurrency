import time
import argparse

from insertion_sort import insertion_sort
from insertion_sort_threading import insertion_sort_threading
from insertion_sort_multiprocessing import insertion_sort_multiprocessing

def parse_args():
  parser = argparse.ArgumentParser(description='Compare searching time without threads, with multithreading, and with multiprocessing')
  parser.add_argument('n', type=int, help='Size of array to search')
  parser.add_argument('num_threads', type=int, help='Number of threads to search with')
  parser.add_argument('num_processes', type=int, help='Number of processes to search with')

  args = parser.parse_args()

  return {
    'n': args.n,
    'num_threads': args.num_threads,
    'num_processes': args.num_processes
  }

def generate_array(n):
  return [i for i in range(n)]

def time_sort(arr, **kwargs):
  num_threads = kwargs.get('num_threads', None)
  num_processes = kwargs.get('num_processes', None)

  res = None
  start = time.time()
  if num_threads:
    res = insertion_sort_threading(arr, num_threads)
  elif num_processes:
    res = insertion_sort_multiprocessing(arr, num_processes)
  else:
    res = insertion_sort(arr, 0, len(arr))
  end = time.time()
  
  return {'result': res, 'time': round(end-start, 3)}

if __name__ == "__main__":
  start = time.time()
  argsDict = parse_args()
  
  to_sort_1 = generate_array(argsDict['n'])
  to_sort_2 = to_sort_1.copy()
  to_sort_3 = to_sort_1.copy()

  no_threads = time_sort(to_sort_1)
  print('{:<15}'.format('No threads'), no_threads)
  
  with_threads = time_sort(to_sort_2, num_threads=argsDict['num_threads'])
  print('{:<15}'.format(f'{argsDict["num_threads"]} threads'), with_threads)
  
  with_processes = time_sort(to_sort_3, num_processes=argsDict['num_processes'])
  print('{:<15}'.format(f'{argsDict["num_processes"]} processes'), with_processes)

  end = time.time()
  print(f'Execution took: {end-start:.3f}s')