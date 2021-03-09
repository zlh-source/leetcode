class Solution:
    def search(self, nums, target) -> int:
        '''寻找元素'''
        l, r = 0, len(nums) - 1
        while l<=r:
            mid = l + (r - l) // 2
            if nums[mid]==target:
                return mid  #注意
            elif nums[mid]<target:
                r=mid+1
            elif nums[mid]>target:
                l=mid-1
        return -1 #注意

    def left_bound(self,nums, target):
        '''寻找左边界'''
        l,r=0,len(nums)-1
        while l<=r:
            mid = l + (r - l) // 2
            if nums[mid]==target:
                r=mid-1 #注意，因为是寻找左边界，所以缩小r,使l最终指向结果
            elif nums[mid]<target:
                l=mid+1
            elif nums[mid]> target:
                r=mid-1

        #检查l的合法性
        if 0>l or l>len(nums)-1 or nums[l]!=target:
            return -1
        else:
            return l #注意

    def right_bound(self,nums, target):
        #寻找右边界
        l,r=0,len(nums)-1
        while l<=r:
            mid = l + (r - l) // 2
            if nums[mid]==target:
                l=mid+1 ##注意，因为是寻找右边界，所以增大l,使r最终指向结果
            elif nums[mid]<target:
                l=mid+1
            elif nums[mid]> target:
                r=mid-1

        #检查r的合法性
        if 0>r or r>len(nums)-1 or nums[r]!=target:
            return -1
        else:
            return r #注意
