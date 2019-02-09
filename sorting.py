import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import numpy as np
import asyncio

class BubbleSort:
    """Bubble sort algorithm implementation."""

    def sort(self, arr, live=False):
        """Sorts given 1d sequence array."""

        if live:
            return self.sort_live_graph(arr)

        for i, _ in enumerate(arr):
            for j,_ in enumerate(arr):
                if j >= len(arr) - 1:
                    break
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr

    def sort_live_graph(self, arr):
        """Same as sort method but this will visualize data while sorting."""

        x = np.arange(len(arr))
        for i, _ in enumerate(arr):
            for j,_ in enumerate(arr):
                if j >= len(arr) - 1:
                    break
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
            plt.cla()
            plt.plot(x, arr)
            plt.pause(0.000001)
        return arr

class MergeSort:
    def __init__(self):
        self.x = None
        self.y = None

    def _merge(self, arr, left, middle, right):

        # visualize

        return arr

    def sort_core(self, arr, left, right):
        """Merge sort recursion."""

        if left < right:
            # pick middle index
            middle = (left + right) // 2
            # get partitions
            left_arr = self.sort_core(arr, left, middle)
            right_arr = self.sort_core(arr, middle + 1, right)

            len_left = len(left_arr)
            len_right = len(right_arr)

            # merge part
            left_pointer = right_pointer = 0
            for k in range(left, right + 1):
                if left_pointer >= len_left:
                    arr[k] = right_arr[right_pointer]
                    right_pointer += 1
                    plt.cla()
                    plt.plot(self.x, arr)
                    plt.pause(0.000001)
                    continue
                if right_pointer >= len_right:
                    arr[k] = left_arr[left_pointer]
                    left_pointer += 1
                    plt.cla()
                    plt.plot(self.x, arr)
                    plt.pause(0.000001)
                    continue
                if left_arr[left_pointer] < right_arr[right_pointer]:
                    arr[k] = left_arr[left_pointer]
                    left_pointer += 1
                else:
                    arr[k] = right_arr[right_pointer]
                    right_pointer += 1
                plt.cla()
                plt.plot(self.x, arr)
                plt.pause(0.000001)

        array = list(arr[left:right + 1])
        return array

    def sort(self, arr, live=True):
        self.x = np.arange(len(arr))
        self.y = arr
        if live:
            return self.sort_core(arr, 0, len(arr) - 1)


class QuickSort:
    """Quick sort algorithm implementation."""

    def __init__(self):
        self.x = None
        self.y = None
        self.fig, self.ax = plt.subplots(1, 1)
        self.points = None

    @staticmethod
    def partition(arr, pivot, r):
        """Partition.
        Picks a target number, split array into 2 parts,
        array with 'less equals than target number' values and array with 'greater than
        target number'.
        """

        target = arr[r]
        index = pivot - 1
        for j in range(pivot, r):
            if arr[j] < target:
                index += 1
                arr[index], arr[j] = arr[j], arr[index]
        arr[index + 1], arr[r] = arr[r], arr[index + 1]
        return index + 1, arr

    def sort_core(self, arr, pivot, r):
        """Sorts given 1d sequence array."""

        if pivot < r:
            q, arr = self.partition(arr, pivot, r)
            arr = self.sort_core(arr, pivot, q - 1)
            arr = self.sort_core(arr, q + 1, r)
        # self.array = arr
        return arr

    def blit(self):
        background = self.fig.canvas.copy_from_bbox(self.ax.bbox)
        self.fig.canvas.restore_region(background)
        self.points.set_ydata(self.y)
        self.ax.draw_artist(self.points)
        self.fig.canvas.blit(self.ax.bbox)

    def animate(self, i):
        self.points.set_ydata(self.y)

    def live_partition(self, arr, pivot, r):
        """Same as partition method, but this will visualize data while sorting."""

        target = arr[r]
        index = pivot - 1
        for j in range(pivot, r):
            if arr[j] < target:
                index += 1
                arr[index], arr[j] = arr[j], arr[index]
                plt.cla()
                plt.plot(self.x, arr)
                plt.pause(0.000001)
        arr[index + 1], arr[r] = arr[r], arr[index + 1]
        plt.cla()
        plt.plot(self.x, arr)
        plt.pause(0.000001)
        return index + 1

    def sort_core_live(self, arr, pivot, r):
        """Same as sort_core method, but this is using live graph partition."""

        if pivot < r:
            q = self.live_partition(arr, pivot, r)
            self.sort_core_live(arr, pivot, q - 1)
            self.sort_core_live(arr, q + 1, r)
        return arr

    def sort(self, arr, pivot, r, live=False):
        """Main method."""

        self.x = np.arange(len(arr))
        self.y = arr
        if live:
            return self.sort_core_live(arr, pivot, r)
        return self.sort_core(arr, pivot, r)
