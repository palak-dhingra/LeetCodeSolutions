# -*- coding: utf-8 -*-
"""
Spyder Editor
Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Your KthLargest class will have a constructor which accepts an integer k and an integer array nums, which contains initial elements from the stream. For each call to the method KthLargest.add, return the element representing the kth largest element in the stream.

Example:

int k = 3;
int[] arr = [4,5,8,2];
KthLargest kthLargest = new KthLargest(3, arr);
kthLargest.add(3);   // returns 4
kthLargest.add(5);   // returns 5
kthLargest.add(10);  // returns 5
kthLargest.add(9);   // returns 8
kthLargest.add(4);   // returns 8
Note:
You may assume that nums' length ≥ k-1 and k ≥ 1.
"""
import heapq
from typing import List

class KthLargest:
    """
    The idea is to ALWAYS maintain a MIN heap with only K elements
    - in this case, the K-the largest element (in the stream)
    - will always be at the root position
    """
    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k
        
        for num in nums:
            self.add(num) # add elements using the function below
        
    def add(self, val: int) -> int:
        
        heapq.heappush(self.heap, val)
        
        # if after adding the new item causes 
        # the heap size to increase beyond k, 
        # then pop out the smallest element 
        if len(self.heap) > self.k: 
            heapq.heappop(self.heap)
            
        return self.heap[0] # the root element


k = 3;
arr = [4,5,8,2];

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

obj = KthLargest(3, arr);
param_1 = obj.add(3);   # returns 4
print(param_1)
param_1 =obj.add(5);   # returns 5
print(param_1)
param_1 = obj.add(10);   # returns 5
print(param_1)
param_1 =obj.add(9);   # returns 8
print(param_1)
param_1 =obj.add(4);   # returns 8
print(param_1)
