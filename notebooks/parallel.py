import numpy as np
import sys
import time
from concurrent.futures import ProcessPoolExecutor, as_completed

## Use sys.argv to pass in an integer value for the number
## of consecutive integers to operate on
length = int(sys.argv[1])

def task(n):
    time.sleep(1)
    return n * n

if __name__ == '__main__':

    numbers = range(0, length)
    ## create a pool of workers
    ## max_workers determines the number of parallel process to run
    with ProcessPoolExecutor(max_workers=4) as executor:
        ## Submit all the jobs to the executor
        results = [executor.submit(task, num) for num in numbers]

        ## As jobs finish, pull the results and print them
        for future in as_completed(results):
                print(f"Result: {future.result()}")