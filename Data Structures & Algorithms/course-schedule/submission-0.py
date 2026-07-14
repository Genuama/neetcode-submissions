class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)


        visited = set() #store all courses along the DFS path

        def dfs(crs):
            if crs in visited:
                return False #cycle detected
            if preMap[crs] == []:
                return True #no cycle detected
            
            visited.add(crs)

            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visited.remove(crs)
            preMap[crs] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
