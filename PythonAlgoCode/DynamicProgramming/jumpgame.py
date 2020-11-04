class Sol:
    def __init__(self, nums):
        self.path = nums
        self.start = 0 
        
    def solve(self, n):
        print(f'n:{n}')
        if n == len(self.path) -1:
            return True
        else:
            if self.path[n] == 0:
                return False
            for i in range(1,self.path[n]+1):
                print(f'i:{i}')
                if self.solve(n+i):
                    return True

s=Sol([2,3,1,1,4])
print(s.solve(0))