

def hanoi(N,cl='a',aux='b',target='c'):
    if N==1:
        print(f'Plate {N} from {cl} to {target}')
        return
    print(f'{N-1},cl: {cl},aux: {target},target: {aux}')
    hanoi(N-1,cl,target,aux)
    print(f'Plate {N} from {cl} to {target}')

    print(f'clean up {N-1},cl: {aux},aux: {cl},target: {target}')
    hanoi(N-1,aux,cl,target)
    
    
hanoi(3)