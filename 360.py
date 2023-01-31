# -*- coding: utf-8 -*-
"""360.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1W1FrQk934NejrtfVd81vFHlWKKhIubDK
"""

import random

# Generate 1000 random values between 0 and 999
values = [str(random.randint(0, 999)) for _ in range(1000)]

# Write the values to a file
with open("random_values.txt", "w") as f:
    f.writelines("\n".join(values))

# Step 2 of 3
# To implement the LRU and FIFO algorithms, you can create a class for each algorithm that stores the blocks in a list or deque and maintains a dictionary to keep track of which blocks are in the list or deque. The get_block method of the class should take a block number as input and return the block if it is in the list or deque, or None if it is not. If the block is not in the list or deque, you can add it to the list or deque and update the dictionary accordingly. If the list or deque is full, you can remove the least recently used or first-in block and add the new block.
# Here is an example of how you can implement the LRU class:


class LRU:
    def _init_(self, block_size):
        self.block_size = block_size
        self.blocks = []
        self.block_map = {}

    def get_block(self, block_num):
        if block_num in self.block_map:
            # Move the block to the front of the list
            self.blocks.remove(block_num)
            self.blocks.insert(0, block_num)
            return self.block_map[block_num]
        return None

    def add_block(self, block_num, block):
        if len(self.blocks) == self.block_size:
            # Remove the least recently used block
            lru_block_num = self.blocks.pop()
            del self.block_map[lru_block_num]
        # Add the new block to the front of the list
        self.blocks.insert(0, block_num)
        self.block_map[block_num] = block



# Explanation | Hint for next step
# Please refer to solution in this step.
# Step 3 of 3
# Here is an example of how you can implement the FIFO class:


from collections import deque

class FIFO:
    def _init_(self, block_size):
        self.block_size = block_size
        self.blocks = deque()
        self.block_map = {}

    def get_block(self, block_num):
        if block_num in self.block_map:
            return self.block_map[block_num]
        return None

    def add_block(self, block_num, block):
        if len(self.blocks) == self.block_size:
            # Remove the first-in block
            fifo_block_num = self.blocks.popleft()
            del self.block_map[fifo_block_num]
        # Add the new block to the end of the deque
        self.blocks.append(block_num)
        self.block_map[block_num] = block

F = FIFO()
print(F)

