class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        ans = []
        def permutate(arr, left):
            if len(arr) == k:
                ans.append(arr)
                return
            if len(arr) + len(left) < k:
                return
            for i in range(len(left)):
                permutate(arr+[left[i]], left[i+1:])
        
        permutate([], [i for i in range(1,n+1)])

        return ans
        