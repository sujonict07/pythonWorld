import functools

lis = [1,1,2,2,3]

a = functools.reduce(lambda a,b:a^b,lis)
print(a)
