#!/usr/bin/env python3

def print_fibonacci(length):
    fibonacci = [0, 1] 
    
    if length == 0: 
        print([])
        return 
    if length == 1:
        print([0])
        return 
    if length == 2:
        print([0, 1])
        return 
    
    for _ in range(2, length):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    
    print(fibonacci[:length])
        