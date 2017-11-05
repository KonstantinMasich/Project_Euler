# PROJECT EULER
# Question 31
# Konstantin Masich
# Python 3.5.2

COINS = [1, 2, 5, 10, 20, 50, 100, 200]
    
def arrangements_num(coin_count, target):
    if target==0:
        return 1
    if target <0 or coin_count <= 0:
        return 0
    return arrangements_num(coin_count-1, target) \
         + arrangements_num(coin_count, target-COINS[coin_count-1])
        
print("Ans:", arrangements_num(len(COINS), COINS[-1]))
