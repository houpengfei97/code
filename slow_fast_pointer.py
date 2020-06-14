
####定义链表节点######
class LinkNode:
    def __init__(self,val):
        self.val = val
        self.next = None


####实现链表及操作#####
class MyLinkList(object):
    def __init__(self):
        self.head = None
        self.length = 0

    ####判断链表是否为空#######
    def is_empty(self):
        if self.head == None:
            return True

    #####获取链表长度########
    def length_get(self):
        cur = self.head
        count = 0
        while cur:
            cur = cur.next
            count+=1
        return count

    #####获取某个节点########
    def get_node(self,index):
        if (index < 0 || index >= self.length):
            return -1
        else:
            cur = self.head
            cnt = 0
            while cur:
                if index == cur:
                    return cur.val
                else:
                    cnt+=1
                    cur = cur.next

    ######创建链表#########
    def addAtHead(self,val):
        """头部添加节点"""
        #####先创建一个节点保存val的值######
        node = LinkNode(val)
        #####将新节点的next指向头结点
        node.next = self.head
        #####将头结点指向新节点，保证head的位置#######
        self.head = node
        self.length+=1

    def addAtTail(self,val):
        """尾部添加节点"""
        node = LinkNode(val)
        ######判断链表是否为空，为空则head直接指向新节点######
        if self.is_empty():
            self.head = node
        #######不为空，则将尾部节点指向新节点#######
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = node
        self.length +=1

    def addAtIndex(self,index,val):
        """指定位置添加节点"""
        #####若指定的位置为第一个节点之前，则执行头部插入#####
        if index <= 0:
            self.addAtHead(val)
        ######若指定位置超过链表尾部，则执行尾部插入######
        elif index > (self.length - 1):
            self.addAtTail(val)
        ######找到指定位置插入######
        else:
            node = LinkNode(val)
            count = 0
        ######将pre指向头结点，移动到指定位置的前一个位置
            pre = self.head
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
            cur = self.head
            pre = None
            cnt = 0
            while (cnt < index):
                pre = cur
                cnt += 1
                cur = cur.next
            pre.next = cur.next
            self.length -= 1

    def



#####回文链表实现########
# class solution:
#     ####Linklist reversed####
#     def reverselist(self,head):
#         new_head = None
#         while(head):
#             cur = head
#             head = head.next
#             cur.next = new_head
#             new_head = cur
#         return new_head


if __name__== '__main__':
    #head = LinkNode()
    obj = solution()
    for i in range(1,10):
        head = obj.linklist_creat(i)
        print (head)
    #def is_palindrome(self,head):








####回文字符串判断######



######查找倒数第K个数##########