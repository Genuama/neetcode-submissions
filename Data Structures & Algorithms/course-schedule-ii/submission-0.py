class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #adjacency list 
        #dfs 
        #return list of courses that i can take to finish all courses [0,len(numCourses)-1] #no cycle must be detected

        output = []
        visit = set()
        cycle = set()

        prevMap = {i:[] for i in range(numCourses)}

        for course,prereq in prerequisites:
            prevMap[course].append(prereq) 
            print(prevMap)


        def dfs(course):
            if course in cycle:
                return False
            if course in visit: 
                return True

            cycle.add(course)
            for prereq in prevMap[course]:
                if dfs(prereq) == False:
                    return False
            cycle.remove(course)
            visit.add(course)
            output.append(course)
            return True
        
        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return output

            
        