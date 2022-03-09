def add(*values):
    sum=0
    values=list(values)
    values[0]=0
    for i in values:
        sum += i
    return sum
print(add(1,2,3,4,5,6))