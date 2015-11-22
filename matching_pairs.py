from string import maketrans    

n = int(raw_input())
def matching(string1, string2):
    return len(string1) == len(string2) and string1.translate(maketrans(string1, string2)) == string2 and string2.translate(maketrans(string2, string1)) == string1
        
lst = []
counter = 0
for x in range(n):
    lst.append(raw_input().strip())
for x in range(len(lst)):
    for y in range(x+1, len(lst)):
        if matching(lst[x], lst[y]):
            counter += 1
print counter