import time
import argparse

from insertion_sort import insertion_sort
from insertion_sort_threading import insertion_sort_threading
from insertion_sort_multiprocessing import insertion_sort_multiprocessing

def parse_args():
  parser = argparse.ArgumentParser(description='Compare searching time without threads, with multithreading, and with multiprocessing')
  parser.add_argument('n', type=int, help='Size of array to search (n >= 1)')
  parser.add_argument('num_threads', type=int, help='Number of threads to search with (1 <= num_threads <= 64)')
  parser.add_argument('num_processes', type=int, help='Number of processes to search with (1 <= num_processes <= 64)')

  args = parser.parse_args()

  if not (args.n >= 1):
    raise ValueError(f'Value of argument n must be >= 1, you put "{args.n}"')
  if not (1 <= args.num_threads <= 64):
    raise ValueError(f'Value of argument num_threads must be between 1 and 64, you put "{args.num_threads}"')
  if not (1 <= args.num_processes <= 64):
    raise ValueError(f'Value of argument num_processes must be between 1 and 64, you put "{args.num_processes}"')

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

  start = time.time()
  if num_threads:
    insertion_sort_threading(arr, num_threads)
  elif num_processes:
    insertion_sort_multiprocessing(arr, num_processes)
  else:
    insertion_sort(arr)
  end = time.time()
  
  return round(end-start, 3)

if __name__ == "__main__":
  start = time.time()
  argsDict = parse_args()
  
  to_sort_1 = generate_array(argsDict['n'])
  to_sort_2 = to_sort_1.copy()
  to_sort_3 = to_sort_1.copy()

  normal_execution = time_sort(to_sort_1)
  print('Normal execution:'.ljust(20), f'{normal_execution:.4f}s')
  
  with_threads = time_sort(to_sort_2, num_threads=argsDict['num_threads'])
  print(f'{argsDict["num_threads"]} thread(s):'.ljust(20), f'{with_threads:.4f}s')
  
  with_processes = time_sort(to_sort_3, num_processes=argsDict['num_processes'])
  print(f'{argsDict["num_processes"]} process(es):'.ljust(20), f'{with_processes:.4f}s')

  end = time.time()
  print('Execution took:'.ljust(20), f'{end-start:.4f}s')