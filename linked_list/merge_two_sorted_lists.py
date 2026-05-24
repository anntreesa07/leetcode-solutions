# 21. Merge Two Sorted Lists

# We can do this by comparing the values of the nodes in both lists and adding the smaller value to the new list. We can use a dummy node to simplify the process of building the new list. 





# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        

        dummy = ListNode()
        current = dummy

        while list1 and list2:
            if list1.val<list2.val:
                current.next=list1   #take value

                list1=list1.next     #move list1
            else:
                current.next=list2
                list2=list2.next     #move list2

            current=current.next     #moves the merged-list pointer forward.

        if list1:                   #one list may still have nodes left, connect them
            current.next = list1
        else:
            current.next = list2        

        return dummy.next
        