class Solution(object):
    def reverseList(self, head):
        pre, cur = None, head
        while cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        return pre
    
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        
        # 思路：
        # 看公式可以发现，其实就是将后半部分的链表，依次插入前半部分。
        # 1. 快慢指针，走到中间和最后 2. 旋转后半部分链表 3. 将后半部分依次插入前半部分
            
        slow, fast = head, head
        
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        tail = self.reverseList(slow)
        
        # head, tail
        cur = head
        while cur:
            cur_next = cur.next
            tail_next = tail.next
            
            cur.next = tail
            tail.next = cur_next
            
            cur = cur_next
            tail = tail_next
        
        return head


        def reorderListStack(self, head):
            stack = []
            cur = head
            count = 0

            while cur:
                stack.append(cur)
                cur = cur.next
                count += 1

            dummy = ListNode()
            cur = dummy
            cur.next = head()

            cnt = 0
            while True:
                cnt += 1
                top = stack.pop()
                stack.pop()??
                tmp = cur.next
                cur.next = top

                if (cnt == count / 2 && count % 2 == 0): 
                    break
                elif (count == count / 2 && count % 2 == 1):
                    top.next = tmp
                    cur = tmp
                    break
                top.next = tmp
                cur = tmp
