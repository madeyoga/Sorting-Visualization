from sorting import QuickSort, BubbleSort, MergeSort
import numpy as np
from random import shuffle
import matplotlib.pyplot as plt
import time
import asyncio

async def main():
    arr = np.arange(100)
    shuffle(arr)
    start_time = time.time()
    QuickSort().sort(arr, 0, len(arr) - 1, live=True)
    elapsed_time = time.time() - start_time
    print('elapsed_time: ' + str(elapsed_time))

    arr = np.arange(100)
    shuffle(arr)
    start_time = time.time()
    BubbleSort().sort(arr, live=True)
    elapsed_time = time.time() - start_time
    print('elapsed_time: ' + str(elapsed_time))

    arr = np.arange(100)
    shuffle(arr)
    print(arr)
    start_time = time.time()
    MergeSort().sort(arr, live=True)
    elapsed_time = time.time() - start_time
    print('elapsed_time: ' + str(elapsed_time))
    print(arr)

    plt.show()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
