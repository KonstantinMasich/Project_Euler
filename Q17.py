def g(num, order, whole_num = -1):
    "Does not handle the 'and' word"
    if order == 1:
        if num == 0:         # 0
            return 0
        if num in {1, 2, 6}: # 1,2,6
            return 3
        if num in {4, 5, 9}: # 4,5,6
            return 4
        else:                # 3,7,8
            return 5         
    if order == 2:
        if num == 0:      # 0
            return 0
        if num == 1:      # 10s
            # Rebuilding whole num:
            whole_num = int(str(whole_num)[-2:])
            if whole_num == 10:               # 10
                return 3
            if whole_num in {11, 12}:         # 11,12
                return 6
            if whole_num in {15, 16}:         # 15,16
                return 7
            if whole_num in {13, 14, 18, 19}: # 13,14,18,19
                return 8
            else:                             # 17
                return 9                     
        if num in {4, 5, 6}: # 40s,50s,60s
            return 5
        if num in {2, 3, 8, 9}: # 20s,30s,40s,80s,90s
            return 6
        else:
            return 7
        if num == 7: # 70s
            return 7
    if order == 3:
        return g(num, 1) + 7
            
def f(x):
    "Returns the 'verbal sum' of all digits in a number"
    l = list(str(x)[::-1])
    index = 1
    total = 0
    for num in l:
        if index == 1 and len(l)>1 and l[1]=="1":
            pass
        else:
            total += g(int(num), index, whole_num = x)  
        index += 1
    if len(str(x)) == 3:
        if str(x)[-2:] == "00":
            return total
        else:
            return total + 3   
    return total

res = 0
for i in range(1000):
    res += f(i)
res += 11 # one thousand
print(res)
