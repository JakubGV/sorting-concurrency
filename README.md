# threading-searching-performance
 
## Linear Search Concurrency
This self-directed project was inspired by trying to perform a faster linear search on an array of numbers.
However, this implementation did not give me the performance gains I expected to see.
The communication of the processes seemed to be a big slowdown and there weren't many elegant ways to terminate other processes early if a process found the right key.
Due to this, I transitioned into emulating a large array being sorted in chunks.

## Sorting Concurrency
With sorting implemented, the performance matched closer to what I expected but I still did not see the gains of using multiprocessing as I expected. Because of the Python GIL, I didn't expect threads to yield much of a performance gain on a CPU-bound task.
Upon researching why my performance gains don't match what I expect, I found that copying large arrays into the memory of the different processes can add a lot of extra time that the normal execution path didn't need to do.
To minimize the effect of copying the entire large array, I instead broke the array into chunks and sent that to the threads/processes to process.

## Results and Analysis

### Results
n | num_threads | num_processes | normal_time (s) | thread_time (s) | process_time (s)
--- | --- | --- | --- | --- | ---
30000000 | 2 | 2 | 3.5420 | 3.7240 | 4.2280
30000000 | 2 | 8 | 3.5820 | 3.6500 | 3.4060
40000000 | 2 | 2 | 4.7320 | 5.0700 | 5.7210
40000000 | 2 | 8 | 4.7540 | 4.8950 | 4.5300
50000000 | 2 | 2 | 5.8550 | 6.2310 | 7.2430
50000000 | 2 | 8 | 5.9660 | 6.0740 | 5.7810
100000000 | 2 | 2 | 12.0030 | 12.2480 | 15.1400
100000000 | 2 | 8 | 11.9520 | 12.0880 | 10.8010
100000000 | 8 | 12 | 12.6560 | 12.2860 | 10.4480

### Analysis
Key things to notice here are that as the input size increases, the more the concurrent implementations get an advantage. This intuitively makes sense as the 'fixed' cost of making extra threads/processes is dominated by the performance gains from parallelism. Another thing, the more threads and processes we created, the better it performed at the task. The system this was run on has 8 logical processors. When we ran the performance comparison with 8 processes, we were able to outperform normal, single-process execution.

## What I learned
* Knowledge of the Python GIL
* Using `argparse` for command line arguments
* Using the `threading` library
* Using the `multiprocessing` library
* More comfortable with string formatting and setting precision