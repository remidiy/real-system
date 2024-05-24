class Node:
    def __init__(self, val: int, next = None, prev =None):
        self.val = val
        self.next = next
        self.prev = prev
class MyLinkedList:

    def __init__(self):
        self.head = None

    def find_by_index(self, index):
        curr = self.head
        while curr and index:
            curr = curr.next
            index -= 1
        return curr

        
    def get(self, index: int) -> int:
        curr = self.find_by_index(index)
        return curr.val if curr else -1
    
    def addAtHead(self, val: int) -> None:
        curr = self.head
        node = Node(val)
        if curr is None:
            self.head = node
        else:
            curr.prev = node
            node.next = curr
            self.head = node
        

    def addAtTail(self, val: int) -> None:
        curr = self.head
        if curr is None:
            self.head = Node(val)
        while curr.next:
            curr = curr.next

        curr.next = Node(val)
        curr.next.prev = curr

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0: self.addAtHead(val)
        curr = self.find_by_index(index)
        if curr is None: 
            self.addAtTail(val)
            return
        n = Node(val)
        p = curr.prev
        n.next = curr
        curr.prev = n
        n.prev = p
        if p: p.next = n


    def deleteAtIndex(self, index: int) -> None:
        curr = self.find_by_index(index)
        if curr:
            l = curr.next
            p = curr.prev
            if p: 
                p.next = l
            else:
                self.head = l
            if l: l.prev = p

            if p is None and l is None: self.head = None

    def show(self):
        cur = self.head
        while cur:
            print(cur.val)
            cur = cur.next
        
if __name__ == "__main__":
    # obj = MyLinkedList()
    # obj.addAtHead(1)
    # obj.addAtTail(3)
    # obj.addAtIndex(1,2)
    # obj.deleteAtIndex(0)
    # print("-->", obj.get(0))
    # # obj.addAtHead(6)
    # # obj.addAtTail(4)
    # # # print(obj.get(4))
    # # obj.addAtHead(4)
    # # obj.addAtIndex(5,0)
    # # obj.addAtHead(6)
    # obj.show()
    print(not "")