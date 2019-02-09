import numpy as np
import pprint as pp
from random import shuffle
import asyncio

x = np.arange(1000)

random_data = np.arange(1000)
shuffle(random_data)

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

# style.use('fivethirtyeight')

async def bubble_sort():
    # ax1.clear()
    for i in range (len(random_data)):
        for j in range(len(random_data)):
            if j >= len(random_data) - 1:
                break
            if random_data[j] > random_data[j+1]:
                random_data[j], random_data[j+1] = random_data[j+1], random_data[j]
            plt.cla()
            plt.plot(x, random_data)
            plt.pause(0.000001)

async def partition(p, r):
    target = random_data[r]
    i = p - 1
    for j in range (p, r):
        if random_data[j] <= target:
            i += 1
            random_data[i], random_data[j] = random_data[j], random_data[i]
    random_data[i + 1], random_data[r] = random_data[r], random_data[i + 1]

    plt.cla()
    plt.plot(x, random_data)
    plt.pause(0.000001)

    return i + 1

async def quick_sort(p, r):
    if p < r:
        q = await partition(p, r)
        await quick_sort(p, q - 1)
        await quick_sort(q + 1, r)

async def merge_sort():
    return

async def draw():
    plt.show()

async def main():

    tasks = [
        asyncio.ensure_future(draw()),
        asyncio.ensure_future(quick_sort(0, len(random_data) - 1))
        # asyncio.ensure_future(bubble_sort())
    ]
    await asyncio.wait(tasks)
    print('done')


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
