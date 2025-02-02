def binary_search(target, arr):
    if not arr:
        return False
    l,r = 0,len(arr)-1
    while l<=r:
        mid = (l+r)//2
        if arr[mid] == target:
            return True
        if arr[mid] < target:
            l = mid + 1
        if arr[mid] > target:
            r = mid - 1
    return False



def bubble_sort(nums):
    for i in range(len(nums)):
        for j in range(1,len(nums)-i):
            if nums[j] < nums[j-1]:
                nums[j-1],nums[j] = nums[j],nums[j-1]
    
    return nums


#with swap flag 
def bubble_sort(nums):
    swapping = True
    end = len(nums)
    while swapping:
        swapping = False
        for i in range(1, end):
            if nums[i - 1] > nums[i]:
                temp = nums[i - 1]
                nums[i - 1] = nums[i]
                nums[i] = temp
                swapping = True
        end -= 1
    return nums



def merge_sort(nums):
    if(len(nums)<2):
        return nums
    N = len(nums)
    sorted_left_side,sorted_right_side = merge_sort(nums[0:N//2]),merge_sort(nums[N//2:])
    return merge(sorted_left_side,sorted_right_side)


def merge(first, second):
    final = []
    i,j =0,0
    
    while i < len(first) and j < len(second):
        if first[i] <= second[j] :
            final.append(first[i])
            i+=1
        else:
            final.append(second[j])
            j+=1
    
    final.extend(first[i:])
    final.extend(second[j:])
    
    return final

#print(merge([1,3,5,7],[2,4,6,8]))
