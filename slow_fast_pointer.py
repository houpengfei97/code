
####定义链表节点######
class LinkNode:
    def __init__(self,val):
        self.val = val
        self.next = None


####实现链表及操作#####
class MyLinkList(object):
    def __init__(self):
        self._head = None
        self.length = 0

    ####判断链表是否为空#######
    def is_empty(self):
        if self._head == None:
            return True

    #####获取链表长度########
    def length_get(self):
        cur = self._head
        count = 0
        while cur:
            cur = cur.next
            count+=1
        return count

    #####获取某个节点########
    def get_node(self,index):
        if (index < 0 or index >= self.length):
            return -1
        else:
            cur = self._head
            cnt = 0
            while cur:
                if index == cnt:
                    return cur.val
                else:
                    cnt+=1
                    cur = cur.next

    ######创建链表#########
    def addAthead(self,val):
        """头部添加节点"""
        #####先创建一个节点保存val的值######
        node = LinkNode(val)
        #####将新节点的next指向头结点
        node.next = self._head
        #####将头结点指向新节点，保证_head的位置#######
        self._head = node
        self.length+=1

    def addAtTail(self,val):
        """尾部添加节点"""
        node = LinkNode(val)
        ######判断链表是否为空，为空则_head直接指向新节点######
        if self.is_empty():
            self._head = node
        #######不为空，则将尾部节点指向新节点#######
        else:
            cur = self._head
            while cur.next:
                cur = cur.next
            cur.next = node
        self.length +=1

    def addAtIndex(self,index,val):
        """指定位置添加节点"""
        #####若指定的位置为第一个节点之前，则执行头部插入#####
        if index <= 0:
            self.addAt_head(val)
        ######若指定位置超过链表尾部，则执行尾部插入######
        elif index > (self.length - 1):
            self.addAtTail(val)
        ######找到指定位置插入######
        else:
            node = LinkNode(val)
            count = 0
        ######将pre指向头结点，移动到指定位置的前一个位置
            pre = self._head
            while count < (index - 1):
                count+=1
                pre = pre.next
        ######将新插入节点的next指向插入位置的节点
            node.next = pre.next
            pre.next = node
            self.length +=1
        ########删除链表节点########
    def deleteAtIndex(self,index):
        node = LinkNode(0)
        if index < 0 or index >=self.length:
            return -1
        else:
            cur = self._head
            pre = None
            cnt = 0
            while (cnt < index):
                pre = cur
                cnt += 1
                cur = cur.next
            pre.next = cur.next
            self.length -= 1

    def searchItem(self,item):
        cur = self._head
        while cur:
            if cur.val == item:
                return True
            cur = cur.next
        return False

    def travel(self):
        cur = self._head
        while cur:
            print(cur.val)
            cur = cur.next
        print("")

#####回文链表实现########
        ####Linklist reversed####
    def reverselist(self,head):
        new_head = None
        while head:
            cur = head
            head = head.next
            cur.next = new_head
            new_head = cur
        return new_head

    #####isPalindrome########
    def isPalindrome(self):
        if self._head == None:
            return -1
        slow = fast = self._head
        if fast == None:
            return True
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        if fast:
            slow = slow.next
        new_head = self.reverselist(slow)
        while new_head:
            if self._head.val != new_head.val:
                print('The linklist is not palindrome')
                return False
            self._head = self._head.next
            new_head = new_head.next
        print('The linklist is a palindrome')
        return True



#
#
# #####回文链表实现########
#     ####Linklist reversed####
#     def reverselist(self,head):
#         new_head = None
#         while head:
#             cur = head
#             head = head.next
#             cur.next = new_head
#             new_head = cur
#         return new_head
#
#     #####isPalindrome########
#     def isPalindrome(self,head):
#         if head == None:
#             return -1
#         slow = fast =head
#         if fast == None:
#             return True
#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next
#         if fast:
#             slow = slow.next
#         new_head = self.reverselist(slow)
#         while new_head:
#             if head.val != new_head.val:
#                 return False
#             head = head.next
#             new_head = new_head.next
#         return True


if __name__== '__main__':
    Mylinkedlist = LinkNode
    obj = MyLinkList()
    obj.addAthead(1)
    obj.addAthead(2)
    obj.addAthead(4)
    obj.addAthead(2)
    obj.addAthead(1)

    #obj.addAthead(1)

    #obj.addAtTail(2)
    #obj.addAtIndex(1,3)
    #obj.is_empty()
    #print('The linkedlist have {} items!'.format(obj.length_get()))
    #print(obj.get_node(1))
    #print(obj.get_node(0))
    #for i in range(1,10):
        #obj.addAthead(i)
    obj.travel()
    obj.isPalindrome()








####回文字符串判断######



######查找倒数第K个数##########
