**intution**
=>we have to find second largest and smallest element from an array .
approach:
->without sorting array we can find first traverse the array and find largest and smallest element from array 
-> by using largest check each element which are smaller than largest ele and it should be max among all elemnts in an array
->by using smallest check each element which are greater than smaller ele and it should not equal to small element and should be minimium among all elements in an array
code:2
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def getSecondOrderElements(n: int,  a: [int]) -> [int]:
    # Write your code here.
    max1=max(a)
    min1=min(a)
    secondm=10**9+1
    secondl=-1
    for i in range(n):
        if a[i]!=max1 and a[i]<max1:
            secondl=max(secondl,a[i])
        if a[i]!=min1 and a[i]>min1:
            secondm=min(secondm,a[i])
    return [secondl,secondm]
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
approach 2:
=> first we have traverse array finding both large and second large 
=>we take large=a[0] ,secondl=a[0] first traverse the array by two coditions we change our large and second l
condition 1: large will check is another element which greater than me if it is then this large becomes secondl=large and the new element is our new large
condition 2: large is greater than new elment thats okay, but what about second large it also should be greater than the new element so by using max we can change our secondl which is greater among these 2 .
  => same as small follows but in this small we take small=seconds=10**9 based on our constraint they gave 
condition1 :
small traverse checks each element from array whether it is smaller .if there is a ele which is smaller than our small then we assign small to second small and new elemnt as small
codnition2:
if there is no element which is smaller than our small but seconds it aslo smaller than new element so we dont know we can use min con and find which smaller among those twoo and we take that as our second small
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
code:3
def getSecondOrderElements(n: int,  a: [int]) -> [int]:
    # Write your code here.
    large=a[0]
    secondl=a[0]
    small=10**9
    seconds=10**9
    for i in range(n):
        if large>a[i]:
            secondl=max(a[i],secondl) 
        elif large<a[i]:
            secondl=large 
            large=a[i]
        if small<a[i]:
            seconds=min(seconds,a[i])
        elif small>a[i]:
            seconds=small 
            small=a[i]
    return [secondl,seconds]
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
