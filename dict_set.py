#dict
d = {'Michael':95, 'Bob':75,'Tracy':85}
print(d['Michael'])
d['Jack'] = 80
print(d)
print('Thomas' in d)
print(d.get('Thomas'))
print(d.get('Thomas',-1))
print(d)

bob_value = d.pop('Bob')
print(bob_value)
print(d)

#set
s = set([1, 2, 2, 3, 3])
print(s)
s.add(4)
print(s)
s.remove(4)
print(s)

#并集与交集运算
s1 = set([1,2,3])
s2 = set([2,3,4])
s3 = s1 & s2
s4 = s1 | s2
print(s3)
print(s4)

#可变和不可变对象
list = ['a','c','b']
list.sort()
print(list)

a = 'abc'
b = a.replace('a','A')
print(a,b)