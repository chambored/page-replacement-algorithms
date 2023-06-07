#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import unittest
from LRU import LRU
from FIFO import FIFO
from Optimal import Optimal

class TestAlgorithms(unittest.TestCase):
    def setUp(self):
        self.pages = [7,0,1,2,0,3,0,4,2,3,0,3,2,1,2,0,1,7,0,1]
        self.num_frames = 3

    def test_FIFO(self):
        fifo = FIFO()
        result = fifo.run(self.pages, self.num_frames)
        self.assertEqual(result, 15)

    def test_LRU(self):
        lru = LRU()
        result = lru.run(self.pages, self.num_frames)
        self.assertEqual(result, 12)

    def test_Optimal(self):
        opt = Optimal()
        result = opt.run(self.pages, self.num_frames)
        self.assertEqual(result, 9)

if __name__ == '__main__':
    pages = [
        [7,0,1,2,0,3,0,4,2,3,0,3,2,1,2,0,1,7,0,1],
        [8,1,0,7,3,0,3,4,5,3,5,2,0,6,8,4,8,1,5,3],
        [4,6,4,8,6,3,6,0,5,9,2,1,0,4,6,3,0,6,8,4]
    ]

    page_frame_numbers = [3, 5, 7]
    page_string_sizes = [10, 15, 20]

    for index, pageset in enumerate(pages):
        print(f"\nPage Set {index + 1}: Reference String: {pageset}")
        for num_frames in page_frame_numbers:
            print(f"\nPage Frames: {num_frames}")
            print(f"FIFO: {FIFO().run(pageset, num_frames)} page faults")
            print(f"LRU: {LRU().run(pageset, num_frames)} page faults")
            print(f"Optimal: {Optimal().run(pageset, num_frames)} page faults")

    print("\nRandom Page Sets:")
    for size in page_string_sizes:
        for num_frames in page_frame_numbers:
            for i in range(3):  # generating 3 random reference strings
                random_pages = [random.randint(0, 9) for _ in range(size)]
                print(f"\nReference String Size: {size}, Page Frames: {num_frames}")
                print(f"Random Reference String {i + 1}: {random_pages}")
                print(f"FIFO: {FIFO().run(random_pages, num_frames)} page faults")
                print(f"LRU: {LRU().run(random_pages, num_frames)} page faults")
                print(f"Optimal: {Optimal().run(random_pages, num_frames)} page faults") 

    unittest.main()
