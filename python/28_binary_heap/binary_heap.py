#!/usr/bin/python
# -*- coding: UTF-8 -*-

import math
import random


class BinaryHeap:
    """
    大顶堆
    """
    def __init__(self, data=None):
        self._data = []
        if type(data) is list:
            map(self._type_assert, data)
            self._data = data
            # self.heapify()

        self._length = len(self._data)

    def heapify(self):
        """
        堆化
        :return:
        """
        self._heapify(self._data, self._length-1)

    def _heapify(self, data, tail_idx):
        """
        堆化内部实现
        :param data: 需要堆化的数据
        :param tail_idx: 尾元素的索引
        :return:
        """
        # heapify data[:tail_idx+1]
        if tail_idx <= 0:
            return

        # idx of the Last Parent node
        lp = (tail_idx - 1) // 2

        for i in range(lp, -1, -1):
            self._heap_down(data, i, tail_idx)

    @staticmethod
    def _heap_down(data, idx, tail_idx):
        """
        将指定的位置堆化
        :param data: 需要堆化的数据
        :param idx: data: 中需要堆化的位置
        :param tail_idx: 尾元素的索引
        :return:
        """
        assert type(data) is list

        lp = (tail_idx - 1) // 2
        # top-down
        while idx <= lp:
            # Left and Right Child index
            lc = 2 * idx + 1
            rc = lc + 1

            # right child exists
            if rc <= tail_idx:
                tmp = lc if data[lc] > data[rc] else rc
            else:
                tmp = lc

            if data[tmp] > data[idx]:
                data[tmp], data[idx] = data[idx], data[tmp]
                idx = tmp
            else:
                break

    def insert(self, num):
        """
        插入
        :param num:
        :return:
        """
        if self._insert(self._data, num):
            self._length += 1

    @staticmethod
    def _insert(data, num):
        """
        堆中插入元素的内部实现
        :param data:
        :param num:
        :return:
        """
        assert type(data) is list
        assert type(num) is int

        data.append(num)
        length = len(data)

        # idx of New Node
        nn = length - 1
        # bottom-up
        while nn > 0:
            p = (nn-1) // 2
            if data[nn] > data[p]:
                data[nn], data[p] = data[p], data[nn]
                nn = p
            else:
                break

        return True

    def delete_root(self):
        """
        删除根节点
        :return:
        """
        if self._delete_root(self._data):
            self._length -= 1

    @staticmethod
    def _delete_root(data):
        """
        删除根节点内部实现
        :param data:
        :return:
        """
        assert type(data) is list

        length = len(data)
        if length == 0:
            return False

        data[0], data[-1] = data[-1], data[0]
        data.pop()
        length -= 1

        # length == 0 or == 1, return
        if length > 1:
            BinaryHeap._heap_down(data, 0, length-1)

        return True

    @staticmethod
    def _type_assert(num):
        assert type(num) is int

    @staticmethod
    def _draw_heap(data):
        """
        格式化打印
        :param data:
        :return:
        """
        length = len(data)

        if length == 0:
            return 'empty heap'

        ret = ''
        for i, n in enumerate(data):
            ret += str(n)
            # 每行最后一个换行
            if i == 2**int(math.log(i+1, 2)+1) - 2 or i == len(data) - 1:
                ret += '\n'
            else:
                ret += ', '

        return ret

    def __repr__(self):
        return self._draw_heap(self._data)


if __name__ == '__main__':
    nums = list(range(10))
    random.shuffle(nums)

    bh = BinaryHeap(nums)
    print('--- before heapify ---')
    print(bh)

    # heapify
    bh.heapify()
    print('--- after heapify ---')
    print(bh)

    # insert
    bh.insert(8)
    print('--- insert ---')
    print(bh)

    # delete_root
    bh.delete_root()
    print('--- delete root ---')
    print(bh)