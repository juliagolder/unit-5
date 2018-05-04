#juliagolder
#5/3/18
#selectionSort.py

from random import randint
from time import time

N = 100 #how many numbers will be sorted

def mySort(A):
    for j in range(0,len(A)-1):
        iMin = j
        for i in range(j+1, N):
            if (A[i] < A[iMin]):
                iMin = i
        if iMin != j:
            A[j], A[iMin] = A[iMin], A[j]
    return A

    
if __name__ == '__main__':

    #make a list of N random numbers between 1 and N
    numbers = [0]*N
    for i in range(N):
        numbers[i] = randint(1,N)
    
    pythonSort = sorted(numbers) #Python's sort
    
    #time how long your sort takes
    t1 = time()
    numbers = mySort(numbers)
    t2 = time()
    
    #print whether the sort worked or not
    try:
        assert(numbers == pythonSort)
        print('Your sort took', t2-t1, 'seconds')
    except:
        print('Your sort did not work')
