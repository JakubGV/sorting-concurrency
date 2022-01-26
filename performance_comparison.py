import numpy as np
import random
import time
import pprint

from linear_search import linear_search
from linear_search_threading import linear_search_threading

test = []
random.seed(16)

N = int(input("How large should the array be? "))
num_threads = int(input("How many threads? "))
for i in range(N):
  test.append(i)
search_for = random.randint(0, N-1)

def time_search(arr, search_for, **kwargs):
  num_threads = kwargs.get('num_threads', None)
  
  start = time.process_time()
  res = linear_search(arr, search_for) if num_threads is None else linear_search_threading(arr, search_for, num_threads)
  end = time.process_time()
  
  return {'result': res, 'time': end-start}

no_thread = time_search(test, search_for)
with_thread = time_search(test, search_for, num_threads=num_threads)

print('No thread:')
pprint.pprint(no_thread)
print()

print('2 threads:')
pprint.pprint(with_thread)