class stack:
    def __init__(self):

        self.st = []
    
    def pop(self):
        if self.st == []:
            return None
        else:
            return self.st.pop()
        
    def push(self, data):
        self.st.append(data)
    
    def peek(self):
        if self.st == []:
            return None
        else:
            return self.st[-1]
        
    def print_st(self):
        print(self.st)
    


class queue:
    def __init__(self):
        self.q = []

    def add_queue(self, data):
        self.q.append(data)

    def remove(self):
        if len(self.q) == 0:
            return None
        else:
            item = self.q[0]
            del self.q[0]
            return item
    
    