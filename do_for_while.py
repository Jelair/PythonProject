names = ['Michael','Bob',"Jack"]
for name in names:
    print(name)

sum = 0
for x in [1,2,3,4,5,6,7,8,9,10]:
    sum += x
print(sum)

print(list(range(5)))

sum = 0
for x in range(101):
    sum += x
print(sum)

sum = 0
n = 99
while n > 0:
    sum += n
    n -= 2
print(sum)

L = ['Bart','Lisa','Adam']
for name in L:
    print('Hello,%s', name)