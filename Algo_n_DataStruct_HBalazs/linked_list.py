# Create a simple linked list of strings
class llNode(object):
    def __init__(self, data):
        self.data = data
        self.next_node = None

class linkd_lst(object):
    def __init__(self):
        self.head = None
        self.size = 0

    def insertStart(self, data):
        self.size += 1
        # Instantiate a node object
        new_node = llNode(data)

        # if the linked list is empty, just initialize the head pointer to the new node object instantiated
        if not self.head:
            self.head = new_node
            new_node.next_node = None

        # else if the linked list (ll) already has (n>=1) nodes, do the million dollar magic below,
        # take the next node pointer in the new_node instantiated object and point it to ll's current head and
        # move the ll's head pointer to point to the new_node object
        else:
            new_node.next_node = self.head
            self.head = new_node

    # O(1) operation to get size of linked list, if we initialize size during creation and update at every insertion
    def sizeLl(self):
        return self.size

    # O(n) operation to get size of linked list, if we have to calculate by traversing
    def calcSizeLl(self):
        calc_size = 0
        # Whenever traversing, need to start at root node
        cur_node = self.head
        while cur_node is not None:
            calc_size +=1
            cur_node = cur_node.next_node
        return calc_size

    def insertEnd(self,data):
        self.size +=1
        new_node = llNode(data)
        cur_node = self.head
        while cur_node.next_node is not None:
            cur_node = cur_node.next_node
        cur_node.next_node = new_node
        new_node.next_node = None

    def traversePrint(self):
        cur_node = self.head
        while cur_node is not None:
            print(cur_node.data)
            cur_node = cur_node.next_node

    def removeNode(self,data):
        cur_node = self.head
        if cur_node is None:
            return
        elif cur_node.data == data:
            self.size -= 1
            self.head = cur_node.next_node
        else:
            prev_node = None
            while cur_node.data != data:
                prev_node = cur_node
                cur_node = cur_node.next_node
            self.size -= 1
            prev_node.next_node = cur_node.next_node

def main():
    myll = linkd_lst()
    myll.insertStart('World')
    myll.insertStart('Hello')
    myll.insertEnd('How are you?')
    return myll

if __name__ == '__main__':
    myll = main()
    myll.traversePrint()
    print(f'Size of myll is {myll.sizeLl()}')
    myll.removeNode('World')
    myll.traversePrint()
    print(f'New size of myll is {myll.calcSizeLl()}')