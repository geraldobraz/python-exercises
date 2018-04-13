import math
def new_avg(arr,newavg):
    num = newavg * (len(arr) + 1) - sum([n for n in arr])
    if num > 0:
        return math.ceil(num)
    else:
        raise ValueError("-1")

print(new_avg([14, 30, 5, 7, 9, 11, 16], 90))







