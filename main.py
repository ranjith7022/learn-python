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