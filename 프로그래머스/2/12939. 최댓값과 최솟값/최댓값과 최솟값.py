def solution(s):
    nums = list(map(int, s.split()))
    nums.sort()
    maxi = str(nums[-1])
    mini = str(nums[0])
    answer = mini + ' ' + maxi
    return answer