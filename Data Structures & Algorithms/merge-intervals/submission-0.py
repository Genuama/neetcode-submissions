class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #sorting
        #sorted_data = sorted(data, key=lambda x: x[1])
        intervals = sorted(intervals, key=lambda x: x[0])
        print(intervals)
        output = [intervals[0]]
        

        for i in range(1, len(intervals)):
            if intervals[i][0] <= output[-1][1]: #overlap, merge
                output[-1][1] = max(intervals[i][1], output[-1][1])
                print(output)
            else:
                output.append(intervals[i])

            

        return output
