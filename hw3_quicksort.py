# -*- coding: utf-8 -*-
"""
Created on Mon May 13 08:47:11 2024

@author: USER
"""
enter=input("輸入:")
a=list(map(int,enter.split(",")))

def quicksort(array,start,end):
    if start>=end:
        return array
    
    pivot=start
    left=start
    right=end
    print("\n左指標:",left,"右指標:",right)
    
    while (left<right):
        if array[right]>array[pivot]:
            right-=1
        elif array[left]<=array[pivot]:
            left+=1
        elif array[right]<array[pivot] and array[left]>=array[pivot]:
            r=int(array[right])
            l=int(array[left])
            array[left]=r
            array[right]=l
            print(array)
        if right==left:
            l=int(array[left])
            array[left]=array[pivot]
            array[pivot]=l
            print(array)

    quicksort(array,start,left-1)
    quicksort(array,left+1,end)  
    
        
quicksort(a,0,len(a)-1)