#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Answer 1:

import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists):
    # Create a min-heap
    heap = []
    
    # Push the head nodes of all linked lists into the min-heap
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst.val, i))
            lists[i] = lst.next
    
    # Create a dummy node
    dummy = ListNode(0)
    current = dummy
    
    # Merge the linked lists
    while heap:
        val, index = heapq.heappop(heap)
        
        # Create a new node with the popped value
        new_node = ListNode(val)
        
        # Append the new node to the result linked list
        current.next = new_node
        current = current.next
        
        # If the linked list from which the node was popped has a next node, push it into the min-heap
        if lists[index]:
            heapq.heappush(heap, (lists[index].val, index))
            lists[index] = lists[index].next
    
    # Set the next pointer of the last node to None
    current.next = None
    
    # Return the merged sorted linked list
    return dummy.next


# In[3]:


lists = [[1,4,5],[1,3,4],[2,6]]
linked_lists = []
for lst in lists:
    head = ListNode(lst[0])
    node = head
    for val in lst[1:]:
        node.next = ListNode(val)
        node = node.next
    linked_lists.append(head)

result = mergeKLists(linked_lists)

# Convert the result linked list to a list for easier visualization
output = []
node = result
while node:
    output.append(node.val)
    node = node.next

print(output)  


# In[4]:


lists = []
linked_lists = []
for lst in lists:
    head = ListNode(lst[0])
    node = head
    for val in lst[1:]:
        node.next = ListNode(val)
        node = node.next
    linked_lists.append(head)

result = mergeKLists(linked_lists)

# Convert the result linked list to a list for easier visualization
output = []
node = result
while node:
    output.append(node.val)
    node = node.next

print(output) 


# In[1]:


#Answer 2:

import bisect

def countSmaller(nums):
    counts = [0] * len(nums)
    sorted_nums = []

    for i in range(len(nums) - 1, -1, -1):
        # Find the position where nums[i] should be inserted in the sorted list
        # This gives the count of smaller elements to the right of nums[i]
        count = bisect.bisect_left(sorted_nums, nums[i])
        counts[i] = count

        # Insert nums[i] at the correct position in the sorted list
        sorted_nums.insert(count, nums[i])

    return counts


# In[2]:


nums = [5, 2, 6, 1]
result = countSmaller(nums)
print(result)


# In[3]:


nums = [-1]
result = countSmaller(nums)
print(result) 


# In[4]:


nums = [-1, -1]
result = countSmaller(nums)
print(result)


# In[5]:


#Answer 3:

def merge_sort(nums):
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])

    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged


# In[6]:


nums = [5, 2, 3, 1]
result = merge_sort(nums)
print(result)


# In[7]:


nums = [5,1,1,2,0,0]
result = merge_sort(nums)
print(result)


# In[8]:


#Answer 4:

def pushZeroesToEnd(nums):
    count = 0  # Count of non-zero elements

    # Traverse the array and move non-zero elements to the front
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[count] = nums[i]
            count += 1

    # Fill the remaining elements with zeroes
    while count < len(nums):
        nums[count] = 0
        count += 1

    return nums


# In[11]:


arr1 = [1, 2, 0, 4, 3, 0, 5, 0]
result1 = pushZeroesToEnd(arr1)
print(result1)  

arr2 = [1, 2, 0, 0, 0, 3, 6]
result2 = pushZeroesToEnd(arr2)
print(result2) 


# In[12]:


#Answer 5:

def rearrangeAlternate(nums):
    i = 0
    j = len(nums) - 1

    while i < j:
        if nums[i] >= 0 and nums[j] < 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        elif nums[i] < 0:
            i += 1
        else:
            j -= 1

    return nums


# In[13]:


arr1 = [1, 2, 3, -4, -1, 4]
result1 = rearrangeAlternate(arr1)
print(result1)  

arr2 = [-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]
result2 = rearrangeAlternate(arr2)
print(result2)  


# In[14]:


#Answer 6:

def mergeArrays(arr1, arr2):
    n1 = len(arr1)
    n2 = len(arr2)
    merged = []
    i = j = 0

    while i < n1 and j < n2:
        if arr1[i] <= arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1

    while i < n1:
        merged.append(arr1[i])
        i += 1

    while j < n2:
        merged.append(arr2[j])
        j += 1

    return merged


# In[15]:


arr1 = [1, 3, 4, 5]
arr2 = [2, 4, 6, 8]
result = mergeArrays(arr1, arr2)
print(result)


# In[16]:


arr1 = [5, 8, 9]
arr2 = [4, 7, 8]
result = mergeArrays(arr1, arr2)
print(result)


# In[17]:


#Answer 7:

def intersection(nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)
    return list(set1.intersection(set2))


# In[18]:


nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
result = intersection(nums1, nums2)
print(result) 


# In[19]:


nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
result = intersection(nums1, nums2)
print(result)


# In[20]:


#Answer8:

from collections import Counter

def intersect(nums1, nums2):
    counter1 = Counter(nums1)
    result = []
    
    for num in nums2:
        if counter1.get(num, 0) > 0:
            result.append(num)
            counter1[num] -= 1
    
    return result


# In[21]:


nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
result = intersect(nums1, nums2)
print(result)


# In[23]:


nums1 = [4, 9, 5]
nums2 = [9,4,9,8,4]
result = intersect(nums1, nums2)
print(result)


# In[ ]:




