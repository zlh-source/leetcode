class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def __init__(self):
        self.s=None
        self.l=None
        self.r=None

    def reverseTopK(self,head,K):
        '''
        反转前K个链表，不够K则不进行操作
        '''
        if head is None:
            return head,False

        if K==1:
            self.s=head
            return head,True

        new_head,state=self.reverseTopK(head.next,K-1)

        if not state:
            return head,state

        head.next=self.s.next
        self.s.next=head
        self.s=head
        return new_head,state

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        '''
        以k为单位反转链表
        '''
        if head is None:
            return head
        head,state=self.reverseTopK(head,k)
        if not state:
            return head
        t=self.s
        head2=self.reverseKGroup(self.s.next,k)
        t.next=head2
        return head

    def list2link(self,s):
        '''
        list转化为链表
        '''
        head=ListNode()
        tail=head
        for i in range(len(s)):
            if i==0:
                head.val=s[i]
            else:
                tail.next=ListNode(s[i])
                tail=tail.next
        return head

    def link2list(self,s):
        '''
        链表转化为列表
        '''
        res=[]
        while s:
            res.append(s.val)
            s=s.next
        return res

    def rev_print(self,head):
        '''
        递归倒序输出链表
        '''
        if head is None:
            return
        self.rev_print(head.next)
        print(head.val)

    def isPalindrome(self, head: ListNode) -> bool:
        '''
        判断回文链表
        '''
        self.l=head

        def isOK(r):
            if r is None:
                return True
            res=isOK(r.next)
            res = ( res and r.val==self.l.val)
            self.l=self.l.next
            return res

        return isOK(head.next)
