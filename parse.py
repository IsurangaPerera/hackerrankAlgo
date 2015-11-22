# Passes 13 out of 20 test cases

n = int(raw_input())

lst = []
for x in range(n):
    lst.append(raw_input())

ops = []
nums = []

for x in range(len(lst)):
    if lst[x][0].isdigit():
        nums.append(lst[x])
    else:
        ops.append(lst[x][0])
    

#print ops
#print nums
ans = ''
for x in range(len(nums)):
    try:
        ans += nums[x] + ops[x]
    except:
        ans += nums[-1]

try:
    #print ans[:-1]
    print eval(ans)
except:
    print eval(ans[:-1])