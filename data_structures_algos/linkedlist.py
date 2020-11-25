# LL: O(1) inserts at the start
# O(N) at the end
# O(N) to find

class Node:
    def __init__(self, data, next_node):
        self.data = data
        self.next_node = next_node
    
#     def get_data(self):
#         return self.data
    
#     def set_node(self, next_node):
#         self.next_node = next_node

class LL:
    def __init__(self):
        self.head = None
    
    def insert_head(self, data):
        if self.head == None:
            n = Node(data, None)
            self.head = n
        else:
            n = Node(data, self.head)
            self.head = n
    
    def insert_last(self, data):
        n = Node(data, None)
        if self.head == None:
            self.head = n
        else:
            ptr = self.head
            while ptr.next_node!= None:
                ptr = ptr.next_node
            ptr.next_node = n
    
    def find_data_in_LL(self, data):
        ptr = self.head
        if ptr.data == data:
            return True
        while ptr.next_node != None:
            if ptr.data == data:
                return True
            ptr = ptr.next_node
        return False
    
    def print_ll(self):
        ptr = self.head
        while ptr.next_node != None:
            print(ptr.data, end=', ')
            ptr = ptr.next_node
        print(ptr.data)
        
    # def remove_item(self):
    #     ptr = self.head
    #     while ptr.next_node != None:
            