import math
import sys

def quick(numbers):
    if len(numbers)>1:
        pivot = numbers.pop(-1)
        left=[]
        right=[]
        for x in range(0,len(numbers),1):
            if numbers[x]<=pivot:
                left.append(numbers[x])
            else:
                right.append(numbers[x])
        return quick(left) + [pivot] + quick(right)
    else:
        return numbers


if __name__=='__main__':
    numbers=[7,3,6,3,2,3,7,8] #change to a list when doing internal sorting [7,3,6,3,2,3,7,8] or sys.argv[1]
    new_numbers=quick(numbers)
    print(new_numbers)