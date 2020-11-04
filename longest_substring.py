
def lengthOfLongestSubstring( s:str) -> int:
    
    curr_max = 0
    ind = 0
    memo= {}
    longest_max = ''
    while True:
        if ind >= len(s)-1:
            break
        curr_search = ''
        print(f'ind{ind}')
        for index in range(ind, len(s)-1):
            char = s[index]
            if char in memo:
                tmp = memo[char]
            memo[char] = index
            if char not in curr_search:
                curr_search+=char

            else:
                print(curr_search)
                print(memo)
                longest_max = curr_search if len(curr_search)> curr_max else longest_max
                curr_max = max(curr_max, len(curr_search))
                curr_search = ''
                ind = tmp + 1
                break
            
    print(curr_max)
    print(longest_max)

lengthOfLongestSubstring('abcdabcefbb')

#  index   1  2  3  4  5    6
#  string  a  ab a  ab abc  b
#   max    1  2  2  2  3    3


# # Solution.lengthOfLongestSubstring('abcabcbb')
# class Solution:
#     def __init__(self,s):
#         self.s = s
#         self.curr_search_str = ''
#         self.curr_max = 0

#     def solve(self, index):
#         #base case
#         if index >= len(self.s) -1:
#             self.curr_max = max(len(self.curr_search_str), self.curr_max)
#             return True

#         #  Else continue searching next index
#         for i in range(len(self.s)-1):
#             if self.s[index] in self.curr_search_str:
#                 self.curr_max = max(len(self.curr_search_str), self.curr_max)
#                 self.curr_search_str = ''
#                 return True

#             self.curr_search_str = self.curr_search_str+self.s[i]
#             print(self.curr_search_str)
#             self.solve(i)


        
# sol = Solution('abcabcbb')
# sol.solve(0)
# print(sol.curr_max)