class Node:
    def __init__(self,k,v,last=None,next=None):
        self.k,self.v,self.last,self.next=k,v,last,next

class BiLink:
    def __init__(self):
        #虚拟头尾
        self.head=Node("head","head")
        self.tail=Node("tail","tail")
        self.head.next=self.tail
        self.tail.last=self.head

    def add_head(self,node:Node):
        node.next=self.head.next
        node.last=self.head
        self.head.next=node
        node.next.last=node

    def add_tail(self,node:Node):
        node.next=self.tail
        node.last=self.tail.last
        self.tail.last=node
        node.last.next=node

    def del_x(self,node:Node):
        node.last.next=node.next
        node.next.last=node.last
        node.last=None
        node.next=None
        return node

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.map={}
        self.biLink=BiLink()

    def get(self, key: int) -> int:
        '''访问节点时，没有，则返回-1，
        有，则返回该v值，并将该节点移到链表尾部(添加最近使用)'''
        if not str(key) in self.map:
           return -1

        node=self.map[str(key)]
        node=self.biLink.del_x(node)
        self.addRecently(node)
        return node.v


    def put(self, key: int, value: int) -> None:
        '''如果没有该key,则创建该节点，添加至链表尾部，并加入map
        有，则更新map与node中的v值，添加至链表尾部（添加最近使用）
        如果内存超过capacity，则删除队头元素，并删除map中的信息'''
        if not str(key) in self.map:
            #创建新节点
            node=Node(key,value)
            self.addRecently(node)
            self.addMap(node)
        else:
            #获取旧节点，并更新
            node=self.map[str(key)]
            #将node移到tail
            node=self.biLink.del_x(node)
            node.v=value
            self.biLink.add_tail(node)
            self.updateMap(node)
        if self.capacity<len(self.map):
            self.removeLeastRecently()

    def addRecently(self,node:Node):
        self.biLink.add_tail(node)

    def removeLeastRecently(self):
        node=self.biLink.head.next
        self.removeMap(node.k)
        self.biLink.del_x(node)

    def removeMap(self,key):
        self.map.pop(str(key))

    def addMap(self,node:Node):
        self.map[str(node.k)]=node

    def updateMap(self,node:Node):
        self.map[str(node.k)]=node

    def out(self):
        a=self.biLink.head
        while a:
            print(a.v)
            a=a.next
        a=self.biLink.tail
        while a:
            print(a.v)
            a=a.last

#146 LRUCache
lru=LRUCache(2)
lru.put(1,1)
lru.put(2,2)
print(lru.get(1))

