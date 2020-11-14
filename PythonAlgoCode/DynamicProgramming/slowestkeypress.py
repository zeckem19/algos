

def slowestKeyPress(keyTimes) -> int:
    
    curr_longest = 0
    curr_key = -1
    
    for i in range(1, len(keyTimes)):
        key_time = keyTimes[i][1] - keyTimes[i-1][1]
        if key_time> curr_longest:
            curr_longest = key_time
            curr_key = keyTimes[i][0]
        
    return curr_key

print(slowestKeyPress([[0,2],[1,5],[0,9],[2,15]]))
