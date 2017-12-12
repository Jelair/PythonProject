from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x)
print(p.y)

# deque除了实现list的append()和pop()外，还支持appendleft()和popleft()，这样就可以非常高效地往头部添加或删除元素。
from collections import deque
q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)

# 使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值
from collections import defaultdict
dd = defaultdict(lambda : 'N/A')
dd['key1'] = 'abc'
print(dd['key1'])
print(dd['key2'])

# 使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。
# 如果要保持Key的顺序，可以用OrderedDict
from collections import OrderedDict
d = dict([('a', 1), ('b', 2), ('c', 3)])
print(d)
# 注意，OrderedDict的Key会按照插入的顺序排列，不是Key本身排序
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(od)
od = OrderedDict()
od['z'] = 1
od['y'] = 2
od['x'] = 3
print(list(od.keys()))

# OrderedDict 可以实现一个FIFO的dict
# 当容量超出限制时，先删除最早添加的Key
class LastUpdatedOrderedDict(OrderedDict):

    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self._capacity = capacity

    def __setattr__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print('remove:', last)

        if containsKey:
            del self[key]
            print('set:', (key, value))
        else:
            print('add:', (key, value))
        OrderedDict.__setitem__(self, key, value)

# Counter是一个简单的计数器，例如，统计字符出现的个数
# Counter实际上也是dict的一个子类
from collections import Counter
c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1
print(c)