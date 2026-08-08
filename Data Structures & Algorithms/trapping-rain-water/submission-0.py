class Solution:
    def trap(self, height: List[int]) -> int:
        #prefix and suffix arrays
        #precompute
        l_wall = r_wall = 0

        n = len(height)
        if n== 0:
            return 0

        leftMax = [0] * n
        rightMax = [0] * n


 

        for i in range(n):
            j = -i-1
            leftMax[i] = l_wall
            rightMax[j] = r_wall

            l_wall = max(l_wall, height[i])
            r_wall = max(r_wall, height[j])


        summ = 0
        for i in range(n):
            pot = min(leftMax[i], rightMax[i])
            summ += max(0, pot- height[i])

        return summ
      




        
        