import math
import sys

num=[1]

def quick (numbers):
    if len(numbers)>1:
        pivot = numbers.pop(-1)
        left=[]
        right=[]
        for x in range(0,len(numbers),1):
            if numbers[x]>=pivot:
                left.append(numbers[x])
            else:
                right.append(numbers[x])
        return quick(left) + [pivot] + quick(right)
    else:
        return numbers


if __name__=='__main__':
    numbers=sys.argv[1]
    quick(numbers)
