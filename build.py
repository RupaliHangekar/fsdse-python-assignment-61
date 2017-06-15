def solution(list_of_nums):
    d={}
    ce=0
    co=0
    for i in list_of_nums:
        if i%2==0:
            ce=ce+1
        else:
            co=co+1
    d.update({'ODD':co})
    d.update({'EVEN':ce})
    return d

print(solution([1, 2, 3, 5, 8, 9]))
